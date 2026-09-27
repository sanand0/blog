import importlib.util
import sys
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "promote_root_pages", Path(__file__).with_name("promote_root_pages.py")
)
promote_root_pages = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = promote_root_pages
SPEC.loader.exec_module(promote_root_pages)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_promotes_root_pages_and_sitemaps_only_indexable_ones(tmp_path):
    content = tmp_path / "content"
    public = tmp_path / "public"
    blog = public / "blog"

    write(content / "home.md", "---\nroot: /\nslug: home\n---\n")
    write(content / "calvin.md", "---\nroot: /calvin/\nslug: calvin\nrobotsNoIndex: true\n---\n")
    write(
        content / "calvinandhobbes.md",
        "---\nroot: /calvinandhobbes.html\nslug: calvinandhobbes\nrobotsNoIndex: true\n---\n",
    )
    write(blog / "home/index.html", "home")
    write(blog / "calvin/index.html", "calvin")
    write(blog / "calvinandhobbes/index.html", "redirect")
    write(
        blog / "sitemap.xml",
        '<?xml version="1.0" encoding="utf-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>',
    )

    assert promote_root_pages.promote(content, public, blog) == 3
    assert (public / "index.html").read_text() == "home"
    assert (public / "calvin/index.html").read_text() == "calvin"
    assert (public / "calvinandhobbes.html").read_text() == "redirect"
    sitemap = (blog / "sitemap.xml").read_text()
    assert "<loc>https://www.s-anand.net/</loc>" in sitemap
    assert "https://www.s-anand.net/calvin/" not in sitemap
    assert "https://www.s-anand.net/calvinandhobbes.html" not in sitemap


def test_rejects_root_path_escape(tmp_path):
    with pytest.raises(ValueError):
        promote_root_pages.target_path("/../escape", tmp_path)
