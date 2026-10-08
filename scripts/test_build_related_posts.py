from pathlib import Path
import importlib.util
import json
import os
import sys

import pytest


SPEC = importlib.util.spec_from_file_location(
    "build_related_posts", Path(__file__).with_name("build_related_posts.py")
)
build_related_posts = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = build_related_posts
SPEC.loader.exec_module(build_related_posts)


def write_post(
    path: Path,
    title: str,
    *,
    description: str = "",
    body: str = "",
    tags: list[str] | None = None,
    slug: str | None = None,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    slug_line = f"slug: {slug}\n" if slug else ""
    path.write_text(
        "---\n"
        f"title: {title}\n"
        "date: 2026-01-01T00:00:00+00:00\n"
        f"description: {description}\n"
        f"tags: [{', '.join(tags or [])}]\n"
        f"{slug_line}"
        "---\n\n"
        f"{body}\n",
        encoding="utf-8",
    )


def build(tmp_path: Path, *, top_k: int = 3):
    output = tmp_path / "related.json"
    cwd = Path.cwd()
    try:
        os.chdir(tmp_path)
        related = build_related_posts.build_related_posts(output_path=output, top_k=top_k)
    finally:
        os.chdir(cwd)
    return related, output


def test_build_related_posts_writes_compact_slug_neighbors(tmp_path):
    write_post(tmp_path / "posts/2026/source.md", "Alpha alpha alpha", body="common")
    write_post(tmp_path / "posts/2026/title.md", "Alpha alpha alpha", body="other")
    write_post(
        tmp_path / "posts/2026/description.md",
        "Other",
        description="Alpha alpha alpha",
        body="other",
    )
    write_post(tmp_path / "posts/2026/body.md", "Other", body="Alpha alpha alpha")

    related, output = build(tmp_path)

    assert json.loads(output.read_text(encoding="utf-8")) == related
    assert related["source"] == ["title", "description", "body"]
    assert all(isinstance(slug, str) for items in related.values() for slug in items)
    assert output.read_text(encoding="utf-8").count("\n") == 1


def test_idf_weighted_tag_jaccard_breaks_text_ties(tmp_path):
    write_post(tmp_path / "posts/2026/source.md", "same", tags=["rare", "common"])
    write_post(tmp_path / "posts/2026/rare.md", "same", tags=["rare"])
    write_post(tmp_path / "posts/2026/common.md", "same", tags=["common"])
    write_post(tmp_path / "posts/2026/another-common.md", "same", tags=["common"])

    related, _ = build(tmp_path)

    assert related["source"][0] == "rare"


def test_slug_collision_fails(tmp_path):
    write_post(tmp_path / "posts/2025/first.md", "First", slug="duplicate")
    write_post(tmp_path / "posts/2026/second.md", "Second", slug="duplicate")

    with pytest.raises(ValueError, match="Slug collision.*duplicate"):
        build(tmp_path)


def test_sparse_tag_ranking_matches_exhaustive_scoring(tmp_path):
    """Keep the original all-pairs ranking as a small-corpus parity oracle."""
    from random import Random

    rng = Random(1234)
    available_tags = ["ai", "python", "india", "rare", "common", "math"]
    for index in range(30):
        write_post(
            tmp_path / f"posts/2026/post-{index:02}.md",
            f"Topic {index % 4}",
            description=f"Summary {index % 3}",
            body=f"Words for topic {index % 7}",
            tags=rng.sample(available_tags, rng.randrange(4)),
        )

    posts = build_related_posts.source_posts(tmp_path / "posts")
    documents = [" ".join([post.title] * 3 + [post.description] * 2 + [post.body]) for post in posts]
    vectors = build_related_posts.TfidfVectorizer(strip_accents="unicode").fit_transform(documents)
    similarity = (vectors @ vectors.T).toarray()
    build_related_posts.np.fill_diagonal(similarity, -build_related_posts.np.inf)
    tag_counts = {tag: sum(tag in post.tags for post in posts) for post in posts for tag in post.tags}
    tag_idf = {
        tag: build_related_posts.math.log((1 + len(posts)) / (1 + count)) + 1
        for tag, count in tag_counts.items()
    }
    expected = {}
    for source_index, source in enumerate(posts):
        scores = similarity[source_index].copy()
        for target_index, target in enumerate(posts):
            if source_index != target_index:
                scores[target_index] += 0.03 * build_related_posts.weighted_tag_jaccard(
                    source.tags, target.tags, tag_idf
                )
        order = sorted(range(len(posts)), key=lambda index: (-scores[index], posts[index].slug))
        expected[source.slug] = [posts[index].slug for index in order[:8]]

    actual, _ = build(tmp_path, top_k=8)
    assert actual == expected
