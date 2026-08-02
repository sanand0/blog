import csv
import importlib.util
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "linkedin_blog_map", Path(__file__).with_name("linkedin_blog_map.py")
)
linkedin_blog_map = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = linkedin_blog_map
SPEC.loader.exec_module(linkedin_blog_map)


def configure(tmp_path, monkeypatch):
    analysis_dir = tmp_path / "analysis"
    posts_dir = tmp_path / "posts/2026"
    analysis_dir.mkdir()
    posts_dir.mkdir(parents=True)
    linkedin_path = tmp_path / "linkedin-posts.jsonl"
    monkeypatch.setattr(linkedin_blog_map, "ROOT", tmp_path)
    monkeypatch.setattr(linkedin_blog_map, "LINKEDIN_PATH", linkedin_path)
    monkeypatch.setattr(
        linkedin_blog_map, "OUTPUT_PATH", analysis_dir / "linkedin-blog-map.tsv"
    )
    monkeypatch.setattr(
        linkedin_blog_map,
        "AMBIGUOUS_PATH",
        analysis_dir / "linkedin-blog-map-ambiguous.tsv",
    )
    monkeypatch.setattr(
        linkedin_blog_map,
        "OVERRIDES_PATH",
        analysis_dir / "linkedin-blog-map-overrides.tsv",
    )
    return analysis_dir, posts_dir, linkedin_path


def write_blog(posts_dir, name, body, linkedin=""):
    metadata = f"linkedin: {linkedin}\n" if linkedin else ""
    path = posts_dir / f"{name}.md"
    path.write_text(
        f"---\ntitle: {name}\ndate: 2026-06-01T00:00:00+00:00\n{metadata}---\n\n{body}\n"
    )
    return path


def write_linkedin(
    linkedin_path, content, links=None, url="https://www.linkedin.com/posts/example"
):
    linkedin_path.write_text(
        json.dumps(
            {
                "type": "post",
                "id": "urn:li:activity:7470074745900802048",
                "postId": "7470074745900802048",
                "url": url,
                "postedAt": "2025-01-01T00:00:00Z",
                "content": content,
                "links": links or [],
            }
        )
        + "\n"
    )


def read_rows(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_output_paths_remain_in_analysis_directory():
    root = Path(__file__).parents[1]
    assert linkedin_blog_map.ROOT == root
    assert linkedin_blog_map.OUTPUT_PATH == root / "analysis/linkedin-blog-map.tsv"
    assert (
        linkedin_blog_map.AMBIGUOUS_PATH
        == root / "analysis/linkedin-blog-map-ambiguous.tsv"
    )
    assert (
        linkedin_blog_map.OVERRIDES_PATH
        == root / "analysis/linkedin-blog-map-overrides.tsv"
    )


def test_markdown_text_excludes_code_and_html():
    text = """---\ntitle: Test\n---\nVisible prose<script>secret tokens here</script>\n```js\nmore secret tokens\n```<b>ending</b>"""
    assert linkedin_blog_map.markdown_text(text) == "Visible prose ending"


def test_linkedin_date_uses_activity_id_not_drifting_scraped_date():
    item = {
        "postId": "7470074745900802048",
        "postedAt": "2025-01-01T00:00:00Z",
    }
    assert linkedin_blog_map.linkedin_date(item) == datetime(
        2026, 6, 9, 11, 30, 6, 700000, tzinfo=UTC
    )


def test_main_uses_direct_url_but_does_not_write_frontmatter_by_default(
    tmp_path, monkeypatch
):
    analysis_dir, posts_dir, linkedin_path = configure(tmp_path, monkeypatch)
    blog_path = write_blog(
        posts_dir,
        "matching-post",
        "A distinctive phrase about mapping LinkedIn posts to blog posts.",
    )
    write_blog(
        posts_dir,
        "unrelated-post",
        "Completely unrelated material about another topic.",
    )
    write_linkedin(
        linkedin_path,
        "A distinctive phrase about mapping LinkedIn posts to blog posts.",
        ["https://s-anand.net/blog/matching-post/"],
    )

    linkedin_blog_map.main()

    row = read_rows(analysis_dir / "linkedin-blog-map.tsv")[0]
    assert row["blog_filename"] == "posts/2026/matching-post.md"
    assert row["match_method"] == "direct_url"
    assert "linkedin:" not in blog_path.read_text()


def test_write_frontmatter_only_when_explicit(tmp_path, monkeypatch):
    _, posts_dir, linkedin_path = configure(tmp_path, monkeypatch)
    blog_path = write_blog(
        posts_dir,
        "matching-post",
        "A distinctive phrase about mapping LinkedIn posts to blog posts.",
    )
    write_blog(
        posts_dir,
        "unrelated-post",
        "Completely unrelated material about another topic.",
    )
    write_linkedin(
        linkedin_path,
        "A distinctive phrase about mapping LinkedIn posts to blog posts.",
        ["https://s-anand.net/blog/matching-post/"],
    )

    linkedin_blog_map.main(write_frontmatter=True)

    assert "linkedin: https://www.linkedin.com/posts/example/" in blog_path.read_text()


def test_generated_output_is_not_an_authoritative_input(tmp_path, monkeypatch):
    analysis_dir, posts_dir, linkedin_path = configure(tmp_path, monkeypatch)
    write_blog(
        posts_dir,
        "matching-post",
        "A distinctive phrase shared in both places for reliable matching.",
    )
    write_blog(
        posts_dir,
        "wrong-post",
        "Unrelated food preferences and restaurant recommendations.",
    )
    write_linkedin(
        linkedin_path,
        "A distinctive phrase shared in both places for reliable matching.",
    )
    (analysis_dir / "linkedin-blog-map.tsv").write_text(
        "linkedin_url\tblog_filename\tlinkedin_content\tblog_content\n"
        "https://www.linkedin.com/posts/example/\tposts/2026/wrong-post.md\t\t\n"
    )

    linkedin_blog_map.main()

    row = read_rows(analysis_dir / "linkedin-blog-map.tsv")[0]
    assert row["blog_filename"] == "posts/2026/matching-post.md"


def test_weak_frontmatter_is_sent_to_review_not_accepted(tmp_path, monkeypatch):
    analysis_dir, posts_dir, linkedin_path = configure(tmp_path, monkeypatch)
    url = "https://www.linkedin.com/posts/example/"
    write_blog(
        posts_dir,
        "wrong-post",
        "Restaurant choices, desserts, and food preferences.",
        url,
    )
    write_blog(
        posts_dir,
        "other-post",
        "A different unrelated article with enough words to be a candidate for scoring.",
    )
    write_linkedin(
        linkedin_path, "Generate a colorful sketchnote from my blog post.", url=url
    )

    linkedin_blog_map.main()

    row = read_rows(analysis_dir / "linkedin-blog-map.tsv")[0]
    review = read_rows(analysis_dir / "linkedin-blog-map-ambiguous.tsv")[0]
    assert row["blog_filename"] == ""
    assert review["reason"] == "weak_frontmatter"
    assert review["best_blog_filename"] == "posts/2026/wrong-post.md"


def test_manual_override_is_authoritative(tmp_path, monkeypatch):
    analysis_dir, posts_dir, linkedin_path = configure(tmp_path, monkeypatch)
    write_blog(
        posts_dir,
        "manual-post",
        "Manual mapping content need not resemble the LinkedIn rewrite.",
    )
    write_blog(
        posts_dir,
        "other-post",
        "A different unrelated article with enough words to be scored.",
    )
    write_linkedin(linkedin_path, "A rewritten LinkedIn post with different wording.")
    (analysis_dir / "linkedin-blog-map-overrides.tsv").write_text(
        "linkedin_url\tblog_filename\n"
        "https://www.linkedin.com/posts/example/\tposts/2026/manual-post.md\n"
    )

    linkedin_blog_map.main()

    row = read_rows(analysis_dir / "linkedin-blog-map.tsv")[0]
    assert row["blog_filename"] == "posts/2026/manual-post.md"
    assert row["match_method"] == "override"


def test_blank_override_marks_reviewed_no_match(tmp_path, monkeypatch):
    analysis_dir, posts_dir, linkedin_path = configure(tmp_path, monkeypatch)
    write_blog(
        posts_dir,
        "matching-post",
        "A distinctive phrase shared in both places for reliable matching.",
    )
    write_blog(
        posts_dir,
        "other-post",
        "A different article with enough words to be scored as a candidate.",
    )
    write_linkedin(
        linkedin_path,
        "A distinctive phrase shared in both places for reliable matching.",
    )
    (analysis_dir / "linkedin-blog-map-overrides.tsv").write_text(
        "linkedin_url\tblog_filename\nhttps://www.linkedin.com/posts/example/\t\n"
    )

    linkedin_blog_map.main()

    row = read_rows(analysis_dir / "linkedin-blog-map.tsv")[0]
    assert row["blog_filename"] == ""
    assert row["match_method"] == "override_no_match"
    assert read_rows(analysis_dir / "linkedin-blog-map-ambiguous.tsv") == []


def test_main_prints_relative_summary_and_copyable_override_rows(
    tmp_path, monkeypatch, capsys
):
    analysis_dir, posts_dir, linkedin_path = configure(tmp_path, monkeypatch)
    url = "https://www.linkedin.com/posts/example/"
    write_blog(
        posts_dir,
        "wrong-post",
        "Restaurant choices, desserts, and food preferences.",
        url,
    )
    write_blog(
        posts_dir,
        "other-post",
        "A different unrelated article with enough words to be a candidate for scoring.",
    )
    write_linkedin(
        linkedin_path, "Generate a colorful sketchnote from my blog post.", url=url
    )

    linkedin_blog_map.main()

    output = capsys.readouterr().out
    assert "analysis/linkedin-blog-map.tsv: matched 0" in output
    assert "analysis/linkedin-blog-map-ambiguous.tsv: review 1" in output
    assert (
        "analysis/linkedin-blog-map-overrides.tsv: add reviewed lines from below"
        in output
    )
    assert "leave it blank to mark no match" in output
    assert f"{url}\tposts/2026/wrong-post.md" in output
    assert read_rows(analysis_dir / "linkedin-blog-map-overrides.tsv") == []
