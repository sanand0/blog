---
title: The Non-Obvious Impact of Reasoning Defaults
date: "2025-10-05T02:31:58Z"
lastmod: "2025-10-05T02:32:16Z"
categories:
  - llms
wp_id: 4225
---

![The Non-Obvious Impact of Reasoning Defaults](/blog/assets/reasoning-effort.webp)

Yesterday, I discovered how much reasoning improves model quality.

My [Tools in Data Science assignment](https://exam.sanand.workers.dev/tds-2025-09-ga3#hq-ipify-llms-txt) asks students to draft an [`llms.txt`](https://llmstxt.org/) file for [ipify](https://www.ipify.org/) and auto-checks with [GPT-5 Nano](https://platform.openai.com/docs/models/gpt-5-nano) - a fast, cheap reasoning model.

I set [`reasoning_effort`](https://platform.openai.com/docs/guides/reasoning) to `minimal` and ran this checklist:

```text
1. Starts with "# ipify" and explains ipify.
2. Markdown sections on API access, support (e.g. GitHub, libraries).
3. Covers API endpoints (IPv4, IPv6, universal) and formats (text, JSON, JSONP).
4. Mentions free, no-auth usage, availability, open-source, safeguards.
5. Has maintenance metadata (e.g. "Last updated: <Month YYYY>").
6. Mentions robots.txt alignment. Stay concise (no filler, <= ~15 links).

If even one checklist item is missing or wrong, fail it.

Respond with EXACTLY one line:
PASS - <brief justification>
or
FAIL - <brief explanation of the first failed item>.
```

With a perfect `llms.txt`, it claimed "Metadata section is missing" and "JSONP not mentioned" -- though both were present.

With an `llms.txt` **without** a metadata or API section, it sometimes marked it as correct!

This surprised me. `gpt-5-nano` doesn't usually make such basic mistakes.

**Then** I realized: [`reasoning_effort`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-reasoning_effort) defaults to `medium`.

When I set reasoning effort back to `medium`, it added ~5 seconds and ~3,000 reasoning tokens but evaluates correctly.

GPT-5 Nano High is a frontier model on my [LLM Pricing Chart](https://sanand0.github.io/llmpricing/), i.e. there's no cheaper model for that quality. But this conflates GPT-5 Nano cost with GPT-5 Nano **High** quality. I don't yet know how to estimate and compare costs of reasoning models.

My takeaways:

- My "quantitative" evaluation of frontier models on the [LLM Pricing](https://sanand0.github.io/llmpricing/) is flawed and needs rethinking.
- Reasoning can make smaller models **much** more powerful. Appreciate it and **use reasoning more**.
- Reasoning models cost **far** more than non-reasoning models. **Benchmark actual costs** from usage.

Reasoning is a cheap way to buy accuracy. Just don’t forget you’re paying for it.

Also: **beware default settings**! Explicit is better than implicit.

[LinkedIn](https://www.linkedin.com/posts/sanand0_yesterday-i-discovered-how-much-reasoning-activity-7380798995851509760-y-Eg)
