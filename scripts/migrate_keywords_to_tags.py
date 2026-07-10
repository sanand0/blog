#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["ruamel.yaml>=0.18", "typer>=0.12", "pyyaml>=6.0"]
# ///
"""One-time migration from front matter keywords to canonical tags."""

from __future__ import annotations

from dataclasses import dataclass
from io import StringIO
from pathlib import Path
import re
from typing import Annotated, Any

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq
import typer
import yaml


app = typer.Typer(add_completion=False)
ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
MULTI_HYPHEN_RE = re.compile(r"-+")
MANUAL_ALIASES = {
    "artificial-intelligence": "ai",
    "large-language-model": "llms",
    "large-language-models": "llms",
    "llm": "llms",
    "visualisation": "data-visualization",
    "visualization": "data-visualization",
    "data-visualisation": "data-visualization",
    "dataviz": "data-visualization",
    "books": "book",
    "genai": "generative-ai",
    "gen-ai": "generative-ai",
}


@dataclass(frozen=True)
class MarkdownDoc:
    front_text: str
    body: str
    metadata: CommentedMap


def make_yaml() -> YAML:
    """Return a ruamel parser matching summarize.py's front matter behavior."""
    parser = YAML()
    parser.preserve_quotes = True
    parser.default_flow_style = False
    parser.width = 100000
    return parser


def parse_doc(text: str) -> MarkdownDoc | None:
    """Parse front matter while preserving the raw front matter text."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    metadata = make_yaml().load(match.group(1)) or CommentedMap()
    if not isinstance(metadata, CommentedMap):
        return None
    return MarkdownDoc(front_text=match.group(1), body=text[match.end() :], metadata=metadata)


def dump_key(key: str, value: list[str]) -> str:
    """Render one YAML key with ruamel."""
    data = CommentedMap()
    seq = CommentedSeq(value)
    seq.fa.set_flow_style()
    data[key] = seq
    stream = StringIO()
    make_yaml().dump(data, stream)
    return stream.getvalue()


def top_level_key_span(front_text: str, key: str) -> tuple[int, int] | None:
    """Return byte offsets for a top-level YAML key block in front_text."""
    lines = front_text.splitlines(keepends=True)
    start = None
    offset = 0
    for index, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}\s*:", line):
            start = offset
            break
        offset += len(line)
    if start is None:
        return None
    end = offset + len(lines[index])
    for line in lines[index + 1 :]:
        if line and not line.startswith((" ", "\t", "-")) and re.match(r"^[A-Za-z0-9_-]+\s*:", line):
            break
        end += len(line)
    return start, end


def as_list(value: Any) -> list[str]:
    """Return front matter scalars/sequences as strings."""
    if value is None:
        return []
    items = value if isinstance(value, list) else [value]
    return [str(item).strip() for item in items if str(item).strip()]


def normalize_slug(value: str) -> str:
    """Match normalize_tags.py slug rules for migration."""
    text = value.strip().lower()
    text = text.replace("&", " and ")
    text = text.replace("+", " plus ")
    text = text.replace("'", "")
    text = NON_ALNUM_RE.sub("-", text)
    text = MULTI_HYPHEN_RE.sub("-", text).strip("-")
    return MANUAL_ALIASES.get(text, text)


def load_tag_map(path: Path) -> tuple[set[str], dict[str, str]]:
    """Load canonical tags plus migration aliases from metadata-tags.yml."""
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    tags = payload.get("tags") or {}
    canonical = set(tags)
    alias_to_canonical = {tag: tag for tag in canonical}
    for tag, details in tags.items():
        for alias in details.get("aliases") or []:
            alias_to_canonical[normalize_slug(str(alias))] = tag
    return canonical, alias_to_canonical


def migrate_tags(keywords: list[str], existing_tags: list[str], canonical: set[str], aliases: dict[str, str]) -> list[str]:
    """Map old keywords and existing tags to canonical tag slugs."""
    output: list[str] = []
    for raw in [*existing_tags, *keywords]:
        slug = normalize_slug(raw)
        tag = aliases.get(slug) or (slug if slug in canonical else "")
        if tag and tag not in output:
            output.append(tag)
    return output


def migrate_text(text: str, canonical: set[str], aliases: dict[str, str]) -> tuple[str, bool]:
    """Return migrated Markdown text and whether it changed."""
    doc = parse_doc(text)
    if doc is None or "keywords" not in doc.metadata:
        return text, False
    keywords = as_list(doc.metadata.get("keywords"))
    existing_tags = as_list(doc.metadata.get("tags"))
    tags = migrate_tags(keywords, existing_tags, canonical, aliases)

    keyword_span = top_level_key_span(doc.front_text, "keywords")
    if keyword_span is None:
        return text, False
    tag_span = top_level_key_span(doc.front_text, "tags")
    front_text = doc.front_text
    replacement = dump_key("tags", tags) if tags else ""

    if tag_span:
        start, end = tag_span
        front_text = front_text[:start] + replacement + front_text[end:]
        keyword_span = top_level_key_span(front_text, "keywords")
        if keyword_span is None:
            new_text = front_text
        else:
            start, end = keyword_span
            new_text = front_text[:start] + front_text[end:]
    else:
        start, end = keyword_span
        new_text = front_text[:start] + replacement + front_text[end:]

    new_text = new_text.strip("\n")
    return f"---\n{new_text}\n---\n\n{doc.body.lstrip(chr(10))}", True


def source_files(root: Path = ROOT) -> list[Path]:
    """Return source posts/pages markdown files."""
    return sorted([*(root / "posts").rglob("*.md"), *(root / "pages").rglob("*.md")])


def migrate_files(root: Path, tags_path: Path, dry_run: bool = False) -> dict[str, int]:
    """Migrate all posts/pages and return counts."""
    canonical, aliases = load_tag_map(tags_path)
    counts = {"checked": 0, "changed": 0}
    for path in source_files(root):
        counts["checked"] += 1
        original = path.read_text(encoding="utf-8")
        migrated, changed = migrate_text(original, canonical, aliases)
        if changed:
            counts["changed"] += 1
            if not dry_run:
                path.write_text(migrated, encoding="utf-8")
    return counts


@app.command()
def main(
    tags_path: Annotated[Path, typer.Option()] = ROOT / "metadata-tags.yml",
    dry_run: Annotated[bool, typer.Option("--dry-run")] = False,
) -> None:
    """Rewrite source front matter from keywords to tags."""
    counts = migrate_files(ROOT, tags_path, dry_run)
    status = "would-change" if dry_run else "changed"
    typer.echo(f"checked\t{counts['checked']}\t{status}\t{counts['changed']}")


if __name__ == "__main__":
    app()
