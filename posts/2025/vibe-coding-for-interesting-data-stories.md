---
title: Vibe-Coding for Interesting Data Stories
date: "2025-10-06T09:03:35Z"
lastmod: "2025-10-06T09:03:38Z"
categories:
  - links
wp_id: 4228
---

![Vibe-Coding for Interesting Data Stories](/blog/assets/gardener.webp)

Last weekend, I fed Codex my browser history and said "explore." It found a pattern I call **rabbit holes** -- three ways we browse:

1. **Linear spiral** - one page > next page > next. E.g. filing income tax, clicking "next" on the [PyCon schedule](https://in.pycon.org/2025/program/schedule/).
2. **Hub & spoke** - hub > open tabs > back to hub. E.g. exploring [DHH](https://en.wikipedia.org/wiki/David_Heinemeier_Hansson)'s Ubuntu setup, checking Firebase config.
3. **Wide survey** - source > many, many pages. E.g. clearing inbox, scanning news.

Then Claude Code built this [lovely data story](https://sanand0.github.io/datastories/browser-history/rabbit-holes/).

---

My goal? Find challenges in vibe-coding **interesting** data stories. I found several.

**A. I don't know what I want.**

Solution? **Ask for multiple options**. More options = more ideas. Codex proposed two I hadn't planned: [rabbit holes](https://sanand0.github.io/datastories/browser-history/rabbit-holes/) and [search funnels](https://sanand0.github.io/datastories/browser-history/search-funnels/).

**B. I don't know if it'll turn out well.**

Solution? **Build them all**. Don't pre-judge. I **did not** expect rabbit holes to be interesting - a clear prediction error.

**C. Reviewing is the bottleneck.** It's slow and painful.

Solution? **Make reviews easy**.

- **Ask for review-friendly output**. E.g. A table/heatmap comparing options.
- **Use LLMs to pre-review**. E.g. Pick top 3 with reasons.
- **Review output, not code**. E.g. Have it build a working demo, **then** review.

**D. Model / tool strengths vary.**

Solution? **Align with strengths**. For example:

- **Use GPT-5 for planning**. It's better than GPT-5-Codex or Claude 4.5 Sonnet.
- **Code UI with Claude 4.5 Sonnet**. It's better than most models.

---

Check out the [prompts & process](https://sanand0.github.io/datastories/browser-history/).

**Try this**: Pick one messy dataset you have. Ask an LLM for five ways to explore it. Build them all. One will surprise you.

[LinkedIn](https://www.linkedin.com/posts/sanand0_last-weekend-i-fed-codex-my-browser-history-activity-7381531293542449152-uZXX)
