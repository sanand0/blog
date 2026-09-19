from pathlib import Path
import importlib.util
import json
import sys


SPEC = importlib.util.spec_from_file_location("talks", Path(__file__).with_name("talks.py"))
talks = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = talks
SPEC.loader.exec_module(talks)


SAMPLE = {
    "date": "2026-09-19",
    "time": "2026-09-19T09:30:00+05:30",
    "duration": 90,
    "title": "How Do You Manage Something Smarter Than You?",
    "categories": ["latest"],
    "details": "Managing AI resembles managing experts.",
    "links": [
        {
            "type": "page",
            "url": "2026-08-07-data-hack-summit/",
            "primary": True,
            "ignore": True,
        },
        {
            "type": "video",
            "url": "https://media.s-anand.net/talk.webm",
            "minutes": 58,
            "ignore": True,
        },
        {
            "type": "transcript",
            "url": "2026-08-07-data-hack-summit/transcript.md",
        },
    ],
    "event": {
        "name": "Data Hack Summit 2026",
        "url": "https://example.com/event",
    },
    "location": "Bangalore",
    "images": [
        {
            "type": "comic",
            "url": "2026-08-07-data-hack-summit/comic-page.avif",
        },
        {
            "type": "screenshot",
            "label": "Survey",
            "url": "2026-08-07-data-hack-summit/survey.avif",
        },
    ],
}


def write_config(path: Path, entries: list[dict]) -> None:
    path.write_text(json.dumps({"talks": entries}), encoding="utf-8")


def test_render_post_is_natural_and_uses_config_only():
    text = talks.render_post(SAMPLE)

    assert 'title: "How Do You Manage Something Smarter Than You?"' in text
    assert 'date: "2026-09-19T09:30:00+05:30"' in text
    assert "categories:\n- talks" in text
    assert "tags: []" in text
    assert 'description: "Managing AI resembles managing experts."' in text
    assert (
        'talk_url: "https://talks.s-anand.net/2026-08-07-data-hack-summit/"'
        in text
    )
    assert "talk_categories:" not in text
    assert "\nevent:" not in text
    assert "\nlocation:" not in text
    assert (
        "I conducted a session on Sat, 19 Sep 2026 at "
        "[Data Hack Summit 2026](https://example.com/event) - Bangalore." in text
    )
    assert "**Summary**: Managing AI resembles managing experts." in text
    assert (
        "[Here's the link to the session]"
        "(https://talks.s-anand.net/2026-08-07-data-hack-summit/)" in text
    )
    assert (
        "[![Comic](https://talks.s-anand.net/"
        "2026-08-07-data-hack-summit/comic-page.avif)]"
        "(https://talks.s-anand.net/2026-08-07-data-hack-summit/)" in text
    )
    assert (
        "[![Survey Screenshot](https://talks.s-anand.net/"
        "2026-08-07-data-hack-summit/survey.avif)]"
        "(https://talks.s-anand.net/2026-08-07-data-hack-summit/)" in text
    )
    assert "**Links**:" in text
    assert "- [Video](https://media.s-anand.net/talk.webm) (58 min)" in text
    assert (
        "- [Transcript](https://talks.s-anand.net/"
        "2026-08-07-data-hack-summit/transcript.md)" in text
    )


def test_generate_never_overwrites_existing_post(tmp_path):
    config = tmp_path / "config.json"
    posts = tmp_path / "posts"
    write_config(config, [SAMPLE])

    first = talks.generate(config, posts)
    path = posts / "2026/how-do-you-manage-something-smarter-than-you.md"
    assert first == {"created": 1, "existing": 0, "skipped": 0}

    path.write_text(path.read_text() + "\nMy manual edit.\n", encoding="utf-8")
    second = talks.generate(config, posts)

    assert second == {"created": 0, "existing": 1, "skipped": 0}
    assert path.read_text(encoding="utf-8").endswith("My manual edit.\n")


def test_generate_only_latest(tmp_path):
    config = tmp_path / "config.json"
    posts = tmp_path / "posts"
    archive = {**SAMPLE, "categories": ["archive"], "title": "Older Talk"}
    other = {**SAMPLE, "categories": ["others"], "title": "Someone Else's Talk"}
    write_config(config, [SAMPLE, archive, other])

    result = talks.generate(config, posts)

    assert result == {"created": 1, "existing": 0, "skipped": 2}
    assert len(list(posts.rglob("*.md"))) == 1


def test_talk_url_frontmatter_marks_session_as_covered(tmp_path):
    config = tmp_path / "config.json"
    posts = tmp_path / "posts"
    write_config(config, [SAMPLE])
    existing = posts / "2026/my-better-title.md"
    existing.parent.mkdir(parents=True)
    existing.write_text(
        """---
title: My Better Title
date: 2026-09-21
talk_url: "https://talks.s-anand.net/2026-08-07-data-hack-summit/"
---

I rewrote this completely.
""",
        encoding="utf-8",
    )

    result = talks.generate(config, posts)

    assert result == {"created": 0, "existing": 1, "skipped": 0}
    assert not (posts / "2026/how-do-you-manage-something-smarter-than-you.md").exists()


def test_incidental_body_link_does_not_mark_session_as_covered(tmp_path):
    config = tmp_path / "config.json"
    posts = tmp_path / "posts"
    write_config(config, [SAMPLE])
    incidental = posts / "2026/another-topic.md"
    incidental.parent.mkdir(parents=True)
    incidental.write_text(
        """---
title: Another Topic
date: 2026-09-20
---

See https://talks.s-anand.net/2026-08-07-data-hack-summit/ as an example.
""",
        encoding="utf-8",
    )

    result = talks.generate(config, posts)

    assert result == {"created": 1, "existing": 0, "skipped": 0}


def test_duplicate_titles_get_date_suffixes(tmp_path):
    config = tmp_path / "config.json"
    posts = tmp_path / "posts"
    one = {**SAMPLE, "title": "Vibe Coding", "date": "2025-05-10"}
    two = {**SAMPLE, "title": "Vibe Coding", "date": "2025-12-10"}
    write_config(config, [one, two])

    talks.generate(config, posts)

    assert (posts / "2025/vibe-coding-2025-05-10.md").exists()
    assert (posts / "2025/vibe-coding-2025-12-10.md").exists()


def test_slugify_drops_apostrophes():
    assert talks.slugify("You Don't Even Need to Code") == "you-dont-even-need-to-code"
    assert talks.slugify("What's Left For Us") == "whats-left-for-us"


def test_description_without_details_is_assembled_from_config_facts():
    sample = {**SAMPLE}
    sample.pop("details")
    assert (
        talks.talk_description(sample)
        == "How Do You Manage Something Smarter Than You? — Data Hack Summit 2026 — Bangalore"
    )


def test_event_intro_without_location():
    sample = {**SAMPLE}
    sample.pop("location")
    text = talks.render_post(sample)
    assert (
        "I conducted a session on Sat, 19 Sep 2026 at "
        "[Data Hack Summit 2026](https://example.com/event)." in text
    )


def test_image_label_does_not_repeat_type():
    assert talks.image_label({"type": "poster", "label": "Event Poster"}) == "Event Poster"
    assert talks.image_label({"type": "comic", "label": "Day 1"}) == "Day 1 Comic"


def test_display_date_is_fixed_english_format():
    assert talks.display_date("2026-09-19") == "Sat, 19 Sep 2026"


def test_session_datetime_defaults_to_noon_ist():
    sample = {**SAMPLE}
    sample.pop("time")
    assert talks.session_datetime(sample) == "2026-09-19T12:00:00+05:30"
    assert 'date: "2026-09-19T12:00:00+05:30"' in talks.render_post(sample)


def test_session_datetime_preserves_config_offset():
    assert talks.session_datetime(SAMPLE) == "2026-09-19T09:30:00+05:30"
