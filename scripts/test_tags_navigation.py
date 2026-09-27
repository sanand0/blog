import json
import re
from pathlib import Path

PUBLIC = Path("public/blog")


def corpus_by_slug() -> dict[str, dict]:
    records = {}
    with (PUBLIC / "corpus.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            records[record["slug"]] = record
    return records


def test_llms_tag_page_and_feed_exist_with_many_posts():
    html = (PUBLIC / "tag/llms/index.html").read_text(encoding="utf-8")

    assert (PUBLIC / "tag/llms/index.xml").is_file()
    assert "RSS feed" in html
    assert html.count('class="post-entry tag-entry"') > 50
    assert 'class="term-count-badge"' in html


def test_single_page_has_tags_and_matching_permalink():
    html = (PUBLIC / "beating-ai-detectors-by-reading-aloud/index.html").read_text(
        encoding="utf-8"
    )
    canonical = corpus_by_slug()["beating-ai-detectors-by-reading-aloud"]["url"]

    assert 'class="post-meta-tags"' in html
    assert f'<a href="{canonical}">Permalink</a>' in html


def test_date_links_only_target_post_publication_archives():
    post = (PUBLIC / "english-movie-dialogues-quiz/index.html").read_text(encoding="utf-8")
    published = re.search(r'<span class="post-meta-date">(.*?)</span>', post, re.DOTALL).group(1)
    updated = re.search(r'<span class="post-meta-updated">(.*?)</span>', post, re.DOTALL).group(1)
    page = (PUBLIC / "time/index.html").read_text(encoding="utf-8")
    page_date = re.search(r'<span class="post-meta-date">(.*?)</span>', page, re.DOTALL).group(1)

    assert 'href="/blog/2006/11/27/"' in published
    assert "<a " not in updated
    assert "<a " not in page_date


def test_paginated_pages_have_self_canonical_metadata():
    for path, expected in [
        ("page/2/index.html", "/blog/page/2/"),
        ("author/sanand/page/2/index.html", "/blog/author/sanand/page/2/"),
    ]:
        html = (PUBLIC / path).read_text(encoding="utf-8")
        assert f'<link rel="canonical" href="{expected}">' in html
        assert f'<meta property="og:url" content="{expected}">' in html


def test_footer_links_render_without_javascript():
    html = (PUBLIC / "beating-ai-detectors-by-reading-aloud/index.html").read_text(
        encoding="utf-8"
    )

    assert 'id="footer-categories"' in html and "/blog/category/llms/" in html
    assert 'id="footer-archives"' in html and "/blog/2026/" in html
    assert 'id="footer-tags"' in html and "/blog/tag/llms/" in html
    assert 'id="footer-pages"' in html and "/blog/about-me/" in html


def test_tags_index_uses_count_badges_not_nested_superscripts():
    html = (PUBLIC / "tags/index.html").read_text(encoding="utf-8")

    assert 'class="term-count-badge"' in html
    assert "<sup><strong><sup>" not in html


def test_category_list_entries_do_not_gain_tag_or_permalink_meta():
    html = (PUBLIC / "category/llms/index.html").read_text(encoding="utf-8")

    assert 'class="post-meta-tags"' not in html
    assert 'class="post-meta-permalink"' not in html
