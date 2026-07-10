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
        record["source_markdown_url"].split("/main/", 1)[1]
        for record in records
        if "/posts/" in record["source_markdown_url"]
    ]

    assert len(related) >= len(posts) - 1
    for path in random.Random(42).sample(posts, 50):
        items = related[path]
        assert 3 <= len(items) <= 5
        assert all(item["path"] != path for item in items)


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
