#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "numpy>=2.2",
#   "pandas>=2.2",
#   "pyarrow>=20.0",
#   "pyyaml>=6.0",
#   "typer>=0.12",
# ]
# ///
"""Build a reviewable canonical tag vocabulary from existing keywords."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
import re
from typing import Annotated, Any

import numpy as np
import pandas as pd
import typer
import yaml


app = typer.Typer(add_completion=False)

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
MULTI_HYPHEN_RE = re.compile(r"-+")
ACRONYMS = {
    "ai": "AI",
    "api": "API",
    "apis": "APIs",
    "css": "CSS",
    "gpt": "GPT",
    "html": "HTML",
    "llm": "LLM",
    "llms": "LLMs",
    "mcp": "MCP",
    "pdf": "PDF",
    "rss": "RSS",
    "ui": "UI",
    "ux": "UX",
}
MANUAL_ALIASES = {
    "artificial-intelligence": "ai",
    "large-language-model": "llms",
    "large-language-models": "llms",
    "llm": "llms",
    "visualisation": "data-visualization",
    "visualization": "data-visualization",
    "data-visualisation": "data-visualization",
    "dataviz": "data-visualization",
    "genai": "generative-ai",
    "gen-ai": "generative-ai",
}


@dataclass
class KeywordInfo:
    raw: str
    slug: str
    folded: str
    paths: set[str] = field(default_factory=set)

    @property
    def count(self) -> int:
        return len(self.paths)


@dataclass
class TagGroup:
    canonical: str
    aliases: set[str] = field(default_factory=set)
    paths: set[str] = field(default_factory=set)
    centroid: np.ndarray | None = None

    @property
    def count(self) -> int:
        return len(self.paths)


def split_front_matter(text: str) -> dict[str, Any]:
    """Return YAML front matter from a Markdown file."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    payload = yaml.safe_load(match.group(1)) or {}
    return payload if isinstance(payload, dict) else {}


def as_list(value: Any) -> list[str]:
    """Return a front matter value as a clean string list."""
    if value is None:
        return []
    items = value if isinstance(value, list) else [value]
    return [str(item).strip() for item in items if str(item).strip()]


def markdown_files(root: Path = ROOT) -> list[Path]:
    """Return source post/page Markdown files."""
    return sorted([*(root / "posts").rglob("*.md"), *(root / "pages").rglob("*.md")])


def normalize_slug(value: str) -> str:
    """Normalize a freeform keyword into a URL/tag slug."""
    text = value.strip().lower()
    text = text.replace("&", " and ")
    text = text.replace("+", " plus ")
    text = text.replace("'", "")
    text = NON_ALNUM_RE.sub("-", text)
    text = MULTI_HYPHEN_RE.sub("-", text).strip("-")
    return MANUAL_ALIASES.get(text, text)


def singular_token(token: str) -> str:
    """Apply a conservative English singular fold."""
    if len(token) <= 3 or token in {"css", "rss", "llms"}:
        return token
    if token.endswith("ies") and len(token) > 4:
        return f"{token[:-3]}y"
    if token.endswith("ses") or token.endswith("xes") or token.endswith("ches") or token.endswith("shes"):
        return token[:-2]
    if token.endswith("s") and not token.endswith(("ss", "us", "is")):
        return token[:-1]
    return token


def folded_slug(slug: str) -> str:
    """Return a slug used only for trivial variant detection."""
    return "-".join(singular_token(token) for token in slug.split("-"))


def display_name(slug: str) -> str:
    """Render a human-readable name for descriptions."""
    words = []
    for token in slug.split("-"):
        words.append(ACRONYMS.get(token, token))
    return " ".join(words)


def collect_keywords(root: Path = ROOT) -> dict[str, KeywordInfo]:
    """Collect keyword occurrences by source document."""
    by_slug: dict[str, KeywordInfo] = {}
    for path in markdown_files(root):
        rel_path = path.relative_to(root).as_posix()
        front_matter = split_front_matter(path.read_text(encoding="utf-8", errors="replace"))
        for raw in set(as_list(front_matter.get("keywords"))):
            slug = normalize_slug(raw)
            if not slug:
                continue
            info = by_slug.setdefault(slug, KeywordInfo(raw=raw, slug=slug, folded=folded_slug(slug)))
            info.paths.add(rel_path)
    return by_slug


def collect_keyword_aliases(root: Path = ROOT) -> dict[str, set[str]]:
    """Collect original keyword spellings for each normalized slug."""
    aliases: dict[str, set[str]] = defaultdict(set)
    for path in markdown_files(root):
        front_matter = split_front_matter(path.read_text(encoding="utf-8", errors="replace"))
        for raw in as_list(front_matter.get("keywords")):
            slug = normalize_slug(raw)
            if slug:
                aliases[slug].add(raw)
    return aliases


def load_embeddings(path: Path) -> dict[str, np.ndarray]:
    """Load document embeddings as normalized vectors keyed by source path."""
    if not path.is_file():
        return {}
    frame = pd.read_parquet(path, columns=["path", "embedding"])
    embeddings: dict[str, np.ndarray] = {}
    for row in frame.itertuples(index=False):
        vector = np.array(row.embedding, dtype=np.float32)
        norm = np.linalg.norm(vector)
        if norm:
            embeddings[str(row.path)] = vector / norm
    return embeddings


def centroid(paths: set[str], embeddings: dict[str, np.ndarray]) -> np.ndarray | None:
    """Return a normalized centroid for paths with embeddings."""
    vectors = [embeddings[path] for path in sorted(paths) if path in embeddings]
    if not vectors:
        return None
    center = np.mean(vectors, axis=0)
    norm = np.linalg.norm(center)
    return center / norm if norm else None


def choose_canonical(slugs: list[str], counts: Counter[str]) -> str:
    """Choose the most common, shortest canonical slug in a folded group."""
    return sorted(slugs, key=lambda slug: (-counts[slug], len(slug), slug))[0]


def seed_groups(keywords: dict[str, KeywordInfo], min_count: int) -> tuple[dict[str, TagGroup], dict[str, str]]:
    """Create canonical seed groups from frequent folded keywords."""
    counts = Counter({slug: info.count for slug, info in keywords.items()})
    folded: dict[str, list[str]] = defaultdict(list)
    for slug, info in keywords.items():
        folded[info.folded].append(slug)

    groups: dict[str, TagGroup] = {}
    slug_to_canonical: dict[str, str] = {}
    for slugs in folded.values():
        paths = set().union(*(keywords[slug].paths for slug in slugs))
        if len(paths) < min_count:
            continue
        canonical = MANUAL_ALIASES.get(choose_canonical(slugs, counts), choose_canonical(slugs, counts))
        group = groups.setdefault(canonical, TagGroup(canonical=canonical))
        for slug in slugs:
            slug_to_canonical[slug] = canonical
            group.aliases.add(slug)
            group.paths.update(keywords[slug].paths)
    for canonical, target in MANUAL_ALIASES.items():
        if canonical in slug_to_canonical and target in groups:
            slug_to_canonical[canonical] = target
    return groups, slug_to_canonical


def cosine(left: np.ndarray | None, right: np.ndarray | None) -> float:
    """Return cosine similarity for normalized vectors."""
    if left is None or right is None:
        return 0.0
    return float(np.dot(left, right))


def token_jaccard(left: str, right: str) -> float:
    """Return token-set overlap for two slugs."""
    a = set(left.split("-"))
    b = set(right.split("-"))
    return len(a & b) / max(1, len(a | b))


def similar_enough(alias: str, group: TagGroup, alias_centroid: np.ndarray | None) -> bool:
    """Decide whether a keyword should migrate into an existing canonical group."""
    ratio = SequenceMatcher(None, alias, group.canonical).ratio()
    if folded_slug(alias) == folded_slug(group.canonical):
        return True
    if ratio >= 0.88:
        return True
    if token_jaccard(alias, group.canonical) >= 0.5 and cosine(alias_centroid, group.centroid) >= 0.90:
        return True
    return cosine(alias_centroid, group.centroid) >= 0.96 and token_jaccard(alias, group.canonical) >= 0.25


def plausible_alias(alias: str, canonical: str) -> bool:
    """Return whether a pair is worth checking with embeddings."""
    if folded_slug(alias) == folded_slug(canonical):
        return True
    if token_jaccard(alias, canonical) >= 0.25:
        return True
    return SequenceMatcher(None, alias, canonical).ratio() >= 0.70


def merge_aliases(
    keywords: dict[str, KeywordInfo],
    groups: dict[str, TagGroup],
    slug_to_canonical: dict[str, str],
    embeddings: dict[str, np.ndarray],
) -> dict[str, str]:
    """Map infrequent near-duplicate keywords into canonical groups."""
    for group in groups.values():
        group.centroid = centroid(group.paths, embeddings)

    ordered_groups = sorted(groups.values(), key=lambda group: (-group.count, group.canonical))
    groups_by_token: dict[str, set[str]] = defaultdict(set)
    groups_by_folded: dict[str, set[str]] = defaultdict(set)
    for group in ordered_groups:
        groups_by_folded[folded_slug(group.canonical)].add(group.canonical)
        for token in group.canonical.split("-"):
            groups_by_token[token].add(group.canonical)
    group_lookup = {group.canonical: group for group in ordered_groups}
    keyword_centroids = {
        slug: centroid(info.paths, embeddings)
        for slug, info in keywords.items()
        if slug not in slug_to_canonical
    }
    for slug, info in sorted(keywords.items(), key=lambda item: (-item[1].count, item[0])):
        if slug in slug_to_canonical:
            continue
        if slug in MANUAL_ALIASES and MANUAL_ALIASES[slug] in groups:
            target = MANUAL_ALIASES[slug]
        else:
            alias_centroid = keyword_centroids.get(slug)
            candidate_names = set(groups_by_folded.get(folded_slug(slug), set()))
            for token in slug.split("-"):
                candidate_names.update(groups_by_token.get(token, set()))
            candidates = [group_lookup[name] for name in candidate_names]
            matches = [
                group
                for group in candidates
                if plausible_alias(slug, group.canonical)
                and similar_enough(slug, group, alias_centroid)
            ]
            if not matches:
                continue
            target = sorted(
                matches,
                key=lambda group: (
                    -SequenceMatcher(None, slug, group.canonical).ratio(),
                    -cosine(alias_centroid, group.centroid),
                    -group.count,
                    group.canonical,
                ),
            )[0].canonical
        slug_to_canonical[slug] = target
        groups[target].aliases.add(slug)
        groups[target].paths.update(info.paths)
    return slug_to_canonical


def output_payload(
    keywords: dict[str, KeywordInfo],
    aliases_by_slug: dict[str, set[str]],
    groups: dict[str, TagGroup],
    slug_to_canonical: dict[str, str],
    min_count: int,
) -> dict[str, Any]:
    """Build deterministic metadata-tags.yml payload."""
    dropped = sorted(slug for slug in keywords if slug not in slug_to_canonical)
    ordered = sorted(groups.values(), key=lambda group: (-group.count, group.canonical))
    tags: dict[str, Any] = {}
    for group in ordered:
        original_aliases = set()
        for slug in sorted(group.aliases):
            original_aliases.update(aliases_by_slug.get(slug, {slug}))
        canonical_label = display_name(group.canonical).lower()
        canonical_aliases = sorted(
            alias
            for alias in original_aliases
            if alias.strip().lower() not in {group.canonical, canonical_label}
        )
        tags[group.canonical] = {
            "description": f"Posts about {display_name(group.canonical)}.",
            "aliases": canonical_aliases,
            "count": group.count,
        }
    return {
        "generated_by": "scripts/normalize_tags.py",
        "min_seed_count": min_count,
        "canonical_tag_count": len(tags),
        "dropped_keyword_count": len(dropped),
        "tags": tags,
    }


def build_vocabulary(
    root: Path = ROOT,
    embeddings_path: Path = ROOT / "analysis/embeddings/embeddings.parquet",
    min_count: int = 5,
) -> dict[str, Any]:
    """Build the canonical tag vocabulary payload."""
    keywords = collect_keywords(root)
    aliases_by_slug = collect_keyword_aliases(root)
    groups, slug_to_canonical = seed_groups(keywords, min_count)
    embeddings = load_embeddings(embeddings_path)
    merge_aliases(keywords, groups, slug_to_canonical, embeddings)
    return output_payload(keywords, aliases_by_slug, groups, slug_to_canonical, min_count)


@app.command()
def main(
    output: Annotated[Path, typer.Option()] = ROOT / "metadata-tags.yml",
    embeddings_path: Annotated[Path, typer.Option()] = ROOT / "analysis/embeddings/embeddings.parquet",
    min_count: Annotated[int, typer.Option(help="Minimum documents for canonical seed tags.")] = 5,
) -> None:
    """Write metadata-tags.yml for human review."""
    payload = build_vocabulary(ROOT, embeddings_path, min_count)
    output.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")
    typer.echo(
        f"tags\t{payload['canonical_tag_count']}\tdropped\t{payload['dropped_keyword_count']}\t{output}"
    )


if __name__ == "__main__":
    app()
