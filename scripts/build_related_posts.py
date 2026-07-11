#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6.0", "scikit-learn>=1.6", "typer>=0.12"]
# ///
"""Build static related-post rankings without network access."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import json
import math
from pathlib import Path
import re
from typing import Annotated

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import typer
import yaml


app = typer.Typer(add_completion=False)
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"!?\[([^]]*)\]\([^)]*\)")
MARKUP_RE = re.compile(r"<[^>]+>|[`*_>#~|{}\[\]]")


@dataclass(frozen=True)
class Post:
    slug: str
    path: Path
    title: str
    description: str
    body: str
    tags: frozenset[str]


def clean_markdown(body: str) -> str:
    """Keep visible Markdown text while discarding common markup and link targets."""
    body = MARKDOWN_LINK_RE.sub(r"\1", body)
    return MARKUP_RE.sub(" ", body)


def parse_date(value: object) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).date()
    except ValueError:
        return None


def source_posts(posts_dir: Path = Path("posts")) -> list[Post]:
    """Load published posts and reject ambiguous slugs."""
    posts: list[Post] = []
    slug_paths: dict[str, Path] = {}
    for path in sorted(posts_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        match = FRONTMATTER_RE.match(text)
        if not match:
            continue
        data = yaml.safe_load(match.group(1)) or {}
        if not isinstance(data, dict) or data.get("draft") is True:
            continue
        published = parse_date(data.get("date"))
        if published and published > date.today():
            continue
        slug = str(data.get("slug") or (path.parent.name if path.stem.lower() in {"index", "readme"} else path.stem))
        if slug in slug_paths:
            raise ValueError(f"Slug collision for {slug!r}: {slug_paths[slug]} and {path}")
        slug_paths[slug] = path
        raw_tags = data.get("tags") or []
        tags = raw_tags if isinstance(raw_tags, list) else [raw_tags]
        posts.append(
            Post(
                slug=slug,
                path=path,
                title=str(data.get("title") or path.stem),
                description=str(data.get("description") or "").strip(),
                body=clean_markdown(text[match.end() :]),
                tags=frozenset(str(tag).casefold() for tag in tags if tag),
            )
        )
    return posts


def weighted_tag_jaccard(left: frozenset[str], right: frozenset[str], idf: dict[str, float]) -> float:
    union = left | right
    if not union:
        return 0.0
    return sum(idf[tag] for tag in left & right) / sum(idf[tag] for tag in union)


def build_related_posts(
    output_path: Path = Path("data/related-posts.json"),
    top_k: int = 5,
    posts_dir: Path = Path("posts"),
) -> dict[str, list[str]]:
    """Rank posts by weighted TF-IDF text similarity plus tag overlap."""
    posts = source_posts(posts_dir)
    if len(posts) < 2:
        related = {post.slug: [] for post in posts}
    else:
        documents = [" ".join([post.title] * 3 + [post.description] * 2 + [post.body]) for post in posts]
        vectors = TfidfVectorizer(strip_accents="unicode").fit_transform(documents)
        similarity = (vectors @ vectors.T).toarray()
        np.fill_diagonal(similarity, -np.inf)

        tag_counts = {tag: sum(tag in post.tags for post in posts) for post in posts for tag in post.tags}
        tag_idf = {tag: math.log((1 + len(posts)) / (1 + count)) + 1 for tag, count in tag_counts.items()}
        related = {}
        for source_index, source in enumerate(posts):
            scores = similarity[source_index].copy()
            for target_index, target in enumerate(posts):
                if source_index != target_index:
                    scores[target_index] += 0.03 * weighted_tag_jaccard(source.tags, target.tags, tag_idf)
            order = sorted(range(len(posts)), key=lambda index: (-scores[index], posts[index].slug))
            related[source.slug] = [posts[index].slug for index in order[: min(top_k, len(posts) - 1)]]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(related, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return related


@app.command()
def main(
    output_path: Annotated[Path, typer.Option()] = Path("data/related-posts.json"),
    top_k: Annotated[int, typer.Option()] = 5,
) -> None:
    related = build_related_posts(output_path, top_k)
    typer.echo(f"related-posts\t{len(related)}\t{output_path}")


if __name__ == "__main__":
    app()
