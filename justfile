build: description
  bash setup.sh
description:
  find posts pages -type f -name '*.md' -exec awk 'FNR==1{d="0000-00-00"} /^date:/{d=$2} /^(summary|description|tags):/{print d "\t" FILENAME ":" $0}' {} + | sort -r | cut -f2- > description.md
update:
  #!/usr/bin/env bash
  set -euo pipefail

  # Assumes GEMINI_API_KEY is already loaded.
  mapfile -t markdown < <(find posts pages -name '*.md' -print | sort)
  uv run ~/code/scripts/summarize.py blog "${markdown[@]}" --model gemini-2.5-flash --workers 1

  bash setup.sh
  uv run --with pytest --with pyyaml --with typer --with numpy --with pandas --with pyarrow --with ruamel.yaml --with scikit-learn pytest -q scripts
tags-review:
  uv run scripts/tag_proposals.py evaluate
tags-promote tag description:
  uv run scripts/tag_proposals.py promote "{{tag}}" --description "{{description}}"
til:
  uv run scripts/til.py
linkedin:
  uv run scripts/linkedin_blog_map.py
embeddings:
  # Optional analytical artifact. This deliberately re-embeds invalid legacy vectors.
  uv run analysis/embeddings/embeddings.py
  uv run analysis/embeddings/blogmap.py
  cp -R analysis/embeddings/blogmap ~/r2/files/blog/
serve:
  cd public && python -m http.server 8000
