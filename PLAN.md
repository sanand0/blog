# Blog archive modernization plan

Goal: make the static Hugo archive easier to discover, navigate, cite, and consume without changing existing post URLs or requiring a server.

Done means:
- Each milestone is implemented in order, committed separately, and has passing acceptance tests.
- `bash setup.sh` remains deterministic and offline unless the milestone explicitly defines a separate reviewable LLM-assisted step.
- A before/after sitemap comparison proves no existing URL disappeared.
- Generated `content/` and `public/` are never hand-edited.

## Milestone checklist

1. Canonical corpus export
   - Add `scripts/export_corpus.py` to derive one record per public post/page from generated Hugo output and source front matter.
   - Write `public/blog/corpus.jsonl` and `public/blog/corpus.schema.json`.
   - Add tests for line counts, UTF-8 JSONL, absolute URLs, and URL-to-file resolution.
   - Run `bash setup.sh`, run tests, and commit.

2. Pagefind search
   - Add a pinned Pagefind build step after Hugo.
   - Add `/blog/search/` and a header search entry without adding JS/CSS to non-search pages.
   - Add tests/smoke checks for index coverage, search page assets, and result quality.
   - Run build/tests and commit.

3. Canonical tags
   - Generate `metadata-tags.yml` for review, then stop before source rewrites.
   - After approval, migrate source front matter from `keywords` to `tags`, update `summarize.py`, and add static tag navigation/templates.
   - Add acceptance tests and commit the vocabulary generation separately from the bulk source rewrite.

4. Related posts
   - Precompute nearest neighbors from embeddings and render static related links on posts.
   - Fail clearly when embeddings are missing.
   - Add sample/link integrity tests and commit.

5. `llms.txt` and agent guide
   - Generate `/llms.txt` and `/blog/tags.json` from canonical data.
   - Add agent-facing about/colophon copy and acceptance tests.
   - Run full final verification and commit.

## Progress

- Started: inspected README, `setup.sh`, `hugo.toml`, and current script style.
- Milestone 1: added focused tests for corpus export and implemented `scripts/export_corpus.py`; focused exporter tests pass.
- Milestone 1 complete: committed `ee52d98` after full `bash setup.sh`, corpus integrity checks, script tests, and fresh sitemap diff with zero removals.
- Milestone 2: added pinned Pagefind build, `/search/` page/layout, search-only Pagefind assets, Pagefind body/filter/meta attributes, header Search link, and generated-output tests. Full build reports 2,982 indexed pages and 3 filters; served browser smoke returns `Discussion with Arvind Satyanarayan` first for the GoFish phrase; sitemap diff vs Milestone 1 has zero removals and one added URL.
