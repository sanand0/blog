from pathlib import Path
import importlib.util
import sys


SPEC = importlib.util.spec_from_file_location(
    "migrate_keywords_to_tags", Path(__file__).with_name("migrate_keywords_to_tags.py")
)
migrate_keywords_to_tags = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = migrate_keywords_to_tags
SPEC.loader.exec_module(migrate_keywords_to_tags)


def test_migrate_text_replaces_keywords_with_canonical_tags():
    text = """---
title: Example
date: 2026-07-10
keywords: [LLM, data visualisation, one off]
summary: Keep this exactly.
---

Body
"""
    canonical = {"llms", "data-visualization"}
    aliases = {"llms": "llms", "llm": "llms", "data-visualization": "data-visualization"}

    migrated, changed = migrate_keywords_to_tags.migrate_text(text, canonical, aliases)

    assert changed
    assert "keywords:" not in migrated
    assert "title: Example\ndate: 2026-07-10\n" in migrated
    assert "summary: Keep this exactly." in migrated
    assert "tags: [llms, data-visualization]\n" in migrated
    assert migrated.endswith("\nBody\n")


def test_migrate_text_merges_existing_tags_and_block_keywords():
    text = """---
title: Book Post
tags: [book]
keywords:
  - Large Language Models
  - ignored one-off
description: Existing description
---

Body
"""
    canonical = {"book", "llms"}
    aliases = {"book": "book", "llms": "llms", "large-language-models": "llms"}

    migrated, changed = migrate_keywords_to_tags.migrate_text(text, canonical, aliases)

    assert changed
    assert "keywords:" not in migrated
    assert "tags: [book, llms]\n" in migrated
    assert "description: Existing description" in migrated


def test_migrate_text_deletes_keywords_when_no_tags_match():
    text = """---
title: Untagged
keywords: [private one-off]
---

Body
"""

    migrated, changed = migrate_keywords_to_tags.migrate_text(text, set(), {})

    assert changed
    assert "keywords:" not in migrated
    assert "tags:" not in migrated
    assert "title: Untagged" in migrated
