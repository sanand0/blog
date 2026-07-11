from pathlib import Path
import json
import random
import re


PUBLIC = Path("public/blog")


def test_related_json_has_neighbors_for_all_posts():
    related = json.loads(Path("data/related-posts.json").read_text(encoding="utf-8"))
    records = [
        json.loads(line)
        for line in (PUBLIC / "corpus.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    posts = [
        record["slug"]
        for record in records
        if "/posts/" in record["source_markdown_url"]
    ]

    assert len(related) >= len(posts) - 1
    for slug in random.Random(42).sample(posts, 50):
        items = related[slug]
        assert 3 <= len(items) <= 5
        assert all(isinstance(item, str) and item != slug for item in items)


def test_related_json_is_compact_and_improves_dilbert_results():
    path = Path("data/related-posts.json")
    related = json.loads(path.read_text(encoding="utf-8"))

    assert path.read_text(encoding="utf-8").count("\n") == 1
    assert related["15-years-of-dilbert-searchable"] == [
        "dilbert-search-statistics",
        "dilbert-search-engine",
        "dilbert-browser",
        "gemini-3-flash-ocrs-dilbert-accurately",
        "the-calvin-and-hobbes-search-takedown",
    ]


def test_sample_post_renders_related_links_to_existing_pages():
    html = (PUBLIC / "beating-ai-detectors-by-reading-aloud/index.html").read_text(
        encoding="utf-8"
    )
    block = re.search(r'<section class="related-posts">(.*?)</section>', html, re.S)
    assert block
    links = re.findall(r'<a href="([^"]+)">', block.group(1))
    assert 3 <= len(links) <= 5
    for href in links:
        assert href != "/blog/beating-ai-detectors-by-reading-aloud/"
        assert (PUBLIC / href.removeprefix("/blog/") / "index.html").is_file()


def test_related_posts_render_human_readable_dates():
    html = (PUBLIC / "beating-ai-detectors-by-reading-aloud/index.html").read_text(
        encoding="utf-8"
    )
    block = re.search(r'<section class="related-posts">(.*?)</section>', html, re.S)

    assert block
    assert re.search(r'<time datetime="\d{4}-\d{2}-\d{2}[^"]*">[A-Z][a-z]{2}, \d{1,2} [A-Z][a-z]{2} \d{4}</time>', block.group(1))
