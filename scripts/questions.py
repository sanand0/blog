#!/usr/bin/env -S uv run --script
"""Publish public questions into a page and matching weekly Things I Learned posts."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
import argparse
import re
import sys


TIL_HEADING = "Questions I was asked"
SITE_URL = "https://www.s-anand.net/blog/questions-i-am-asked/"
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
DATE_ROW_RE = re.compile(r"^- \d{1,2} \S+ \d{4}\. ")
ROW_RE = re.compile(
    r"^- (?P<day>\d{1,2} [A-Z][a-z]{2} \d{4})\. "
    r"(?P<speaker>.+?): #(?P<visibility>PUBLIC|PRIVATE) (?P<body>.+)$"
)
SPEAKER_RE = re.compile(r"^(?P<name>.+?)(?: \((?P<organization>[^()]*)\))?$")
TIL_RE = re.compile(r"^things-i-learned-(?P<day>\d{2}-[a-z]{3}-\d{4})\.md$")
HEADING_RE = re.compile(r"(?m)^#{1,6}[ \t]+(?P<title>.+?)[ \t]*$")


class ParseError(ValueError):
    """Raised when a dated source row cannot be parsed safely."""


class ManagedSectionError(ValueError): pass


@dataclass(frozen=True)
class Question:
    day: date
    name: str
    organization: str | None
    visibility: str
    question: str
    answer: str | None
    status: str | None
    order: int
    line: int


@dataclass(frozen=True)
class SyncResult:
    written: int
    page_changed: bool
    til_changed: int
    public_questions: int
    skipped_weeks: int


def _without_html_comments(markdown: str) -> str:
    """Remove HTML comments while preserving line numbers for diagnostics."""
    if markdown.count("<!--") != markdown.count("-->"):
        raise ParseError("unbalanced HTML comment markers")
    return COMMENT_RE.sub(lambda match: "\n" * match.group(0).count("\n"), markdown)


def parse_questions(markdown: str) -> list[Question]:
    """Parse all dated question rows outside HTML comments; reject malformed dated rows."""
    questions: list[Question] = []
    errors: list[str] = []
    for line_no, line in enumerate(_without_html_comments(markdown).splitlines(), 1):
        if not DATE_ROW_RE.match(line):
            continue
        match = ROW_RE.match(line)
        if not match:
            errors.append(f"line {line_no}: cannot parse dated row: {line}")
            continue
        speaker = SPEAKER_RE.match(match["speaker"])
        if not speaker:
            errors.append(f"line {line_no}: cannot parse speaker: {match['speaker']}")
            continue
        try:
            day = datetime.strptime(match["day"], "%d %b %Y").date()
        except ValueError as error:
            errors.append(f"line {line_no}: invalid date {match['day']}: {error}")
            continue

        body = match["body"].strip()
        answer: str | None = None
        status: str | None = None
        if " #ANS " in body:
            question, answer = body.split(" #ANS ", 1)
            status = "ANS"
        else:
            failed = re.match(r"^(?P<question>.*?)(?: #FAIL(?: (?P<answer>.*))?)$", body)
            if failed:
                question = failed["question"]
                answer = failed["answer"] or None
                status = "FAIL"
            else:
                question = body
        question = question.strip()
        answer = answer.strip() if answer else None
        if not question:
            errors.append(f"line {line_no}: empty question: {line}")
            continue
        questions.append(
            Question(
                day=day,
                name=speaker["name"].strip(),
                organization=(speaker["organization"] or "").strip() or None,
                visibility=match["visibility"],
                question=question,
                answer=answer,
                status=status,
                order=len(questions),
                line=line_no,
            )
        )
    if errors:
        raise ParseError("\n".join(errors))
    return questions


def week_ending(day: date) -> date:
    """Return the TIL Sunday covering the preceding Sunday-through-Saturday week."""
    return day + timedelta(days=7 - ((day.weekday() + 1) % 7))


def public_by_week(items: list[Question]) -> dict[date, list[Question]]:
    """Group public questions by TIL week, newest first within each week."""
    grouped: dict[date, list[Question]] = {}
    for item in items:
        if item.visibility == "PUBLIC":
            grouped.setdefault(week_ending(item.day), []).append(item)
    for values in grouped.values():
        values.sort(key=lambda item: (-item.day.toordinal(), item.order))
    return grouped


def _qa_line(item: Question) -> str:
    if item.answer:
        return f"- **Question**: {item.question}\\\n  **Answer**: {item.answer}"
    return f"- **Question**: {item.question}"


def render_page(items: list[Question]) -> str:
    """Render the complete anonymized public archive."""
    grouped = public_by_week(items)
    parts = [
        "---",
        "title: Questions I am asked",
        "description: Questions people ask me, and my answers.",
        "---",
        "",
        "# Questions I am asked",
        "",
        "Questions people ask me, with names, organizations, and exact dates removed.",
    ]
    for sunday in sorted(grouped, reverse=True):
        parts.extend(
            [
                "",
                f"## Week ending {sunday:%d %b %Y} {{#week-ending-{sunday:%Y-%m-%d}}}",
                "",
                *(_qa_line(item) for item in grouped[sunday]),
            ]
        )
    return "\n".join(parts) + "\n"


def render_til_block(sunday: date, items: list[Question]) -> str:
    """Render the public Q&A section for one TIL post."""
    link = f"{SITE_URL}#week-ending-{sunday:%Y-%m-%d}"
    return "\n".join(
        [f"## {TIL_HEADING}", "", f"[Week ending {sunday:%d %b %Y}]({link})", "", *(_qa_line(item) for item in items)]
    )


def replace_til_section(content: str, block: str | None) -> str:
    """Replace/remove the Questions I was asked Markdown section, wherever it appears."""
    headings = list(HEADING_RE.finditer(content))
    targets = [
        (index, match)
        for index, match in enumerate(headings)
        if re.sub(r"[ \t]+#+[ \t]*$", "", match["title"]).strip().casefold()
        == TIL_HEADING.casefold()
    ]
    if len(targets) > 1:
        raise ManagedSectionError(f"found {len(targets)} '{TIL_HEADING}' headings")
    if not targets:
        if block is None:
            return content
        separator = "" if content.endswith("\n\n") else "\n" if content.endswith("\n") else "\n\n"
        return f"{content}{separator}{block.rstrip()}\n"

    index, target = targets[0]
    end = headings[index + 1].start() if index + 1 < len(headings) else len(content)
    start = target.start() - (target.start() > 0 and content[target.start() - 1] == "\n")
    before = content[:start]
    if block is None:
        return before + ("\n" if end < len(content) and before.endswith("\n") else "") + content[end:]
    separator = "" if before.endswith("\n\n") else "\n" if before.endswith("\n") else "\n\n"
    replacement = separator + (f"{block.rstrip()}\n\n" if end < len(content) else f"{block.rstrip()}\n")
    return before + replacement + content[end:]


def _til_posts(posts_dir: Path) -> dict[date, Path]:
    posts: dict[date, Path] = {}
    for path in posts_dir.glob("*/things-i-learned-*.md"):
        match = TIL_RE.match(path.name)
        if match:
            sunday = datetime.strptime(match["day"], "%d-%b-%Y").date()
            posts[sunday] = path
    return posts


def sync(source: Path, page: Path, posts_dir: Path) -> SyncResult:
    """Plan all outputs, validate them, then write only byte-different files."""
    items = parse_questions(source.read_text(encoding="utf-8"))
    grouped = public_by_week(items)
    til_posts = _til_posts(posts_dir)

    planned: list[tuple[Path, str]] = [(page, render_page(items))]
    til_changed = 0
    for sunday, path in til_posts.items():
        current = path.read_text(encoding="utf-8")
        block = render_til_block(sunday, grouped[sunday]) if sunday in grouped else None
        desired = replace_til_section(current, block)
        planned.append((path, desired))

    changed = [(path, desired) for path, desired in planned if not path.exists() or path.read_text(encoding="utf-8") != desired]
    page_changed = any(path == page for path, _ in changed)
    til_changed = sum(path != page for path, _ in changed)

    for path, desired in changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(desired, encoding="utf-8")

    return SyncResult(
        written=len(changed),
        page_changed=page_changed,
        til_changed=til_changed,
        public_questions=sum(len(values) for values in grouped.values()),
        skipped_weeks=len(set(grouped) - set(til_posts)),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path.home() / "Dropbox/notes/questions-i-am-asked.md")
    parser.add_argument("--page", type=Path, default=Path("pages/questions-i-am-asked.md"))
    parser.add_argument("--posts-dir", type=Path, default=Path("posts"))
    args = parser.parse_args()
    try:
        result = sync(args.source, args.page, args.posts_dir)
    except ParseError as error:
        print(f"WARNING: parsing errors; no files written:\n{error}", file=sys.stderr)
        return 1
    except ManagedSectionError as error:
        print(f"WARNING: {error}; no files written", file=sys.stderr)
        return 1
    print(
        f"questions: {result.public_questions} public; {result.written} files written "
        f"({result.til_changed} TIL); {result.skipped_weeks} weeks have no TIL post"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
