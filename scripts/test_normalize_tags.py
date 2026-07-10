from pathlib import Path
import importlib.util
import sys


SPEC = importlib.util.spec_from_file_location(
    "normalize_tags", Path(__file__).with_name("normalize_tags.py")
)
normalize_tags = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = normalize_tags
SPEC.loader.exec_module(normalize_tags)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_slug_normalization_and_plural_fold():
    assert normalize_tags.normalize_slug("Data Visualisation") == "data-visualization"
    assert normalize_tags.normalize_slug("Large Language Models") == "llms"
    assert normalize_tags.folded_slug("search-engines") == "search-engine"
    assert normalize_tags.display_name("llms") == "LLMs"


def test_build_vocabulary_merges_reviewable_aliases(tmp_path):
    write(
        tmp_path / "posts/2026/a.md",
        "---\ntitle: A\nkeywords: [LLMs, Data Visualization, Search Engines]\n---\n\nA",
    )
    write(
        tmp_path / "posts/2026/b.md",
        "---\ntitle: B\nkeywords: [llm, data visualisation, search engine]\n---\n\nB",
    )
    write(
        tmp_path / "pages/c.md",
        "---\ntitle: C\nkeywords: [large language models, dataviz, private one-off]\n---\n\nC",
    )

    payload = normalize_tags.build_vocabulary(
        root=tmp_path,
        embeddings_path=tmp_path / "missing.parquet",
        min_count=2,
    )

    assert payload["canonical_tag_count"] == 3
    assert payload["tags"]["llms"]["count"] == 3
    assert "llm" in payload["tags"]["llms"]["aliases"]
    assert "large language models" in payload["tags"]["llms"]["aliases"]
    assert payload["tags"]["data-visualization"]["count"] == 3
    assert payload["tags"]["search-engine"]["count"] == 2
    assert payload["dropped_keyword_count"] == 1
