#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=2.2", "pandas>=2.2", "pyarrow>=20.0", "pyyaml>=6.0", "typer>=0.12"]
# ///
"""Build static related-post data from embeddings."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated
from datetime import date
import json
import re

import numpy as np
import pandas as pd
import typer
import yaml


app = typer.Typer(add_completion=False)
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def source_posts() -> pd.DataFrame:
    """Load public post metadata from source markdown."""
    rows = []
    for path in sorted(Path("posts").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        match = FRONTMATTER_RE.match(text)
        if not match:
            continue
        data = yaml.safe_load(match.group(1)) or {}
        if not isinstance(data, dict) or data.get("draft") is True:
            continue
        raw_date = data.get("date")
        parsed_date = pd.to_datetime(raw_date, utc=True, errors="coerce")
        if not pd.isna(parsed_date) and parsed_date.date() > date.today():
            continue
        tags = data.get("tags") or []
        rows.append(
            {
                "path": path.as_posix(),
                "title": str(data.get("title") or path.stem),
                "date": parsed_date,
                "tags": tags if isinstance(tags, list) else [tags],
                "description": str(data.get("description") or "").strip(),
            }
        )
    return pd.DataFrame(rows)


def tag_set(values: object) -> set[str]:
    """Return a Python set from parquet list values."""
    if values is None:
        return set()
    if isinstance(values, np.ndarray):
        return set(values.tolist())
    if isinstance(values, list):
        return set(values)
    return set()


def build_related_posts(
    embeddings_path: Path = Path("analysis/embeddings/embeddings.parquet"),
    output_path: Path = Path("data/related-posts.json"),
    top_k: int = 5,
) -> dict[str, list[dict[str, str]]]:
    """Write related posts keyed by source path."""
    if not embeddings_path.is_file():
        raise FileNotFoundError(
            f"Missing embeddings parquet: {embeddings_path}. "
            "Run analysis/embeddings/embeddings.py first."
        )
    embeddings = pd.read_parquet(
        embeddings_path,
        columns=["path", "embedding"],
    )
    posts = source_posts().reset_index(drop=True)
    embedding_map = {
        str(row.path): np.array(row.embedding, dtype=np.float32)
        for row in embeddings.itertuples(index=False)
    }
    dim = len(next(iter(embedding_map.values())))
    vectors = np.vstack(
        [embedding_map.get(path, np.zeros(dim, dtype=np.float32)) for path in posts["path"]]
    )
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    vectors = vectors / np.maximum(norms, 1e-12)
    similarity = vectors @ vectors.T
    np.fill_diagonal(similarity, -np.inf)

    tag_sets = [tag_set(values) for values in posts["tags"]]
    related: dict[str, list[dict[str, str]]] = {}
    for source_index, source in posts.iterrows():
        shared = np.array([len(tag_sets[source_index] & tags) for tags in tag_sets], dtype=np.float32)
        score = similarity[source_index] + shared * 0.001
        order = np.argsort(-score)
        items: list[dict[str, str]] = []
        for target_index in order:
            if target_index == source_index or not np.isfinite(similarity[source_index, target_index]):
                continue
            target = posts.iloc[int(target_index)]
            items.append(
                {
                    "path": str(target["path"]),
                    "title": str(target["title"]),
                    "date": pd.Timestamp(target["date"]).date().isoformat()
                    if not pd.isna(target["date"])
                    else "",
                    "description": str(target["description"] or ""),
                }
            )
            if len(items) == top_k:
                break
        related[str(source["path"])] = items

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(related, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return related


@app.command()
def main(
    embeddings_path: Annotated[Path, typer.Option()] = Path("analysis/embeddings/embeddings.parquet"),
    output_path: Annotated[Path, typer.Option()] = Path("data/related-posts.json"),
    top_k: Annotated[int, typer.Option()] = 5,
) -> None:
    related = build_related_posts(embeddings_path, output_path, top_k)
    typer.echo(f"related-posts\t{len(related)}\t{output_path}")


if __name__ == "__main__":
    app()
