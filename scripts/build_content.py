#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6.0", "typer>=0.12"]
# ///
from __future__ import annotations

import calendar
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
import shutil
from typing import Any, Iterable

import typer
import yaml


app = typer.Typer(add_completion=False)

INDEX_FILENAMES = {"index", "readme"}


@dataclass
class MarkdownDoc:
    front_matter: dict[str, Any]
    body: str


def split_front_matter(text: str) -> MarkdownDoc:
    """Split Markdown into front matter and body, returning empty metadata if absent."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return MarkdownDoc(front_matter={}, body=text)

    end_index = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break
    if end_index is None:
        return MarkdownDoc(front_matter={}, body=text)

    front_text = "".join(lines[1:end_index])
    body = "".join(lines[end_index + 1 :])
    front_matter = yaml.safe_load(front_text) or {}
    if not isinstance(front_matter, dict):
        front_matter = {}
    return MarkdownDoc(front_matter=front_matter, body=body)


def render_front_matter(data: dict[str, Any]) -> str:
    """Render YAML front matter for Markdown output."""
    yaml_text = yaml.safe_dump(
        data, sort_keys=False, allow_unicode=True, default_flow_style=False
    ).strip()
    return f"---\n{yaml_text}\n---\n"


def derive_slug(path: Path) -> str:
    """Derive slug from the file name or parent folder for index files."""
    name = path.stem
    if name.lower() in INDEX_FILENAMES:
        name = path.parent.name
    return name


def parse_date(value: str) -> datetime | None:
    """Parse ISO or date-only values into datetimes for archive grouping."""
    if not value:
        return None
    value = value.strip()
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        pass
    for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


def write_markdown(path: Path, doc: MarkdownDoc, slug: str) -> None:
    """Write Markdown with updated slug front matter."""
    front_matter = dict(doc.front_matter)
    front_matter.pop("slug", None)
    front_matter["slug"] = slug
    body = doc.body.lstrip("\n")
    output = render_front_matter(front_matter)
    if body:
        output = output + "\n" + body
    if not output.endswith("\n"):
        output += "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")


def load_metadata(path: Path) -> dict[str, Any]:
    """Load site metadata from YAML, returning an empty dict on missing."""
    if not path.exists():
        return {}
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(payload, dict):
        return {}
    return payload


def write_index(path: Path, title: str, params: dict[str, Any] | None = None) -> None:
    """Write a simple _index.md with title and optional params."""
    data: dict[str, Any] = {"title": title}
    if params:
        data.update(params)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_front_matter(data), encoding="utf-8")


def write_term_pages(
    content_dir: Path,
    section: str,
    label: str,
    terms: Iterable[dict[str, Any]],
    slug_key: str = "slug",
    name_key: str = "name",
) -> None:
    """Write taxonomy-like index pages with display names."""
    base_dir = content_dir / section
    write_index(base_dir / "_index.md", label)
    seen: set[str] = set()
    for term in terms:
        slug = (term.get(slug_key) or "").strip()
        if not slug or slug in seen:
            continue
        seen.add(slug)
        name = (term.get(name_key) or "").strip() or slug
        write_index(base_dir / slug / "_index.md", name)


def write_posts_index(content_dir: Path, author_login: str | None) -> None:
    """Write posts section index with optional author cascade."""
    data: dict[str, Any] = {"title": "Posts"}
    if author_login:
        data["cascade"] = {"author": author_login}
    path = content_dir / "posts" / "_index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_front_matter(data), encoding="utf-8")


def write_archive_index(path: Path, title: str, params: dict[str, int]) -> None:
    """Write archive index pages for year/month/day groupings."""
    data = {"title": title, "type": "archive", **params}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_front_matter(data), encoding="utf-8")


def write_archives(content_dir: Path, dates: list[datetime]) -> None:
    """Generate archive index pages for all year/month/day buckets."""
    if not dates:
        return
    years = sorted({dt.year for dt in dates})
    months = sorted({(dt.year, dt.month) for dt in dates})
    days = sorted({(dt.year, dt.month, dt.day) for dt in dates})

    for year in years:
        write_archive_index(
            content_dir / f"{year}" / "_index.md",
            title=str(year),
            params={"year": year},
        )
    for year, month in months:
        title = f"{calendar.month_name[month]} {year}"
        write_archive_index(
            content_dir / f"{year}" / f"{month:02d}" / "_index.md",
            title=title,
            params={"year": year, "month": month},
        )
    for year, month, day in days:
        title = f"{calendar.month_name[month]} {day}, {year}"
        write_archive_index(
            content_dir / f"{year}" / f"{month:02d}" / f"{day:02d}" / "_index.md",
            title=title,
            params={"year": year, "month": month, "day": day},
        )


@app.command()
def build(
    metadata_path: Path = Path("metadata.yml"),
    posts_dir: Path = Path("posts"),
    pages_dir: Path = Path("pages"),
    content_dir: Path = Path("content"),
) -> None:
    """Generate Hugo content from posts/pages with slug injection."""
    if content_dir.exists():
        shutil.rmtree(content_dir)
    content_dir.mkdir(parents=True, exist_ok=True)

    metadata = load_metadata(metadata_path)
    categories = metadata.get("categories") or []
    tags = metadata.get("tags") or []
    authors = metadata.get("authors") or []

    write_term_pages(content_dir, "categories", "Categories", categories)
    write_term_pages(content_dir, "tags", "Tags", tags)
    write_term_pages(
        content_dir, "author", "Author", authors, slug_key="login", name_key="display_name"
    )

    author_login = ""
    if authors and isinstance(authors, list):
        author_login = (authors[0].get("login") or "").strip()
    write_posts_index(content_dir, author_login or None)

    post_dates: list[datetime] = []
    post_files = sorted(path for path in posts_dir.rglob("*.md") if path.is_file())
    for path in post_files:
        rel_path = path.relative_to(posts_dir)
        slug = derive_slug(rel_path)
        doc = split_front_matter(path.read_text(encoding="utf-8"))
        write_markdown(content_dir / "posts" / rel_path, doc, slug)
        date_value = doc.front_matter.get("date") or ""
        if isinstance(date_value, datetime):
            post_dates.append(date_value)
        elif isinstance(date_value, date):
            post_dates.append(datetime.combine(date_value, datetime.min.time()))
        elif isinstance(date_value, str):
            dt = parse_date(date_value)
            if dt:
                post_dates.append(dt)

    page_files = sorted(path for path in pages_dir.rglob("*.md") if path.is_file())
    for path in page_files:
        rel_path = path.relative_to(pages_dir)
        slug = derive_slug(rel_path)
        doc = split_front_matter(path.read_text(encoding="utf-8"))
        write_markdown(content_dir / rel_path, doc, slug)

    write_archives(content_dir, post_dates)

    typer.echo(f"posts\t{len(post_files)}")
    typer.echo(f"pages\t{len(page_files)}")
    typer.echo(f"content\t{content_dir}")


if __name__ == "__main__":
    app()
