import importlib.util
import sys
from datetime import date
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "mistakes", Path(__file__).with_name("mistakes.py")
)
mistakes = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mistakes
SPEC.loader.exec_module(mistakes)


def test_parse_mistakes_preserves_text_around_fix_and_accepts_leading_tags():
    source = """# Mistakes I made

- 01 Sep 2026. #PUBLIC #HIGH #OVERSTATED I said **\"Skills are just prompts.\"** #FIX Skills can also package code and resources. Evidence: [OpenAI — Skills](https://example.com/skills) <!-- source: transcript.md:10 -->
- 31 Aug 2026. #PRIVATE #MEDIUM #FALSE I described **a secret claim.** #FIX Secret correction. Evidence: Internal contract. <!-- source: private.md:20 -->
- 30 Aug 2026. #LOW #PUBLIC #FALSE #EXPERIMENTAL I called Henry **an ambassador.** #FIX He was not one. Evidence: [Bio](https://example.com/bio)
"""
    parsed = mistakes.parse_mistakes(source)

    assert [(m.day, m.public) for m in parsed] == [
        (date(2026, 9, 1), True),
        (date(2026, 8, 31), False),
        (date(2026, 8, 30), True),
    ]
    assert parsed[0].claim == 'I said **"Skills are just prompts."**'
    assert (
        parsed[0].correction
        == "Skills can also package code and resources. Evidence: [OpenAI — Skills](https://example.com/skills)"
    )
    assert parsed[0].tags == ("HIGH", "OVERSTATED")
    assert parsed[1].claim == "I described **a secret claim.**"
    assert parsed[2].tags == ("LOW", "FALSE", "EXPERIMENTAL")
    assert "transcript.md" not in parsed[0].correction

    custom = mistakes.parse_mistakes(
        "- 30 Aug 2026. #PUBLIC #Experimental-v2 #ODD_TAG I said X. #FIX Y.\n"
    )[0]
    assert custom.tags == ("Experimental-v2", "ODD_TAG")
    assert mistakes.render_entry(custom).endswith("**Experimental-v2 · ODD_TAG**")


def test_parse_mistakes_rejects_dated_rows_without_fix_or_visibility():
    with pytest.raises(mistakes.ParseError, match=r"line 2.*#FIX"):
        mistakes.parse_mistakes(
            "# Header\n- 01 Sep 2026. #PUBLIC #HIGH #FALSE I said **wrong** but forgot the correction.\n"
        )
    with pytest.raises(mistakes.ParseError, match=r"line 1.*PUBLIC.*PRIVATE"):
        mistakes.parse_mistakes(
            "- 01 Sep 2026. #HIGH #FALSE I said **wrong.** #FIX Right.\n"
        )


def test_render_entry_preserves_wording_puts_fix_second_and_tags_last():
    item = mistakes.parse_mistakes(
        '- 01 Sep 2026. #PUBLIC #LOW #FALSE I said **"1960s is when Studio Ghibli starts trying to catch up" with Disney.** #FIX Studio Ghibli was established in 1985. Evidence: [Studio Ghibli — company history](https://www.ghibli.jp/profile/)\n'
    )[0]

    rendered = mistakes.render_entry(item)
    assert rendered == (
        '- I said **"1960s is when Studio Ghibli starts trying to catch up" with Disney.**\\\n'
        "  **Correction**: Studio Ghibli was established in 1985. Evidence: [Studio Ghibli — company history](https://www.ghibli.jp/profile/)\\\n"
        "  **LOW · FALSE**"
    )


def test_render_page_is_public_only_grouped_newest_first_and_cross_linkable():
    parsed = mistakes.parse_mistakes(
        """- 01 Sep 2026. #PUBLIC #LOW #FALSE I said **Newer.** #FIX New fix. Evidence: [New](https://new.example)
- 31 Aug 2026. #PRIVATE #HIGH #FALSE I said **Hidden.** #FIX Hidden fix. Evidence: Secret.
- 29 Aug 2026. #PUBLIC #MEDIUM #OVERSTATED I said **Older.** #FIX Old fix. Evidence: [Old](https://old.example)
"""
    )
    page = mistakes.render_page(parsed)

    assert "Hidden" not in page
    assert page.index("week-ending-2026-09-06") < page.index("week-ending-2026-08-30")
    assert "## Week ending 06 Sep 2026 {#week-ending-2026-09-06}" in page
    assert "#PUBLIC" not in page and "#LOW" not in page and "#FALSE" not in page
    assert "What I got wrong, and what I should say instead." in page


def test_replace_til_section_preserves_other_content_and_is_idempotent():
    original = "---\ntitle: Existing\ntags: [hand-edited]\n---\n\nThis week, I learned:\n\n- Keep me.\n\n## Questions I was asked\n\nKeep questions.\n"
    block = "## Mistakes I made\n\n[Week ending 06 Sep 2026](https://example.test)\n\n- I said Wrong.\\\n  **Correction**: Right.\\\n  **False · High impact**"

    updated = mistakes.replace_til_section(original, block)
    assert "tags: [hand-edited]" in updated
    assert "## Questions I was asked\n\nKeep questions." in updated
    assert updated.index("## Questions I was asked") < updated.index(
        "## Mistakes I made"
    )
    assert mistakes.replace_til_section(updated, block) == updated
    assert mistakes.replace_til_section(updated, None).rstrip() == original.rstrip()


def test_sync_updates_archive_and_matching_til_without_touching_frontmatter(tmp_path):
    source = tmp_path / "mistakes.md"
    page = tmp_path / "pages/mistakes-i-made.md"
    posts = tmp_path / "posts"
    post = posts / "2026/things-i-learned-06-sep-2026.md"
    post.parent.mkdir(parents=True)
    base = (
        "---\ntitle: TIL\ntags: [keep]\n---\n\nThis week, I learned:\n\n- Existing.\n"
    )
    post.write_text(base)
    source.write_text(
        "- 01 Sep 2026. #PUBLIC #HIGH #OVERSTATED I said **Too much.** #FIX Say less. Evidence: [Source](https://example.com) <!-- source: local.md:1 -->\n"
    )

    first = mistakes.sync(source, page, posts)
    assert first.written == 2
    assert first.public_mistakes == 1
    assert "I said **Too much.**" in page.read_text()
    til = post.read_text()
    assert "tags: [keep]" in til
    assert "## Mistakes I made" in til
    assert "local.md" not in til
    assert "**Correction**: Say less. Evidence: [Source](https://example.com)" in til
    assert "**HIGH · OVERSTATED**" in til
    assert "https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-09-06" in til

    second = mistakes.sync(source, page, posts)
    assert second.written == 0

    source.write_text(
        "- 01 Sep 2026. #PRIVATE #HIGH #OVERSTATED I said **Too much.** #FIX Say less. Evidence: [Source](https://example.com)\n"
    )
    hidden = mistakes.sync(source, page, posts)
    assert hidden.written == 2
    assert "Too much" not in page.read_text()
    assert post.read_text() == base
