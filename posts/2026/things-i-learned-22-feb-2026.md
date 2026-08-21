---
title: Things I Learned - 22 Feb 2026
date: 2026-02-22T00:00:00+00:00
categories:
- til
description: I learned how tree-sitter handles malformed code, Cloudflare's Markdown for Agents serves HTML as Markdown, WebM can compress better than animated WebP, and Copilot can customize commit messages.
tags: [developer-tools, programming-languages, github-copilot, prompt-engineering]
---

This week, I learned:

- [tree-sitter](https://github.com/tree-sitter/tree-sitter) is a fast incremental parser generator. That means you can use it to create a parser for _any_ language that works even if there are errors, e.g. malformed JSON, Python, etc. It's used by most editors. For example, [tree-sitter-python](https://github.com/tree-sitter/tree-sitter-python) is a fast forgiving Python parser. There are [official parsers](https://github.com/tree-sitter/tree-sitter/wiki/List-of-parsers) and [community parsers](https://github.com/tree-sitter-grammars)
  - **Programming Languages:** All popular ones, less popular ones like Ada, Fortran, Lua, Zig, ... and even niche / domain-specific languages (Gleam, TLA⁺).
  - **Markup & Data Formats:** HTML, XML, Markdown, JSON, YAML, TOML, CSV, ...
  - **Query, Scripting & Config:** SQL, GraphQL, Bash, Dockerfile, Regex, Terraform (HCL), ...
- Ligature fonts are nice, but it might not be worth forming a habit out of. [Claude](https://claude.ai/share/3cb9d834-b85a-4aa6-bf9f-e7051101d5c6)
- Cloudflare introduced [Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/). This converts websites from HTML to Markdown via `Accept: text/markdown` for any Cloudflare endpoint which has enabled this feature. This requires a Pro account.
- [Microgrants](https://github.com/nayafia/microgrants) is a list of microgrants programs - where you can give small amounts of money, e.g. $50 - $1K as well as large fellowships over $100K. This includes student grants, creative & community grants, tech grants, social & policy grants, etc.
- "Animated web formats are simply video codecs ... stripped of their most powerful feature." A `.webm` file is likely to compress _much_ better than an animated `.webp`, etc. [Gemini](https://gemini.google.com/share/a83f37623107)
- esbuild can compile CSS files to support old browsers, e.g. nested rules, custom properties, etc. Usage: `esbuild input.css --target=chrome90 --outfile=output.css`. [Julia Evans](https://jvns.ca/til/esbuild-can-build-css/)
- New jargon I learnt: [Human-On-The-Loop](https://tools.s-anand.net/askai/?q=What+is+Human+On+The+Loop+vs+Human+In+The+Loop%3F+Give+it+to+me+in+a+sentence.). [Treasure In Treasure Out](https://tools.s-anand.net/askai/?q=What%27s+Treasure+In+Treasure+Out+-+as+opposed+to+Garbage+In+Garbage+Out%3F+Give+it+to+me+in+a+sentence.)
- VS Code's GitHub Copilot extension supports a `github.copilot.chat.commitMessageGeneration.instructions` setting that lets you add a `[{"text": ...}]` or `[{"file": "path/to/file.ext"}]` prompt to the commit message generation. I've pointed this to my [`git-commit.md`](https://github.com/sanand0/scripts/blob/main/agents/custom-prompts/git-commit.md) custom prompt.
