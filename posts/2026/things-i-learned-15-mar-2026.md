---
title: Things I Learned - 15 Mar 2026
date: 2026-03-15T00:00:00+00:00
categories:
- til
description: I learned that Timsort is remarkably fast, moor replaces bat for wrapping via keyboard shortcuts, --help is a useful agent prompt prefix, and Claude Opus 4.6 solved a problem Knuth studied.
tags: [ai-agents, agentic-workflows, problem-solving, web-browsers]
---

This week, I learned:

- [Timsort](https://en.wikipedia.org/wiki/Timsort) is one of the [fastest sorting algorithms](https://simonwillison.net/2026/Mar/11/sorting-algorithms/).
- Switching from [`bat`](https://github.com/sharkdp/bat) to [`moor`](https://github.com/walles/moor) as a pager, since `bat` doesn't support wrapping via keyboard shortcuts. [Gemini](https://gemini.google.com/share/812da811d636)
- "Use `(some-command) --help` to ..." is an efficient prompt prefix that tells agents to read the docs and use a CLI tool to solve a problem. For example, "Use `uvx rodney --help` and `ffmpeg` for a demo video of GitHub PRs".
- As agents improve, we'll have more mediorce output (e.g. dashboards) since people won't know to ask for better, or validate the result. They'll hire experts who know to ask better and verify better.
- Claude Opus 4.6 solved a problem Knuth was working on! [Knuth](https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf)
- [Cognitive debt](https://simonwillison.net/tags/cognitive-debt/) is what Simon Willison calls it when we build (or, in my case, say/write) stuff we don't understand. The debt framing is apt. One solution is to generate a version intended for AI to read, and another for us. [#](https://simonwillison.net/2026/Feb/17/release-notes-webcomic/)
- How can an innovator learn accountability? "I'm wired to start fires. Should I learn to also run the fire department, hire someone who does, or just stay a fire-starter and let others deal with the mess?" ANS: First, accountability is high value, so **do it**! Second, prefer a partner over building muscle. Build muscle only if output is checkable, has value, and customers will pay. [Claude](https://claude.ai/share/d2c6a479-3aaf-402d-a2b9-318532158a92) | [ChatGPT](https://chatgpt.com/share/69b0e234-64b8-8003-93b5-f244b05a7545) | [Gemini](https://gemini.google.com/share/38f8bab88751)
  - Commit publicly. Put your name on the output.
  - Commit to process (or narrowly defined output) rather than outcome.
  - Optimize with data, code, checklists, workflows, culture, etc.
- OpenAI released [gpt-realtime-1.5](https://developers.openai.com/api/docs/models/gpt-realtime-1.5) and [gpt-audio-1.5](https://developers.openai.com/api/docs/models/gpt-audio-1.5). Buth are ~20% cheaper than the 4o versions, but 6.7x more expensive than [gpt-realtime-mini](https://developers.openai.com/api/docs/models/gpt-realtime-mini). 1 second is about 10 tokens, so an hour of audio input at $32/MTok is about $1.15.
- The "Effort" setting for AVIF files on [Squoosh](https://squoosh.app/) doesn't reduce file size - it increases quality slightly (for a tiny _increase_ in file size). So, set the quality to whatever file size you need and increase the effort for a slightly better quality.
- [Polya](https://en.wikipedia.org/wiki/George_P%C3%B3lya) believed in teaching problem-solving rather than solutions, i.e. teach [How to Solve It](https://en.wikipedia.org/wiki/How_to_Solve_It), not just _what_ you get at the end. To me, this includes:
  - Understand the problem (from different perspectives)
  - Plan (with different mental models)
  - Execute (the easy bit)
  - Look back (post-mortem, retrospectives, etc.)
- [Browserless](https://github.com/browserless/browserless) lets you run browsers via an API. Useful when you don't want the overhead of setting up a browser infrastructure, or for multiple browsers in parallel. Scraping, testing, web app automation, PDF/screenshot/video generation, etc. are all possible. [Gemini](https://gemini.google.com/share/3c547e57030b)
- OpenAI has a [Websocket mode](https://developers.openai.com/api/docs/guides/websocket-mode/)
- [GitHub Agentic Workflows](https://github.github.com/gh-aw/setup/creating-workflows/) lets you "compile" a Markdown file into an agentic GitHub action. Useful as a sceptical reviewer, issue-to-prototype builder, data to story generator, automated code migrator, etc. [Gemini](https://gemini.google.com/share/d604275d42d7) [Claude](https://claude.ai/share/e4beeed2-e49e-49be-99bd-d6ce5678a7a7)

## Questions I was asked

[Week ending 15 Mar 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-03-15)

- **Question**: How do you share insights during the learning phase - how do you write your blog?\
  **Answer**: Writing is not only for others; the big benefit is clarifying your own thinking; start by putting notes on GitHub.
- **Question**: Who motivates you to do all these workshops?\
  **Answer**: I do it for self-learning; I commit to talks on topics I don't know - the commitment forces the learning.
- **Question**: AGI - within 3-5 years, do you think we'll see it?\
  **Answer**: "I talk to it like a human - that is AGI; we got there last year."
- **Question**: What's the "LLM Psychologist" title about?\
  **Answer**: Nothing to do with psychology formally; Andrej Karpathy coined the term in 2023, it sounded cool, called HR: "Do you have any problem if I call myself LLM Psychologist?"
- **Question**: Starting AI in first year - is it like giving a calculator before learning tables? Won't students become dullards?\
  **Answer**: It's like learning how to use the internet; whoever gets there early has an edge; the bigger risk is underuse, not overuse.
- **Question**: I want to build my own CRM. Is it doable with no coding experience?\
  **Answer**: Why build a CRM at all - upload your Excel to ChatGPT, tell it who to chase, you already have a CRM.
- **Question**: If somebody wanted to build Gramener 2.0 today with LLMs, how would you rebuild it?\
  **Answer**: Moats are based on taste and judgment now; regulation remains; custom software renaissance means services beat SaaS.
