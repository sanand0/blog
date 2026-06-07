from datetime import date
import difflib
from pathlib import Path
import importlib.util
import sys

import pytest
from typer.testing import CliRunner


SPEC = importlib.util.spec_from_file_location("til", Path(__file__).with_name("til.py"))
til = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = til
SPEC.loader.exec_module(til)


def test_target_sundays_defaults_and_range():
    assert til.target_sundays(today=date(2026, 6, 7)) == [date(2026, 6, 7)]
    assert til.target_sundays(today=date(2026, 6, 10)) == [date(2026, 6, 7)]
    assert til.target_sundays(start=date(2026, 5, 24), end=date(2026, 6, 7)) == [
        date(2026, 5, 24),
        date(2026, 5, 31),
        date(2026, 6, 7),
    ]


def test_target_sundays_rejects_non_sundays():
    with pytest.raises(ValueError, match="Sunday"):
        til.target_sundays(week=date(2026, 6, 6))


def test_covered_sundays_returns_only_weeks_with_notes():
    notes = [
        til.Note(date(2026, 5, 31), "- Sunday", 0),
        til.Note(date(2026, 6, 1), "- Monday", 1),
        til.Note(date(2026, 6, 20), "- Later Saturday", 2),
    ]

    assert til.covered_sundays(notes) == [date(2026, 6, 7), date(2026, 6, 21)]


def test_extract_notes_keeps_nested_markdown():
    notes = til.extract_notes(
        """# Notes
- 06 Jun 2026. First note
  - nested detail
ignored
- 31 May 2026. Older note
"""
    )
    assert notes[0].body == "- First note\n  - nested detail"
    assert notes[0].day == date(2026, 6, 6)


def test_render_post_merges_sources_in_descending_date_order(tmp_path):
    source_a = tmp_path / "til.md"
    source_b = tmp_path / "llms.md"
    source_a.write_text("- 06 Jun 2026. Saturday\n- 01 Jun 2026. Monday\n")
    source_b.write_text("- 05 Jun 2026. Friday\n")

    output = til.render_post(date(2026, 6, 7), [source_a, source_b])

    assert "title: Things I Learned - 07 Jun 2026" in output
    assert "date: 2026-06-07T00:00:00+00:00" in output
    assert "categories:\n  - til" in output
    assert output.index("- Saturday") < output.index("- Friday") < output.index("- Monday")
    assert "\nThis week, I learned:\n\n" in output


def test_write_post_refuses_overwrite_without_force(tmp_path):
    path = tmp_path / "post.md"
    path.write_text("existing")

    with pytest.raises(FileExistsError):
        til.write_post(path, "new", force=False)

    til.write_post(path, "new", force=True)
    assert path.read_text() == "new"


def test_file_diff_compares_entire_existing_and_generated_files(tmp_path):
    path = tmp_path / "post.md"
    path.write_text("old first\nsame\nold last\n")

    diff = til.file_diff(path, "new first\nsame\nnew last\n")

    expected = "".join(
        difflib.unified_diff(
            ["old first\n", "same\n", "old last\n"],
            ["new first\n", "same\n", "new last\n"],
            fromfile=str(path),
            tofile=f"{path} (generated)",
        )
    )
    assert diff == expected
    assert "old first" in diff and "old last" in diff
    assert "new first" in diff and "new last" in diff


def test_existing_post_is_not_overwritten_and_prints_diff(tmp_path):
    source_dir = tmp_path / "source"
    posts_dir = tmp_path / "posts"
    source_dir.mkdir()
    path = posts_dir / "2026/things-i-learned-07-jun-2026.md"
    path.parent.mkdir(parents=True)
    path.write_text("existing\n")
    (source_dir / "til.md").write_text("- 06 Jun 2026. New note\n")
    (source_dir / "llms.md").write_text("")

    result = CliRunner().invoke(
        til.app,
        [
            "--week",
            "2026-06-07",
            "--source-dir",
            str(source_dir),
            "--posts-dir",
            str(posts_dir),
            "--format",
            "text",
        ],
    )

    assert result.exit_code == 0
    assert path.read_text() == "existing\n"
    assert "would-overwrite" in result.stdout
    assert "-existing" in result.stdout
    assert "+- New note" in result.stdout

    forced = CliRunner().invoke(
        til.app,
        [
            "--week",
            "2026-06-07",
            "--source-dir",
            str(source_dir),
            "--posts-dir",
            str(posts_dir),
            "--force",
            "--format",
            "text",
        ],
    )
    assert forced.exit_code == 0
    assert "overwritten" in forced.stdout
    assert "--- " not in forced.stdout
