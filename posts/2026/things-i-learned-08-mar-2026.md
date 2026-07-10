---
title: Things I Learned - 08 Mar 2026
date: 2026-03-08T00:00:00+00:00
categories:
  - til
description: I increased Claude Code's output limit to 64k, adopted agent-friendly CLI practices with Google Workspace, and switched to the 'just' task runner. I've also stopped manual code formatting now that AI handles most of my development.
tags: [claude-code, prompt-engineering]
---

This week, I learned:

- IITM has launched a [4 year degree in management & data science](https://study.iitm.ac.in/mg/).
- "Use AI to replace early-career mentorship: use AI-driven synthetic practice when traditional apprenticeship pathways collapse. AI can generate personalized coaching, replacing the missing junior loop with training environments." [Jack Clark](https://jack-clark.net/about/)
- Observability is more than logging. It's agents watching feeds and signalling insights!
- The [GPT 5.4 prompt guidance](https://developers.openai.com/api/docs/guides/prompt-guidance) is a bit complex, but here's what it's broadly saying: ([Gemini](https://gemini.google.com/share/b359f1e5fb50))
  - It'll over-complicate answers and front-end design unless you tell it exactly how you want it
  - It'll keep checking with you or give up (e.g. on errors) unless you tell it otherwise, e.g. with checklists or rules
- Claude Code supports [32K output tokens](https://code.claude.com/docs/en/settings) by default. Since I generate large data stories, I usually hit this limit and lose an entire session. Setting the environment variable `CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000` (which is the maximum) reduces this problem.
- [Google Workspace CLI](https://github.com/googleworkspace/cli) lets you run `npx -y @googleworkspace/cli` as a single unified service for all Google Workspace APIs. It follows [agent-friendly CLI practices](https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/) which I turned into a [SKILL.md](https://github.com/sanand0/scripts/blob/live/agents/agent-friendly-cli/SKILL.md).
- I've been using `mise use -g ubi:owner/repo` to install GitHub packages. The [`ubi` backend](https://mise.jdx.dev/dev-tools/backends/ubi.html) is now [deprecated](https://github.com/jdx/mise/discussions/7727) in favor of the new [`github` backend](https://mise.jdx.dev/dev-tools/backends/github.html). This works fine for most repos, with edge cases like [jtroo/kanata](https://github.com/jtroo/kanata/) which still require `ubi:jtroo/kanata` as of now.
- On the margin, I'll likely switch to [`just`](https://github.com/casey/just) as my task runner. [Claude](https://claude.ai/share/9ec242a3-e0e8-4d82-b80b-fa8bac036ed4)
- With AI now writing almost all of my code, I don't see much need to format it. Code formatters like `ruff`, `dprint`, `biome`, etc. are not relevant when AI will be reading and writing the code, not humans. I just format the prompts in Markdown.
- Salt is the duct tape of food ingredients. Lemon juice, vinegar, butter/oil, onion/garlic, etc. are runners-up. [Claude](https://claude.ai/share/8a783928-e726-439c-8415-3bc673ff4645)
- Claude's [prompt to import memory](https://claude.com/import-memory) from other AI providers doesn't seem to work with Claude's free account: ["No memories or stored context found."](https://claude.ai/share/fc8b9173-b47c-4ebd-a8f7-b87b03433706)
