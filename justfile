build: description
  bash setup.sh
description:
  find posts pages -type f -name '*.md' -exec awk 'FNR==1{d="0000-00-00"} /^date:/{d=$2} /^(summary|description|keywords):/{print d "\t" FILENAME ":" $0}' {} + | sort -r | cut -f2- > description.md
til:
  uv run scripts/til.py
linkedin:
  uv run scripts/linkedin_blog_map.py
embeddings:
  uv run analysis/embeddings/embeddings.py
  uv run analysis/embeddings/blogmap.py
  cp -R analysis/embeddings/blogmap ~/r2/files/blog/
