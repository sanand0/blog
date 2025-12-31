# Anand's Blog

Content and build pipeline for https://s-anand.net/

## Repo structure

- `pages/`: Standalone pages as Markdown (`pages/slug.md`).
  - [Home page](pages/s-anand.md)
- `posts/`: Blog posts as Markdown (`posts/yyyy/slug.md`).
- `assets/`: Converted media files used by posts (WebP/OPUS). Served at `/blog/assets/`.
- `layouts/`: Hugo layout overrides for theme customizations.
- `static/`: Static files (CSS overrides, favicon assets).
- `themes/PaperMod/`: Hugo theme sources (vendored).
- `scripts/`: Conversion and utility scripts.
- `.github/workflows/deploy.yml`: Deployment workflow for GitHub Pages.

Generated files:

- `content/`: Generated Hugo content (posts/pages + taxonomy and archive index pages).
- `public/`: Build output (deployed to GitHub Pages).

Run this script to build the site:

```bash
bash setup.sh
```
