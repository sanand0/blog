#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6.0", "typer>=0.12"]
# ///
"""Build static agent-facing exports."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Annotated
import json
import re

import typer
import yaml


app = typer.Typer(add_completion=False)
SITE_ROOT = "https://www.s-anand.net"
BLOG_ROOT = f"{SITE_ROOT}/blog"
URL_RE = re.compile(r"https://www\.s-anand\.net/[^\s)>\"]+")


def load_corpus(corpus_path: Path) -> list[dict]:
    """Load JSONL corpus records."""
    return [json.loads(line) for line in corpus_path.read_text(encoding="utf-8").splitlines()]


def load_tag_descriptions(metadata_tags_path: Path) -> dict[str, str]:
    """Read canonical tag descriptions."""
    data = yaml.safe_load(metadata_tags_path.read_text(encoding="utf-8")) or {}
    tags = data.get("tags", {})
    return {
        slug: str(info.get("description") or f"Posts about {slug.replace('-', ' ')}.")
        for slug, info in tags.items()
    }


def corpus_tag_counts(records: list[dict]) -> Counter[str]:
    """Count tags in public corpus records."""
    counts: Counter[str] = Counter()
    for record in records:
        counts.update(record.get("tags") or [])
    return counts


def rendered_tag_count(public_root: Path, slug: str) -> int | None:
    """Count entries in a rendered tag page when available."""
    path = public_root / f"blog/tag/{slug}/index.html"
    if not path.is_file():
        return None
    count = path.read_text(encoding="utf-8").count('class="post-entry tag-entry"')
    return count or None


def write_tags_json(
    records: list[dict],
    descriptions: dict[str, str],
    public_root: Path,
    output_path: Path,
) -> list[dict]:
    """Write canonical tags with public corpus counts."""
    corpus_counts = corpus_tag_counts(records)
    tags = [
        {
            "slug": slug,
            "url": f"{BLOG_ROOT}/tag/{slug}/",
            "count": rendered_tag_count(public_root, slug) or corpus_counts.get(slug, 0),
            "description": description,
        }
        for slug, description in descriptions.items()
        if (rendered_tag_count(public_root, slug) or corpus_counts.get(slug, 0)) > 0
    ]
    tags.sort(key=lambda item: (-item["count"], item["slug"]))
    output_path.write_text(
        json.dumps({"tags": tags}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return tags


def build_llms_txt(tags: list[dict], output_path: Path) -> str:
    """Write the llms.txt entrypoint."""
    lines = [
        "# S Anand",
        "",
        "S Anand's site is a long-running personal archive about technology, data visualization, education, AI, LLMs, books, work, and life, with canonical post URLs preserved back to the late 1990s.",
        "",
        "## Core Resources",
        "",
        f"- [About S Anand]({BLOG_ROOT}/s-anand/): short profile, contact links, recent posts, and update options.",
        f"- [Corpus JSONL]({BLOG_ROOT}/corpus.jsonl): one JSON record per public post or page, including plain text and raw Markdown source URL.",
        f"- [Corpus Schema]({BLOG_ROOT}/corpus.schema.json): field definitions for the corpus export.",
        f"- [Canonical Tags]({BLOG_ROOT}/tags.json): topic vocabulary with counts and descriptions.",
        f"- [Main RSS Feed]({BLOG_ROOT}/index.xml): latest posts feed.",
        "",
        "## Top Tags",
        "",
    ]
    for tag in tags[:15]:
        lines.append(f"- [{tag['slug']}]({tag['url']}): {tag['description']}")
    lines.extend(
        [
            "",
            "## Notes For Agents",
            "",
            "Every HTML page links its raw Markdown source in the head with `rel=\"alternate\" type=\"text/markdown\"`. Cite posts with their canonical URL from `corpus.jsonl`; the site is published as a no-copyright/CC0-style archive for broad reuse.",
            "",
        ]
    )
    text = "\n".join(lines)
    output_path.write_text(text, encoding="utf-8")
    return text


def public_path_for_url(url: str, public_root: Path) -> Path:
    """Map a site URL to its generated public path."""
    if url == f"{SITE_ROOT}/llms.txt":
        return public_root / "llms.txt"
    if not url.startswith(BLOG_ROOT + "/"):
        raise ValueError(f"URL is outside the site: {url}")
    path = url.removeprefix(BLOG_ROOT + "/")
    target = public_root / "blog" / path
    if url.endswith("/"):
        target = target / "index.html"
    return target


def validate_llms_links(text: str, public_root: Path) -> None:
    """Fail if llms.txt links do not resolve in public/."""
    missing = []
    for url in sorted(set(URL_RE.findall(text))):
        path = public_path_for_url(url.rstrip("."), public_root)
        if not path.is_file():
            missing.append(f"{url} -> {path}")
    if missing:
        raise FileNotFoundError("Broken llms.txt links:\n" + "\n".join(missing))


def build_agent_exports(
    public_root: Path = Path("public"),
    metadata_tags_path: Path = Path("metadata-tags.yml"),
) -> tuple[list[dict], str]:
    """Generate tags.json and llms.txt."""
    corpus_path = public_root / "blog/corpus.jsonl"
    if not corpus_path.is_file():
        raise FileNotFoundError(f"Missing corpus export: {corpus_path}")
    records = load_corpus(corpus_path)
    descriptions = load_tag_descriptions(metadata_tags_path)
    tags = write_tags_json(records, descriptions, public_root, public_root / "blog/tags.json")
    text = build_llms_txt(tags, public_root / "llms.txt")
    validate_llms_links(text, public_root)
    return tags, text


@app.command()
def main(
    public_root: Annotated[Path, typer.Option()] = Path("public"),
    metadata_tags_path: Annotated[Path, typer.Option()] = Path("metadata-tags.yml"),
) -> None:
    tags, _ = build_agent_exports(public_root, metadata_tags_path)
    typer.echo(f"agent-exports\t{len(tags)}\t{public_root / 'llms.txt'}")


if __name__ == "__main__":
    app()
