# Anand's Blog

Content and build pipeline for https://s-anand.net/

## Source files

Content:

- `pages/`: Standalone pages as Markdown (`pages/slug.md`).
  - [Home page](pages/s-anand.md)
  - Pages can be nested: `pages/lists/slug.md`
- `posts/`: Blog posts as Markdown (`posts/yyyy/slug.md`).
- `assets/`: Converted media files used by posts (WebP/OPUS). Served at `/blog/assets/`.

Configuration & Code:

- `metadata.yml` for taxonomies (categories, tags), and author info
- `hugo.toml`: Hugo site configuration
- `setup.sh`: Build script to generate content and build site
- `.github/workflows/deploy.yml`: Deployment workflow for GitHub Pages.
- `layouts/`: Hugo layout overrides for theme customizations.
  - `layouts/partials/head.html` generates `<title>` by capitalizing (e.g. [blog → Blog](https://www.s-anand.net/blog/)) and deduplicating site title (e.g. ["S Anand | S Anand" -> "S Anand"](https://www.s-anand.net/)).
- `static/`: Static files (CSS overrides, favicon assets).
- `themes/PaperMod/`: Hugo theme sources (vendored).
- `scripts/`: Conversion and utility scripts.
- `justfile`: Justfile for local pre-processing (e.g. analysis).
- `analysis/`: Data analysis scripts and results (e.g. embedding analysis).

Auto-generated (DO NOT edit!):

- `content/`: Contains Hugo content (posts/pages + taxonomy and archive index pages).
- `public/`: Build output (deployed to GitHub Pages).

**After editing source files**, rebuild with:

```bash
bash setup.sh
```

This runs:

1. `scripts/build_content.py` - generates `content/` from `posts/`, `pages/`, and `metadata.yml`
2. `hugo` - builds static site to `public/blog/`
3. Post-processing scripts for comments and feed normalization
4. Copies special pages to `public/` root

[GitHub](.github/workflows/deploy.yml) automatically runs `setup.sh` on push to `main` and deploys `public/` to GitHub Pages.

WIP commits are pushed to the `live` branch. The `prod` branch holds permanent changes - in case of rollbacks to main.

## Embeddings

`content/embeddings.parquet` contains [Gemini Embedding 2](https://ai.google.dev/gemini-api/docs/embeddings) vectors for every page and post.

```bash
scripts/embeddings.py                    # embed all new/changed files
scripts/embeddings.py --since 2025-01   # only files modified after a date
scripts/embeddings.py --limit 10        # test run: at most 10 files
scripts/embeddings.py --force           # re-embed all, ignoring hashes
```

- Model: `gemini-embedding-2-preview`, 768 dimensions, `RETRIEVAL_DOCUMENT` task
- Each file's title (from frontmatter) is prepended to the body before embedding
- State is persisted in `content/embeddings.duckdb` so interrupted runs resume automatically — only files whose content hash changed are re-embedded

## Frontmatter

Required:

- `title: ...` is used for the post/page title.

Optional but recommended:

- `date: ...` (ISO 8601 format) is used for sorting posts and displaying the date on the post page.
- `description: ...` has [meta description](https://gohugo.io/methods/page/description/). Currently manually AI-generated.
- `keywords: [..., ...]` has [page keywords](https://gohugo.io/methods/page/keywords/). Currently manually AI-generated.

Optional:

- `classes: wrap-code` adds the `wrap-code` class to the post's main `<article>` element, which applies CSS to wrap long code blocks.
- `build: { list: never, render: always }` ensures that posts/pages are not listed _anywhere_ blog index but are still rendered.
- `robotsNoIndex: true` adds a `<meta name="robots" content="noindex">` tag to the page header to prevent indexing by search engines.
- `aliases: ["old-path"]` adds redirects from old-path to the current page using [Hugo Aliases](https://gohugo.io/content-management/urls/#aliases).
