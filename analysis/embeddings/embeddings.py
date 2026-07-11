#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "google-genai>=1.34.0",
#   "duckdb>=0.10",
#   "typer",
#   "python-dotenv",
#   "rich",
#   "tenacity",
# ]
# ///
"""Generate Gemini embeddings for blog pages and posts, stored in DuckDB + Parquet.

DuckDB tracks which files are done (by content hash), so re-runs skip unchanged files
automatically. Final results are exported to embeddings.parquet.

Usage:
    embeddings.py                   # embed all new/changed files
    embeddings.py --since 2025-01   # only files modified since that date
    embeddings.py --limit 10        # test run: embed at most 10 files
    embeddings.py --force           # re-embed all files, ignoring stored hashes
"""

import hashlib
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import duckdb
import typer
from dotenv import load_dotenv
from google import genai
from google.genai import errors as genai_errors
from rich.console import Console
from rich.progress import BarColumn, MofNCompleteColumn, Progress, SpinnerColumn, TextColumn
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

load_dotenv(override=True)

ROOT = Path(__file__).parent.parent.parent
DB_PATH = ROOT / "analysis" / "embeddings" / "embeddings.duckdb"
PARQUET_PATH = ROOT / "analysis" / "embeddings" / "embeddings.parquet"
MODEL = "gemini-embedding-2"
DIMENSIONS = 768     # 768 is sufficient and 4× cheaper storage than 3072
CHUNK_SIZE = 20      # vectors committed together after independent API requests
MAX_CHARS = 20_000   # truncate each file before embedding
EMBEDDING_INPUT_VERSION = "2026-03-15-strip-comments-prune-dumps-20k"
CACHE_HASH_VERSION = "2026-07-11-independent-contents"

console = Console()
app = typer.Typer()

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_TITLE_RE = re.compile(r"^title:\s*['\"]?(.*?)['\"]?\s*$", re.MULTILINE)
_COMMENTS_RE = re.compile(r"\n##\s+Comments\b.*$", re.DOTALL | re.IGNORECASE)
_IMAGE_LINE_RE = re.compile(r"^\s*!?\[[^\]]*\]\([^)]+\)\s*$")
_URL_ONLY_RE = re.compile(r"^\s*(?:[-*+]\s+)?https?://\S+\s*$")
_LINK_ONLY_RE = re.compile(r"^\s*(?:[-*+]\s+)?\[[^\]]+\]\([^)]+\)\s*$")
_URL_RE = re.compile(r"https?://\S+")
_MARKDOWN_LINK_RE = re.compile(r"!\[([^\]]*)\]\([^)]+\)|\[([^\]]+)\]\([^)]+\)")
_WORD_RE = re.compile(r"\b[\w'-]+\b")


# ---------------------------------------------------------------------------
# DuckDB state
# ---------------------------------------------------------------------------


def get_db() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(str(DB_PATH))
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS embeddings (
            path       TEXT PRIMARY KEY,
            hash       TEXT NOT NULL,
            embedding  FLOAT[{DIMENSIONS}],
            hash_version TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    columns = {row[1] for row in conn.execute("PRAGMA table_info('embeddings')").fetchall()}
    if "hash_version" not in columns:
        conn.execute("ALTER TABLE embeddings ADD COLUMN hash_version TEXT")
    return conn


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def content_hash(path: Path) -> str:
    """Hash exactly the text sent to Gemini, so metadata-only edits are free."""
    payload = read_content(path).encode("utf-8") + b"\0" + EMBEDDING_INPUT_VERSION.encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:16]


def strip_comments(text: str) -> str:
    """Drop trailing blog comment sections from markdown content."""
    return _COMMENTS_RE.sub("", text).strip()


def cleaned_line_text(line: str) -> str:
    """Remove markdown link syntax and URLs so word counts reflect prose."""
    line = _MARKDOWN_LINK_RE.sub(lambda match: (match.group(1) or match.group(2) or " "), line)
    line = _URL_RE.sub(" ", line)
    return line


def is_dump_line(line: str) -> bool:
    """Detect lines that are mostly images or bare links with little semantic text."""
    stripped = line.strip()
    if not stripped:
        return False
    if _IMAGE_LINE_RE.match(stripped) or _URL_ONLY_RE.match(stripped):
        return True
    if not _LINK_ONLY_RE.match(stripped):
        return False
    return len(_WORD_RE.findall(cleaned_line_text(stripped))) <= 3


def strip_link_image_dump(text: str) -> str:
    """Remove long image/link dumps only when the remaining prose is tiny."""
    lines = text.splitlines()
    dump_lines = [line for line in lines if is_dump_line(line)]
    prose_words = sum(len(_WORD_RE.findall(cleaned_line_text(line))) for line in lines if not is_dump_line(line))
    if len(dump_lines) < 8 or prose_words > 120:
        return text.strip()
    kept = [line for line in lines if not is_dump_line(line)]
    return "\n".join(kept).strip()


def read_content(path: Path) -> str:
    """Return cleaned file text with title prepended, truncated to MAX_CHARS."""
    text = path.read_text(encoding="utf-8", errors="replace")
    title = ""
    m = _FRONTMATTER_RE.match(text)
    if m:
        t = _TITLE_RE.search(m.group(1))
        if t:
            title = t.group(1).strip()
        text = text[m.end():].strip()
    text = strip_comments(text)
    text = strip_link_image_dump(text)
    if title:
        text = f"{title}\n\n{text}"
    return text[:MAX_CHARS]


def all_files() -> list[Path]:
    return sorted([*ROOT.glob("pages/**/*.md"), *ROOT.glob("posts/**/*.md")])


@retry(
    retry=retry_if_exception_type(genai_errors.ServerError),
    wait=wait_exponential(multiplier=2, min=5, max=60),
    stop=stop_after_attempt(5),
)
def _embed_call(client, texts: list[str]) -> list[list[float]]:
    vectors: list[list[float]] = []
    for text in texts:
        result = client.models.embed_content(
            model=MODEL,
            contents=text,
            config={"task_type": "RETRIEVAL_DOCUMENT", "output_dimensionality": DIMENSIONS},
        )
        if len(result.embeddings) != 1:
            raise RuntimeError(f"Expected one embedding for one document; received {len(result.embeddings)}")
        vectors.append(list(result.embeddings[0].values))
    return vectors


def embed_with_backoff(client, texts: list[str]) -> list[list[float]]:
    """Call embed_content with exponential back-off on rate-limit errors."""
    delay = 10
    for attempt in range(6):
        try:
            return _embed_call(client, texts)
        except genai_errors.ClientError as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                console.print(f"[yellow]Rate-limited — retrying in {delay}s (attempt {attempt + 1})[/yellow]")
                time.sleep(delay)
                delay = min(delay * 2, 120)
            else:
                raise
    raise RuntimeError("Embedding rate-limit retries exhausted")


def export_parquet(conn: duckdb.DuckDBPyConnection) -> None:
    conn.execute(f"COPY embeddings TO '{PARQUET_PATH}' (FORMAT PARQUET)")
    n = conn.execute("SELECT COUNT(*) FROM embeddings").fetchone()[0]
    console.print(f"[green]Exported {n} embeddings → {PARQUET_PATH}[/green]")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


@app.command()
def main(
    since: Optional[str] = typer.Option(None, help="Only embed files modified after this ISO date"),
    limit: Optional[int] = typer.Option(None, help="Max files to process (for testing)"),
    force: bool = typer.Option(False, "--force", help="Re-embed files even if hash is unchanged"),
) -> None:
    """Generate Gemini embeddings for pages/** and posts/** markdown files."""
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    conn = get_db()

    # Parse optional time cutoff (only when explicitly requested via --since).
    # We intentionally do NOT auto-apply the parquet mtime as a cutoff: the hash
    # check already skips unchanged files, and auto-cutoff breaks incremental test runs.
    cutoff: Optional[datetime] = None
    if since:
        cutoff = datetime.fromisoformat(since).astimezone(timezone.utc)
        console.print(f"Cutoff: {cutoff}")

    # Load already-embedded path→(hash, hash_version) from DuckDB.
    existing: dict[str, tuple[str, str | None]] = {}
    if not force:
        existing = {
            path: (hash_value, hash_version)
            for path, hash_value, hash_version in conn.execute(
                "SELECT path, hash, hash_version FROM embeddings"
            ).fetchall()
        }

    # Collect files that need embedding.
    to_embed: list[tuple[str, Path, str]] = []
    hash_hits = 0
    migrated_hashes = 0
    for f in all_files():
        rel = str(f.relative_to(ROOT))
        h = content_hash(f)
        row = existing.get(rel)
        if row and row[0] == h and row[1] == CACHE_HASH_VERSION:
            hash_hits += 1
            continue  # content unchanged — skip
        if row and row[1] != CACHE_HASH_VERSION:
            migrated_hashes += 1
        if cutoff:
            mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
            if mtime < cutoff:
                continue  # older than explicit cutoff — skip
        to_embed.append((rel, f, h))

    eligible = len(to_embed)  # before --limit is applied
    if limit:
        to_embed = to_embed[:limit]

    all_count = len(all_files())
    cap_note = f" (capped by --limit {limit}; {eligible} eligible)" if limit and limit < eligible else ""
    console.print(f"Files: {all_count} total, {hash_hits} hash-skipped, {len(to_embed)} to embed{cap_note}")
    if migrated_hashes:
        console.print(f"Invalidating {migrated_hashes} vectors created with an older embedding contract.")

    if not to_embed:
        console.print("Nothing new to embed.")
        export_parquet(conn)
        return

    # Embed in chunks; each chunk is committed to DuckDB immediately so the run
    # is resumable — if interrupted, already-processed files are skipped on re-run.
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Embedding...", total=len(to_embed))

        for i in range(0, len(to_embed), CHUNK_SIZE):
            chunk = to_embed[i : i + CHUNK_SIZE]
            texts = [read_content(f) for _, f, _ in chunk]
            vectors = embed_with_backoff(client, texts)

            for (rel, _, h), vec in zip(chunk, vectors):
                conn.execute(
                    "INSERT OR REPLACE INTO embeddings (path, hash, embedding, hash_version) VALUES (?, ?, ?, ?)",
                    [rel, h, vec, CACHE_HASH_VERSION],
                )
            progress.advance(task, len(chunk))

    export_parquet(conn)


if __name__ == "__main__":
    app()
