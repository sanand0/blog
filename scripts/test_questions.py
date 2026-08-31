from datetime import date
import importlib.util
from pathlib import Path
import sys

import pytest


SPEC = importlib.util.spec_from_file_location("questions", Path(__file__).with_name("questions.py"))
questions = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = questions
SPEC.loader.exec_module(questions)


def test_parse_questions_extracts_fields_and_ignores_comments_and_prose():
    source = """# Questions I am asked
Intro text that may change.
<!--
- 31 Dec 2026. Broken prompt example
-->
- 22 Aug 2026. Alice (Acme): #PUBLIC How should we start? #ANS Start small.
- 21 Aug 2026. Bob: #PRIVATE What is secret? #ANS Very secret.
- 16 Apr 2026. Naveen: #PUBLIC How do we win? #FAIL \"I don't know.\"
Footer text.
"""
    parsed = questions.parse_questions(source)

    assert [(q.day, q.name, q.organization, q.visibility) for q in parsed] == [
        (date(2026, 8, 22), "Alice", "Acme", "PUBLIC"),
        (date(2026, 8, 21), "Bob", None, "PRIVATE"),
        (date(2026, 4, 16), "Naveen", None, "PUBLIC"),
    ]
    assert parsed[0].question == "How should we start?"
    assert parsed[0].answer == "Start small."
    assert parsed[2].status == "FAIL"
    assert parsed[2].answer == '"I don\'t know."'


def test_parse_questions_rejects_malformed_dated_rows_with_line_number():
    with pytest.raises(questions.ParseError, match=r"line 2.*#PUBLIC"):
        questions.parse_questions(
            "# Header\n- 22 Aug 2026. #PUBLIC Alice (Acme): Wrong tag position #ANS Nope\n"
        )


def test_render_page_is_public_only_grouped_and_ordered():
    parsed = questions.parse_questions(
        """- 23 Aug 2026. Sunday: #PUBLIC New week? #ANS Yes.
- 22 Aug 2026. Alice: #PUBLIC Later? #ANS A.
- 20 Aug 2026. Bob: #PRIVATE Hidden? #ANS Secret.
- 20 Aug 2026. Carol: #PUBLIC Earlier? #ANS B.
"""
    )
    page = questions.render_page(parsed)

    assert "Hidden?" not in page
    assert page.index("week-ending-2026-08-30") < page.index("week-ending-2026-08-23")
    assert page.index("Later?") < page.index("Earlier?")
    assert "Alice" not in page and "Carol" not in page
    assert "- **Question**: Later?\\\n  **Answer**: A." in page


def test_replace_til_section_preserves_other_sections_and_is_idempotent():
    original = "---\ntitle: Existing\ntags: [hand-edited]\n---\n\n# Main\n\n- Keep me.\n\n### After\n\nKeep this too.\n"
    block = "## Questions I was asked\n\n[Week ending 23 Aug 2026](https://example.test)\n\n- **Question**: Q?\\\n  **Answer**: A."

    updated = questions.replace_til_section(original, block)
    assert updated.startswith(original)
    assert "Keep this too.\n\n## Questions I was asked" in updated
    assert questions.replace_til_section(updated, block) == updated

    mixed_case = updated.replace("## Questions I was asked", "#### qUeStIoNs I WaS AsKeD")
    replaced = questions.replace_til_section(mixed_case, block.replace("Q?", "Changed?"))
    assert "Changed?" in replaced and "Keep this too." in replaced
    assert questions.replace_til_section(replaced, None).rstrip() == original.rstrip()


def test_replace_til_section_stops_at_next_heading_and_rejects_duplicates():
    content = "# Main\n\n## QUESTIONS I WAS ASKED\n\nold\n\n### Next section\n\nkeep\n"
    updated = questions.replace_til_section(content, "## Questions I was asked\n\nnew")
    assert "old" not in updated
    assert "### Next section\n\nkeep" in updated
    with pytest.raises(questions.ManagedSectionError):
        questions.replace_til_section(
            "## Questions I was asked\nA\n## QUESTIONS I WAS ASKED\nB\n", "new"
        )


def test_sync_moves_updates_and_removes_questions_without_rewriting_unchanged_files(tmp_path):
    source = tmp_path / "questions.md"
    page = tmp_path / "pages/questions-i-am-asked.md"
    posts = tmp_path / "posts"
    old_post = posts / "2026/things-i-learned-23-aug-2026.md"
    new_post = posts / "2026/things-i-learned-30-aug-2026.md"
    old_post.parent.mkdir(parents=True)
    base_old = "---\ntitle: Old week\ntags: [keep]\n---\n\nThis week, I learned:\n\n- Existing old.\n"
    base_new = "---\ntitle: New week\ndescription: keep me\n---\n\nThis week, I learned:\n\n- Existing new.\n"
    old_post.write_text(base_old)
    new_post.write_text(base_new)
    source.write_text("- 22 Aug 2026. Alice (Acme): #PUBLIC Original question? #ANS Original answer.\n")

    first = questions.sync(source, page, posts)
    assert first.written == 2  # page + old TIL
    assert "Original question?" in old_post.read_text()
    assert new_post.read_text() == base_new
    page_before = page.read_text()
    old_before = old_post.read_text()
    second = questions.sync(source, page, posts)
    assert second.written == 0
    assert page.read_text() == page_before and old_post.read_text() == old_before

    # Sunday moves into the next TIL week; content changes at the same time.
    source.write_text("- 23 Aug 2026. Alice (Acme): #PUBLIC Updated question? #ANS Updated answer.\n")
    moved = questions.sync(source, page, posts)
    assert moved.written == 3  # page + remove old block + add new block
    assert old_post.read_text() == base_old
    assert "Updated question?" in new_post.read_text()
    assert "Original question?" not in new_post.read_text()
    assert "description: keep me" in new_post.read_text()

    # Making it private removes it from both generated surfaces.
    source.write_text("- 23 Aug 2026. Alice (Acme): #PRIVATE Updated question? #ANS Updated answer.\n")
    hidden = questions.sync(source, page, posts)
    assert hidden.written == 2  # page + remove new block
    assert new_post.read_text() == base_new
    assert "Updated question?" not in page.read_text()


def test_sync_parses_everything_before_writing(tmp_path):
    source = tmp_path / "questions.md"
    page = tmp_path / "page.md"
    posts = tmp_path / "posts"
    posts.mkdir()
    page.write_text("do not touch\n")
    source.write_text("- 22 Aug 2026. #PUBLIC Alice: malformed\n")

    with pytest.raises(questions.ParseError):
        questions.sync(source, page, posts)
    assert page.read_text() == "do not touch\n"


def test_parse_questions_warns_on_date_like_typos_and_unclosed_comments():
    with pytest.raises(questions.ParseError, match="JUl"):
        questions.parse_questions("- 29 JUl 2023. Mohit: #PUBLIC What now? #ANS Fix it.\n")
    with pytest.raises(questions.ParseError, match="unbalanced HTML comment"):
        questions.parse_questions(
            "<!--\n- 22 Aug 2026. Alice: #PUBLIC This must stay commented? #ANS Yes.\n"
        )
