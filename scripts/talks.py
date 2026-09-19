#!/usr/bin/env -S uv run --script
"""Create deterministic blog posts for the latest talks in ~/code/talks/config.json.

Existing files are never modified. `talk_url` in blog front matter is the explicit
one-to-one marker that a session already has a blog post.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
import unicodedata

TALKS_BASE = "https://talks.s-anand.net/"
ROOT = Path(__file__).resolve().parents[1]


def absolute_url(url: str) -> str:
    return url if url.startswith(("http://", "https://")) else TALKS_BASE + url.lstrip("/")


def slugify(text: str) -> str:
    ascii_text = (
        unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    )
    ascii_text = ascii_text.replace("'", "")
    return re.sub(r"(^-|-$)", "", re.sub(r"[^a-z0-9]+", "-", ascii_text))


def source_link(talk: dict) -> tuple[int | None, dict | None]:
    links = talk.get("links", [])
    for index, link in enumerate(links):
        if link.get("primary"):
            return index, link
    return (0, links[0]) if links else (None, None)


def talk_url(talk: dict) -> str:
    _, link = source_link(talk)
    return absolute_url(link["url"]) if link else ""


def yaml_value(value) -> str:
    """JSON is valid YAML and gives deterministic quoting without a YAML dependency."""
    return json.dumps(value, ensure_ascii=False, separators=(", ", ": "))


def link_label(link: dict) -> str:
    if link.get("label"):
        return link["label"]
    return {
        "page": "Page",
        "video": "Video",
        "transcript": "Transcript",
        "audio": "Audio",
        "slides": "Slides",
        "code": "Code",
        "chat": "Chat",
        "screencast": "Screencast",
    }.get(link.get("type"), str(link.get("type") or "Link").title())


def image_label(image: dict) -> str:
    kind = str(image.get("type") or "image").replace("-", " ")
    label = str(image.get("label") or "").strip()
    if label and kind.lower() in label.lower():
        return label.title()
    return f"{label} {kind}".strip().title()


def session_datetime(talk: dict) -> str:
    """Use the catalog time, or noon IST when no session time is known."""
    return str(talk.get("time") or f"{talk['date']}T12:00:00+05:30")


def display_date(value: str) -> str:
    day = date.fromisoformat(value)
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{weekdays[day.weekday()]}, {day.day:02d} {months[day.month - 1]} {day.year}"


def talk_description(talk: dict) -> str:
    details = str(talk.get("details") or "").strip()
    if details:
        return details
    parts = [talk["title"]]
    if talk.get("event", {}).get("name"):
        parts.append(talk["event"]["name"])
    if talk.get("location"):
        parts.append(talk["location"])
    return " — ".join(parts)


def render_post(talk: dict) -> str:
    source_index, _ = source_link(talk)
    source = talk_url(talk)
    description = talk_description(talk)

    front = [
        "---",
        f"title: {yaml_value(talk['title'])}",
        f"date: {yaml_value(session_datetime(talk))}",
        "categories:",
        "- talks",
        "tags: []",
        f"description: {yaml_value(description)}",
        f"talk_url: {yaml_value(source)}",
        "---",
        "",
    ]

    body: list[str] = []
    event = talk.get("event")
    location = str(talk.get("location") or "").strip()

    if event:
        name = event["name"]
        event_text = f"[{name}]({event['url']})" if event.get("url") else name
        when = display_date(talk["date"])
        intro = f"I conducted a session on {when} at {event_text}"
        if location:
            intro += f" - {location}"
        body += [intro + ".", ""]
    elif location:
        when = display_date(talk["date"])
        body += [f"I conducted a session on {when} at {location}.", ""]

    if talk.get("speakers"):
        people = []
        for speaker in talk["speakers"]:
            name = speaker["name"]
            people.append(f"[{name}]({speaker['url']})" if speaker.get("url") else name)
        body += [f"**Speakers**: {', '.join(people)}", ""]

    body += [f"**Summary**: {description}", ""]

    if source:
        body += [f"[Here's the link to the session]({source})", ""]

    target = source or None
    for image in talk.get("images", []):
        image_url = absolute_url(image["url"])
        body.append(
            f"[![{image_label(image)}]({image_url})]({target or image_url})"
        )
        body.append("")

    other_links = [
        link
        for index, link in enumerate(talk.get("links", []))
        if index != source_index
    ]
    if other_links:
        body += ["**Links**:", ""]
        for link in other_links:
            suffix = f" ({link['minutes']} min)" if link.get("minutes") else ""
            body.append(
                f"- [{link_label(link)}]({absolute_url(link['url'])}){suffix}"
            )
        body.append("")

    return "\n".join(front + body).rstrip() + "\n"


def covered_talk_urls(posts_dir: Path) -> set[str]:
    """Return canonical talk URLs explicitly claimed by blog front matter."""
    covered: set[str] = set()
    if not posts_dir.exists():
        return covered
    for path in posts_dir.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---\n", 4)
        head = text[4:end] if end >= 0 else ""
        match = re.search(r'^talk_url:\s*["\']?([^"\'\s]+)', head, re.M)
        if match:
            covered.add(match.group(1).rstrip("/"))
    return covered


def generate(config_path: Path, posts_dir: Path) -> dict[str, int]:
    entries = json.loads(config_path.read_text(encoding="utf-8"))["talks"]
    selected = [talk for talk in entries if "latest" in talk.get("categories", [])]
    slug_counts = Counter(
        (talk["date"][:4], slugify(talk["title"])) for talk in selected
    )
    covered = covered_talk_urls(posts_dir)
    result = {"created": 0, "existing": 0, "skipped": len(entries) - len(selected)}

    for talk in selected:
        year = talk["date"][:4]
        slug = slugify(talk["title"])
        if slug_counts[(year, slug)] > 1:
            slug = f"{slug}-{talk['date']}"
        path = posts_dir / year / f"{slug}.md"

        if path.exists() or talk_url(talk).rstrip("/") in covered:
            result["existing"] += 1
            continue

        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_post(talk), encoding="utf-8")
        result["created"] += 1

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=Path,
        default=Path.home() / "code/talks/config.json",
    )
    parser.add_argument("--posts-dir", type=Path, default=ROOT / "posts")
    args = parser.parse_args()
    result = generate(args.config.expanduser(), args.posts_dir.expanduser())
    print(
        f"talks: {result['created']} created, {result['existing']} existing, "
        f"{result['skipped']} non-latest entries skipped"
    )


if __name__ == "__main__":
    main()
