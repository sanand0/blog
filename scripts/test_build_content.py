from pathlib import Path
import importlib.util
import sys


SPEC = importlib.util.spec_from_file_location(
    "build_content", Path(__file__).with_name("build_content.py")
)
build_content = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = build_content
SPEC.loader.exec_module(build_content)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build(tmp_path: Path) -> Path:
    content = tmp_path / "content"
    build_content.build(
        metadata_path=tmp_path / "missing-metadata.yml",
        tag_metadata_path=tmp_path / "missing-tags.yml",
        posts_dir=tmp_path / "posts",
        pages_dir=tmp_path / "pages",
        content_dir=content,
    )
    return content


def test_skill_readme_and_skill_become_one_section_page(tmp_path):
    pages = tmp_path / "pages"
    write(
        pages / "skills/example/README.md",
        """---
description: Readme description
tags: [one, two]
---

README body.
""",
    )
    write(
        pages / "skills/example/SKILL.md",
        """---
name: example
description: Skill description
---

SKILL body.
""",
    )
    write(pages / "skills/example/notes.md", "# Notes\n")

    content = build(tmp_path)

    skill_page = content / "skills/example/_index.md"
    text = skill_page.read_text(encoding="utf-8")
    assert skill_page.exists()
    assert not (content / "skills/example/README.md").exists()
    assert not (content / "skills/example/SKILL.md").exists()
    assert (content / "skills/example/notes.md").exists()
    assert "title: example" in text
    assert "summary: Skill description" in text
    assert "description: Skill description" in text
    assert "Readme description" not in text
    assert "sourcePath: pages/skills/example/SKILL.md" in text
    assert "- /skills/example/skill/" in text
    assert "- /skills/example/example/" in text
    assert "SKILL body.\n\nREADME body." in text
    skills_index = (content / "skills/_index.md").read_text(encoding="utf-8")
    assert "title: Skills" in skills_index
    assert "Reusable AI agent skills" in skills_index


def test_skill_without_readme_still_gets_directory_page(tmp_path):
    skill = tmp_path / "pages/skills/skill-only/SKILL.md"
    write(
        skill,
        """---
name: skill-only
description: Skill-only description
---

Only skill body.
""",
    )

    content = build(tmp_path)

    skill_page = content / "skills/skill-only/_index.md"
    text = skill_page.read_text(encoding="utf-8")
    assert skill_page.exists()
    assert not (content / "skills/skill-only/SKILL.md").exists()
    assert "title: skill-only" in text
    assert "summary: Skill-only description" in text
    assert "description: Skill-only description" in text
    assert "slug: skill-only" in text
    assert "sourcePath: pages/skills/skill-only/SKILL.md" in text
    assert "Only skill body." in text
