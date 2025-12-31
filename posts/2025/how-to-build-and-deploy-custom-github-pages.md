---
title: How to build and deploy custom GitHub Pages
date: "2025-04-01T05:59:18Z"
lastmod: "2025-04-01T05:59:20Z"
categories:
  - coding
wp_id: 4010
---

Here's the [GitHub Actions](https://github.com/features/actions) file (`.github/workflows/deploy.yaml`) I use to publish to [GitHub pages](https://pages.github.com/).

```yaml
name: Deploy to GitHub Pages

on:
  # Run when pushed. Use { branches: [main, master] } to run only on specific branches
  push:
  # Allow manual triggering of the workflow
  workflow_dispatch:
  # OPTIONAL: Run at a specific cron schedule, e.g. first day of every month at 12:00 UTC (noon)
  schedule:
    - cron: "0 12 1 * *"

permissions:
  # To deploy to GitHub Pages
  pages: write
  # To verify that deployment originated from the right source
  id-token: write

jobs:
  # Run as a single build + deploy job to reduce setup time
  deploy:
    # Specify the deployment environment. Displays the URL in the GitHub Actions UI
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    # Run on the latest Ubuntu LTS
    runs-on: ubuntu-latest
   \
    steps:
      # Checkout the repository
      - uses: actions/checkout@v4

      # Run whatever commands you want
      - run: echo '<h1>Hello World</h1>' > index.html

      # Upload a specific page to GitHub Pages. Defaults to _site
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .

      # Deploy the built site to GitHub Pages. The `id:` is required to show the URL in the GitHub Actions UI
      - id: deployment
        uses: actions/deploy-pages@v4
```

This is based on [Simon Willison's workflow](https://til.simonwillison.net/github-actions/github-pages) and some of my earlier actions.

This **combines build and deploy** jobs. For simple sites, that's simpler and more efficient. For complex builds with parallel execution or need for better error recovery, multiple jobs will help.

I build sites with [uv](https://github.com/astral-sh/uv), [node](https://nodejs.org/), or [deno](https://deno.com/). Here are examples of each

A sample [uv-based deployment](https://github.com/sanand0/webfeatures/blob/main/.github/workflows/deploy.yml).

```yaml
# Install uv
- uses: astral-sh/setup-uv@v5
# Run a Python script
- run: uv run scraper.py
```

A sample [node package.json deployment](https://github.com/gramener/gramex-network/blob/main/.github/workflows/deploy.yml) and an [npx deployment](https://github.com/sanand0/llmhallucinations/blob/main/.github/workflows/deploy.yml).

```yaml
# Install node
- uses: actions/setup-node@v4
  with:
    node-version: 20
    registry-url: https://npm.pkg.github.com/
# Install and build via package.json
- run: npm install
- run: npm run build
# Or, directly use npx. For example, generate HTML with Marp
- run: npx -y @marp-team/marp-cli@latest README.md -o index.html
# Update content directly, e.g. add an SVG favicon as a data URL
- run: sed -i 's/<\/head>/<link rel="icon" type="image\/svg+xml" href="data:image\/svg+xml;base64,..."\/><\/head>/g' index.html
```

A sample [deno deployment](https://github.com/sanand0/til/blob/main/.github/workflows/deploy.yml).

```yaml
# Install deno
- uses: denoland/setup-deno@v1
  with:
    deno-version: v1.x
# Run a Deno script. Use environment variables if needed
- env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  run: deno run --allow-read --allow-write --allow-env --allow-net script.js
```
