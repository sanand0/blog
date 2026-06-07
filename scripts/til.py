#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.12"]
# ///
"""Create weekly blog posts from ~/code/til/{til,llms}.md."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta
import difflib
import json
from pathlib import Path
import re
from typing import Annotated

import typer


app = typer.Typer(add_completion=False, no_args_is_help=False)
NOTE_RE = re.compile(r"^- (?P<day>\d{1,2} [A-Za-z]{3} \d{4})\.\s*(?P<body>.*)$")


@dataclass(frozen=True)
class Note:
    day: date
    body: str
    order: int


@dataclass
class Result:
    sunday: str
    start: str
    end: str
    notes: int
    path: str
    status: str
    diff: str | None = None


def extract_notes(markdown: str) -> list[Note]:
    """Extract dated top-level bullets and their indented continuation lines."""
    notes: list[Note] = []
    current: Note | None = None
    for line in markdown.splitlines():
        match = NOTE_RE.match(line)
        if match:
            current = Note(
                day=datetime.strptime(match["day"], "%d %b %Y").date(),
                body=f"- {match['body']}",
                order=len(notes),
            )
            notes.append(current)
        elif current and line.startswith("  "):
            current = Note(current.day, f"{current.body}\n{line}", current.order)
            notes[-1] = current
        else:
            current = None
    return notes


def target_sundays(
    week: date | None = None,
    start: date | None = None,
    end: date | None = None,
    today: date | None = None,
) -> list[date]:
    """Return one Sunday or every Sunday in an inclusive target-Sunday range."""
    if week and (start or end):
        raise ValueError("--week cannot be combined with --start or --end")
    if bool(start) != bool(end):
        raise ValueError("--start and --end must be used together")
    if week:
        start = end = week
    if not start:
        current = today or date.today()
        start = end = current - timedelta(days=(current.weekday() + 1) % 7)
    if start.weekday() != 6 or end.weekday() != 6:
        raise ValueError("Target dates must be Sundays")
    if start > end:
        raise ValueError("--start must not be after --end")
    return [start + timedelta(days=offset) for offset in range(0, (end - start).days + 1, 7)]


def covered_sundays(notes: list[Note]) -> list[date]:
    """Return target Sundays for every week containing at least one note."""
    return sorted(
        {
            note.day + timedelta(days=7 - ((note.day.weekday() + 1) % 7))
            for note in notes
        }
    )


def load_notes(paths: list[Path]) -> list[Note]:
    """Load notes from source files, preserving source order for date ties."""
    notes: list[Note] = []
    for path in paths:
        if not path.is_file():
            raise FileNotFoundError(f"Source not found: {path}")
        for note in extract_notes(path.read_text(encoding="utf-8")):
            notes.append(Note(note.day, note.body, len(notes)))
    return notes


def render_post(sunday: date, sources: list[Path], notes: list[Note] | None = None) -> str:
    """Render the post for the Sunday covering the preceding Sunday through Saturday."""
    start = sunday - timedelta(days=7)
    available_notes = notes if notes is not None else load_notes(sources)
    notes = sorted(
        (note for note in available_notes if start <= note.day < sunday),
        key=lambda note: (-note.day.toordinal(), note.order),
    )
    body = "\n".join(note.body for note in notes)
    return (
        "---\n"
        f"title: Things I Learned - {sunday:%d %b %Y}\n"
        f"date: {sunday:%Y-%m-%d}T00:00:00+00:00\n"
        "categories:\n"
        "  - til\n"
        "---\n\n"
        "This week, I learned:\n\n"
        f"{body}\n"
    )


def write_post(path: Path, content: str, force: bool) -> None:
    """Write a post, refusing to replace an existing file unless forced."""
    if path.exists() and not force:
        raise FileExistsError(f"Post exists; use --force to replace it: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def file_diff(path: Path, generated: str) -> str:
    """Return a unified diff of the entire existing and generated files."""
    return "".join(
        difflib.unified_diff(
            path.read_text(encoding="utf-8").splitlines(keepends=True),
            generated.splitlines(keepends=True),
            fromfile=str(path),
            tofile=f"{path} (generated)",
        )
    )


def describe() -> dict[str, object]:
    """Return the CLI contract for agents."""
    return {
        "default": "Generate the most recent Sunday, covering the preceding Sunday through Saturday",
        "options": {
            "--all": "Generate every week containing at least one source note",
            "--week YYYY-MM-DD": "Generate one target Sunday",
            "--start YYYY-MM-DD --end YYYY-MM-DD": "Generate an inclusive range of target Sundays",
            "--source-dir PATH": "Directory containing til.md and llms.md",
            "--posts-dir PATH": "Blog posts directory",
            "--dry-run": "Report without writing",
            "--force": "Replace existing posts; otherwise show their full-file diffs",
            "--format json|text": "Output format",
        },
    }


def parse_iso_date(value: str | None, option: str) -> date | None:
    """Parse a YYYY-MM-DD CLI value."""
    if value is None:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"{option} must be YYYY-MM-DD: {value}") from error


@app.command()
def main(
    week: Annotated[str | None, typer.Option(help="One target Sunday (YYYY-MM-DD).")] = None,
    start: Annotated[str | None, typer.Option(help="First target Sunday (YYYY-MM-DD).")] = None,
    end: Annotated[str | None, typer.Option(help="Last target Sunday (YYYY-MM-DD).")] = None,
    all_: Annotated[bool, typer.Option("--all", help="Every week containing notes.")] = False,
    source_dir: Annotated[Path, typer.Option()] = Path.home() / "code/til",
    posts_dir: Annotated[Path, typer.Option()] = Path("posts"),
    dry_run: Annotated[bool, typer.Option()] = False,
    force: Annotated[bool, typer.Option()] = False,
    format_: Annotated[str, typer.Option("--format")] = "json",
    describe_: Annotated[bool, typer.Option("--describe")] = False,
) -> None:
    """Create Things I Learned weekly posts."""
    if describe_:
        typer.echo(json.dumps(describe(), indent=2))
        return
    if format_ not in {"json", "text"}:
        raise typer.BadParameter("must be json or text", param_hint="--format")
    try:
        sources = [source_dir / "til.md", source_dir / "llms.md"]
        notes = load_notes(sources)
        if all_ and (week or start or end):
            raise ValueError("--all cannot be combined with --week, --start, or --end")
        sundays = (
            covered_sundays(notes)
            if all_
            else target_sundays(
                parse_iso_date(week, "--week"),
                parse_iso_date(start, "--start"),
                parse_iso_date(end, "--end"),
            )
        )
        planned = []
        for sunday in sundays:
            path = posts_dir / str(sunday.year) / f"things-i-learned-{sunday:%d-%b-%Y}.md".lower()
            content = render_post(sunday, sources, notes)
            exists = path.exists()
            diff = file_diff(path, content) if exists and not force else None
            result = Result(
                sunday=sunday.isoformat(),
                start=(sunday - timedelta(days=7)).isoformat(),
                end=(sunday - timedelta(days=1)).isoformat(),
                notes=sum(
                    1
                    for line in content.split("This week, I learned:\n\n", 1)[1].splitlines()
                    if line.startswith("- ")
                ),
                path=str(path),
                status=(
                    "would-overwrite"
                    if exists and (force or diff)
                    else "unchanged"
                    if exists
                    else "would-create"
                ),
                diff=diff,
            )
            planned.append((path, content, result))
        if not dry_run:
            for path, content, result in planned:
                if not path.exists() or force:
                    existed = path.exists()
                    write_post(path, content, force)
                    result.status = "overwritten" if existed else "written"
    except (FileNotFoundError, FileExistsError, ValueError) as error:
        raise typer.BadParameter(str(error)) from error

    results = [asdict(result) for _, _, result in planned]
    if format_ == "json":
        typer.echo(json.dumps(results, indent=2))
    else:
        for result in results:
            typer.echo(
                f"{result['status']}\t{result['notes']}\t{result['start']}..{result['end']}\t{result['path']}"
            )
            if result["diff"]:
                typer.echo(result["diff"], nl=False)


if __name__ == "__main__":
    app()
