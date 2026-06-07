build:
  bash setup.sh
til:
  uv run scripts/til.py
linkedin:
  uv run scripts/linkedin_blog_map.py
embeddings:
  uv run analysis/embeddings/embeddings.py
  uv run analysis/embeddings/blogmap.py
  cp -R analysis/embeddings/blogmap ~/r2/files/blog/
