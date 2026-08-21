---
title: Things I Learned - 10 May 2026
date: 2026-05-10T00:00:00+00:00
categories:
- til
description: I learned how to speed up xz, move Ubuntu windows between monitors, and use Claude Code routines. I also tested rtk, a CLI proxy that cut token use by about half.
tags: [productivity, coding-agents, claude-code, llms]
---

This week, I learned:

- I'm experimenting with [Tauon MusicBox](https://tauonmusicbox.rocks/) as an alternative to VLC as a music player. Update: 01 Jun 2026. I switched back to VLC. Tauon Music Box is glitch. It stops songs mid-way and doesn't play automatically when launched.
- `xz` is pretty slow by default. `xz -T0` uses all available threads and speeds it up ~3X. Enabling "Performance mode" (over a power-saver mode) produces a further speed-up of ~2X for me. For a 200MB file, that reduces the time from ~1 minute to 10 seconds.
- Notes from [Simon Willison's notes from the Claude Code event](https://simonwillison.net/2026/May/6/code-w-claude-2026/):
  - "Design for the next model". Build things that don't quite work today on the assumption that they'll start working with a model upgrade in the future.
  - "The advisor strategy". Instead of using a smarter model to plan, use smaller models to ask Opus for advice-on-demand.
  - Dreaming looks really interesting. You can run a task over night which examines previous sessions and creates new memories.
  - A [routine](https://code.claude.com/docs/en/routines) is a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors, packaged once and run automatically. Routines execute on Anthropic-managed cloud infrastructure, so they keep working when your laptop is closed.
- Overheard: "VCs say, 'OpenAI wants to get into commerce, so why are you getting into commerce?' A few weeks later, 'OpenAI no longer wants to get into commerce, so why are you?"
- Delightful discovery of the day: Super + Shift + Arrow keys to move windows between monitors on Ubuntu.
- [television](https://github.com/alexpasmantier/television) is a fast, portable fuzzy finder. Like `fzf` but faster, useful for files, text, git repos, docker images, etc.
- I added `approvals_reviewer = "auto_review"` to my `~/.codex/config.toml`. This enables [auto review](https://alignment.openai.com/auto-review) which uses an LLM to figure out whether to ask a human to approve or not. It's a lot less intrusive than asking every time. Not perfectly safe, though.
- Copilot supports a [`/chronicle`](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle) command that suggest tips and improvements when using Copilot. It's like `/insights` on Claude Code and
- [Carbonyl](https://github.com/fathyb/carbonyl/releases) is a CLI Chromium browser. Sort of like Lynx, but supports audio/video, JavaScript, even WASM, etc. This was the [author's first Rust project](https://fathy.fr/carbonyl).
- I tried [Zed](https://zed.dev/) as an alternative to VS Code. It's fast and lightweight, but lacks the ecosystem of VS Code. Plugins are harder to build and Markdown support is weak. I would use it on a flight to save power, not otherwise. This is similar to others' experience. [ChatGPT](https://chatgpt.com/share/69f703b4-409c-83ea-a9fd-0c601de973f3) <!-- https://chatgpt.com/c/69f6cf11-f870-83ea-b9bb-e35402db3226 --> UPDATE 05 Jun 2026. It DOES use some battery power - more than I'd like. I am uninstalling it.
- [LocalSend](https://github.com/localsend/localsend) is a pretty quick way to share files between phone and laptop even if you don't have a network - if you connect the laptop to the phone hotspot.
- [GNOME Network Displays](https://flathub.org/en/apps/org.gnome.NetworkDisplays) works pretty well if you want to screencast your screen to a network display - e.g. a Smart TV with Miracast or Chromecast support.
- I'm evaluating [rtk](https://github.com/rtk-ai/rtk) - a CLI proxy to reduce tokens. For example `rtk ls` or `rtk git status` shows agent-friendly compact output. I just added one like to my AGENTS.md: "Always prefix shell commands with `rtk`. Examples: `rtk git status`, `rtk pytest -q`, etc." instead of using `rtk init -g`. I am testing it out, so I don't know the impact, but it seems harmless. (Based on 2 days' usage, across 216 commands, it saved ~50% of 37K tokens. Not much, but harmless.)
- The emerging convention to mark a section of HTML / Markdown as AI generated content is to wrap it in:
  - `<section ai-disclosure="ai-generated" data-ai-model="claude-sonnet-4.6" data-ai-provider="Anthropic">` ([W3C AI Content Disclosure Community Group](https://www.w3.org/community/ai-content-disclosure/)).
