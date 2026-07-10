---
title: Things I Learned - 14 Sep 2025
date: 2025-09-14T00:00:00+00:00
categories:
  - til
description: I discovered why weak ties matter for opportunities and tested tools like mise, ast-grep, and hurl. I also learned how non-associative floating-point addition causes LLM non-determinism and why shrinking output tokens significantly reduces latency.
tags: [llms, latency]
---

This week, I learned:

- Though I'm connected on LinkedIn with people I can't remember (weak ties), pruning them shrinks serendipity. Weak ties, despite noise, are disproportionately valuable for opportunities, e.g. intros, jobs, and pruning reduces future upside. [Science](https://www.science.org/doi/10.1126/science.abl4476)
- Claude has a Python + Node code interpreter that can access GitHub, PyPi, npm and Google. [Simon Willison](https://simonwillison.net/2025/Sep/9/claude-code-interpreter/)
- [SuperTinyIcons](https://github.com/edent/SuperTinyIcons) has very small icons for many websites and is available via CDN. Sample: `http://cdn.jsdelivr.net/npm/super-tiny-icons/images/svg/github.svg`
- [Clock bench](https://x.com/alek_safar/status/1964383077792141390?t=BzvyMoZH18jDBEop7XeZpA) is an LLM benchmark based on how well LLMs tell the time from an analog clock. Humans (89%) are _much_ better than the best model (Gemini 2.5 Pro - 13%).
- Veo 3 is now available via API. Veo 3 fast is 15s/second. [Google](https://developers.googleblog.com/en/veo-3-and-veo-3-fast-new-pricing-new-configurations-and-better-resolution/)
- ChatGPT has full support for MCPs via Developer mode in Plus and Pro accounts, via "Developer mode". [OpenAI](https://platform.openai.com/docs/guides/developer-mode)
- In Pyodide, you can use `from js import document` and then `document.querySelector` to manipulate the DOM directly from Python. `from pyodide.http import pyfetch` lets you use fetch.
- [`gtrending`](https://pypi.org/project/gtrending) is a Python package that fetches trending GitHub repos, users, etc. `uvx gtrending repos --language rust --since weekly` fetches trending Rust repos of the week.
- [`astgrep`](https://ast-grep.github.io/) lets you search in code (across languages) using AST patterns. Like [semgrep](https://github.com/semgrep/semgrep) but [more](https://ast-grep.github.io/advanced/tool-comparison.html) about code search than security. `uvx --from ast-grep-cli ast-grep` runs from the CLI. Useful for [code rewriting](https://ast-grep.github.io/guide/rewrite/transform.html), fast [linting](https://ast-grep.github.io/guide/project/lint-rule.html), [code search](https://ast-grep.github.io/guide/pattern-syntax.html).
- [`hurl`](https://github.com/Orange-OpenSource/hurl) is a CLI config-based HTTP automation tool. Useful for tests, bulk (templatized) HTTP requests, etc.
- [`rustdesk`](https://rustdesk.com/) is an open-source remote desktop software. TeamViewer alternative. Self-hostable.
- [`prek`](https://github.com/j178/prek) is a much faster version of [`pre-commit`](https://pre-commit.com/) - a cross-language pre-commit hook manager.
- ⭐ [`mise`](https://mise.jdx.dev/) is a tool version manager. Combines nvm/fnm, pipx, etc. Supports running [several tools](https://mise.jdx.dev/registry.html) with a smooth installation.
- The [npm phishing email was a great one](https://xeiaso.net/notes/2025/we-dodged-a-bullet/). It [compromised chalk](https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised) which is used in most npm packages. This may be one of the best supply chain attacks in recent times and makes me want to pin versions instead of using `npx -y`. Also makes me glad that I'm sponsoring [@isaacs](https://github.com/isaacs) and [@sindresorhus](https://github.com/sindresorhus) - two _critical_ open source maintainers.
- "I pay for YouTube Premium. For my money, it’s the best bang-for-the-buck subscription service on the market". - [Gavin Andregg](https://anderegg.ca/2025/09/08/youtube-is-a-mysterious-monopoly)
- LLMs are non deterministic because GPUs add floating point numbers concurrently and FP addition is non associative - order matters. [Thinking Machines](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
- Claude.ai can [natively work with Excel, PPTX, DOCX, and PDF files now](https://www.anthropic.com/news/create-files).
- With embeddings, atomic labels + hierarchy beat instruction-heavy prompts. Prefer short, concrete sub-labels (e.g., “promotion,” “job security,” “flexibility”) that roll up to a parent "career" rather than a composite instruction like “Total Rewards and Career Growth”. Embedding similarity is not smart enough to figure this out.
- Today, RPA is cheaper than LLMs in some areas. But it's a moving target. LLM costs are fall fast: 70–90% declines across major providers in 1.5 years. Therefore, waiting has option value. But classic IT compares static quotes, not declining curves, and hence is likely to under-procure LLM solutions.
- ⭐ The biggest near-term ROI for LLMs in data science is like ‘boring’ data work: PII tagging, data dictionaries, ER/joins, SDTM mapping, etc.. People expect flashy GenAI, but LLMs can bootstrap schema matching and data-cleaning, speeding engineer verification, which is more useful at scale.
- You can create an [infinite leaflet map with nano banana](https://github.com/seezatnap/nano-banana-infinimap).
- [Codex CLI](https://github.com/openai/codex) with high reasoning effort seems far more comprehensive than [Codex online](https://chatgpt.com/codex). I asked both to identify the system requirements (URLs to access, software to install, ports to open) for my [Tools in Data Science course](https://tds.s-anand.net/). Codex CLI got it right one shot (after 10 minutes of thinking). Codex online missed several items even after 4 attempts.
- The [Reod](https://coppermind.net/wiki/Reod) on [Elantris](<https://coppermind.net/wiki/Elantris_(city)>) might have been triggered by [Jaddeth](https://coppermind.net/wiki/Jaddeth) who might be an [Autonomy](https://coppermind.net/wiki/Autonomy) avatar. [ChatGPT](https://chatgpt.com/share/68be4c74-afa8-800c-b004-7a1565cb2487)
- Output tokens dominate latency. Decoding is sequential (one token depends on all prior tokens), so long completions are the main throttle. Shrinking _returned_ text (e.g., send spans/tags instead of echoing paragraphs) yields a far bigger win on latency than shrinking inputs.
