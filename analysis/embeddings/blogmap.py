#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "joblib>=1.4",
#   "numpy>=2.2",
#   "pandas>=2.2",
#   "pyarrow>=20.0",
#   "pyyaml>=6.0",
#   "scikit-learn>=1.6",
#   "typer>=0.12",
#   "umap-learn>=0.5.7",
# ]
# ///
"""Generate analysis/embeddings/blogmap/blogmap.json for the UMAP visualization.

Reads raw embeddings from analysis/embeddings/embeddings.parquet, runs
PCA → UMAP → KMeans, and exports a compact JSON file consumed by
analysis/embeddings/blogmap/index.html.

Fitted models are cached in analysis/embeddings/models/ so that subsequent
runs only project NEW posts through transform/predict, keeping existing UMAP
coordinates and cluster assignments stable.

Performance notes:
  - `import umap` triggers numba JIT compilation (~7–10 s). We defer the
    import to only the branches that actually call UMAP (refit or new posts).
  - Post metadata is cached in models/meta_cache.parquet (keyed by mtime) so
    markdown files are only re-parsed when they change.
  - When no new posts exist, we skip loading embeddings and models entirely.

Usage:
    blogmap.py                # incremental update (new posts only)
    blogmap.py --refit        # refit all models from scratch
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[2]
EMBEDDINGS_PARQUET = ROOT / "analysis" / "embeddings" / "embeddings.parquet"
BLOGMAP_DIR = ROOT / "analysis" / "embeddings" / "blogmap"
JSON_OUT = BLOGMAP_DIR / "blogmap.json"
MODELS_DIR = ROOT / "analysis" / "embeddings" / "models"

# Model hyper-parameters — frozen for stability
N_CLUSTERS = 12
N_PCA = 50
UMAP_NEIGHBORS = 35
UMAP_MIN_DIST = 0.18

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


# ---------------------------------------------------------------------------
# Markdown metadata helpers
# ---------------------------------------------------------------------------


def _parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1))
        return fm if isinstance(fm, dict) else {}
    except yaml.YAMLError:
        return {}


def _normalize_list(value: object) -> list[str]:
    if value is None or value == "":
        return []
    items = value if isinstance(value, list) else [value]
    return [str(x).strip() for x in items if str(x).strip()]


def _parse_date(value: object) -> str | None:
    """Return ISO date string or None."""
    if value is None:
        return None
    ts = pd.to_datetime(str(value), utc=True, errors="coerce")
    if pd.isna(ts):
        return None
    return ts.strftime("%Y-%m-%d")


def read_post_metadata(cache_file: Path) -> pd.DataFrame:
    """Read path, title, date, primary_category, path_slug for all posts.

    Results are cached in *cache_file* (parquet). Only files whose mtime has
    changed since the last run are re-parsed, making subsequent calls fast.
    """
    md_paths = sorted((ROOT / "posts").rglob("*.md"))

    # Build a map of rel_path → current mtime (as int nanoseconds)
    current_mtimes: dict[str, int] = {
        str(p.relative_to(ROOT)): p.stat().st_mtime_ns for p in md_paths
    }

    # Load existing cache if available
    if cache_file.exists():
        cached = pd.read_parquet(cache_file)
        cached_map: dict[str, dict] = {
            row["path"]: row.to_dict() for _, row in cached.iterrows()
        }
    else:
        cached_map = {}

    rows: list[dict] = []
    changed = 0
    for path in md_paths:
        rel = str(path.relative_to(ROOT))
        mtime = current_mtimes[rel]
        cached_row = cached_map.get(rel)
        if cached_row and cached_row.get("mtime") == mtime:
            rows.append(cached_row)
            continue
        # Parse (only for new/modified files)
        changed += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = _parse_frontmatter(text)
        cats = _normalize_list(fm.get("categories"))
        rows.append(
            {
                "path": rel,
                "mtime": mtime,
                "title": str(fm.get("title") or path.stem.replace("-", " ")).strip(),
                "date": _parse_date(fm.get("date")),
                "primary_category": cats[0] if cats else "(none)",
                "path_slug": path.stem,
            }
        )

    df = pd.DataFrame(rows)
    if changed:
        print(f"  Parsed {changed} new/modified markdown files (cached {len(rows)-changed})")
        df.to_parquet(cache_file, index=False)
    return df


# ---------------------------------------------------------------------------
# Cluster helpers
# ---------------------------------------------------------------------------


def _reorder_labels(raw: np.ndarray) -> tuple[np.ndarray, dict[int, int]]:
    """Relabel clusters by descending size; return (mapped labels, old→new map)."""
    counts = pd.Series(raw).value_counts().sort_values(ascending=False)
    label_map = {int(old): new for new, old in enumerate(counts.index)}
    mapped = np.array([label_map[k] for k in raw], dtype=np.int32)
    return mapped, label_map


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(refit: bool = False) -> None:
    """Generate blogmap.json.

    Args:
        refit: When True, ignore saved models and refit from scratch.
    """
    BLOGMAP_DIR.mkdir(parents=True, exist_ok=True)
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    meta_cache_file = MODELS_DIR / "meta_cache.parquet"
    coords_file = MODELS_DIR / "coords.parquet"
    pca_file = MODELS_DIR / "pca.joblib"
    umap_file = MODELS_DIR / "umap.joblib"
    km_file = MODELS_DIR / "kmeans.joblib"
    lmap_file = MODELS_DIR / "label_map.json"
    bounds_file = MODELS_DIR / "bounds.json"
    model_files = [pca_file, umap_file, km_file, lmap_file, coords_file]

    # ------------------------------------------------------------------
    # 1. Read markdown metadata (mtime-cached — fast on repeat runs)
    # ------------------------------------------------------------------
    print("Reading markdown metadata…")
    meta = read_post_metadata(meta_cache_file)

    # ------------------------------------------------------------------
    # 2. Check for new posts without loading full embeddings
    # ------------------------------------------------------------------
    use_models = not refit and all(f.exists() for f in model_files)

    if use_models:
        # Only need paths column to detect new posts
        cached_paths = set(pd.read_parquet(coords_file, columns=["path"])["path"])
        meta_paths = set(meta["path"])
        new_paths = meta_paths - cached_paths

        if not new_paths:
            # Fast path: no new posts, no need to load embeddings or models
            print("No new posts — using cached coordinates")
            cache = pd.read_parquet(coords_file)
            bounds = json.loads(bounds_file.read_text()) if bounds_file.exists() else None
            frame = meta.merge(cache[["path", "umap_1", "umap_2", "cluster"]], on="path")
            _write_json(frame, bounds)
            return

        # New posts found — need full embeddings + models (+ umap for transform)
        print(f"Loading embeddings for {len(new_paths)} new posts…")
        emb = pd.read_parquet(EMBEDDINGS_PARQUET, columns=["path", "embedding"])
        emb = emb[emb["path"].isin(new_paths)].copy()

        import joblib
        from sklearn.preprocessing import normalize

        print("Loading cached models…")
        pca = joblib.load(pca_file)
        import umap as _umap_mod
        reducer = joblib.load(umap_file)
        km = joblib.load(km_file)
        label_map: dict[int, int] = {int(k): int(v) for k, v in json.loads(lmap_file.read_text()).items()}
        cache = pd.read_parquet(coords_file)

        print(f"  Projecting {len(emb)} new posts…")
        new_vecs = normalize(np.vstack(emb["embedding"].tolist()).astype(np.float32))
        new_pca = pca.transform(new_vecs)
        new_umap = reducer.transform(new_vecs)
        new_km_raw = km.predict(new_pca[:, :20])
        new_km = np.array(
            [label_map.get(int(k), int(k)) for k in new_km_raw], dtype=np.int32
        )
        new_rows = pd.DataFrame(
            {
                "path": emb["path"].values,
                "umap_1": new_umap[:, 0].round(4),
                "umap_2": new_umap[:, 1].round(4),
                "cluster": new_km,
            }
        )
        cache = pd.concat([cache, new_rows], ignore_index=True)
        cache.to_parquet(coords_file, index=False)
        print(f"  Cache updated ({len(cache)} total)")

        bounds = json.loads(bounds_file.read_text()) if bounds_file.exists() else None
        frame = meta.merge(cache[["path", "umap_1", "umap_2", "cluster"]], on="path")
        _write_json(frame, bounds)
        return

    # ------------------------------------------------------------------
    # 3. Full refit — load everything and fit from scratch
    # ------------------------------------------------------------------
    print("Loading all embeddings…")
    emb = pd.read_parquet(EMBEDDINGS_PARQUET)
    post_paths = set(meta["path"])
    emb = emb[emb["path"].isin(post_paths)].copy()
    frame = emb.merge(meta, on="path", how="inner")
    print(f"  {len(frame)} posts with embeddings")

    # Lazy imports — skip ~7 s numba JIT when not needed
    import joblib
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import normalize
    import umap as _umap_mod

    vectors = normalize(np.vstack(frame["embedding"].tolist()).astype(np.float32))

    print("Fitting PCA + UMAP + KMeans from scratch…")
    n_pca = min(N_PCA, len(frame) - 1)
    pca = PCA(n_components=n_pca, random_state=42)
    pca_feat = pca.fit_transform(vectors)
    print(f"  PCA done ({n_pca} components)")

    reducer = _umap_mod.UMAP(
        n_components=2,
        n_neighbors=UMAP_NEIGHBORS,
        min_dist=UMAP_MIN_DIST,
        metric="cosine",
        random_state=42,
    )
    umap_coords = reducer.fit_transform(vectors)
    print("  UMAP done")

    km = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init="auto")
    raw_labels = km.fit_predict(pca_feat[:, :20])
    labels, label_map = _reorder_labels(raw_labels)
    print(f"  KMeans done ({N_CLUSTERS} clusters)")

    # Persist models
    joblib.dump(pca, pca_file)
    joblib.dump(reducer, umap_file)
    joblib.dump(km, km_file)
    lmap_file.write_text(json.dumps(label_map))

    cache = pd.DataFrame(
        {
            "path": frame["path"].values,
            "umap_1": umap_coords[:, 0].round(4),
            "umap_2": umap_coords[:, 1].round(4),
            "cluster": labels,
        }
    )
    cache.to_parquet(coords_file, index=False)

    # Compute IQR-based outlier bounds (3×IQR — loose fence for island outliers)
    bounds = {}
    for col in ("umap_1", "umap_2"):
        q1, q3 = cache[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        bounds[f"{col}_min"] = float(q1 - 3 * iqr)
        bounds[f"{col}_max"] = float(q3 + 3 * iqr)
    bounds_file.write_text(json.dumps(bounds))
    print("  Models and coordinate cache saved")

    frame = frame.merge(cache[["path", "umap_1", "umap_2", "cluster"]], on="path")
    _write_json(frame, bounds)


def _write_json(frame: pd.DataFrame, bounds: dict | None) -> None:
    """Filter outliers and write blogmap.json."""
    # Merge coords if not already present
    if bounds is None:
        bounds = {}
        for col in ("umap_1", "umap_2"):
            q1, q3 = frame[col].quantile([0.25, 0.75])
            iqr = q3 - q1
            bounds[f"{col}_min"] = float(q1 - 3 * iqr)
            bounds[f"{col}_max"] = float(q3 + 3 * iqr)

    before = len(frame)
    frame = frame[
        (frame["umap_1"] >= bounds["umap_1_min"])
        & (frame["umap_1"] <= bounds["umap_1_max"])
        & (frame["umap_2"] >= bounds["umap_2_min"])
        & (frame["umap_2"] <= bounds["umap_2_max"])
    ].copy()
    print(f"Kept {len(frame)} posts after outlier filter (removed {before - len(frame)})")

    records = []
    for row in frame.itertuples(index=False):
        date_str = row.date
        if not date_str or (isinstance(date_str, float) and np.isnan(date_str)):
            continue
        date_str = str(date_str)
        records.append(
            {
                "s": row.path_slug,
                "t": row.title,
                "d": date_str,
                "y": int(date_str[:4]),
                "c": row.primary_category,
                "k": int(row.cluster),
                "u1": float(row.umap_1),
                "u2": float(row.umap_2),
            }
        )

    cat_counts = pd.Series([r["c"] for r in records]).value_counts()
    u1_vals = [r["u1"] for r in records]
    u2_vals = [r["u2"] for r in records]

    output = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "data": records,
        "cats": cat_counts.index.tolist(),
        "minYear": min(r["y"] for r in records),
        "maxYear": max(r["y"] for r in records),
        "xDom": [round(min(u1_vals), 2), round(max(u1_vals), 2)],
        "yDom": [round(min(u2_vals), 2), round(max(u2_vals), 2)],
    }

    with open(JSON_OUT, "w") as f:
        json.dump(output, f, separators=(",", ":"), ensure_ascii=False)

    size_kb = JSON_OUT.stat().st_size / 1024
    print(f"Wrote {len(records)} posts → {JSON_OUT} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    import typer

    typer.run(main)
