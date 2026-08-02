#!/usr/bin/env -S uv run
"""Map scraped LinkedIn posts to matching blog posts."""

from __future__ import annotations

import argparse
import csv
import html
import json
import math
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINKEDIN_PATH = Path.home() / "Documents/data/linkedin-posts.jsonl"
OUTPUT_PATH = ROOT / "analysis/linkedin-blog-map.tsv"
AMBIGUOUS_PATH = ROOT / "analysis/linkedin-blog-map-ambiguous.tsv"
OVERRIDES_PATH = ROOT / "analysis/linkedin-blog-map-overrides.tsv"
MAP_FIELDS = (
    "linkedin_url",
    "blog_filename",
    "linkedin_content",
    "blog_content",
    "match_method",
    "score",
    "date_delta_days",
)
AMBIGUOUS_FIELDS = (
    "linkedin_url",
    "reason",
    "best_blog_filename",
    "best_score",
    "best_date_delta_days",
    "second_blog_filename",
    "second_score",
)
OVERRIDE_FIELDS = ("linkedin_url", "blog_filename")
SAFE_FRONTMATTER_METHODS = {"override", "direct_url"}


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
    """Remove metadata, code, HTML, and Markdown while retaining prose."""
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(
        r"<(script|style|noscript)\b.*?</\1>",
        " ",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return ascii_text(html.unescape(text))


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
    parsed = datetime.fromisoformat(value.strip("\"'").replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)


def linkedin_date(item: dict[str, object]) -> datetime:
    """Use the Snowflake timestamp in the activity ID; relative scraped dates drift."""
    value = str(item.get("postId") or item.get("id") or item.get("url") or "")
    match = re.search(r"(?:activity:)?(\d{16,})", value)
    if match:
        milliseconds = int(match.group(1)) >> 22
        return datetime.fromtimestamp(milliseconds / 1000, UTC)
    return parse_date(str(item["postedAt"]))


def frontmatter_linkedin_urls(content: str) -> set[str]:
    """Read scalar, inline-list, or YAML-list LinkedIn metadata without a YAML dependency."""
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", content, flags=re.DOTALL)
    if not match:
        return set()
    lines = match.group(1).splitlines()
    urls: set[str] = set()
    for index, line in enumerate(lines):
        field = re.match(r"^linkedin:\s*(.*)$", line)
        if not field:
            continue
        urls.update(
            re.findall(r"https://www\.linkedin\.com/[^\s,\]\"']+", field.group(1))
        )
        for child in lines[index + 1 :]:
            if not re.match(r"^\s+", child):
                break
            urls.update(re.findall(r"https://www\.linkedin\.com/[^\s,\]\"']+", child))
        break
    return {url.rstrip("/") + "/" for url in urls}


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
            if item.get("type") != "post":
                continue
            linked_slugs = {
                match.group(1)
                for link in item.get("links", [])
                if (match := re.search(r"s-anand\.net/blog/([^/?#]+)", link))
            }
            url = item["url"].rstrip("/") + "/"
            posts.append(
                (
                    url,
                    make_document(url, item.get("content", ""), linkedin_date(item)),
                    linked_slugs,
                )
            )
    return posts


def load_overrides() -> dict[str, str]:
    """Load reviewed mappings; a blank filename explicitly means no blog match."""
    if not OVERRIDES_PATH.exists():
        return {}
    with OVERRIDES_PATH.open(newline="") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        return {
            row["linkedin_url"].rstrip("/") + "/": (
                row.get("blog_filename") or ""
            ).strip()
            for row in rows
            if row.get("linkedin_url")
        }


def score(linkedin: Document, blog: Document) -> tuple[float, int]:
    shared_shingles = len(linkedin.shingles & blog.shingles)
    phrase_overlap = shared_shingles / max(
        1, min(len(linkedin.shingles), len(blog.shingles))
    )
    shared_words = linkedin.word_counts.keys() & blog.word_counts.keys()
    dot = sum(
        linkedin.word_counts[word] * blog.word_counts[word] for word in shared_words
    )
    left = math.sqrt(sum(count * count for count in linkedin.word_counts.values()))
    right = math.sqrt(sum(count * count for count in blog.word_counts.values()))
    cosine = dot / max(1, left * right)
    return 0.8 * phrase_overlap + 0.2 * cosine, shared_shingles


def rank_candidates(
    linkedin: Document, blogs: list[Document]
) -> list[tuple[float, int, Document]]:
    """Exhaustively rank only unresolved posts; deterministic mappings skip this work."""
    return sorted(
        ((*score(linkedin, blog), blog) for blog in blogs),
        key=lambda item: item[0],
        reverse=True,
    )


def is_eligible(linkedin: Document, blog: Document, shared_shingles: int) -> bool:
    """Reject coincidences from generic phrases and tiny blog posts."""
    if shared_shingles < 2:
        return False
    if len(blog.words) >= 20:
        return True
    return " ".join(blog.words) in " ".join(linkedin.words)


def date_delta_days(left: Document, right: Document) -> float:
    if not left.date or not right.date:
        return 99999
    return abs((left.date - right.date).total_seconds()) / 86400


def truncate(text: str) -> str:
    return markdown_text(text)[:200]


def review_row(
    url: str,
    reason: str,
    best: Document,
    best_score: float,
    delta: float,
    second: Document,
    second_score: float,
) -> dict[str, str]:
    return {
        "linkedin_url": url,
        "reason": reason,
        "best_blog_filename": best.path,
        "best_score": f"{best_score:.3f}",
        "best_date_delta_days": f"{delta:.1f}",
        "second_blog_filename": second.path,
        "second_score": f"{second_score:.3f}",
    }


def add_linkedin_metadata(rows: list[dict[str, str]]) -> None:
    """Write only deterministic mappings; fuzzy matches remain reviewable output."""
    for row in rows:
        if (
            not row["blog_filename"]
            or row["match_method"] not in SAFE_FRONTMATTER_METHODS
        ):
            continue
        path = ROOT / row["blog_filename"]
        content = path.read_text()
        existing = frontmatter_linkedin_urls(content)
        if row["linkedin_url"] in existing:
            continue
        if existing:
            raise ValueError(f"{path} already has different linkedin metadata")
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


def main(write_frontmatter: bool = False) -> None:
    blogs = load_blog_posts()
    if len(blogs) < 2:
        raise ValueError("At least two blog posts are required")
    blogs_by_path = {blog.path: blog for blog in blogs}
    blogs_by_slug = {Path(blog.path).stem: blog for blog in blogs}
    blogs_by_linkedin: dict[str, list[Document]] = {}
    for blog in blogs:
        for url in frontmatter_linkedin_urls(blog.content):
            blogs_by_linkedin.setdefault(url, []).append(blog)
    linkedin_posts = sorted(
        load_linkedin_posts(),
        key=lambda item: item[1].date or datetime.min.replace(tzinfo=UTC),
    )
    overrides = load_overrides()
    rows: list[dict[str, str]] = []
    ambiguous: list[dict[str, str]] = []
    matched = 0

    for index, (url, linkedin, linked_slugs) in enumerate(linkedin_posts, 1):
        best, second = blogs[:2]
        best_score = second_score = 0.0
        best_shared = second_shared = 0
        method = ""
        reason = ""
        is_match = False

        if url in overrides:
            override = overrides[url]
            if not override:
                method = "override_no_match"
            else:
                if override not in blogs_by_path:
                    raise ValueError(f"Override for {url} points to missing {override}")
                best = blogs_by_path[override]
                best_score, best_shared = score(linkedin, best)
                method = "override"
                is_match = True
        else:
            direct_matches = sorted(
                {
                    blogs_by_slug[slug].path: blogs_by_slug[slug]
                    for slug in linked_slugs
                    if slug in blogs_by_slug
                }.values(),
                key=lambda blog: blog.path,
            )
            frontmatter_matches = blogs_by_linkedin.get(url, [])
            if len(direct_matches) == 1:
                best = direct_matches[0]
                best_score, best_shared = score(linkedin, best)
                method = "direct_url"
                is_match = True
            elif len(direct_matches) > 1:
                best, second = direct_matches[:2]
                best_score, best_shared = score(linkedin, best)
                second_score, second_shared = score(linkedin, second)
                reason = "multiple_direct_urls"
            elif len(frontmatter_matches) == 1:
                best = frontmatter_matches[0]
                best_score, best_shared = score(linkedin, best)
                if best_score >= 0.5 or (
                    best_score >= 0.12 and is_eligible(linkedin, best, best_shared)
                ):
                    method = "frontmatter"
                    is_match = True
                else:
                    reason = "weak_frontmatter"
            elif len(frontmatter_matches) > 1:
                best, second = sorted(frontmatter_matches, key=lambda blog: blog.path)[
                    :2
                ]
                best_score, best_shared = score(linkedin, best)
                second_score, second_shared = score(linkedin, second)
                reason = "conflicting_frontmatter"
            else:
                candidates = rank_candidates(linkedin, blogs)
                best_score, best_shared, best = candidates[0]
                second_score, second_shared, second = candidates[1]
                delta = date_delta_days(linkedin, best)
                margin = best_score - second_score
                passes_score = best_score >= 0.32 or (
                    delta <= 14 and best_score >= 0.22
                )
                is_match = (
                    passes_score
                    and margin >= 0.04
                    and (best_score >= 0.8 or is_eligible(linkedin, best, best_shared))
                )
                if is_match:
                    method = "fuzzy"
                elif best_score >= 0.18 and is_eligible(linkedin, best, best_shared):
                    reason = "close_second" if margin < 0.04 else "near_threshold"

        delta = date_delta_days(linkedin, best)
        margin = best_score - second_score
        second_is_plausible = second_score >= 0.32 and is_eligible(
            linkedin, second, second_shared
        )
        if not reason and method == "fuzzy" and second_is_plausible and margin < 0.08:
            reason = "close_second"
        if reason:
            ambiguous.append(
                review_row(url, reason, best, best_score, delta, second, second_score)
            )
        if is_match:
            matched += 1
        rows.append(
            {
                "linkedin_url": url,
                "blog_filename": best.path if is_match else "",
                "linkedin_content": truncate(linkedin.content),
                "blog_content": truncate(best.content) if is_match else "",
                "match_method": method,
                "score": f"{best_score:.3f}" if is_match else "",
                "date_delta_days": f"{delta:.1f}" if is_match else "",
            }
        )
        if index % 25 == 0:
            print(f"Scored {index}/{len(linkedin_posts)} LinkedIn posts", flush=True)

    write_tsv(OUTPUT_PATH, rows, MAP_FIELDS)
    write_tsv(AMBIGUOUS_PATH, ambiguous, AMBIGUOUS_FIELDS)
    if not OVERRIDES_PATH.exists():
        write_tsv(OVERRIDES_PATH, [], OVERRIDE_FIELDS)
    if write_frontmatter:
        add_linkedin_metadata(rows)
    print(f"{OUTPUT_PATH.relative_to(ROOT)}: matched {matched}")
    print(f"{AMBIGUOUS_PATH.relative_to(ROOT)}: review {len(ambiguous)}")
    print(f"{OVERRIDES_PATH.relative_to(ROOT)}: add reviewed lines from below")
    print(
        "Keep or edit the second column to accept a match; leave it blank to mark no match."
    )
    for row in ambiguous:
        print(f"{row['linkedin_url']}\t{row['best_blog_filename']}")


def write_tsv(path: Path, rows: list[dict[str, str]], fields: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-frontmatter",
        action="store_true",
        help="Write only manual/direct URL mappings into blog front matter.",
    )
    main(write_frontmatter=parser.parse_args().write_frontmatter)
