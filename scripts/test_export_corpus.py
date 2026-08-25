from pathlib import Path
from datetime import date
import importlib.util
import json
import sys


SPEC = importlib.util.spec_from_file_location(
    "export_corpus", Path(__file__).with_name("export_corpus.py")
)
export_corpus = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = export_corpus
SPEC.loader.exec_module(export_corpus)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_export_corpus_writes_one_valid_record_per_regular_content_page(tmp_path):
    content = tmp_path / "content"
    public = tmp_path / "public/blog"
    write(
        content / "posts/2026/example.md",
        """---
title: Example Post
date: 2026-07-01T00:00:00+00:00
lastmod: 2026-07-02T00:00:00+00:00
categories:
  - Coding
tags:
  - llms
description: A test post
slug: example-post
sourcePath: posts/2026/example.md
---

# Heading

This is **body** text with [a link](https://example.com/) and `code`.
""",
    )
    write(
        content / "about.md",
        """---
title: About
description: About page
slug: about
sourcePath: pages/about.md
---

![Alt text](/image.webp)

About *plain* text.
""",
    )
    write(
        content / "skills/example/_index.md",
        """---
title: example
summary: Skill description
description: Skill description
slug: example
sourcePath: pages/skills/example/SKILL.md
---

Skill text.

Skill readme text.
""",
    )
    write(content / "posts/_index.md", "---\ntitle: Posts\n---\n")
    write(
        content / "posts/2026/future.md",
        """---
title: Future Post
date: 2026-08-23T00:00:00+00:00
slug: future-post
sourcePath: posts/2026/future.md
---

Not public yet.
""",
    )
    write(public / "example-post/index.html", "<html></html>")
    write(public / "about/index.html", "<html></html>")
    write(public / "skills/example/index.html", "<html></html>")

    records = export_corpus.export_corpus(
        content_dir=content,
        public_dir=public,
        base_url="https://www.s-anand.net/blog/",
        raw_markdown_base="https://raw.githubusercontent.com/sanand0/blog/main",
        today=date(2026, 7, 10),
    )

    lines = (public / "corpus.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(lines) == 3
    assert len(records) == 3
    parsed = [json.loads(line) for line in lines]
    assert [record["url"] for record in parsed] == [
        "https://www.s-anand.net/blog/about/",
        "https://www.s-anand.net/blog/example-post/",
        "https://www.s-anand.net/blog/skills/example/",
    ]
    assert parsed[1]["source_markdown_url"].endswith("/posts/2026/example.md")
    assert parsed[1]["word_count"] == 10
    assert "body text with a link and code" in parsed[1]["text"]
    assert parsed[0]["text"] == "Alt text About plain text."
    assert parsed[2]["title"] == "example"
    assert parsed[2]["description"] == "Skill description"
    assert parsed[2]["source_markdown_url"].endswith("/pages/skills/example/SKILL.md")
    assert parsed[2]["text"] == "Skill text. Skill readme text."
    assert (public / "corpus.schema.json").is_file()


def test_redirect_pages_are_not_exported_to_agent_corpus(tmp_path):
    content = tmp_path / "content"
    public = tmp_path / "public/blog"
    write(
        content / "talks.md",
        """---
title: Talks
redirect: https://talks.s-anand.net/
slug: talks
sourcePath: pages/talks.md
---

This page moved.
""",
    )

    records = export_corpus.export_corpus(
        content_dir=content,
        public_dir=public,
        base_url="https://www.s-anand.net/blog/",
        raw_markdown_base="https://raw.githubusercontent.com/sanand0/blog/main",
        today=date(2026, 8, 25),
    )

    assert records == []
    assert (public / "corpus.jsonl").read_text(encoding="utf-8") == ""


def test_export_corpus_fails_when_a_url_has_no_public_file(tmp_path):
    content = tmp_path / "content"
    public = tmp_path / "public/blog"
    write(
        content / "posts/2026/missing.md",
        """---
title: Missing
slug: missing
sourcePath: posts/2026/missing.md
---

Body
""",
    )

    try:
        export_corpus.export_corpus(
            content_dir=content,
            public_dir=public,
            base_url="https://www.s-anand.net/blog/",
            raw_markdown_base="https://raw.githubusercontent.com/sanand0/blog/main",
        )
    except FileNotFoundError as error:
        assert "missing/index.html" in str(error)
    else:
        raise AssertionError("Expected missing public file to fail")


def test_export_corpus_falls_back_to_humanized_slug_for_missing_title(tmp_path):
    content = tmp_path / "content"
    public = tmp_path / "public/blog"
    write(
        content / "posts/2026/missing-title.md",
        """---
slug: missing-title
sourcePath: posts/2026/missing-title.md
---

Body
""",
    )
    write(public / "missing-title/index.html", "<html></html>")

    records = export_corpus.export_corpus(
        content_dir=content,
        public_dir=public,
        base_url="https://www.s-anand.net/blog/",
        raw_markdown_base="https://raw.githubusercontent.com/sanand0/blog/main",
    )

    assert records[0]["title"] == "Missing title"
