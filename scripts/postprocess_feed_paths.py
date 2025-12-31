#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil
import sys


def create_feed_paths(root: Path) -> int:
    if not root.exists():
        raise FileNotFoundError(root)
    created = 0
    for xml_path in root.rglob("index.xml"):
        if xml_path.parent.name == "feed":
            continue
        html_path = xml_path.with_name("index.html")
        if not html_path.exists():
            continue
        feed_dir = xml_path.parent / "feed"
        feed_dir.mkdir(parents=True, exist_ok=True)
        dest = feed_dir / "index.xml"
        shutil.copy2(xml_path, dest)
        created += 1
    return created


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("public/blog")
    created = create_feed_paths(root)
    print(f"feeds\t{created}")


if __name__ == "__main__":
    main()
