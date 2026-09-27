#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6.0"]
# ///
import re
import shutil
from pathlib import Path
from xml.sax.saxutils import escape

import yaml


def front_matter(path: Path) -> dict:
    """Read YAML front matter from a generated Hugo content file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    _, header, _ = text.split("---", 2)
    return yaml.safe_load(header) or {}


def rendered_path(path: Path, content_dir: Path, public_blog: Path) -> Path:
    """Return the HTML file Hugo renders for one generated content page."""
    rel = path.relative_to(content_dir)
    if rel.name == "_index.md":
        return public_blog / rel.parent / "index.html"
    slug = front_matter(path).get("slug") or rel.stem
    return public_blog / rel.parent / slug / "index.html"


def target_path(root: str, public_dir: Path) -> Path:
    """Map a root URL path to its file under public/."""
    if not root.startswith("/") or ".." in Path(root).parts:
        raise ValueError(f"Invalid root path: {root}")
    rel = root.lstrip("/")
    return public_dir / rel / "index.html" if not rel or root.endswith("/") else public_dir / rel


def add_sitemap_urls(
    sitemap_path: Path,
    roots: list[str],
    site_root: str = "https://www.s-anand.net",
) -> None:
    """Add promoted, indexable root URLs to Hugo's generated sitemap."""
    text = sitemap_path.read_text(encoding="utf-8")
    existing = set(re.findall(r"<loc>(.*?)</loc>", text))
    urls = [f"{site_root.rstrip('/')}{root}" for root in roots]
    entries = "".join(
        f"  <url>\n    <loc>{escape(url)}</loc>\n  </url>\n"
        for url in urls
        if url not in existing
    )
    if entries:
        text = text.replace("</urlset>", f"{entries}</urlset>")
        sitemap_path.write_text(text, encoding="utf-8")


def promote(
    content_dir: Path = Path("content"),
    public_dir: Path = Path("public"),
    public_blog: Path = Path("public/blog"),
) -> int:
    """Copy Hugo-rendered root pages and sitemap only indexable promoted URLs."""
    targets: set[Path] = set()
    indexable_roots: list[str] = []
    count = 0
    for path in sorted(content_dir.rglob("*.md")):
        metadata = front_matter(path)
        root = metadata.get("root")
        if not root:
            continue
        root = str(root)
        source = rendered_path(path, content_dir, public_blog)
        target = target_path(root, public_dir)
        if target in targets:
            raise ValueError(f"Duplicate root target: {root}")
        if not source.is_file():
            raise FileNotFoundError(source)
        targets.add(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        sitemap = metadata.get("sitemap") or {}
        sitemap_disabled = isinstance(sitemap, dict) and sitemap.get("disable")
        if not metadata.get("robotsNoIndex") and not sitemap_disabled:
            indexable_roots.append(root)
        count += 1

    add_sitemap_urls(public_blog / "sitemap.xml", indexable_roots)
    return count


if __name__ == "__main__":
    count = promote()
    print(f"root-pages\t{count}")
