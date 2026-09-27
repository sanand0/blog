#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# ///
import re
from pathlib import Path

CANONICAL_RE = re.compile(r'<link rel="canonical" href="[^"]*">')
OG_URL_RE = re.compile(r'<meta property="og:url" content="[^"]*">')


def pagination_url(path: Path, root: Path, base_path: str = "/blog/") -> str:
    """Return the public URL for a generated paginator HTML file."""
    rel = path.relative_to(root)
    return f"{base_path.rstrip('/')}/{rel.parent.as_posix().strip('/')}/"


def rewrite_metadata(html: str, url: str) -> str:
    """Set canonical and Open Graph URLs to the paginator's actual URL."""
    html, canonical_count = CANONICAL_RE.subn(
        f'<link rel="canonical" href="{url}">', html, count=1
    )
    html, og_count = OG_URL_RE.subn(
        f'<meta property="og:url" content="{url}">', html, count=1
    )
    if canonical_count != 1 or og_count != 1:
        raise ValueError(
            f"Expected one canonical and og:url, got {canonical_count} and {og_count}"
        )
    return html


def apply(root: Path = Path("public/blog")) -> int:
    """Fix self-referential metadata for generated paginator pages."""
    count = 0
    for path in sorted(root.glob("**/page/[0-9]*/index.html")):
        original = path.read_text(encoding="utf-8")
        updated = rewrite_metadata(original, pagination_url(path, root))
        if updated != original:
            path.write_text(updated, encoding="utf-8")
        count += 1
    return count


if __name__ == "__main__":
    print(f"pagination-metadata\t{apply()}")
