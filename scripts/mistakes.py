#!/usr/bin/env -S uv run --script
"""Publish public mistakes into an archive page and matching weekly TIL posts."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

TIL_HEADING = "Mistakes I made"
SITE_URL = "https://www.s-anand.net/blog/mistakes-i-made/"
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
ROW_RE = re.compile(
    r"^- (?P<day>\d{1,2} \S+ \d{4})\. (?P<tags>(?:#\S+\s+)*)(?P<body>.+)$"
)
TIL_RE = re.compile(r"^things-i-learned-(?P<day>\d{2}-[a-z]{3}-\d{4})\.md$")
HEADING_RE = re.compile(r"(?m)^#{1,6}[ \t]+(?P<title>.+?)[ \t]*$")


class ParseError(ValueError):
    """Raised when a dated source row cannot be parsed safely."""


@dataclass(frozen=True)
class Mistake:
    day: date
    public: bool
    tags: tuple[str, ...]
    claim: str
    correction: str


@dataclass(frozen=True)
class SyncResult:
    written: int
    til_changed: int
    public_mistakes: int
    skipped_weeks: int


def _without_html_comments(markdown: str) -> str:
    """Remove HTML comments while preserving line numbers for diagnostics."""
    if markdown.count("<!--") != markdown.count("-->"):
        raise ParseError("unbalanced HTML comment markers")
    return COMMENT_RE.sub(lambda match: "\n" * match.group(0).count("\n"), markdown)


def parse_mistakes(markdown: str) -> list[Mistake]:
    """Parse date, leading tags, and the text on either side of #FIX."""
    mistakes: list[Mistake] = []
    for line_no, line in enumerate(_without_html_comments(markdown).splitlines(), 1):
        if not (match := ROW_RE.match(line)):
            continue
        try:
            day = datetime.strptime(match["day"], "%d %b %Y").date()  # noqa: DTZ007
        except ValueError as error:
            raise ParseError(
                f"line {line_no}: invalid date {match['day']}: {error}"
            ) from error

        tags = tuple(tag[1:] for tag in match["tags"].split())
        visibility = {tag.upper() for tag in tags} & {"PUBLIC", "PRIVATE"}
        if len(visibility) != 1:
            raise ParseError(f"line {line_no}: expected #PUBLIC or #PRIVATE: {line}")

        claim, marker, correction = match["body"].partition(" #FIX ")
        if not marker or not claim.strip() or not correction.strip():
            raise ParseError(f"line {line_no}: expected text #FIX text: {line}")
        mistakes.append(
            Mistake(
                day=day,
                public="PUBLIC" in visibility,
                tags=tuple(
                    tag for tag in tags if tag.upper() not in {"PUBLIC", "PRIVATE"}
                ),
                claim=claim.strip(),
                correction=correction.strip(),
            )
        )
    return mistakes


def week_ending(day: date) -> date:
    """Return the Sunday ending the Sunday-through-Saturday TIL week containing day."""
    return day + timedelta(days=7 - ((day.weekday() + 1) % 7))


def public_by_week(items: list[Mistake]) -> dict[date, list[Mistake]]:
    """Group public mistakes by TIL week, newest first within each week."""
    grouped: dict[date, list[Mistake]] = {}
    for item in items:
        if item.public:
            grouped.setdefault(week_ending(item.day), []).append(item)
    for values in grouped.values():
        values.sort(key=lambda item: item.day, reverse=True)
    return grouped


def render_entry(item: Mistake) -> str:
    """Render source wording, correction, then source tags."""
    lines = [f"- {item.claim}\\", f"  **Correction**: {item.correction}"]
    if item.tags:
        lines[-1] += "\\"
        lines.append(f"  **{' · '.join(item.tags)}**")
    return "\n".join(lines)


def render_page(items: list[Mistake]) -> str:
    """Render the complete public mistakes archive."""
    grouped = public_by_week(items)
    parts = [
        "---",
        "title: Mistakes I made",
        "description: Factual claims I got wrong, overstated, or could not support, with corrections.",
        "---",
        "",
        "# Mistakes I made",
        "",
        "What I got wrong, and what I should say instead. This excludes opinions, predictions, harmless approximations, and debatable claims.",
    ]
    for sunday in sorted(grouped, reverse=True):
        parts.extend(
            [
                "",
                f"## Week ending {sunday:%d %b %Y} {{#week-ending-{sunday:%Y-%m-%d}}}",
                "",
                *(render_entry(item) for item in grouped[sunday]),
            ]
        )
    return "\n".join(parts) + "\n"


def render_til_block(sunday: date, items: list[Mistake]) -> str:
    """Render the public mistakes section for one TIL post."""
    link = f"{SITE_URL}#week-ending-{sunday:%Y-%m-%d}"
    return "\n".join(
        [
            f"## {TIL_HEADING}",
            "",
            f"[Week ending {sunday:%d %b %Y}]({link})",
            "",
            *(render_entry(item) for item in items),
        ]
    )


def replace_til_section(content: str, block: str | None) -> str:
    """Replace/remove the managed Mistakes I made Markdown section, wherever it appears."""
    headings = list(HEADING_RE.finditer(content))
    targets = [
        (index, match)
        for index, match in enumerate(headings)
        if re.sub(r"[ \t]+#+[ \t]*$", "", match["title"]).strip().casefold()
        == TIL_HEADING.casefold()
    ]
    if len(targets) > 1:
        raise ParseError(f"found {len(targets)} '{TIL_HEADING}' headings")
    if not targets:
        if block is None:
            return content
        separator = (
            ""
            if content.endswith("\n\n")
            else "\n"
            if content.endswith("\n")
            else "\n\n"
        )
        return f"{content}{separator}{block.rstrip()}\n"

    index, target = targets[0]
    end = headings[index + 1].start() if index + 1 < len(headings) else len(content)
    start = target.start() - (
        target.start() > 0 and content[target.start() - 1] == "\n"
    )
    before = content[:start]
    if block is None:
        return (
            before
            + ("\n" if end < len(content) and before.endswith("\n") else "")
            + content[end:]
        )
    separator = (
        "" if before.endswith("\n\n") else "\n" if before.endswith("\n") else "\n\n"
    )
    replacement = separator + (
        f"{block.rstrip()}\n\n" if end < len(content) else f"{block.rstrip()}\n"
    )
    return before + replacement + content[end:]


def _til_posts(posts_dir: Path) -> dict[date, Path]:
    posts: dict[date, Path] = {}
    for path in posts_dir.glob("*/things-i-learned-*.md"):
        match = TIL_RE.match(path.name)
        if match:
            sunday = datetime.strptime(match["day"], "%d-%b-%Y").date()  # noqa: DTZ007
            posts[sunday] = path
    return posts


def sync(source: Path, page: Path, posts_dir: Path) -> SyncResult:
    """Plan all outputs, validate them, then write only byte-different files."""
    items = parse_mistakes(source.read_text(encoding="utf-8"))
    grouped = public_by_week(items)
    til_posts = _til_posts(posts_dir)

    planned: list[tuple[Path, str]] = [(page, render_page(items))]
    for sunday, path in til_posts.items():
        current = path.read_text(encoding="utf-8")
        block = render_til_block(sunday, grouped[sunday]) if sunday in grouped else None
        planned.append((path, replace_til_section(current, block)))

    changed = [
        (path, desired)
        for path, desired in planned
        if not path.exists() or path.read_text(encoding="utf-8") != desired
    ]
    til_changed = sum(path != page for path, _ in changed)
    for path, desired in changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(desired, encoding="utf-8")

    return SyncResult(
        written=len(changed),
        til_changed=til_changed,
        public_mistakes=sum(len(values) for values in grouped.values()),
        skipped_weeks=len(set(grouped) - set(til_posts)),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", type=Path, default=Path.home() / "Dropbox/notes/mistakes-i-made.md"
    )
    parser.add_argument("--page", type=Path, default=Path("pages/mistakes-i-made.md"))
    parser.add_argument("--posts-dir", type=Path, default=Path("posts"))
    args = parser.parse_args()
    try:
        result = sync(args.source, args.page, args.posts_dir)
    except ParseError as error:
        print(f"WARNING: {error}; no files written", file=sys.stderr)
        return 1
    print(
        f"mistakes: {result.public_mistakes} public; {result.written} files written "
        f"({result.til_changed} TIL); {result.skipped_weeks} weeks without TIL posts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
