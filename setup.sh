#!/bin/bash

# Exit on error
set -e

# Build content
uv run scripts/build_content.py
uv run scripts/where.py
grep -E '^(summary|description|keywords):' posts/**/*.md pages/**/*.md | sort > description.md

# Build
mise x hugo -- hugo
npx -y pagefind@1.5.2 --site public/blog

# Add nofollow to comment links
uv run scripts/postprocess_comments_nofollow.py

# Normalize feed URLs
uv run scripts/postprocess_feed_paths.py public/blog

# Export canonical corpus
uv run scripts/export_corpus.py

# Copy special pages
cp public/blog/s-anand/index.html public/   # From blog/pages/s-anand.md
cp -R public/blog/calvin/ public/           # From blog/pages/calvin.md

# Ideas for other pages that we could copy to public/ directly:
#   /p/ is a Medium/WordPress convention
#   /i/ for images, assets
#   /s/ for static / special pages
#   app, pub, doc, try, use, set, hub, lab, box, kit, ...
#   go, at for links
