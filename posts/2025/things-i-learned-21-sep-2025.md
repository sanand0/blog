---
title: Things I Learned - 21 Sep 2025
date: 2025-09-21T00:00:00+00:00
categories:
  - til
description: I found that ChatGPT’s thinking mode can over-edit images and learned to measure LLM accuracy against human agreement. I also explore CLI tools like ugrep and yt-dlp, VS Code terminal tricks, and why organizational transaction costs inflate budgets.
keywords: [ugrep, yt-dlp, systemd, llm-as-a-judge, vs code, transaction costs, chatgpt]
---

This week, I learned:

- When editing an image, ChatGPT's non-thinking mode does a _much_ better job of preserving the original image features than the thinking mode. When editing my photo, I found that the thinking mode creates images that looks quite different than me. A surprising effect of overthinking.
- ⭐ When evaluating model accuracy, compare with human accuracy rather than perfect accuracy. SMEs rarely agree among themselves, so it's unlikely that they will agree with an LLM. Instead, measure how often the LLM agrees with the majority of SMEs and how often it disagrees with all SMEs. This gives a more realistic measure of accuracy. [LLMs instead of Human Judges?](https://aclanthology.org/2025.acl-short.20.pdf) and [Judging LLM-as-a-Judge](https://arxiv.org/pdf/2306.05685). [ChatGPT](https://chatgpt.com/share/68cfc068-0c5c-800c-b961-81e6a061b05f)
- I understand at least one mechanism of how costs are inflated in large organizations. Even people who want to keep costs low find that the process of tracking expenses, submitting receipts, answering questions around approval, adds transaction cost. So, rather than going for a $10 plus top up mechanism, I would rather go for and ask people to take a $500 top up. Better ask for more and waste than have to ask again.
- YouTube downloaders: [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the CLI, [Stacher](https://stacher.io/) for Windows/Mac/Linux, [Cobalt](https://cobalt.tools/) for a web-based app. [Ref](https://windowsread.me/p/best-youtube-downloaders)
- VS Code a bunch of features I discovered:
  - It can run a terminal in its own new window for over a year (via Ctrl+P > Terminal: Move Terminal into New Window). Now, <kbd>Ctrl + Alt + Shift + \`</kbd> does this directly.
  - [Terminal Intellisense](https://code.visualstudio.com/docs/terminal/shell-integration#_intellisense-preview) shows completion suggestions in the UI. Very helpful. Ctrl+Space triggers the menu completion.
- ⭐ "We find that the per-step error rate itself rises as the task progresses", i.e. once a conversation goes the wrong way, it's really hard to correct it. [The Illusion of Diminishing Returns](https://arxiv.org/html/2509.09677)
- [Japonaise Cake](https://www.google.com/search?q=japonaise) is the name of the pastry that I had as a child and grew up longing for. I have spent several weeks searching for it in the roadside bakeries at Bangalore and Chennai but only [one bakery](https://cakebee.in/products/japonaise-cake) seems to have it.
- `systemd` is the modern way to run scheduled jobs, instead of `cron`. It's far more complex. But it can catch up on missed runs via a `Persistent` option. [Working with systemd timers](https://documentation.suse.com/smart/systems-management/html/systemd-working-with-timers/index.html)
- ⭐ Vice-chancellors of universities resist AI in education because (a) their faculty does not know AI and (b) AI is unreliable. But they are interested in (a) large-scale AI-evaluation and (b) AI-enabling entire campus.
- [tldr.sh](https://tldr.sh/) offers concise man pages, e.g. `uvx tldr jq`. [cheat.sh](http://cheat.sh/) offers detailed examples, e.g. `curl cheat.sh/jq` or `curl cheat.sh/:help`.
- [`ugrep`](https://github.com/Genivia/ugrep) is a fast drop-in replacement for `grep`. It supports fuzzy search with a customizable Levenshtein distance. Also `ug -Q` shows an interactive TUI searches like VS Code's "Search in Files" feature. Very intuitive.
- [Dagger](https://dagger.io/) lets you write CI/CD workflows in Python. I tried running it but after 7m of pulling large Docker containers, I gave up. Too heavy.
- [dotslash](https://dotslash-cli.com/) lets you write scripts that downloads GitHub releases, caches, and runs them. Requires writing scripts. I prefer [`mise`](https://mise.jdx.dev/).
- ChatGPT has a quota for searches. I saw this phrase in the reasoning traces: "I'll avoid overloading on citations since we only have a few calls left." It doesn't seem to be in ChatGPT's [system prompt](https://github.com/elder-plinius/CL4R1T4S/blob/476a209169e8cf0c7cad97c7ccf4c5afb2248067/OPENAI/ChatGPT5-08-07-2025.mkd) from last month, so it's either part of the tool response or a new prompt.
- Depending on the underlying chips that a model uses, the floating point multiplications may differ and model quality can vary. So Claude 4 Opus running on Anthropic's GPUs can produce different results from when running on Google's GPUs or Amazon's GPUs.
