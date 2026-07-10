from pathlib import Path
import json


PUBLIC = Path("public/blog")


def test_search_page_loads_pagefind_bundle():
    html = (PUBLIC / "search/index.html").read_text(encoding="utf-8")

    assert "/blog/pagefind/pagefind-ui.css" in html
    assert "/blog/pagefind/pagefind-ui.js" in html
    assert 'new PagefindUI({' in html
    assert 'id="search"' in html


def test_pagefind_index_covers_archive_pages():
    entry = json.loads((PUBLIC / "pagefind/pagefind-entry.json").read_text(encoding="utf-8"))
    page_count = sum(language["page_count"] for language in entry["languages"].values())

    assert entry["version"] == "1.5.2"
    assert page_count > 2800


def test_non_search_pages_do_not_load_pagefind_or_fuse_payloads():
    html = (PUBLIC / "beating-ai-detectors-by-reading-aloud/index.html").read_text(
        encoding="utf-8"
    )

    assert "pagefind-ui.css" not in html
    assert "pagefind-ui.js" not in html
    assert "assets/js/search" not in html
    assert "fuse" not in html.lower()
