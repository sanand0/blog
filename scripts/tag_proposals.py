#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9", "ruamel.yaml"]
# ///
"""Evaluate and explicitly promote proposed blog tags."""

import difflib
from hashlib import sha256
from io import StringIO
import json
import os
from pathlib import Path
import re
import tempfile
from typing import Annotated, Any

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq
import typer


app = typer.Typer(add_completion=False)
TOKEN_RE = re.compile(r"[a-z0-9]+")


def make_yaml() -> YAML:
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 100000
    return yaml


def slug(value: str) -> str:
    text = str(value).strip().lower().replace("&", " and ").replace("+", " plus ").replace("'", "")
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text)).strip("-")


def trivial_form(value: str) -> str:
    words = TOKEN_RE.findall(value.lower())
    return "".join(word[:-1] if word.endswith("s") and len(word) > 3 else word for word in words)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---") or (end := text.find("\n---", 3)) < 0:
        return CommentedMap(), text
    return make_yaml().load(text[3:end]) or CommentedMap(), text[end + 4 :].lstrip("\n")


def dump_document(metadata: dict, body: str) -> bytes:
    stream = StringIO()
    make_yaml().dump(metadata, stream)
    return f"---\n{stream.getvalue()}---\n\n{body}".encode()


def load_yaml(path: Path) -> dict:
    return make_yaml().load(path.read_text(encoding="utf-8")) or {}


def lexical_candidates(proposal: str, canonical: dict, limit: int = 5) -> list[dict]:
    proposal_tokens = set(TOKEN_RE.findall(proposal.lower()))
    rows = []
    for tag, details in canonical.items():
        variants = [tag, *(str(alias) for alias in details.get("aliases") or [])]
        best = max(variants, key=lambda value: (difflib.SequenceMatcher(None, slug(proposal), slug(value)).ratio(), value))
        best_tokens = set(TOKEN_RE.findall(best.lower()))
        similarity = round(difflib.SequenceMatcher(None, slug(proposal), slug(best)).ratio(), 4)
        shared = sorted(proposal_tokens & best_tokens)
        score = round(similarity + len(shared) / max(len(proposal_tokens | best_tokens), 1), 4)
        rows.append({"tag": str(tag), "score": score, "evidence": {"variant": best, "similarity": similarity, "shared_tokens": shared}})
    return sorted(rows, key=lambda row: (-row["score"], row["tag"]))[:limit]


def classify(proposal: str, canonical: dict, current_sources: int) -> tuple[str, str | None]:
    proposal_slug = slug(proposal)
    for tag in canonical:
        if proposal_slug == slug(tag):
            return "rejected", str(tag)
    for tag, details in canonical.items():
        variants = [tag, *(str(alias) for alias in details.get("aliases") or [])]
        if any(trivial_form(proposal) == trivial_form(variant) for variant in variants):
            return "alias", str(tag)
        if any(
            difflib.SequenceMatcher(None, proposal_slug, slug(variant)).ratio() >= 0.88
            for variant in variants
        ):
            return "alias", str(tag)
    return ("ready" if current_sources >= 3 else "pending"), None


def evaluate(metadata_path: Path, ledger_path: Path, root: Path) -> list[dict]:
    canonical = load_yaml(metadata_path).get("tags") or {}
    proposals = load_yaml(ledger_path).get("proposals") or {}
    rows = []
    for proposal, details in sorted(proposals.items(), key=lambda item: slug(str(item[0]))):
        current, stale = [], []
        for source, evidence in sorted((details.get("sources") or {}).items()):
            path = Path(source) if Path(source).is_absolute() else root / source
            digest = sha256(path.read_bytes()).hexdigest() if path.is_file() else None
            (current if digest == evidence.get("content_hash") else stale).append(source)
        status, match = classify(str(proposal), canonical, len(current))
        rows.append(
            {
                "proposal": str(proposal),
                "status": status,
                "canonical": match,
                "current_sources": len(current),
                "sources": current,
                "stale_sources": stale,
                "nearest": lexical_candidates(str(proposal), canonical),
            }
        )
    return rows


def render(data: Any, fmt: str) -> None:
    if fmt == "json":
        typer.echo(json.dumps(data, sort_keys=True))
        return
    for row in data if isinstance(data, list) else [data]:
        nearest = ", ".join(f"{item['tag']} ({item['score']:.4f})" for item in row.get("nearest", []))
        typer.echo(f"{row['proposal']}: {row['status']} [{row['current_sources']} current] nearest: {nearest}")


def yaml_bytes(data: dict) -> bytes:
    stream = StringIO()
    make_yaml().dump(data, stream)
    return stream.getvalue().encode()


def atomic_replace_many(updates: dict[Path, bytes]) -> None:
    """Stage every output, then replace all paths with rollback on a replace failure."""
    originals = {path: path.read_bytes() if path.exists() else None for path in updates}
    staged: dict[Path, Path] = {}
    replaced: list[Path] = []
    try:
        for path, content in updates.items():
            fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
            with os.fdopen(fd, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            staged[path] = Path(name)
        for path in sorted(updates, key=str):
            os.replace(staged[path], path)
            replaced.append(path)
        for directory in {path.parent for path in updates}:
            fd = os.open(directory, os.O_RDONLY)
            try:
                os.fsync(fd)
            finally:
                os.close(fd)
    except BaseException:
        for path in reversed(replaced):
            original = originals[path]
            if original is None:
                path.unlink(missing_ok=True)
            else:
                fd, name = tempfile.mkstemp(prefix=f".{path.name}.rollback.", dir=path.parent)
                with os.fdopen(fd, "wb") as handle:
                    handle.write(original)
                os.replace(name, path)
        raise
    finally:
        for path in staged.values():
            path.unlink(missing_ok=True)


@app.command("evaluate")
def evaluate_command(
    root: Annotated[Path, typer.Option("--root")] = Path("."),
    metadata: Annotated[Path, typer.Option("--metadata")] = Path("metadata-tags.yml"),
    ledger: Annotated[Path, typer.Option("--ledger")] = Path("metadata-tag-proposals.yml"),
    fmt: Annotated[str, typer.Option("--format")] = "text",
) -> None:
    """Classify proposals from current source evidence."""
    if fmt not in {"text", "json"}:
        raise typer.BadParameter("must be text or json", param_hint="--format")
    render(evaluate(metadata, ledger, root), fmt)


@app.command()
def promote(
    proposal: str,
    description: Annotated[str, typer.Option("--description")],
    root: Annotated[Path, typer.Option("--root")] = Path("."),
    metadata: Annotated[Path, typer.Option("--metadata")] = Path("metadata-tags.yml"),
    ledger: Annotated[Path, typer.Option("--ledger")] = Path("metadata-tag-proposals.yml"),
    fmt: Annotated[str, typer.Option("--format")] = "text",
) -> None:
    """Explicitly add one ready proposal to metadata and all evidenced posts."""
    rows = {slug(row["proposal"]): row for row in evaluate(metadata, ledger, root)}
    row = rows.get(slug(proposal))
    if row is None:
        raise typer.BadParameter(f"proposal not found: {proposal}")
    if row["status"] != "ready" or row["stale_sources"]:
        raise typer.BadParameter("proposal must have at least 3 current sources and no stale evidence")

    canonical_tag = slug(row["proposal"])
    metadata_data = load_yaml(metadata)
    tags = metadata_data.get("tags") or CommentedMap()
    tags[canonical_tag] = {"description": description.strip(), "aliases": [], "count": len(row["sources"])}
    metadata_data["tags"] = CommentedMap((tag, tags[tag]) for tag in sorted(tags))
    if "canonical_tag_count" in metadata_data:
        metadata_data["canonical_tag_count"] = len(tags)

    updates = {metadata: yaml_bytes(metadata_data)}
    for source in row["sources"]:
        path = Path(source) if Path(source).is_absolute() else root / source
        frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        existing_tags = [str(tag) for tag in frontmatter.get("tags") or []]
        values = sorted(set([*existing_tags, canonical_tag]))
        sequence = CommentedSeq(values)
        sequence.fa.set_flow_style()
        frontmatter["tags"] = sequence
        updates[path] = dump_document(frontmatter, body)

    ledger_data = load_yaml(ledger)
    ledger_data.setdefault("proposals", {}).pop(row["proposal"], None)
    ledger_data["proposals"] = CommentedMap(
        (name, ledger_data["proposals"][name]) for name in sorted(ledger_data["proposals"])
    )
    updates[ledger] = yaml_bytes(ledger_data)
    atomic_replace_many(updates)
    render({"proposal": canonical_tag, "status": "promoted", "current_sources": len(row["sources"]), "nearest": []}, fmt)


if __name__ == "__main__":
    app()
