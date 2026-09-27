#!/bin/bash

# Exit on error
set -e

# Build content
uv run scripts/build_content.py
uv run scripts/build_related_posts.py
uv run scripts/where.py
grep -E '^(summary|description|tags):' posts/**/*.md pages/**/*.md | sort > description.md

# Build
rm -rf public
mise x hugo@0.165.0 -- hugo
uv run scripts/postprocess_pagination_metadata.py
npx -y pagefind@1.5.2 --site public/blog

# Add nofollow to comment links
uv run scripts/postprocess_comments_nofollow.py

# Normalize feed URLs
uv run scripts/postprocess_feed_paths.py public/blog

# Export canonical corpus
uv run scripts/export_corpus.py
uv run scripts/build_agent_exports.py

# Copy root pages and site files
uv run scripts/promote_root_pages.py
cp public/blog/404.html public/             # GitHub Pages custom 404 page
cp robots.txt public/                       # Root crawler and Content Signals policy
