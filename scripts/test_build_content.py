from datetime import datetime
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


def test_post_without_date_is_skipped_with_warning(tmp_path, capsys):
    write(tmp_path / "posts/dated.md", "---\ntitle: Dated\ndate: 2026-09-27\n---\n")
    write(tmp_path / "posts/undated.md", "---\ntitle: Undated\n---\n")

    content = build(tmp_path)
    captured = capsys.readouterr()

    assert (content / "posts/dated.md").is_file()
    assert not (content / "posts/undated.md").exists()
    assert "warning: skipping post without a valid date: posts/undated.md" in captured.err
    assert "posts\t1" in captured.out


def test_day_archives_are_noindex_and_excluded_from_sitemap(tmp_path):
    content = tmp_path / "content"
    build_content.write_archives(content, [datetime(2026, 9, 26)])

    year = build_content.split_front_matter((content / "2026/_index.md").read_text()).front_matter
    month = build_content.split_front_matter((content / "2026/09/_index.md").read_text()).front_matter
    day = build_content.split_front_matter((content / "2026/09/26/_index.md").read_text()).front_matter

    assert "robotsNoIndex" not in year
    assert "robotsNoIndex" not in month
    assert day["robotsNoIndex"] is True
    assert day["sitemap"]["disable"] is True


def test_historical_skill_paths_redirect_to_canonical_repository(tmp_path):
    content = build(tmp_path)
    root = build_content.split_front_matter(
        (content / "skills/_index.md").read_text()
    ).front_matter
    assert root["redirect"] == "https://github.com/sanand0/skills"
    assert root["layout"] == "skill-redirect"
    assert root["robotsNoIndex"] is True
    assert (content / "skills/skills/_index.md").is_file()

    for name in build_content.SKILL_REDIRECTS:
        destination = f"https://github.com/sanand0/skills/blob/main/{name}/SKILL.md"
        for suffix in ("", "/skill", f"/{name}"):
            path = content / "skills" / name / suffix.lstrip("/") / "_index.md"
            assert path.is_file(), path
            data = build_content.split_front_matter(path.read_text()).front_matter
            assert data["redirect"] == destination
            assert data["layout"] == "skill-redirect"
            assert data["sitemap"]["disable"] is True

    assert len(build_content.SKILL_REDIRECTS) == 16
