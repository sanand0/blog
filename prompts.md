# Prompts

## Fix broken build, 18 Jul 2026

<!--
cd ~/code/blog
dev.sh -- codex --yolo --model gpt-5.6-sol --config model_reasoning_effort=medium
-->

Fix this error reported by https://github.com/sanand0/blog/actions/runs/29627661213/job/88035125459:

```
Start building sites …
hugo v0.156.0-9d914726dee87b0e8e3d7890d660221bde372eec linux/amd64 BuildDate=2026-02-18T16:39:55Z VendorInfo=gohugoio

ERROR error building site: render: [en v1.0.0 guest] failed to render pages: render of "/" failed: "/home/runner/work/blog/blog/themes/PaperMod/layouts/_default/baseof.html:12:50": execute of template failed: template: list.html:12:50: executing "list.html" at <.Language.Direction>: can't evaluate field Direction in type *langs.Language
Total in 2372 ms
render of "/home/runner/work/blog/blog/content/1999/_index.md" failed: "/home/runner/work/blog/blog/themes/PaperMod/layouts/_default/baseof.html:12:50": execute of template failed: template: archive/list.html:12:50: executing "archive/list.html" at <.Language.Direction>: can't evaluate field Direction in type *langs.Language
Error: Process completed with exit code 1.
```

--- <!-- steering -->

On the margin, I prefer upgrading the Hugo version on local and GitHub Actions to the latest stable version, e.g. 0.163, and changing this accordingly.

<!-- codex resume 019f7323-93c9-7063-bebe-ca8713033e89 --yolo -->

## Include search in 404, 18 Jul 2026

<!--
cd ~/code/blog
dev.sh -- codex --yolo --model gpt-5.5 --config model_reasoning_effort=medium
-->

Modify the search component so that

- Tags are not visible (there are too many), just categories and years.
- ONLY if this is very easy to do (max 2 additional lines of code, preferably reducing lines of code):
  - auto-hide empty categories/years/..., i.e. where the count is zero, as the results are updated
  - override `gap: calc(20px * var(--pagefind-ui-scale))` on `.pagefind-ui__filter-group.svelte-1v2r7ls.svelte-1v2r7ls` to 1/4th of the current gap so that the categories, years, ... are closer together and take up less vertical space.
  - The clear button `.pagefind-ui__search-clear.svelte-e9gkc3` has `padding: 0 calc(15px * var(--pagefind-ui-scale)) 0 calc(2px * var(--pagefind-ui-scale))` which means that the clear button is aligned to the left edge of the button - it should be centered.

Also, currently the 404 page is a static HTML.
Instead, let's include the same search component on the page.
Pre-populate it with the relevant part of the incorrect URL (e.g. https://www.s-anand.net/blog/innovation-team_methods/ might search for "innovation team methods").
Keep changes minimal and elegant.

---

Make sure the 404 page will be used by GitHub Pages as the 404 page. (If already done, no action required.)

<!-- codex resume 019f730d-b8e0-7980-9e85-424b94d8bd4b --yolo -->

## Fix broken setup.sh, 17 Jul 2026

<!--
cd ~/code/blog
dev.sh -- codex --yolo --model gpt-5.5 --config model_reasoning_effort=medium
-->

`setup.sh` fails. Fix it - minimally. Maybe the problem is with content, rather than code or config?

<!-- codex resume 019f6f37-ed31-74a1-b0b8-0d8519362827 --yolo -->

## Upgrade search, tags, related posts, agent corpus, 10 Jul 2026

<!--
cd ~/code/blog
dev.sh -p ~/code/scripts -- codex --yolo --model gpt-5.5 --config model_reasoning_effort=medium
-->

<!-- Prompt: https://claude.ai/chat/6a861ed5-5437-4033-8879-625e574d8b8a -->

```markdown
This repo (`~/code/blog`) builds https://www.s-anand.net/ — a Hugo static site with ~2,900 posts in `posts/yyyy/slug.md` and pages in `pages/`, deployed to GitHub Pages. Read `README.md` first. The build is `bash setup.sh`: `scripts/build_content.py` generates `content/` from `posts/`, `pages/`, and `metadata.yml`, then Hugo (via `mise x hugo -- hugo`) builds to `public/blog/`, then post-processing scripts run.

One file OUTSIDE this repo is also in scope: `~/code/scripts/summarize.py`, the tool that generates front matter metadata for new blog posts (see Milestone 3).

**Goal:** make this 27-year archive easy to discover, navigate, cite, and consume — for humans AND for AI agents — using only static files that will survive long-term. No servers, no databases, no new hosting.

**Key existing facts (verified — rely on these):**

- Every post has LLM-generated `description` and `keywords: [...]` front matter. Hugo's `tags` taxonomy is nearly unused (~16 posts; `metadata.yml` defines one tag, `book`). Navigation runs on 33 coarse WordPress-era `categories`.
- `hugo.toml` already outputs RSS for taxonomy terms (`term = ["HTML", "RSS"]`), so every tag page gets a feed automatically once tags exist.
- The PaperMod theme ships a fuse.js search (`themes/PaperMod/layouts/_default/search.html`, hooks in `layouts/partials/head.html`) but no search page exists and no `index.json` is built. Do NOT use fuse.js — a 2,900-post client-side JSON index is too heavy. Use Pagefind instead.
- `analysis/embeddings/embeddings.py` computes Gemini embeddings for all posts into `analysis/embeddings/embeddings.parquet` (regenerate if missing; it is incremental via duckdb). `analysis/embeddings/analyze_embeddings.py` has clustering/similarity code you can reuse.
- Every page's HTML head links its raw Markdown source (`rel=alternate type=text/markdown` → raw.githubusercontent.com). Keep this.
- The footer nav (Categories / Archives / Pages) is filled client-side by `static/js/site.js` from `nav.json`. Without JS, the footer is empty.
- `layouts/_default/single.html` shows only prev/next links — no related posts.
- Permalinks are `posts = "/:slug/"`. NEVER change existing URLs. Some posts date to 1999.

## Guardrails

- Every existing URL must keep returning the same content. Run a before/after diff of the sitemap to prove no URL disappeared.
- Static output only. Everything must work on GitHub Pages with JavaScript disabled, except the search box UI itself.
- Keep `setup.sh` deterministic and offline. No LLM calls inside the build. LLM-assisted steps (tag vocabulary, tag migration) run as separate scripts whose output is committed and human-reviewable.
- Don't edit `content/` or `public/` by hand — they are generated. Source of truth is `posts/`, `pages/`, `metadata.yml`, `layouts/`, `scripts/`.
- Follow the repo's existing script style (uv single-file scripts with inline deps, like `scripts/til.py`).
- Add tests to `tests/` for each new script, matching existing test conventions.
- Work in milestones, in order. Commit after each milestone with all acceptance tests passing.

---

## Milestone 1 — Canonical corpus export (the spine)

Search, tags, related posts, and llms.txt should all consume one canonical record per post/page, so human-facing features and agent-facing exports never drift apart.

Create `scripts/export_corpus.py`, run near the end of `setup.sh`, writing:

- `public/blog/corpus.jsonl` — one JSON object per public post/page:
  `slug, url, title, date, lastmod, categories, tags, description, word_count, source_markdown_url, text` (plain text of the body, markdown stripped). (`tags` will be sparse until Milestone 3; the corpus regenerates every build and picks them up automatically.)
- `public/blog/corpus.schema.json` — field definitions with one-line descriptions.

**Acceptance tests:**

- `corpus.jsonl` line count equals the number of public posts + pages (assert against `content/` count; fail the build on mismatch).
- Every line parses as JSON; every `url` maps to a file that exists in `public/`.
- File is valid UTF-8; each `url` is absolute (`https://www.s-anand.net/...`).

## Milestone 2 — Site search with Pagefind

- Add `npx -y pagefind --site public/blog` to `setup.sh` after the Hugo build (pin a pagefind version).
- Create a `/blog/search/` page hosting the Pagefind UI. Add a search link/box to the header partial.
- Configure Pagefind filters/metadata for category, tag, and year so results can be sliced.

**Acceptance tests:**

- `public/blog/search/index.html` exists and loads the Pagefind bundle.
- The Pagefind index covers >2,800 pages (check its metadata).
- Local smoke test (`npx serve public`): searching a distinctive phrase from a known recent post returns that post first (hard-code one phrase in the test).
- Added JS/CSS payload on non-search pages is zero.

## Milestone 3 — Merge keywords into a single canonical `tags` vocabulary

Decision already made: there will be ONE topic field, `tags`. The freeform `keywords` field is retired. Do not maintain a permanent alias map — migrate the source files once, then keep the vocabulary canonical at write time.

**3a. Build the canonical vocabulary (one-time, LLM/embeddings-assisted, reviewed):**

- Create `scripts/normalize_tags.py`. Collect all keywords across posts and pages. Normalize: lowercase, hyphenate, singular/plural fold. Cluster near-duplicates using `analysis/embeddings/embeddings.parquet` plus string similarity (e.g. `llm`, `llms`, `large language models` → `llms`; `data visualization`, `dataviz`, `visualisation` → `data-visualization`).
- Output a reviewable `metadata-tags.yml`: for each canonical tag, its aliases (used only during this migration), a one-line description, and the projected post count. Target roughly 200–500 tags; drop tags that would match fewer than 3 posts (those posts keep their other tags).
- STOP and ask me to review `metadata-tags.yml` before proceeding.

**3b. Rewrite source files (one-time, after my approval):**

- For every post/page: map its `keywords` through the vocabulary, write the result as `tags: [...]` in the SOURCE front matter, and delete the `keywords` line. Source files are now the single truth; `build_content.py` needs no mapping logic.
- This touches ~2,900 files — make it a single, separately reviewable commit. Preserve all other front matter and formatting exactly (use the same YAML round-trip approach as `~/code/scripts/summarize.py`, which uses ruamel.yaml).

**3c. Keep the vocabulary canonical for future posts:**

- Modify `~/code/scripts/summarize.py`'s `blog` content set: replace the `keywords` FieldDef with a `tags` FieldDef. Its prompt must include the canonical tag list from `metadata-tags.yml` and instruct: strongly prefer existing tags; propose a new tag only when nothing fits, and mark proposals so they are easy to review (e.g. a `proposed-tags` field or a console warning). New approved tags get added to `metadata-tags.yml` with a description.
- The vocabulary file stays in the blog repo; summarize.py reads it by path.

**3d. Templates and navigation:**

- `/blog/tags/` index page listing tags with counts, sorted by count, each with its one-line description.
- Tag term pages grouped by year, showing count, description, and an explicit RSS link (feeds already exist via Hugo term output).
- Show tags on each post page (in `single.html`).
- Render the footer's Categories / Archives / Pages lists — plus top tags — as static HTML at build time, keeping `site.js` only for progressive enhancement. (This fixes the current empty-footer-without-JS problem.)
- Also, in .post-meta line, minimally add a [Permalink](https://www.s-anand.net/blog/...) link that adds the permalink based on the `metadata.yaml` site.link base URL.

**Acceptance tests:**

- No `keywords:` remains in any source post/page; ≥90% of posts have ≥1 tag; median tags per post between 3 and 8.
- Permalink links work and match the canonical URL in `corpus.jsonl`.
- No two canonical tags are trivial variants (test: no pair differs only by plural/hyphen/case).
- `/blog/tag/llms/` (or the canonical LLM tag) exists with >50 posts and a working `index.xml` feed.
- `curl` (no JS) of any post page shows footer category/archive/tag links in raw HTML.
- Existing category pages and feeds are unchanged.
- `summarize.py --dry-run blog` on a sample new post emits only canonical tags or clearly flagged proposals.

## Milestone 4 — Related posts on every post page

- Using `analysis/embeddings/embeddings.parquet`, precompute the top 5 nearest neighbors per post at build time (regenerate embeddings first if the parquet is missing or stale — `embeddings.py` is incremental).
- Write neighbors into a JSON sidecar or generated front matter, and render a "Related" section in `layouts/_default/single.html` (title + date + description), after the post body, before prev/next. Plain static HTML — no JS.
- Blend rule: prefer embedding similarity; break ties with shared tags.

**Acceptance tests:**

- Every post page (sample 50 across decades) has a Related block with 3–5 links, none self-referencing, all resolving to existing pages.
- Spot-check quality: for 5 well-known posts I name during review, related links are topically sensible.
- Build fails loudly with a clear message if the parquet is missing, rather than silently skipping.

## Milestone 5 — `llms.txt` and agent guide

Create at build time:

- `/llms.txt` at the site root (`public/llms.txt`), following the llmstxt.org convention: one-paragraph site description, then curated links with one-line descriptions: about page, `corpus.jsonl`, `corpus.schema.json`, `tags.json`, main RSS feed, top ~15 tag pages, and a note that every HTML page links its raw Markdown source via `rel=alternate`.
- `/blog/tags.json` — canonical tags with counts and descriptions (generated from `metadata-tags.yml` + actual counts).
- Add a short "For AI agents" section to the colophon/about page describing these resources and how to cite posts (canonical URL + CC0 license).

**Acceptance tests:**

- `public/llms.txt` exists, is valid Markdown, and every URL in it resolves within `public/`.
- `tags.json` counts match the tag pages' actual post counts.
- End-to-end check: using ONLY `llms.txt` → `tags.json` → `corpus.jsonl`, a script can list all posts about LLM evaluation with titles, dates, and URLs.

## Final verification (run after all milestones)

1. Full `bash setup.sh` completes cleanly from scratch.
2. Sitemap diff vs. the pre-change build: no URLs removed; only additions.
3. All tests in `tests/` pass.
4. `public/` renders correctly with JS disabled (spot-check home, a post, a tag page, the tags index, search page shell, footer).
5. Summarize in the PR description: files added, URLs added, the tag vocabulary size, and the exact commands a future agent needs to consume the corpus.
```

--- <!-- steering -->

Prefer writing tags in one line, like `tags: [x, y, ...]`

--- <!-- steering -->

Be token efficient when passing the canonical tag list to the LLM in summarize.py

--- <!-- steering -->

Use the GEMINI_API_KEY in ~/code/blog/.env

--- <!-- steering -->

Compact when appropriate.

---

Are there any scripts that are no longer required, e.g. one-time scripts used for migration? Remove them.
Update README.md adding a section documenting what I need to run to keep the site up-to-date, e.g. embeddings, summarize, generating tags, etc. including a self-explanatory bash code block I can copy-paste.

--- <!-- steering -->

Simplify the script to keep the site up to date. E.g. Assume GEMINI_API_KEY is loaded. If the summarize.py is idempotent, maybe there's no need to check if markdown has changed? What else can we simplify?

---

Make the "Keeping the site up to date" script a justfile command and refer to that in README.md.

---

I ran `just update` and it is updating posts, e.g.

```
UPDATED watching-videos-with-a-plastic-cover.md +['tags'] | 1268in/91out tok $0.0027
UPDATED things-i-learned-29-mar-2026.md +['tags'] | 3458in/106out tok $0.0061
UPDATED things-i-learned-22-mar-2026.md +['tags'] | 2027in/72out tok $0.0037
UPDATED things-i-learned-11-jan-2026.md +['tags'] | 2575in/97out tok $0.0047
UPDATED my-food-preferences.md +['tags'] | 1645in/64out tok $0.0030
^C
```

I interrupted it. But aren't the posts already updated? Also, this costs a lot... what can we do to reduce the cost per tag? If there's something that will reduce cost without losing quality, do it. Else check with me.

---

Make just update use gemini-2.5-flash

---

Every time I run `just update`, even with no changes, it re-embeds most of the posts

First time: Files: 2990 total, 278 hash-skipped, 2712 to embed
Next time: Files: 2990 total, 414 hash-skipped, 2576 to embed

How can we avoid it?

Also, Improve the UI for:

- the search link location. Currently, .nav is on one line, with the .logo inside it, which includes a .logo-switches containing the dark mode; the #menu is on the next line. This doesn't look nice. Put it on one line, elegantly.
- .footer has 3 .footer-columns in one row, and then the fourth dangling - in desktop view. I'd like to see all 4 columns in one row to the extent possible. I don't mind .footer being wider. Do ensure resonsiveness.
- The design of `<sup>` doesn't look nice. Is there a better UI to indicate the number of posts in /blog/tag/*/? E.g. as a small circle with the number inside it, or something else? It doesn't have to be a `<sup>` tag - use whatever is semantic.
- The `<time>` in `.related-posts` is YYYY-MM-DD. I prefer something like `Wed, 3 Jul 2002`.

---

Is there a way to auto-decide on the proposed tags, e.g. if they're a genuine, repeated, category, without losing them? What would be nice is that if the proposed tags were added to the list of tags or any other version-controlled file as "proposed" against specific posts, and evaluated against the existing tags to see if (a) there is a genuine reason to introduce a new tag, i.e. it's distinct enough, and (b) if it's repeated often enough to justify the addition, and then added if required.

Finally, the related posts seem to have very little relatedness! When I read them, I don't find the posts to have much in common. For example, 15-years-of-dilbert-searchable/ mentions voip-rates, hiccups, infyblogs-dashboard, wisdom-and-intelligence, and short-notes. None of these seem related. Other comics-related posts (e.g. Calvin & Hobbes) are notably missing. Why is that? Explore a few random posts' related posts and see how related they are, see if you can improve the algorithm, and share examples of before-vs-after for a few posts and check with me. Iterate a few times if required. Use sub-agents if that'll help.

--- <!-- steering -->

If it helps, I'm OK for the related posts to be generated on my local machine and committed, making it one-time rather than at build time.
If we're committing, I'd like the related posts to be more compact, e.g. just the filenames matching a filename (or a slug or ID), rather than all other details - which are derivable.

--- <!-- steering -->

Also, if we're committing, maybe partitioning the file, e.g. by year or something, might help keep the git objects from bloating too much.
Of course, I'm not convinced this is a good idea in the first place.

----

Commit everything, including my changes (prompts.md, blog posts), in logical groups.

<!-- codex resume 019f4cdd-c6ad-7bf2-977e-f5cdb9a31f1c --yolo -->

## TIL, 07 Jun 2026

<!--
cd ~/code/blog; dev.sh -p ~/code/til/
codex --yolo --model gpt-5.5 --config model_reasoning_effort=medium
-->

Migrate TIL into my blog. See how ~/code/til/ converts the til.md and llms.md into weekly blog posts as a GitHub deploy workflow. Write a concise agent-friendly CLI scripts/til.py that does something similar. It should create a posts/yyyy/things-i-learned-dd-mmm-yyyy.md file. It'll always be on a Sunday, covering everything up to the previous day (Saturday). Title is like "Things I Learned - 07 Jun 2026". Categories: "til" (add to the metadata.yml). "date" should be mid-day UTC of the Sunday. The post should begin with a line "This week, I learned:". By default, it should run for the latest week (i.e. generate it for the most recent Sunday). I should be able to run this for any week or time range. It should be fast and not overwrite existing files unless forced.

Run and test for a few weeks and await my feedback.

---

Updates:

- Include the date on which I learned each item. For example: "21 May 2026. BitWarden seems to be sneakily ..."
- If the target file for any week already exists and we're not forcing the generation, generate the content anyway and show the diff between the two entire files. Then I can decide whether to force or not.
- Instead of 12 pm UTC, set the time to 00:00 UTC on the blog posts.
- Move tests/test_til.py to scripts/test_til.py.
- Re-run for the same TILs you created.
- Tell me how to run til.py for all time periods covered by til.md / llms.md - don't run it yet.
- Update README.md explaining til.py. I'll be running it weekly on Sundays.

---

I take back what I said. Remove the date from each item. For example, just say "BitWarden seems to be sneakily ..." without the date.

Move analysis/linkedin_blog_map.py to scripts/linkedin_blog_map.py. Make sure it still updates analysis/linkedin-blog-map.tsv -- only the script path is changed. Run and test.

Update README.md explaining linkedin_blog_map.py. I'll be running it whenever I post on LinkedIn.

<!-- codex resume 019ea045-6afd-7080-a8da-9750a33c89ab --yolo -->

## LinkedIn posts, 06 Jun 2026

<!--
cd ~/code/blog; dev.sh -p ~/Documents/data
codex --yolo --model gpt-5.5 --config model_reasoning_effort=medium
-->

~/Documents/data/linkedin-posts.jsonl contains all my LinkedIn posts (and comments - but you can skip those.)

Most of my posts, especially in the last few years, are simple rewrites of my blog posts. For example, https://www.linkedin.com/feed/update/urn:li:activity:7467813154660667392/ is a rewrite of posts/2026/my-most-memorable-anniversary.md.

I rewrite by (a) shortening and simplifying (occasionally adding) and (b) converting Markdown to Unicode, e.g. **bold**, _italics_, `code` to 𝗯𝗼𝗹𝗱 or 𝐛𝐨𝐥𝐝, 𝘪𝘵𝘢𝘭𝘪𝘤𝘴, 𝚌𝚘𝚍𝚎.

I usually post on LinkedIn a few hours or days after I post on my blog, but occasionally post a few minutes earlier.

The LinkedIn scraper that generated the JSONL may not be very reliable, but the url: and content: fields seem to be reasonably correct.

I want to create a TSV mapping of all LinkedIn post URLs (e.g. https://www.linkedin.com/feed/update/urn:li:activity:7467813154660667392/) to the corresponding blog post filename (e.g. posts/2026/my-most-memorable-anniversary.md) if there is one, and leave it blank if none exist. The TSV should also contain the ASCII-ified LinkedIn content (200 chars, truncated) and the blog post content (200 chars, truncated) for reference. (Multiple matches are unlikely but if there are, let me know.)

Execute this in the most token-efficient direct and simple way without errors.

If you need any inputs, ask me.

---

I have manually updated analysis/linkedin-blog-map.tsv. Make sure that if we re-run analysis/linkedin_blog_map.py it will not change any existing mappings and append add new ones (if any). To facilitate this, sort the existing TSV by date (oldest LinkedIn post first) and keep it sorted that way.

Next, add a linkedin: YAML metadata to the blog posts that have a LinkedIn post.

Lastly, for such posts, render a link to the LinkedIn post at the bottom of the blog post. The text can simply include the LinkedIn icon and the words "LinkedIn post".

Run `setup.sh` and test.

---

Write the post-mortem and tool failures - the path should be writeable.

<!-- codex resume 019e9afa-f977-7282-8bf5-c1825e2853ff --yolo -->

## AI generated content, 23 May 2026 (Claude Sonnet 4.6 - medium)

Make sure contents inside a `<section ai-disclosure="ai-generated" data-ai-model="..." data-ai-provider="...">` are subtly styled like in `assets/ai-generated-sample.avif` and in a way consistent with the theme and future proof (e.g. use opacity along with darkness/lightness rather than changing hues, handle dark mode, etc.)

Add a small "AI" badge at the top right (hover should reveal the model and provider information), mention "AI-GENERATED - Model - Provider" at the bottom in small font, make the background SUBTLY different, add a SUBTLE border with the left border being thicker.

Search the standard to see if other data-_ attributes are allowed. In any case, future-proof it to handle any data-ai-_ attributes for the future.

Run and test visually. Revise as required.

<!-- I manually adjusted the paddings and removed the border -->
<!-- claude --resume de719afa-09f2-4110-a581-f9eca2729cbc -->

## Markdown link, 31 Mar 2026 (Copilot - gpt-5.4-mini xhigh)

Add a <link rel="alternate" type="text/markdown" href="..."> header to all posts/pages that links to the GitHub raw markdown file for that page.

Run bash setup.sh and verify that the header is present in the generated HTML files.

## Header link and JSON navigation, 21 Mar 2026 (Claude Code - Sonnet 4.6)

<!-- https://claude.ai/code/session_012J8cWHH5wUncaFXr5HBmHN -->

Clicking on the "S Anand" on the header on all pages currently takes me to https://www.s-anand.net/blog/ which is the blog root but it should instead take me to https://www.s-anand.net/

Commit this.

Instead of adding the categories, archives and pages to each page, use JavaScript to pre-create a JSON that is loaded and rendered on every page.

Modify the archives so that it shows the monthly links for the current (latest) year and the yearly links for past years. For example, Mar 2026, Feb 2026, Jan 2026, 2025, 2024, ...

Commit this.

---

<!-- claude --teleport session_012J8cWHH5wUncaFXr5HBmHN -->

I ran `bash setup.sh` and under public/ the .nav > .logo > a element still links to /blog/ across pages.

---

Improve the visual appearance of the footer columns. Specifically:

- Modify the links so that they take up the full width of the column
- Add a single-pixel horizontal line below links that have numbers (categories, archives) whose width is proportional to the number of items in that category/archive. Use the third largest value as 100% width to eliminate outliers.
- Think of and apply other improvements to the visual design of the footer columns to make them more visually appealing and easier to navigate

---

The footer looks fine but is not visible on / which is actually copied from /blog/s-anand/ into / (see setup.sh).
Make sure this will still work.

Review the code changes made so far in this session. How could we simplify, shorten, and make it more elegant and maintainable? Refactor as needed.

<!-- claude --resume b8c8b5ea-7ade-4677-a9c1-2598ad9a4e3d -->
