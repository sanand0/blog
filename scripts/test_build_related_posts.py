from pathlib import Path
import importlib.util
import json
import sys

import pandas as pd


SPEC = importlib.util.spec_from_file_location(
    "build_related_posts", Path(__file__).with_name("build_related_posts.py")
)
build_related_posts = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = build_related_posts
SPEC.loader.exec_module(build_related_posts)


def write_post(path: Path, title: str, tags: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        f"title: {title}\n"
        "date: 2026-01-01T00:00:00+00:00\n"
        f"tags: [{', '.join(tags)}]\n"
        f"description: Description for {title}\n"
        "---\n\nBody\n",
        encoding="utf-8",
    )


def test_build_related_posts_requires_embeddings(tmp_path):
    try:
        build_related_posts.build_related_posts(
            embeddings_path=tmp_path / "missing.parquet",
            output_path=tmp_path / "related.json",
        )
    except FileNotFoundError as error:
        assert "Run analysis/embeddings/embeddings.py" in str(error)
    else:
        raise AssertionError("Expected missing embeddings to fail")


def test_build_related_posts_writes_neighbors_without_self_reference(tmp_path):
    rows = []
    for index in range(6):
        path = f"posts/2026/post-{index}.md"
        write_post(tmp_path / path, f"Post {index}", ["llms"] if index < 3 else ["data-visualization"])
        rows.append(
            {
                "path": path,
                "embedding": [1.0, float(index) / 10, 0.0] if index < 3 else [0.0, 1.0, float(index) / 10],
            }
        )
    embeddings = tmp_path / "documents.parquet"
    pd.DataFrame(rows).to_parquet(embeddings)
    output = tmp_path / "related.json"

    cwd = Path.cwd()
    try:
        import os
        os.chdir(tmp_path)
        related = build_related_posts.build_related_posts(embeddings, output, top_k=5)
    finally:
        os.chdir(cwd)

    parsed = json.loads(output.read_text(encoding="utf-8"))
    assert parsed == related
    assert len(related) == 6
    for path, items in related.items():
        assert 3 <= len(items) <= 5
        assert all(item["path"] != path for item in items)
