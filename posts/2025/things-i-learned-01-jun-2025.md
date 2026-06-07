---
title: Things I Learned - 01 Jun 2025
date: 2025-06-01T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- MicroVMs like [firecracker](https://github.com/firecracker-microvm/firecracker) are like containers but offer higher isolation with slightly higher latency and memory via `kvm` hypervisors. [ChatGPT](https://chatgpt.com/share/683c1251-3f48-800c-95d4-6a3e9a2b63ac)
- I was exploring free alternatives to the $4/mo Hetzner instance I use. Google offers a free e2 micro instance. But it's _much_ smaller than the Hetzner CAX11/CX-22 server I run. 25% of CPU, 25% of RAM (which is the main problem -- 1 GB is often not enough), slower HDD, 5% of outbound traffic. Hetzner remains one of the best value offerings.
- Planning to use [pretty-quick](https://www.npmjs.com/package/pretty-quick) instead of [prettier](https://www.npmjs.com/package/prettier). It's a wrapper that only fixes changed files based on git.
- [f2](https://github.com/ayoisaiah/f2) is an intuitive cross-platform renaming tool. Usage:
  ```bash
  f2 -f 'jpeg' -r 'jpg'
  f2 -r '{id3.artist}/{id3.album}/${1}_{id3.title}{ext}'
  ```
- git worktrees can create multiple copies of code. This is useful when using different coding agents run the same task in parallel. [Ref](https://www.skeptrune.com/posts/git-worktrees-agents-and-tmux/)
  - `git worktree add -b $newbranch worktree/$path` creates a copy of HEAD in $path as a $newbranch
  - `git push` from branch and create a pull request
  - `git worktree remove worktree/$path` to remove worktree
  - `git worktree prune` for garbage collection
- LLMs optimize for compression. Humans optimize for adaptive flexibility. [Ref](https://www.linkedin.com/posts/ravid-shwartz-ziv-8bb18761_you-know-all-those-arguments-that-llms-think-activity-7333886415568605186-LA54/) [arXiv](https://arxiv.org/abs/2505.17117)
- Gemini Deep Research accepts files and images. Cross-checking reports, providing private sources, etc. is now realistic. [Ref](https://workspaceupdates.googleblog.com/2025/05/deep-research-updates-gemini-io-2025.html)
- The new Flux1.Kontext model seems _very_ good at image editing. Costs 4-8c per image. [Peter Gostev](https://www.linkedin.com/posts/peter-gostev_image-editing-with-black-forrest-labs-activity-7334272870556057602-5An1)
- Today, I'd go with [Node's native test runner](https://nodejs.org/api/test.html) for backend JS testing. I used [node-tap](https://node-tap.org/) earlier. For front-end, I'd pick [vitest](https://vitest.dev/). [ChatGPT](https://chatgpt.com/share/683808bf-c01c-800c-a5ea-18df8394414c)
- ⭐ DuckLake is a DuckDB extension that makes Parquet files editable with history. And much more. [DuckDB](https://duckdb.org/2025/05/27/ducklake.html)
- When processing presentations for RAG via OCR:
  - [How to parse PDF docs for RAG](https://cookbook.openai.com/examples/parse_pdf_docs_for_rag) is a useful OpenAI cookbook with a GPT 4o prompt
- Here's one way controls inflate cost. Tracking expenses, submitting receipts, and justifying usage adds transaction cost. So, rather than a $10 monthly top-up, I'd rather top-up $200 (even if it might go unused), rather than have to ask again.
