#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "matplotlib>=3.9",
#   "numpy>=2.2",
#   "pandas>=2.2",
#   "pyarrow>=20.0",
#   "pyyaml>=6.0",
#   "scikit-learn>=1.6",
#   "seaborn>=0.13",
#   "umap-learn>=0.5.7",
# ]
# ///
"""Analyze blog embeddings and export plots plus summary datasets."""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yaml
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    calinski_harabasz_score,
    normalized_mutual_info_score,
    silhouette_score,
)
from sklearn.preprocessing import normalize
import umap


matplotlib.use("Agg")
sns.set_theme(style="whitegrid")

ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "analysis" / "embeddings" / "embeddings.parquet"
OUT_DIR = Path(__file__).resolve().parent
MAX_EMBED_CHARS = 10_000
TOP_NEIGHBORS = 20
PLOT_DPI = 180
FINE_CLUSTER_COUNT = 12

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
URL_RE = re.compile(r"https?://\S+")
MARKDOWN_LINK_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)|\[[^\]]*\]\([^)]+\)")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]+`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
NON_WORD_RE = re.compile(r"[^a-z0-9\s-]")
MULTISPACE_RE = re.compile(r"\s+")


@dataclass
class MarkdownDoc:
    front_matter: dict
    body: str


def split_front_matter(text: str) -> MarkdownDoc:
    """Split markdown into front matter and body."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return MarkdownDoc(front_matter={}, body=text)
    try:
        front_matter = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        front_matter = {}
    if not isinstance(front_matter, dict):
        front_matter = {}
    return MarkdownDoc(front_matter=front_matter, body=text[match.end() :])


def parse_date(value: object) -> pd.Timestamp | pd.NaT:
    """Parse front-matter date into UTC timestamp when possible."""
    if value is None or value == "":
        return pd.NaT
    if isinstance(value, datetime):
        ts = pd.Timestamp(value)
    elif isinstance(value, date):
        ts = pd.Timestamp(datetime.combine(value, datetime.min.time()))
    else:
        ts = pd.to_datetime(str(value), utc=True, errors="coerce")
    if pd.isna(ts):
        return pd.NaT
    if ts.tzinfo is None:
        ts = ts.tz_localize("UTC")
    else:
        ts = ts.tz_convert("UTC")
    return ts


def normalize_list(value: object) -> list[str]:
    """Normalize front-matter taxonomy values into a clean string list."""
    if value is None or value == "":
        return []
    if isinstance(value, list):
        items = value
    else:
        items = [value]
    return [str(item).strip() for item in items if str(item).strip()]


def remove_comments_section(body: str) -> tuple[str, str, int | None]:
    """Split markdown before and after a comments heading."""
    for marker in ("\n## Comments", "\n### Comments", "\n## comments"):
        index = body.find(marker)
        if index >= 0:
            return body[:index].rstrip(), body[index:].lstrip(), index
    return body, "", None


def clean_text_for_terms(text: str) -> str:
    """Drop markdown noise so TF-IDF terms describe topics, not syntax."""
    text = HTML_COMMENT_RE.sub(" ", text)
    text = CODE_FENCE_RE.sub(" ", text)
    text = URL_RE.sub(" ", text)
    text = MARKDOWN_LINK_RE.sub(" ", text)
    text = INLINE_CODE_RE.sub(" ", text)
    text = text.lower()
    text = NON_WORD_RE.sub(" ", text)
    text = MULTISPACE_RE.sub(" ", text)
    return text.strip()


def markdown_rows() -> pd.DataFrame:
    """Load markdown metadata and content statistics for all posts/pages."""
    rows: list[dict] = []
    for kind_dir in ("posts", "pages"):
        for path in sorted((ROOT / kind_dir).rglob("*.md")):
            rel_path = str(path.relative_to(ROOT))
            raw = path.read_text(encoding="utf-8", errors="replace")
            doc = split_front_matter(raw)
            front_matter = doc.front_matter
            body = doc.body.strip()
            title = str(front_matter.get("title") or "").strip()
            categories = normalize_list(front_matter.get("categories"))
            tags = normalize_list(front_matter.get("tags"))
            body_without_comments, comment_text, comment_index = remove_comments_section(body)
            embed_source = f"{title}\n\n{body}" if title else body
            parts = Path(rel_path).parts
            page_section = parts[1] if parts[0] == "pages" and len(parts) > 2 else ""

            rows.append(
                {
                    "path": rel_path,
                    "title": title or Path(rel_path).stem.replace("-", " "),
                    "kind": "post" if kind_dir == "posts" else "page",
                    "page_section": page_section,
                    "date": parse_date(front_matter.get("date")),
                    "year": pd.NA,
                    "month": pd.NA,
                    "categories": categories,
                    "primary_category": categories[0] if categories else None,
                    "tags": tags,
                    "tag_count": len(tags),
                    "category_count": len(categories),
                    "word_count": len(re.findall(r"\b\w+\b", body_without_comments)),
                    "char_count": len(body),
                    "input_char_count": len(embed_source),
                    "was_truncated": len(embed_source) > MAX_EMBED_CHARS,
                    "has_comments": bool(comment_text),
                    "comment_char_count": len(comment_text),
                    "comment_share": len(comment_text) / max(1, len(body)),
                    "has_images": "![](" in body or "[![" in body,
                    "link_count": body.count("]("),
                    "code_fence_count": body.count("```"),
                    "body_clean": clean_text_for_terms(body_without_comments),
                    "embed_clean": clean_text_for_terms(embed_source[:MAX_EMBED_CHARS]),
                    "path_slug": Path(rel_path).stem,
                    "post_year_folder": int(parts[1]) if parts[0] == "posts" and parts[1].isdigit() else pd.NA,
                    "comments_start": comment_index if comment_index is not None else pd.NA,
                }
            )

    frame = pd.DataFrame(rows)
    frame["year"] = frame["date"].dt.year.astype("Int64")
    frame["month"] = frame["date"].dt.month.astype("Int64")
    frame["categories_text"] = frame["categories"].apply(lambda values: " | ".join(values))
    frame["tags_text"] = frame["tags"].apply(lambda values: " | ".join(values))
    frame["subtype"] = np.where(
        frame["kind"].eq("page"),
        frame["page_section"].replace("", "root-page"),
        frame["year"].astype("string").fillna("undated-post"),
    )
    return frame


def choose_cluster_count(features: np.ndarray) -> tuple[int, pd.DataFrame]:
    """Pick a pragmatic KMeans cluster count using several metrics."""
    records: list[dict] = []
    for clusters in range(4, 21):
        model = KMeans(n_clusters=clusters, random_state=42, n_init="auto")
        labels = model.fit_predict(features)
        records.append(
            {
                "clusters": clusters,
                "inertia": float(model.inertia_),
                "silhouette": float(
                    silhouette_score(
                        features,
                        labels,
                        sample_size=min(1500, len(features)),
                        random_state=42,
                    )
                ),
                "calinski_harabasz": float(calinski_harabasz_score(features, labels)),
            }
        )
    metrics = pd.DataFrame(records)
    max_silhouette = metrics["silhouette"].max()
    candidates = metrics.loc[metrics["silhouette"] >= max_silhouette - 0.01].copy()
    target = int(candidates.iloc[(candidates["clusters"] - 12).abs().argmin()]["clusters"])
    return target, metrics


def top_terms_by_cluster(texts: pd.Series, clusters: pd.Series) -> dict[int, list[str]]:
    """Find distinctive terms for each cluster."""
    vectorizer = TfidfVectorizer(
        stop_words="english",
        min_df=5,
        max_df=0.30,
        ngram_range=(1, 2),
    )
    matrix = vectorizer.fit_transform(texts)
    terms = np.array(vectorizer.get_feature_names_out())
    global_mean = np.asarray(matrix.mean(axis=0)).ravel() + 1e-9

    cluster_terms: dict[int, list[str]] = {}
    for cluster_id in sorted(clusters.unique()):
        mask = clusters.eq(cluster_id).to_numpy()
        cluster_mean = np.asarray(matrix[mask].mean(axis=0)).ravel()
        score = cluster_mean / global_mean
        order = np.argsort(score)[::-1]
        chosen: list[str] = []
        for idx in order:
            term = terms[idx]
            if len(term) < 3:
                continue
            if any(token.isdigit() for token in term.split()):
                continue
            chosen.append(term)
            if len(chosen) == 6:
                break
        cluster_terms[int(cluster_id)] = chosen
    return cluster_terms


def reorder_clusters(labels: np.ndarray) -> np.ndarray:
    """Relabel clusters by descending size for readability."""
    counts = pd.Series(labels).value_counts().sort_values(ascending=False)
    mapping = {old: new for new, old in enumerate(counts.index)}
    return np.array([mapping[label] for label in labels], dtype=int)


def fit_clusters(features: np.ndarray, cluster_count: int) -> np.ndarray:
    """Fit KMeans and relabel clusters by descending size."""
    model = KMeans(n_clusters=cluster_count, random_state=42, n_init="auto")
    return reorder_clusters(model.fit_predict(features))


def cosine_pair_matrix(vectors: np.ndarray) -> np.ndarray:
    """Compute dense cosine similarity matrix."""
    return vectors @ vectors.T


def save_cluster_selection_plot(metrics: pd.DataFrame) -> None:
    fig, ax1 = plt.subplots(figsize=(9, 5))
    ax2 = ax1.twinx()
    ax1.plot(metrics["clusters"], metrics["silhouette"], marker="o", color="#1f77b4")
    ax2.plot(metrics["clusters"], metrics["calinski_harabasz"], marker="s", color="#ff7f0e")
    ax1.set_xlabel("Clusters (k)")
    ax1.set_ylabel("Silhouette", color="#1f77b4")
    ax2.set_ylabel("Calinski-Harabasz", color="#ff7f0e")
    ax1.set_title("Cluster Selection Metrics")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "cluster-selection.png", dpi=PLOT_DPI)
    plt.close(fig)


def scatter_plot(
    frame: pd.DataFrame,
    x_col: str,
    y_col: str,
    hue_col: str,
    path: Path,
    title: str,
    palette: str | list[str] = "tab20",
    alpha: float = 0.78,
    size: float = 16,
    legend: bool = True,
) -> None:
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.scatterplot(
        data=frame,
        x=x_col,
        y=y_col,
        hue=hue_col,
        palette=palette,
        s=size,
        alpha=alpha,
        linewidth=0,
        ax=ax,
        legend=legend,
    )
    ax.set_title(title)
    ax.set_xlabel(x_col.replace("_", " ").title())
    ax.set_ylabel(y_col.replace("_", " ").title())
    if legend:
        sns.move_legend(ax, "upper left", bbox_to_anchor=(1.01, 1.0), borderaxespad=0)
    fig.tight_layout()
    fig.savefig(path, dpi=PLOT_DPI)
    plt.close(fig)


def label_extremes(ax: plt.Axes, frame: pd.DataFrame, x_col: str, y_col: str, n: int = 12) -> None:
    """Label interesting points without turning the plot into static."""
    candidates = pd.concat(
        [
            frame.nlargest(n // 3, x_col),
            frame.nsmallest(n // 3, x_col),
            frame.nlargest(n // 3, y_col),
            frame.nsmallest(n // 3, y_col),
        ]
    ).drop_duplicates(subset="path")
    for row in candidates.itertuples():
        ax.text(getattr(row, x_col), getattr(row, y_col), row.title[:36], fontsize=7, alpha=0.85)


def heatmap_plot(data: pd.DataFrame, path: Path, title: str, fmt: str = ".2f", cmap: str = "mako") -> None:
    fig_width = max(7, 0.7 * len(data.columns))
    fig_height = max(5, 0.45 * len(data.index))
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    sns.heatmap(data, cmap=cmap, annot=False, fmt=fmt, ax=ax)
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(path, dpi=PLOT_DPI)
    plt.close(fig)


def mmr_rerank(candidate_ids: list[int], source_id: int, similarities: np.ndarray, top_k: int = 5) -> list[int]:
    """Diversify related-post suggestions while staying semantically close."""
    selected: list[int] = []
    candidate_pool = list(candidate_ids)
    while candidate_pool and len(selected) < top_k:
        best_id = None
        best_score = -math.inf
        for candidate_id in candidate_pool:
            penalty = max((similarities[candidate_id, seen] for seen in selected), default=0.0)
            score = 0.85 * similarities[source_id, candidate_id] - 0.15 * penalty
            if best_id is None or score > best_score:
                best_id = candidate_id
                best_score = score
        selected.append(best_id)
        candidate_pool.remove(best_id)
    return selected


def build_cluster_summary(
    frame: pd.DataFrame,
    vectors: np.ndarray,
    cluster_col: str,
    cluster_terms: dict[int, list[str]],
) -> pd.DataFrame:
    """Summarize cluster archetypes and exemplars."""
    cluster_rows: list[dict] = []
    for cluster_id in sorted(frame[cluster_col].unique()):
        cluster_mask = frame[cluster_col].eq(cluster_id).to_numpy()
        ids = np.flatnonzero(cluster_mask)
        centroid = normalize(vectors[ids].mean(axis=0, keepdims=True))[0]
        exemplar_order = ids[np.argsort(-(vectors[ids] @ centroid))]
        category_counts = Counter(frame.loc[cluster_mask, "primary_category"].dropna())
        kind_counts = Counter(frame.loc[cluster_mask, "kind"])
        page_sections = frame.loc[cluster_mask, "page_section"].replace("", "root-page")
        section_counts = Counter(page_sections[frame.loc[cluster_mask, "kind"].eq("page")])
        years = frame.loc[cluster_mask & frame["year"].notna(), "year"]
        cluster_rows.append(
            {
                "cluster": int(cluster_id),
                "size": int(cluster_mask.sum()),
                "share": float(cluster_mask.mean()),
                "top_terms": " | ".join(cluster_terms[int(cluster_id)][:6]),
                "top_categories": " | ".join(f"{name}:{count}" for name, count in category_counts.most_common(5)),
                "kinds": " | ".join(f"{name}:{count}" for name, count in kind_counts.most_common()),
                "page_sections": " | ".join(f"{name}:{count}" for name, count in section_counts.most_common(5)),
                "median_year": float(years.median()) if not years.empty else np.nan,
                "exemplar_paths": " | ".join(frame.iloc[exemplar_order[:5]]["path"].tolist()),
                "exemplar_titles": " | ".join(frame.iloc[exemplar_order[:5]]["title"].tolist()),
            }
        )
    return pd.DataFrame(cluster_rows).sort_values("size", ascending=False)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    embeddings = pd.read_parquet(INPUT_PATH)
    metadata = markdown_rows()
    frame = embeddings.merge(metadata, on="path", how="left", validate="one_to_one")
    missing_metadata = frame["title"].isna().sum()
    if missing_metadata:
        raise RuntimeError(f"{missing_metadata} embedding rows are missing markdown metadata")

    vectors = np.vstack(frame["embedding"].to_numpy()).astype(np.float32)
    vectors = normalize(vectors)
    similarity = cosine_pair_matrix(vectors).astype(np.float32)
    np.fill_diagonal(similarity, -1.0)

    pca_model = PCA(n_components=min(50, len(frame) - 1), random_state=42)
    pca_features = pca_model.fit_transform(vectors)
    frame["pca_1"] = pca_features[:, 0]
    frame["pca_2"] = pca_features[:, 1]

    umap_features = umap.UMAP(
        n_components=2,
        n_neighbors=35,
        min_dist=0.18,
        metric="cosine",
        random_state=42,
    ).fit_transform(vectors)
    frame["umap_1"] = umap_features[:, 0]
    frame["umap_2"] = umap_features[:, 1]

    broad_clusters, cluster_metrics = choose_cluster_count(pca_features[:, :20])
    fine_clusters = FINE_CLUSTER_COUNT
    save_cluster_selection_plot(cluster_metrics)

    frame["cluster_broad"] = fit_clusters(pca_features[:, :20], broad_clusters)
    frame["cluster"] = fit_clusters(pca_features[:, :20], fine_clusters)
    broad_terms = top_terms_by_cluster(frame["body_clean"], frame["cluster_broad"])
    fine_terms = top_terms_by_cluster(frame["body_clean"], frame["cluster"])
    frame["cluster_broad_name_terms"] = frame["cluster_broad"].map(
        {key: ", ".join(value[:3]) for key, value in broad_terms.items()}
    )
    frame["cluster_name_terms"] = frame["cluster"].map(
        {key: ", ".join(value[:3]) for key, value in fine_terms.items()}
    )

    neighbor_ids = np.argsort(-similarity, axis=1)[:, :TOP_NEIGHBORS]
    neighbor_sims = np.take_along_axis(similarity, neighbor_ids, axis=1)
    frame["nearest_neighbor_similarity"] = neighbor_sims[:, 0]
    frame["mean_top5_similarity"] = neighbor_sims[:, :5].mean(axis=1)
    frame["mean_top10_similarity"] = neighbor_sims[:, :10].mean(axis=1)
    frame["outlier_score"] = 1 - frame["mean_top5_similarity"]
    frame["hubness"] = np.bincount(neighbor_ids[:, :10].ravel(), minlength=len(frame))

    primary_categories = frame["primary_category"].fillna("(none)").to_numpy()
    category_sets = frame["categories"].apply(set).to_list()

    neighbor_rows: list[dict] = []
    for source_index, target_indices in enumerate(neighbor_ids):
        source_categories = category_sets[source_index]
        source_row = frame.iloc[source_index]
        for rank, target_index in enumerate(target_indices, start=1):
            target_row = frame.iloc[target_index]
            shared_categories = sorted(source_categories & category_sets[target_index])
            neighbor_rows.append(
                {
                    "source_path": source_row["path"],
                    "source_title": source_row["title"],
                    "source_kind": source_row["kind"],
                    "source_year": source_row["year"],
                    "source_cluster": int(source_row["cluster"]),
                    "source_cluster_broad": int(source_row["cluster_broad"]),
                    "target_path": target_row["path"],
                    "target_title": target_row["title"],
                    "target_kind": target_row["kind"],
                    "target_year": target_row["year"],
                    "target_cluster": int(target_row["cluster"]),
                    "target_cluster_broad": int(target_row["cluster_broad"]),
                    "rank": rank,
                    "similarity": float(similarity[source_index, target_index]),
                    "same_kind": source_row["kind"] == target_row["kind"],
                    "same_cluster": int(source_row["cluster"]) == int(target_row["cluster"]),
                    "same_primary_category": source_row["primary_category"] == target_row["primary_category"],
                    "shared_categories": " | ".join(shared_categories),
                    "shared_category_count": len(shared_categories),
                    "year_gap": (
                        abs(int(source_row["year"]) - int(target_row["year"]))
                        if pd.notna(source_row["year"]) and pd.notna(target_row["year"])
                        else pd.NA
                    ),
                    "target_hubness": int(target_row["hubness"]),
                }
            )
    neighbors = pd.DataFrame(neighbor_rows)

    labeled_mask = frame["categories"].map(bool).to_numpy()
    labeled_indices = np.flatnonzero(labeled_mask)
    baseline_same_category = float(
        np.mean(
            [
                np.mean(
                    [
                        bool(category_sets[source_id] & category_sets[target_id])
                        for target_id in labeled_indices
                        if target_id != source_id
                    ]
                )
                for source_id in labeled_indices
            ]
        )
    )
    category_alignment_rows: list[dict] = []
    for k in (1, 3, 5, 10):
        hit_rate = float(
            np.mean(
                [
                    np.mean(
                        [
                            bool(category_sets[source_id] & category_sets[target_id])
                            for target_id in neighbor_ids[source_id, :k]
                        ]
                    )
                    for source_id in labeled_indices
                ]
            )
        )
        category_alignment_rows.append(
            {
                "k": k,
                "same_category_hit_rate": hit_rate,
                "baseline_same_category_rate": baseline_same_category,
                "lift_vs_baseline": hit_rate / baseline_same_category,
            }
        )
    category_alignment = pd.DataFrame(category_alignment_rows)

    same_cluster_rate_rows = []
    for k in (1, 3, 5, 10):
        same_cluster_rate_rows.append(
            {
                "k": k,
                "same_cluster_hit_rate": float(
                    np.mean(
                        [
                            np.mean(frame.iloc[targets]["cluster"].to_numpy() == frame.iloc[source_id]["cluster"])
                            for source_id, targets in enumerate(neighbor_ids[:, :k])
                        ]
                    )
                ),
            }
        )
    cluster_neighbor_alignment = pd.DataFrame(same_cluster_rate_rows)

    primary_category_counts = frame["primary_category"].value_counts(dropna=True)
    sizeable_categories = primary_category_counts[primary_category_counts >= 25].index.tolist()
    category_stats_rows = []
    valid_similarity = similarity.copy()
    np.fill_diagonal(valid_similarity, np.nan)
    overall_mean_similarity = float(np.nanmean(valid_similarity))
    for category in sizeable_categories:
        ids = frame.index[frame["primary_category"].eq(category)].to_numpy()
        within = similarity[np.ix_(ids, ids)].astype(float)
        np.fill_diagonal(within, np.nan)
        category_stats_rows.append(
            {
                "category": category,
                "count": len(ids),
                "within_mean_similarity": float(np.nanmean(within)),
                "lift_vs_global": float(np.nanmean(within) / overall_mean_similarity),
            }
        )
    category_stats = pd.DataFrame(category_stats_rows).sort_values(
        ["lift_vs_global", "count"], ascending=[False, False]
    )

    single_category_mask = frame["category_count"].eq(1) & frame["primary_category"].isin(sizeable_categories)
    cluster_nmi = float(
        normalized_mutual_info_score(
            frame.loc[single_category_mask, "primary_category"],
            frame.loc[single_category_mask, "cluster"],
        )
    )
    cluster_nmi_broad = float(
        normalized_mutual_info_score(
            frame.loc[single_category_mask, "primary_category"],
            frame.loc[single_category_mask, "cluster_broad"],
        )
    )

    cluster_category = (
        frame.loc[frame["primary_category"].isin(sizeable_categories), ["cluster", "primary_category"]]
        .value_counts()
        .rename("count")
        .reset_index()
        .pivot(index="cluster", columns="primary_category", values="count")
        .fillna(0)
    )
    cluster_category_share = cluster_category.div(cluster_category.sum(axis=1), axis=0)

    category_neighbor_rows = []
    labeled_neighbors = neighbors.loc[
        neighbors["source_path"].isin(frame.loc[labeled_mask, "path"])
        & neighbors["target_path"].isin(frame.loc[labeled_mask, "path"])
        & neighbors["rank"].le(5)
    ].copy()
    category_prevalence = (
        frame.loc[frame["primary_category"].isin(sizeable_categories), "primary_category"].value_counts(normalize=True).to_dict()
    )
    for source_category in sizeable_categories:
        source_subset = labeled_neighbors.loc[
            frame.set_index("path").loc[labeled_neighbors["source_path"], "primary_category"].to_numpy()
            == source_category
        ].copy()
        target_categories = frame.set_index("path").loc[source_subset["target_path"], "primary_category"].fillna("(none)")
        target_distribution = target_categories.value_counts(normalize=True)
        for target_category, observed in target_distribution.items():
            baseline = category_prevalence.get(target_category)
            if baseline is None or baseline == 0:
                continue
            category_neighbor_rows.append(
                {
                    "source_category": source_category,
                    "target_category": target_category,
                    "observed_share": observed,
                    "baseline_share": baseline,
                    "lift": observed / baseline,
                    "support": int((target_categories == target_category).sum()),
                }
            )
    category_overlap = pd.DataFrame(category_neighbor_rows).sort_values(
        ["lift", "support"], ascending=[False, False]
    )
    overlap_matrix = (
        category_overlap.loc[
            category_overlap["source_category"].isin(sizeable_categories[:12])
            & category_overlap["target_category"].isin(sizeable_categories[:12])
        ]
        .pivot(index="source_category", columns="target_category", values="lift")
        .fillna(1.0)
    )

    kind_mix = (
        neighbors.loc[neighbors["rank"].le(5)]
        .groupby(["source_kind", "target_kind"])
        .size()
        .rename("count")
        .reset_index()
    )
    kind_mix["share"] = kind_mix.groupby("source_kind")["count"].transform(lambda values: values / values.sum())

    posts = frame.loc[frame["kind"].eq("post") & frame["date"].notna()].sort_values("date").copy()
    post_indices = posts.index.to_numpy()
    novelty_rows: list[dict] = []
    for position, source_index in enumerate(post_indices):
        previous_ids = post_indices[:position]
        if len(previous_ids) == 0:
            novelty_rows.append(
                {
                    "path": frame.iloc[source_index]["path"],
                    "title": frame.iloc[source_index]["title"],
                    "date": frame.iloc[source_index]["date"],
                    "year": frame.iloc[source_index]["year"],
                    "best_previous_path": None,
                    "best_previous_title": None,
                    "best_previous_similarity": np.nan,
                    "novelty": np.nan,
                }
            )
            continue
        previous_sims = similarity[source_index, previous_ids]
        best_pos = int(previous_sims.argmax())
        best_previous_index = previous_ids[best_pos]
        best_previous_similarity = float(previous_sims[best_pos])
        novelty_rows.append(
            {
                "path": frame.iloc[source_index]["path"],
                "title": frame.iloc[source_index]["title"],
                "date": frame.iloc[source_index]["date"],
                "year": frame.iloc[source_index]["year"],
                "best_previous_path": frame.iloc[best_previous_index]["path"],
                "best_previous_title": frame.iloc[best_previous_index]["title"],
                "best_previous_similarity": best_previous_similarity,
                "novelty": 1 - best_previous_similarity,
            }
        )
    novelty = pd.DataFrame(novelty_rows)
    frame = frame.merge(novelty[["path", "best_previous_path", "best_previous_similarity", "novelty"]], on="path", how="left")

    yearly_posts = frame.loc[frame["kind"].eq("post") & frame["year"].notna()].copy()
    valid_years = yearly_posts["year"].value_counts().sort_index()
    valid_years = valid_years[valid_years >= 10]
    yearly_vectors: list[dict] = []
    previous_year = None
    previous_vector = None
    year_cluster_mix = (
        yearly_posts.loc[yearly_posts["year"].isin(valid_years.index)]
        .groupby(["year", "cluster"])
        .size()
        .rename("count")
        .reset_index()
    )
    year_cluster_mix["share"] = year_cluster_mix.groupby("year")["count"].transform(lambda values: values / values.sum())
    for year in valid_years.index:
        ids = yearly_posts.index[yearly_posts["year"].eq(year)].to_numpy()
        vector = normalize(vectors[ids].mean(axis=0, keepdims=True))[0]
        drift = np.nan if previous_vector is None else 1 - float(vector @ previous_vector)
        similarity_to_previous = np.nan if previous_vector is None else float(vector @ previous_vector)
        yearly_vectors.append(
            {
                "year": int(year),
                "count": int(len(ids)),
                "drift_from_previous_year": drift,
                "similarity_to_previous_year": similarity_to_previous,
            }
        )
        previous_year = year
        previous_vector = vector

    yearly_summary = pd.DataFrame(yearly_vectors)

    year_centroid_matrix = np.vstack(
        [
            normalize(
                vectors[yearly_posts.index[yearly_posts["year"].eq(year)].to_numpy()].mean(axis=0, keepdims=True)
            )[0]
            for year in valid_years.index
        ]
    )
    year_pca = PCA(n_components=2, random_state=42).fit_transform(year_centroid_matrix)
    yearly_summary["pca_1"] = year_pca[:, 0]
    yearly_summary["pca_2"] = year_pca[:, 1]

    cluster_summary = build_cluster_summary(frame, vectors, "cluster", fine_terms)
    broad_cluster_summary = build_cluster_summary(frame, vectors, "cluster_broad", broad_terms)

    outliers = frame.sort_values("outlier_score", ascending=False).head(40).copy()
    hubs = frame.sort_values(["hubness", "mean_top5_similarity"], ascending=[False, False]).head(40).copy()
    bridges = (
        neighbors.loc[neighbors["rank"].le(10)]
        .groupby("source_path")
        .agg(
            distinct_target_clusters=("target_cluster", "nunique"),
            distinct_target_kinds=("target_kind", "nunique"),
            mean_similarity=("similarity", "mean"),
        )
        .reset_index()
        .merge(frame[["path", "title", "cluster", "kind", "primary_category"]], left_on="source_path", right_on="path")
        .sort_values(["distinct_target_clusters", "mean_similarity"], ascending=[False, False])
        .head(40)
    )

    related_rows = []
    post_frame = frame.loc[frame["kind"].eq("post")].copy()
    for source_index in post_frame.index:
        candidates = [idx for idx in neighbor_ids[source_index] if frame.iloc[idx]["kind"] == "post"][:15]
        diversified = mmr_rerank(candidates, source_index, similarity, top_k=5)
        for pure_rank, target_index in enumerate(candidates[:5], start=1):
            related_rows.append(
                {
                    "strategy": "pure_cosine",
                    "source_path": frame.iloc[source_index]["path"],
                    "source_title": frame.iloc[source_index]["title"],
                    "target_path": frame.iloc[target_index]["path"],
                    "target_title": frame.iloc[target_index]["title"],
                    "rank": pure_rank,
                    "similarity": float(similarity[source_index, target_index]),
                    "same_primary_category": frame.iloc[source_index]["primary_category"] == frame.iloc[target_index]["primary_category"],
                    "target_hubness": int(frame.iloc[target_index]["hubness"]),
                }
            )
        for rerank, target_index in enumerate(diversified, start=1):
            related_rows.append(
                {
                    "strategy": "diversified_mmr",
                    "source_path": frame.iloc[source_index]["path"],
                    "source_title": frame.iloc[source_index]["title"],
                    "target_path": frame.iloc[target_index]["path"],
                    "target_title": frame.iloc[target_index]["title"],
                    "rank": rerank,
                    "similarity": float(similarity[source_index, target_index]),
                    "same_primary_category": frame.iloc[source_index]["primary_category"] == frame.iloc[target_index]["primary_category"],
                    "target_hubness": int(frame.iloc[target_index]["hubness"]),
                }
            )
    related_posts = pd.DataFrame(related_rows)

    frame["cluster_label"] = frame["cluster"].map(
        {cluster_id: ", ".join(terms[:3]) for cluster_id, terms in fine_terms.items()}
    )
    frame["cluster_broad_label"] = frame["cluster_broad"].map(
        {cluster_id: ", ".join(terms[:3]) for cluster_id, terms in broad_terms.items()}
    )
    frame["primary_category"] = frame["primary_category"].fillna("(none)")
    frame["page_section"] = frame["page_section"].replace("", "(not-page)")

    frame_for_plot = frame.copy()
    frame_for_plot["year_label"] = frame_for_plot["year"].astype("string").fillna("undated")
    top_categories_for_plot = primary_category_counts.head(10).index.tolist()
    frame_for_plot["category_for_plot"] = np.where(
        frame_for_plot["primary_category"].isin(top_categories_for_plot),
        frame_for_plot["primary_category"],
        "other/none",
    )

    scatter_plot(
        frame_for_plot,
        "pca_1",
        "pca_2",
        "cluster_label",
        OUT_DIR / "pca-clusters.png",
        f"PCA View of Embedding Space ({fine_clusters} clusters)",
        legend=False,
    )
    scatter_plot(
        frame_for_plot,
        "umap_1",
        "umap_2",
        "cluster_label",
        OUT_DIR / "umap-clusters.png",
        f"UMAP View of Embedding Space ({fine_clusters} clusters)",
        legend=False,
    )
    scatter_plot(
        frame_for_plot,
        "umap_1",
        "umap_2",
        "cluster_broad_label",
        OUT_DIR / "umap-broad-clusters.png",
        f"UMAP View of Broad Corpus Phases ({broad_clusters} clusters)",
        legend=False,
    )
    scatter_plot(
        frame_for_plot,
        "umap_1",
        "umap_2",
        "category_for_plot",
        OUT_DIR / "umap-categories.png",
        "UMAP Colored by Top Categories",
        palette="tab10",
        legend=False,
    )

    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(
        frame_for_plot["umap_1"],
        frame_for_plot["umap_2"],
        c=frame_for_plot["year"].fillna(frame_for_plot["year"].median()).astype(float),
        cmap="viridis",
        s=16,
        alpha=0.8,
        linewidths=0,
    )
    ax.set_title("UMAP Colored by Year")
    ax.set_xlabel("UMAP 1")
    ax.set_ylabel("UMAP 2")
    fig.colorbar(scatter, ax=ax, label="Year")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "umap-year.png", dpi=PLOT_DPI)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 6))
    sns.scatterplot(
        data=frame.sort_values("kind"),
        x="hubness",
        y="mean_top5_similarity",
        hue="kind",
        size="outlier_score",
        sizes=(18, 140),
        alpha=0.8,
        ax=ax,
    )
    label_extremes(ax, frame.sort_values("outlier_score", ascending=False).head(20), "hubness", "mean_top5_similarity")
    ax.set_title("Hubness vs Local Density")
    ax.set_xlabel("Times Appearing in Others' Top 10")
    ax.set_ylabel("Mean Top-5 Neighbor Similarity")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "hubness-vs-density.png", dpi=PLOT_DPI)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 6))
    novelty_valid = novelty.dropna(subset=["novelty"]).copy()
    sns.scatterplot(data=novelty_valid, x="date", y="novelty", s=18, alpha=0.35, ax=ax)
    yearly_novelty = novelty_valid.groupby("year")["novelty"].mean().reset_index()
    sns.lineplot(data=yearly_novelty, x="year", y="novelty", marker="o", color="#d62728", ax=ax)
    ax.set_title("Novelty Over Time")
    ax.set_ylabel("1 - best similarity to any earlier post")
    ax.set_xlabel("")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "novelty-over-time.png", dpi=PLOT_DPI)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(yearly_summary["pca_1"], yearly_summary["pca_2"], marker="o", color="#1f77b4")
    for row in yearly_summary.itertuples():
        ax.text(row.pca_1, row.pca_2, str(row.year), fontsize=8)
    ax.set_title("Yearly Embedding Centroids")
    ax.set_xlabel("PCA 1")
    ax.set_ylabel("PCA 2")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "year-centroid-drift.png", dpi=PLOT_DPI)
    plt.close(fig)

    year_cluster_heatmap = (
        year_cluster_mix.pivot(index="year", columns="cluster", values="share").fillna(0).sort_index()
    )
    heatmap_plot(year_cluster_heatmap, OUT_DIR / "year-cluster-heatmap.png", "Cluster Share by Year")
    heatmap_plot(
        cluster_category_share.loc[:, cluster_category_share.sum().sort_values(ascending=False).head(10).index],
        OUT_DIR / "cluster-category-heatmap.png",
        "Cluster Mix Across Top Categories",
    )
    heatmap_plot(
        overlap_matrix.loc[:, overlap_matrix.sum().sort_values(ascending=False).head(min(12, overlap_matrix.shape[1])).index],
        OUT_DIR / "category-overlap-heatmap.png",
        "Neighbor Lift Between Categories",
        cmap="rocket",
    )

    frame.sort_values("path").to_parquet(OUT_DIR / "documents.parquet", index=False)
    frame.sort_values("path").drop(columns=["embedding", "body_clean", "embed_clean"]).to_csv(
        OUT_DIR / "documents.csv", index=False
    )
    neighbors.to_parquet(OUT_DIR / "neighbors.parquet", index=False)
    cluster_metrics.to_csv(OUT_DIR / "cluster-metrics.csv", index=False)
    cluster_summary.to_csv(OUT_DIR / "cluster-summary.csv", index=False)
    broad_cluster_summary.to_csv(OUT_DIR / "broad-cluster-summary.csv", index=False)
    category_alignment.to_csv(OUT_DIR / "category-alignment.csv", index=False)
    cluster_neighbor_alignment.to_csv(OUT_DIR / "cluster-neighbor-alignment.csv", index=False)
    category_stats.to_csv(OUT_DIR / "category-cohesion.csv", index=False)
    category_overlap.to_csv(OUT_DIR / "category-overlap.csv", index=False)
    yearly_summary.to_csv(OUT_DIR / "yearly-centroids.csv", index=False)
    novelty.sort_values(["novelty", "date"], ascending=[False, True]).to_csv(OUT_DIR / "novelty.csv", index=False)
    outliers.to_csv(OUT_DIR / "outliers.csv", index=False)
    hubs.to_csv(OUT_DIR / "hubs.csv", index=False)
    bridges.to_csv(OUT_DIR / "bridges.csv", index=False)
    kind_mix.to_csv(OUT_DIR / "kind-neighbor-mix.csv", index=False)
    related_posts.to_parquet(OUT_DIR / "related-posts.parquet", index=False)

    summary = {
        "documents": int(len(frame)),
        "posts": int(frame["kind"].eq("post").sum()),
        "pages": int(frame["kind"].eq("page").sum()),
        "categories_labeled": int(frame["categories"].map(bool).sum()),
        "truncated_inputs": int(frame["was_truncated"].sum()),
        "documents_with_comments": int(frame["has_comments"].sum()),
        "broad_clusters": int(broad_clusters),
        "fine_clusters": int(fine_clusters),
        "cluster_category_nmi_single_label": cluster_nmi,
        "broad_cluster_category_nmi_single_label": cluster_nmi_broad,
        "overall_mean_similarity": overall_mean_similarity,
        "median_top5_similarity": float(frame["mean_top5_similarity"].median()),
    }
    (OUT_DIR / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
