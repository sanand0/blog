from hashlib import sha256
import importlib.util
from pathlib import Path
import sys

from ruamel.yaml import YAML
from typer.testing import CliRunner

SPEC = importlib.util.spec_from_file_location("tag_proposals", Path(__file__).with_name("tag_proposals.py"))
tag_proposals = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tag_proposals
SPEC.loader.exec_module(tag_proposals)


YAML_LOADER = YAML(typ="safe")
RUNNER = CliRunner()


def write_metadata(path: Path) -> None:
    path.write_text(
        """tags:
  llms:
    description: Posts about LLMs.
    aliases: [large language models]
    count: 2
  data-visualization:
    description: Posts about data visualization.
    aliases: [dataviz]
    count: 1
""",
        encoding="utf-8",
    )


def write_post(root: Path, relative: str, text: str) -> str:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return sha256(text.encode()).hexdigest()


def write_ledger(path: Path, proposals: dict) -> None:
    yaml = YAML()
    with path.open("w", encoding="utf-8") as handle:
        yaml.dump({"version": 1, "proposals": proposals}, handle)


def test_evaluate_auto_classifies_and_requires_three_current_sources(tmp_path):
    metadata = tmp_path / "metadata-tags.yml"
    ledger = tmp_path / "metadata-tag-proposals.yml"
    write_metadata(metadata)
    sources = {}
    for index in range(3):
        relative = f"posts/{index}.md"
        sources[relative] = {"content_hash": write_post(tmp_path, relative, f"post {index}\n")}
    write_ledger(
        ledger,
        {
            "LLMs": {"sources": sources},
            "large-language-model": {"sources": sources},
            "data-visualisation": {"sources": sources},
            "agent-memory": {"sources": sources},
            "thin-topic": {"sources": dict(list(sources.items())[:2])},
        },
    )

    result = RUNNER.invoke(
        tag_proposals.app,
        ["evaluate", "--root", str(tmp_path), "--metadata", str(metadata), "--ledger", str(ledger), "--format", "json"],
    )

    assert result.exit_code == 0, result.output
    rows = {row["proposal"]: row for row in tag_proposals.json.loads(result.output)}
    assert rows["LLMs"]["status"] == "rejected"
    assert rows["large-language-model"]["status"] == "alias"
    assert rows["large-language-model"]["canonical"] == "llms"
    assert rows["data-visualisation"]["status"] == "alias"
    assert rows["data-visualisation"]["canonical"] == "data-visualization"
    assert rows["agent-memory"]["status"] == "ready"
    assert rows["thin-topic"]["status"] == "pending"
    assert rows["agent-memory"]["nearest"] == sorted(rows["agent-memory"]["nearest"], key=lambda row: (-row["score"], row["tag"]))


def test_evaluate_marks_changed_source_stale(tmp_path):
    metadata = tmp_path / "metadata-tags.yml"
    ledger = tmp_path / "metadata-tag-proposals.yml"
    write_metadata(metadata)
    digest = write_post(tmp_path, "posts/a.md", "before\n")
    write_ledger(ledger, {"new-topic": {"sources": {"posts/a.md": {"content_hash": digest}}}})
    (tmp_path / "posts/a.md").write_text("after\n", encoding="utf-8")

    rows = tag_proposals.evaluate(metadata, ledger, tmp_path)

    assert rows[0]["current_sources"] == 0
    assert rows[0]["stale_sources"] == ["posts/a.md"]


def test_promote_updates_metadata_posts_and_ledger(tmp_path):
    metadata = tmp_path / "metadata-tags.yml"
    ledger = tmp_path / "metadata-tag-proposals.yml"
    write_metadata(metadata)
    sources = {}
    for index in range(3):
        relative = f"posts/{index}.md"
        text = f"---\ntags: [llms]\n---\n\nPost {index}\n"
        sources[relative] = {"content_hash": write_post(tmp_path, relative, text)}
    write_ledger(ledger, {"agent-memory": {"sources": sources}})

    result = RUNNER.invoke(
        tag_proposals.app,
        ["promote", "agent-memory", "--description", "Posts about agent memory.", "--root", str(tmp_path), "--metadata", str(metadata), "--ledger", str(ledger), "--format", "json"],
    )

    assert result.exit_code == 0, result.output
    metadata_data = YAML_LOADER.load(metadata)
    assert metadata_data["tags"]["agent-memory"]["count"] == 3
    assert "agent-memory" not in YAML_LOADER.load(ledger)["proposals"]
    for index in range(3):
        frontmatter = tag_proposals.parse_frontmatter((tmp_path / f"posts/{index}.md").read_text())[0]
        assert frontmatter["tags"] == ["agent-memory", "llms"]


def test_promote_refuses_stale_evidence_without_writes(tmp_path):
    metadata = tmp_path / "metadata-tags.yml"
    ledger = tmp_path / "metadata-tag-proposals.yml"
    write_metadata(metadata)
    digest = write_post(tmp_path, "posts/a.md", "before\n")
    write_ledger(ledger, {"new-topic": {"sources": {"posts/a.md": {"content_hash": digest}}}})
    (tmp_path / "posts/a.md").write_text("after\n", encoding="utf-8")
    before = metadata.read_bytes(), ledger.read_bytes()

    result = RUNNER.invoke(
        tag_proposals.app,
        ["promote", "new-topic", "--description", "Posts about a new topic.", "--root", str(tmp_path), "--metadata", str(metadata), "--ledger", str(ledger)],
    )

    assert result.exit_code != 0
    assert (metadata.read_bytes(), ledger.read_bytes()) == before
