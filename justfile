build: description
  bash setup.sh
description:
  find posts pages -type f -name '*.md' -exec awk 'FNR==1{d="0000-00-00"} /^date:/{d=$2} /^(summary|description|tags):/{print d "\t" FILENAME ":" $0}' {} + | sort -r | cut -f2- > description.md
update:
  #!/usr/bin/env bash
  set -euo pipefail

  # Assumes GEMINI_API_KEY is already loaded.
  mapfile -t markdown < <(find posts pages -name '*.md' -print | sort)
  uv run ~/code/scripts/summarize.py blog "${markdown[@]}" --workers 1

  # If summarize.py warns about proposed tags, replace them with existing tags
  # or add approved new tags to metadata-tags.yml with a one-line description.

  uv run analysis/embeddings/embeddings.py
  bash setup.sh
  uv run --with pytest --with pyyaml --with typer --with numpy --with pandas --with pyarrow --with ruamel.yaml pytest -q scripts
til:
  uv run scripts/til.py
linkedin:
  uv run scripts/linkedin_blog_map.py
embeddings:
  uv run analysis/embeddings/embeddings.py
  uv run analysis/embeddings/blogmap.py
  cp -R analysis/embeddings/blogmap ~/r2/files/blog/
