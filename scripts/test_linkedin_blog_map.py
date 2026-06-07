from pathlib import Path
import importlib.util
import json
import sys


SPEC = importlib.util.spec_from_file_location(
    "linkedin_blog_map", Path(__file__).with_name("linkedin_blog_map.py")
)
linkedin_blog_map = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = linkedin_blog_map
SPEC.loader.exec_module(linkedin_blog_map)


def test_output_paths_remain_in_analysis_directory():
    root = Path(__file__).parents[1]

    assert linkedin_blog_map.ROOT == root
    assert linkedin_blog_map.OUTPUT_PATH == root / "analysis/linkedin-blog-map.tsv"
    assert linkedin_blog_map.AMBIGUOUS_PATH == root / "analysis/linkedin-blog-map-ambiguous.tsv"


def test_main_writes_analysis_tsvs_and_linkedin_metadata(tmp_path, monkeypatch):
    analysis_dir = tmp_path / "analysis"
    posts_dir = tmp_path / "posts/2026"
    analysis_dir.mkdir()
    posts_dir.mkdir(parents=True)
    blog_path = posts_dir / "matching-post.md"
    blog_path.write_text(
        "---\ntitle: Matching Post\ndate: 2026-06-01T00:00:00+00:00\n---\n\n"
        "A distinctive phrase about mapping LinkedIn posts to blog posts.\n"
    )
    (posts_dir / "unrelated-post.md").write_text(
        "---\ntitle: Unrelated Post\ndate: 2026-05-01T00:00:00+00:00\n---\n\n"
        "Completely unrelated material about another topic.\n"
    )
    linkedin_path = tmp_path / "linkedin-posts.jsonl"
    linkedin_path.write_text(
        json.dumps(
            {
                "type": "post",
                "url": "https://www.linkedin.com/posts/example",
                "postedAt": "2026-06-01T00:00:00Z",
                "content": "A distinctive phrase about mapping LinkedIn posts to blog posts.",
                "links": ["https://s-anand.net/blog/matching-post/"],
            }
        )
        + "\n"
    )
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

    linkedin_blog_map.main()

    assert "posts/2026/matching-post.md" in (
        analysis_dir / "linkedin-blog-map.tsv"
    ).read_text()
    assert (analysis_dir / "linkedin-blog-map-ambiguous.tsv").is_file()
    assert "linkedin: https://www.linkedin.com/posts/example" in blog_path.read_text()
