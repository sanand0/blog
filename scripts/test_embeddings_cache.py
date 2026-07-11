from pathlib import Path


SOURCE = Path("analysis/embeddings/embeddings.py").read_text(encoding="utf-8")


def test_embedding_cache_hashes_embedded_content_not_raw_markdown():
    assert "payload = read_content(path).encode" in SOURCE
    assert "path.read_bytes() + b\"\\0\"" not in SOURCE


def test_embedding_cache_invalidates_old_vector_versions():
    assert "CACHE_HASH_VERSION" in SOURCE
    assert "hash_version" in SOURCE
    assert "row[1] == CACHE_HASH_VERSION" in SOURCE
    assert "row and row[1] is None" not in SOURCE


def test_embedding_requests_keep_documents_independent():
    assert "contents=text" in SOURCE
    assert "len(result.embeddings) != 1" in SOURCE
    assert "contents=texts" not in SOURCE
