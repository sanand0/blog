#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6.0", "typer>=0.12"]
# ///
"""Export a canonical JSONL corpus from generated Hugo content."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import html
import json
from pathlib import Path
import re
import tomllib
from typing import Annotated, Any
from urllib.parse import urlparse

import typer
import yaml


app = typer.Typer(add_completion=False)

DEFAULT_RAW_MARKDOWN_BASE = "https://raw.githubusercontent.com/sanand0/blog/main"
SCHEMA: dict[str, str] = {
    "slug": "Stable slug from the generated content front matter.",
    "url": "Absolute canonical HTML URL for the public page.",
    "title": "Page or post title.",
    "date": "Publication date from front matter, if present.",
    "lastmod": "Last modified date from front matter, if present.",
    "categories": "Category names from front matter.",
    "tags": "Tag names from front matter.",
    "description": "Short page description from front matter.",
    "word_count": "Approximate word count of the plain text body.",
    "source_markdown_url": "Absolute raw GitHub URL for the source Markdown.",
    "text": "Plain text body with Markdown and HTML markup stripped.",
}


@dataclass(frozen=True)
class MarkdownDoc:
    path: Path
    front_matter: dict[str, Any]
    body: str


def split_front_matter(path: Path) -> MarkdownDoc:
    """Split a Markdown file into YAML front matter and body."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return MarkdownDoc(path, {}, text)
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            payload = yaml.safe_load("".join(lines[1:index])) or {}
            front_matter = payload if isinstance(payload, dict) else {}
            return MarkdownDoc(path, front_matter, "".join(lines[index + 1 :]))
    return MarkdownDoc(path, {}, text)


def regular_content_files(content_dir: Path) -> list[Path]:
    """Return generated regular content pages, excluding section/taxonomy indexes."""
    return sorted(
        path
        for path in content_dir.rglob("*.md")
        if path.is_file() and path.name != "_index.md"
    )


def is_public_doc(doc: MarkdownDoc, today: date | None = None) -> bool:
    """Return whether Hugo publishes this regular content page by default."""
    if doc.front_matter.get("draft") is True:
        return False
    date_value = doc.front_matter.get("date")
    if isinstance(date_value, datetime):
        page_date = date_value.date()
    elif isinstance(date_value, date):
        page_date = date_value
    else:
        page_date = None
    return not page_date or page_date <= (today or date.today())


def as_list(value: Any) -> list[str]:
    """Return front matter scalars/sequences as a clean string list."""
    if value is None:
        return []
    if isinstance(value, list):
        items = value
    else:
        items = [value]
    return [str(item).strip() for item in items if str(item).strip()]


def serialize_date(value: Any) -> str:
    """Return dates as ISO strings and leave other scalar date values readable."""
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    return str(value).strip() if value else ""


def page_url(path: Path, content_dir: Path, base_url: str, front_matter: dict[str, Any]) -> str:
    """Return the canonical URL Hugo emits for a generated content file."""
    base = base_url.rstrip("/") + "/"
    rel = path.relative_to(content_dir)
    slug = str(front_matter.get("slug") or path.stem).strip()
    if rel.parts and rel.parts[0] == "posts":
        return f"{base}{slug}/"
    if slug:
        rel = rel.parent / slug
    else:
        rel = rel.with_suffix("")
    return f"{base}{rel.as_posix().lower()}/"


def public_file_for_url(url: str, public_dir: Path, base_url: str) -> Path:
    """Map an absolute site URL to the expected file under public/blog."""
    parsed_url = urlparse(url)
    parsed_base = urlparse(base_url.rstrip("/") + "/")
    base_path = parsed_base.path.rstrip("/") + "/"
    if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
        raise ValueError(f"URL is not absolute: {url}")
    if parsed_url.netloc != parsed_base.netloc or not parsed_url.path.startswith(base_path):
        raise ValueError(f"URL is outside base URL {base_url}: {url}")
    rel = parsed_url.path[len(base_path) :]
    if not rel or rel.endswith("/"):
        rel += "index.html"
    return public_dir / rel


def strip_markdown(markdown: str) -> str:
    """Produce compact plain text from Markdown body text."""
    text = re.sub(r"(?s)```.*?```", " ", markdown)
    text = re.sub(r"(?s)~~~.*?~~~", " ", text)
    text = re.sub(r"\{\{[%<].*?[%>]\}\}", " ", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"^[#>*\-\s]+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[*_~]+", "", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def source_markdown_url(front_matter: dict[str, Any], raw_markdown_base: str) -> str:
    """Return the raw GitHub Markdown URL for a generated sourcePath."""
    source_path = str(front_matter.get("sourcePath") or "").strip()
    if not source_path:
        return ""
    return f"{raw_markdown_base.rstrip('/')}/{source_path}"


def title_for_doc(doc: MarkdownDoc) -> str:
    """Return a non-empty title for agent-facing exports."""
    title = str(doc.front_matter.get("title") or "").strip()
    if title:
        return title
    slug = str(doc.front_matter.get("slug") or doc.path.stem).strip()
    return slug.replace("-", " ").strip().capitalize()


def record_for_doc(
    doc: MarkdownDoc, content_dir: Path, public_dir: Path, base_url: str, raw_markdown_base: str
) -> dict[str, Any]:
    """Build and validate one corpus record."""
    text = strip_markdown(doc.body)
    url = page_url(doc.path, content_dir, base_url, doc.front_matter)
    public_file = public_file_for_url(url, public_dir, base_url)
    if not public_file.is_file():
        raise FileNotFoundError(f"{url} maps to missing public file: {public_file}")
    return {
        "slug": str(doc.front_matter.get("slug") or doc.path.stem),
        "url": url,
        "title": title_for_doc(doc),
        "date": serialize_date(doc.front_matter.get("date")),
        "lastmod": serialize_date(doc.front_matter.get("lastmod")),
        "categories": as_list(doc.front_matter.get("categories")),
        "tags": as_list(doc.front_matter.get("tags")),
        "description": str(doc.front_matter.get("description") or "").strip(),
        "word_count": len(re.findall(r"\b[\w'-]+\b", text)),
        "source_markdown_url": source_markdown_url(doc.front_matter, raw_markdown_base),
        "text": text,
    }


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    """Write UTF-8 JSONL with one object per line."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def export_corpus(
    content_dir: Path = Path("content"),
    public_dir: Path = Path("public/blog"),
    base_url: str = "https://www.s-anand.net/blog/",
    raw_markdown_base: str = DEFAULT_RAW_MARKDOWN_BASE,
    today: date | None = None,
) -> list[dict[str, Any]]:
    """Export corpus files and fail if the output does not match generated content."""
    docs = [
        doc
        for doc in (split_front_matter(path) for path in regular_content_files(content_dir))
        if is_public_doc(doc, today)
    ]
    records = [
        record_for_doc(doc, content_dir, public_dir, base_url, raw_markdown_base) for doc in docs
    ]
    if len(records) != len(docs):
        raise RuntimeError(f"corpus count {len(records)} != public content count {len(docs)}")
    write_jsonl(public_dir / "corpus.jsonl", records)
    (public_dir / "corpus.schema.json").write_text(
        json.dumps(SCHEMA, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return records


def load_hugo_config(path: Path) -> tuple[str, str]:
    """Read baseURL and raw Markdown base from hugo.toml."""
    payload = tomllib.loads(path.read_text(encoding="utf-8"))
    base_url = str(payload.get("baseURL") or "https://www.s-anand.net/blog/")
    raw_markdown_base = (
        str(payload.get("params", {}).get("github", {}).get("rawMarkdownBase") or "")
        or DEFAULT_RAW_MARKDOWN_BASE
    )
    return base_url, raw_markdown_base


@app.command()
def main(
    content_dir: Annotated[Path, typer.Option()] = Path("content"),
    public_dir: Annotated[Path, typer.Option()] = Path("public/blog"),
    hugo_config: Annotated[Path, typer.Option()] = Path("hugo.toml"),
) -> None:
    """Write public/blog/corpus.jsonl and public/blog/corpus.schema.json."""
    base_url, raw_markdown_base = load_hugo_config(hugo_config)
    records = export_corpus(content_dir, public_dir, base_url, raw_markdown_base)
    typer.echo(f"corpus\t{len(records)}\t{public_dir / 'corpus.jsonl'}")


if __name__ == "__main__":
    app()
