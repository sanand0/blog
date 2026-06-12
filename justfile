build: description
  bash setup.sh
description:
  grep -E '^(summary|description|keywords):' posts/**/*.md pages/**/*.md | sort > description.md
til:
  uv run scripts/til.py
linkedin:
  uv run scripts/linkedin_blog_map.py
embeddings:
  uv run analysis/embeddings/embeddings.py
  uv run analysis/embeddings/blogmap.py
  cp -R analysis/embeddings/blogmap ~/r2/files/blog/
