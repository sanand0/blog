---
title: Automating a podcast from GitHub commits
date: "2025-05-04T11:21:20Z"
lastmod: "2025-05-09T09:56:38Z"
categories:
  - coding
  - llms
wp_id: 4094
---

![Automating a podcast from GitHub commits](/blog/assets/Weekly-Codecast-Logo-Design.webp)

Here's an [LLM-generated podcast](https://www.s-anand.net/files/codecast-2025-05-04.mp3) of what I coded last week. [NotebookLM](https://notebooklm.google.com/)-inspired.

The process proved straightforward.

- [Get my GitHub commits for the week](https://github.com/sanand0/sanand0/blob/bfb58a7e53d8071582ef7b209f86ceb275819b44/week/summary.py#L62-L105).
- [Get the repositories I committed to](https://github.com/sanand0/sanand0/blob/bfb58a7e53d8071582ef7b209f86ceb275819b44/week/summary.py#L41-L59) for more context.
- [Have an LLM generate a podcast script](https://github.com/sanand0/sanand0/blob/bfb58a7e53d8071582ef7b209f86ceb275819b44/week/summary.py#L108-L130). I'm using [GPT 4.1 Mini](https://platform.openai.com/docs/models/gpt-4.1-mini) but might shift to Gemini 2.5 Flash or DeepSeek V3.
- […using a detailed prompt](https://github.com/sanand0/sanand0/blob/bfb58a7e53d8071582ef7b209f86ceb275819b44/week/config.toml#L64-L110) beginning with "You are a podcast script assistant for “Anand’s Weekly Codecast.” This episode is for the week of {WEEK}. …". Here's a [sample output](https://github.com/sanand0/sanand0/blob/bfb58a7e53d8071582ef7b209f86ceb275819b44/week/2025-05-04/podcast.md).
- [Convert the script to audio](https://github.com/sanand0/sanand0/blob/bfb58a7e53d8071582ef7b209f86ceb275819b44/week/summary.py#L133-L177). I'm using [GPT 4o Mini TTS](https://platform.openai.com/docs/models/gpt-4o-mini-tts) with [customized voices of Ash and Nova](https://github.com/sanand0/sanand0/blob/bfb58a7e53d8071582ef7b209f86ceb275819b44/week/config.toml#L112-L130).

These now appear on my [GitHub repo](https://github.com/sanand0/) as a weekly summary.

Beyond technical novelty, it reshaped how I think about documentation.

1. I write for two audiences: informing my future self what changed **and** explaining **why** to an LLM that will narrate it. That's an interesting behavioral change.
2. Technical debt is audible. When hearing my week's work, architectural issues and potential next steps become clear. It creates an accountability mechanism that code reviews often miss.
3. Ambient documentation. I stop documenting when coding fast. Converting signals (commits) to consumable content creates "ambient documentation" that accumulates with no extra effort. Audio reduces the energy needed to stay up to date.

This could change how we share technical work. Maybe financial analysts "narrate" spreadsheet changes, designers "explain" Figma iterations, or operators "log" settings adjustments - all automated from version control metadata.

**Converting activity traces into narratives dramatically lowers cost of knowledge & sharing.**

What activity traces do we generate? It's worth exploring what they could become, and how it'd change behavior if we knew those signals would become stories.
