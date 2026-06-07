---
title: Things I Learned - 22 Dec 2024
date: 2024-12-22T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- What to use for hosting: [ChatGPT](https://chatgpt.com/share/676663cd-2560-800c-b53c-2c51ef41be69)
  - GitHub Pages: Static websites, medium files
  - Cloudflare Pages: Static websites, global delivery
  - Vercel: Frontend frameworks (e.g. Next.js) with high DX and ISR, small files
  - Netlify: JAMstack projects, minimal back-end, moderate files
  - Glitch: Small static projects
  - Render: Full-stack apps requiring databases and server-side compute
  - Firebase Hosting: Small sites, limited large files
  - Archive.org: Public archival, large files
  - Google Drive: File sharing, large files
  - Dropbox: File sharing, moderate files
  - Cloudflare R2: Static assets, large file delivery
- Anthropic defines agents. [Building effective agents](https://www.anthropic.com/research/building-effective-agents) + [Cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
  - **Augmented LLMs** are LLMs enhanced with augmentations such as retrieval, tools, and memory.
  - **Workflows** are systems where LLMs and tools are orchestrated through **predefined** code paths.
    - **Prompt chaining**: Pipe each LLM output to the next LLM. A->B->C->Z. E.g. Write report, then translate. Extract results, then verify them. Successively ask follow-up questions.
    - **Routing**: One LLMs decides which other LLM to call next. A->B|C|D->Z. E.g. Evaluate complexity, then pick the right model. Classify request time, then pick the right prompt.
    - **Parallelize: Sectioning** (and **Orchestrator-workers**): Break tasks into independent subtasks, then aggregate. A->B+C+D->Z. E.g. Evaluate contracts against different clauses in parallel.
    - **Parallelize: Voting**: Run same task multiple times, then vote. A->B+B+B->Z. E.g. Review code for prompt injection using different prompts. Evaluate content safety with different thresholds.
    - **Evaluator-optimizer**: One model checks another in a loop. A->B->A->B->...->Z. E.g. Literary translation. Self-healing code. Policy violation checks.
    - **Human-in-the-loop Checkpoints**: The workflow explicitly requests human review at certain stages. A->B->(Human)->C->Z. E.g. Sensitive content review. High-stakes decision making. Ambiguous tasks.
  - **Agents** are LLMs that dynamically direct their own processes and tool usage, consulting tools or the user as needed.
- To download YouTube subtitles, use: `yt-dlp -q --skip-download --convert-subs srt --write-sub --sub-langs "en" --write-auto-sub --print "requested_subtitles.en.url" "$url"` [Simon Willison](https://simonwillison.net/2024/Dec/19/q-and-qv-zsh-functions/#atom-everything)
- o1-preview diagnoses better than doctors. [Harvard](https://arxiv.org/pdf/2412.10849)
- OpenAI's release of ephemeral tokens via sessions (valid for 1 minute) are a useful way of exposing apps for public demos. Currently it works only for the Realtime API, though.
- [SpreadsheetLLM](https://arxiv.org/abs/2407.09025) is a way of encoding spreadsheets in an LLM friendly format. It's good for 1K+ rows. For lower, Markdown > XML > HTML. However, [Table Meets LLM](https://arxiv.org/abs/2305.13062v4) suggests that HTML > XML > Markdown, so this is unclear.
- #HARD prompt. Ask video generators like SORA to generate text in videos. It is of average quality.
- [GPT 4o Mini Realtime](https://platform.openai.com/docs/models#gpt-4o-realtime) was released. A realtime conversation will cost ~50c/hr. About 36c for input, 72c for output. (I extrapolated from the 6c/min audio input cost for GPT 4o Realtime when it was $100/MTok. GPT 4o Mini Realtime is $10/MTok input and $20/MTok output.)
- This is an interesting way to understand software. `Generate a Mermaid sequence diagram showing interactions based on this code.` [Ref](https://llmfoundry.straive.com/history#?t=1734434521298204)
- The King James Bible and all Harry Potters, each, are about $1M tokens (rounded off).
- [markdown2](https://pypi.org/project/markdown2/) is the new de facto Markdown library for Python.
- Claude 3.5 Sonnet is _way_ ahead of competition on the [LMSYS Webdev Arena](https://web.lmarena.ai/leaderboard)
- [Raspberry Pi 5](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/) has a faster CPU, more RAM and GPU, 4K support, multiple USB 3 ports
- Government websites like the official press releases cannot be crawled from outside India. Hence the need for server farms in India!
