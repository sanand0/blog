#!/usr/bin/env -S uv run
"""Map scraped LinkedIn posts to matching blog posts."""

from __future__ import annotations

import csv
import json
import math
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINKEDIN_PATH = Path.home() / "Documents/data/linkedin-posts.jsonl"
OUTPUT_PATH = ROOT / "analysis/linkedin-blog-map.tsv"
AMBIGUOUS_PATH = ROOT / "analysis/linkedin-blog-map-ambiguous.tsv"
MAP_FIELDS = ("linkedin_url", "blog_filename", "linkedin_content", "blog_content")
AMBIGUOUS_FIELDS = (
    "linkedin_url",
    "best_blog_filename",
    "best_score",
    "best_date_delta_days",
    "second_blog_filename",
    "second_score",
)


@dataclass
class Document:
    path: str
    content: str
    date: datetime | None
    words: list[str]
    word_counts: Counter[str]
    shingles: set[tuple[str, ...]]


def ascii_text(text: str) -> str:
    """Convert styled Unicode to ASCII and collapse whitespace."""
    text = unicodedata.normalize("NFKC", text).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", text).strip()


def markdown_text(text: str) -> str:
    """Remove Markdown syntax while retaining readable content."""
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    return ascii_text(text)


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def make_document(path: str, content: str, date: datetime | None) -> Document:
    tokens = words(markdown_text(content))
    return Document(
        path=path,
        content=content,
        date=date,
        words=tokens,
        word_counts=Counter(tokens),
        shingles=set(zip(tokens, tokens[1:], tokens[2:])),
    )


def parse_date(value: str) -> datetime:
    return datetime.fromisoformat(value.strip("\"'").replace("Z", "+00:00"))


def load_blog_posts() -> list[Document]:
    posts = []
    for path in sorted((ROOT / "posts").glob("*/*.md")):
        content = path.read_text()
        match = re.search(r"^date:\s*(.+?)\s*$", content, flags=re.MULTILINE)
        date = parse_date(match.group(1)) if match else None
        posts.append(make_document(str(path.relative_to(ROOT)), content, date))
    return posts


def load_linkedin_posts() -> list[tuple[str, Document, set[str]]]:
    posts = []
    with LINKEDIN_PATH.open() as handle:
        for line in handle:
            item = json.loads(line)
            if item.get("type") == "post":
                linked_slugs = {
                    match.group(1)
                    for link in item.get("links", [])
                    if (match := re.search(r"s-anand\.net/blog/([^/?#]+)", link))
                }
                posts.append(
                    (
                        item["url"],
                        make_document(item["url"], item["content"], parse_date(item["postedAt"])),
                        linked_slugs,
                    )
                )
    return posts


def score(linkedin: Document, blog: Document) -> tuple[float, int]:
    shared_shingles = len(linkedin.shingles & blog.shingles)
    phrase_overlap = shared_shingles / max(1, min(len(linkedin.shingles), len(blog.shingles)))
    shared_words = linkedin.word_counts.keys() & blog.word_counts.keys()
    dot = sum(linkedin.word_counts[word] * blog.word_counts[word] for word in shared_words)
    left = math.sqrt(sum(count * count for count in linkedin.word_counts.values()))
    right = math.sqrt(sum(count * count for count in blog.word_counts.values()))
    cosine = dot / max(1, left * right)
    return 0.8 * phrase_overlap + 0.2 * cosine, shared_shingles


def is_eligible(linkedin: Document, blog: Document, shared_shingles: int) -> bool:
    """Reject coincidences from generic phrases and tiny blog posts."""
    if shared_shingles < 2:
        return False
    if len(blog.words) >= 20:
        return True
    return " ".join(blog.words) in " ".join(linkedin.words)


def truncate(text: str) -> str:
    return ascii_text(markdown_text(text))[:200]


def load_existing_rows() -> dict[str, dict[str, str]]:
    """Load authoritative manual mappings; reruns must not modify these rows."""
    if not OUTPUT_PATH.exists():
        return {}
    with OUTPUT_PATH.open(newline="") as handle:
        return {row["linkedin_url"]: row for row in csv.DictReader(handle, delimiter="\t")}


def add_linkedin_metadata(rows: list[dict[str, str]]) -> None:
    """Add missing LinkedIn front matter without overwriting existing metadata."""
    for row in rows:
        if not row["blog_filename"]:
            continue
        path = ROOT / row["blog_filename"]
        content = path.read_text()
        match = re.search(r"^linkedin:\s*(.+?)\s*$", content, flags=re.MULTILINE)
        if match:
            if match.group(1).strip("\"'") != row["linkedin_url"]:
                raise ValueError(f"{path} has conflicting linkedin metadata")
            continue
        updated, count = re.subn(
            r"\A(---\s*\n.*?)(\n---\s*\n)",
            rf"\1\nlinkedin: {row['linkedin_url']}\2",
            content,
            count=1,
            flags=re.DOTALL,
        )
        if count != 1:
            raise ValueError(f"{path} has no YAML front matter")
        path.write_text(updated)


def main() -> None:
    blogs = load_blog_posts()
    blogs_by_slug = {Path(blog.path).stem: blog for blog in blogs}
    linkedin_posts = sorted(load_linkedin_posts(), key=lambda item: item[1].date)
    existing_rows = load_existing_rows()
    rows = []
    ambiguous = []
    matched = 0

    for index, (url, linkedin, linked_slugs) in enumerate(linkedin_posts, 1):
        if url in existing_rows:
            rows.append(existing_rows[url])
            matched += bool(existing_rows[url]["blog_filename"])
            continue
        candidates = sorted(
            ((*score(linkedin, blog), blog) for blog in blogs),
            key=lambda item: item[0],
            reverse=True,
        )
        best_score, best_shared, best = candidates[0]
        second_score, second_shared, second = candidates[1]
        direct_matches = [blogs_by_slug[slug] for slug in linked_slugs if slug in blogs_by_slug]
        if direct_matches:
            best = direct_matches[0]
            best_score, best_shared = score(linkedin, best)
        delta = abs((linkedin.date - best.date).total_seconds()) / 86400 if best.date else 99999
        margin = best_score - second_score
        passes_score = best_score >= 0.32 or (delta <= 14 and best_score >= 0.22)
        is_match = bool(direct_matches) or (
            passes_score and margin >= 0.04 and is_eligible(linkedin, best, best_shared)
        )
        if is_match:
            matched += 1
        second_is_plausible = (
            second_score >= 0.32 and is_eligible(linkedin, second, second_shared)
        )
        if len(direct_matches) > 1 or (
            not direct_matches and is_match and second_is_plausible and margin < 0.08
        ):
            ambiguous.append(
                {
                    "linkedin_url": url,
                    "best_blog_filename": best.path,
                    "best_score": f"{best_score:.3f}",
                    "best_date_delta_days": f"{delta:.1f}",
                    "second_blog_filename": second.path,
                    "second_score": f"{second_score:.3f}",
                }
            )
        rows.append(
            {
                "linkedin_url": url,
                "blog_filename": best.path if is_match else "",
                "linkedin_content": truncate(linkedin.content),
                "blog_content": truncate(best.content) if is_match else "",
            }
        )
        if index % 25 == 0:
            print(f"Scored {index}/{len(linkedin_posts)} LinkedIn posts")

    write_tsv(OUTPUT_PATH, rows, MAP_FIELDS)
    write_tsv(AMBIGUOUS_PATH, ambiguous, AMBIGUOUS_FIELDS)
    add_linkedin_metadata(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT_PATH}; matched {matched}; ambiguous {len(ambiguous)}")


def write_tsv(path: Path, rows: list[dict[str, str]], fields: tuple[str, ...]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
