#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["beautifulsoup4>=4.12", "typer>=0.12"]
# ///
from __future__ import annotations

from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup
import typer


app = typer.Typer(add_completion=False)

START_MARKER = "<!-- wp-comments-start -->"
END_MARKER = "<!-- wp-comments-end -->"


def iter_html_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.html"):
        if path.is_file():
            yield path


def add_nofollow(block: str) -> tuple[str, int]:
    soup = BeautifulSoup(block, "html.parser")
    updated = 0
    for link in soup.find_all("a", href=True):
        rel = link.get("rel") or []
        if isinstance(rel, str):
            rel_values = rel.split()
        else:
            rel_values = list(rel)
        normalized = {value.lower() for value in rel_values}
        if "nofollow" not in normalized:
            rel_values.append("nofollow")
            link["rel"] = rel_values
            updated += 1
    return soup.decode_contents(), updated


def process_comments(html: str) -> tuple[str, int]:
    if START_MARKER not in html or END_MARKER not in html:
        return html, 0

    updated = 0
    cursor = 0
    output = []

    while True:
        start = html.find(START_MARKER, cursor)
        if start == -1:
            output.append(html[cursor:])
            break
        end = html.find(END_MARKER, start)
        if end == -1:
            output.append(html[cursor:])
            break

        output.append(html[cursor : start + len(START_MARKER)])
        block = html[start + len(START_MARKER) : end]
        updated_block, block_updates = add_nofollow(block)
        output.append(updated_block)
        updated += block_updates
        output.append(END_MARKER)
        cursor = end + len(END_MARKER)

    return "".join(output), updated


@app.command()
def apply(root: Path = Path("public/blog")) -> None:
    files = 0
    touched = 0
    links = 0

    for path in iter_html_files(root):
        original = path.read_text(encoding="utf-8")
        updated, link_updates = process_comments(original)
        files += 1
        if link_updates:
            path.write_text(updated, encoding="utf-8")
            touched += 1
            links += link_updates

    typer.echo(f"files\t{files}")
    typer.echo(f"updated\t{touched}")
    typer.echo(f"links\t{links}")


if __name__ == "__main__":
    app()
