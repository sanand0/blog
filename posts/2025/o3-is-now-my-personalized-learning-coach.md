---
title: O3 Is Now My Personalized Learning Coach
date: "2025-04-20T12:10:53Z"
lastmod: "2025-04-22T02:21:59Z"
categories:
  - education
  - llms
wp_id: 4056
---

![O3 Is Now My Personalized Learning Coach](/blog/assets/ChatGPT-Image-Apr-20-2025-08_04_27-PM.webp)

I use [Deep Research](https://openai.com/index/introducing-deep-research/) to explore topics. For example:

- [Text To Speech Engines](https://chatgpt.com/share/67b63db0-8720-800c-87c6-f0b42581d801). Tortoise TTS leads the open source TTS.
- [Open-Source HTTP Servers](https://chatgpt.com/share/67bafb23-cf14-800c-9b76-65f11285ae3a). Caddy wins.
- [Public API-Based Data Storage Options](https://chatgpt.com/share/67c7edad-bd78-800c-80a7-ed08dd97c1cf). Supabase wins.
- etc.

But these reports are **very** long. With [O3 and O4 Mini](https://openai.com/index/introducing-o3-and-o4-mini/) supporting thinking **with** search, we can do **quick research**, instead of **deep research**. One minute, not ten. One page, not ten.

For example, [I asked O3](https://chatgpt.com/share/6804c7ab-db2c-800c-8525-c11003f54513) to automate my weekly tech learning process:

> From the links at https://www.hntoplinks.com/week pick those that would be of interest to me.\
> Read the articles and explain the key insights -- what's non-obvious and how can I use it.\
> When sharing how I can use it, research alternate approaches and suggest which approach is best.

This brings two new capabilties I **love**.

**Memory**. I said, "**… that would be of interest to me**". Given my past chats and context, it **really** knows me. For example, the reasoning trace shows:

> I'm narrowing down the list for Anand, focusing on his interests like generative AI, open-source tools, and minimal libraries.

That's **exactly** right!

**Long reasoning**. It reads **each** site step by step, unsupervised. Here's a brief reasoning trace:

> [Searched the web](https://filiph.github.io/unsure/)\
> Got the Unsure Calculator article. Now, onto the next one: the Hackable AI assistant with SQLite cron jobs. I'll open it and dive into the details. I think this will be a great fit for Anand, considering the focus on AI tools and development. It should provide some interesting insights!\
> [Searched the web](https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs)\
> Now that we've moved through a couple of articles, it's time to tackle the Gemini 2.5 Flash AI model. I think this one will be particularly interesting for exploring advancements in AI. Let me grab it and dive into the details so I can distill the insights into something relevant.\
> [Searched the web](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/)\
> Next up: I'll open the OpenAI blog article on GPT-4.1 in API. This could bring in some cool technical\
> …

The result is fantastic. While on a trouser shopping trip, I learnt more than when I browse [Hacker News](https://news.ycombinator.com/):

- ["Unsure"](https://filiph.github.io/unsure/) is a tool to calculate **uncertainty** formulas, like the [uncertainties](https://pythonhosted.org/uncertainties/) Python package.
- [Responses API](https://platform.openai.com/docs/api-reference/responses) adds features like linkable history, mid‑chat truncation, flexible reasoning detail, and more.
- [Augment Code](https://www.augmentcode.com/) is an AI code editor that's growing popular on Reddit.
- GPT 4.1's 75% discounted prompt caching (instead of 50%) gives them an edge on repetitive tasks. [OpenAI](https://openai.com/index/gpt-4-1/)
- [Nix flakes](https://wiki.nixos.org/wiki/Flakes) are a reliable alternative to [DevContainers](https://containers.dev/) that don't need Docker - but don't work on Windows.
- TLS certificates will expire in 47 days from 15 Mar 2020. Automated domain renewals are a must. [Digicert](https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days)
- … and a **bunch** of other things.

Here are Hacker News summaries for a month or specific days:

- [Mar 2025](https://chatgpt.com/share/6806f6e6-108c-800c-b4d6-43a3058dd247): [Mistral OCR](https://mistral.ai/news/mistral-ocr) is a dedicated OCR, not an LLM. [DuckDB UI](https://duckdb.org/2025/03/12/duckdb-ui.html) has notebooks!
- [13 Apr 2025](https://chatgpt.com/share/6806f697-500c-800c-a5e8-7d794a6536f0): Learnt about [Signalbloom](https://www.signalbloom.ai/) which automates Q1 summaries and this [MCP Primer](https://www.polarsparc.com/xhtml/MCP.html)
- [15 Apr 2025](https://chatgpt.com/share/6806fc6b-d508-800c-90d6-8d4ea5d93e6f): [12-factor agents](https://github.com/humanlayer/12-factor-agents) shares agent lessons. Send [JSX instead of JSON](https://overreacted.io/jsx-over-the-wire/). [AI as Normal Technology](https://knightcolumbia.org/content/ai-as-normal-technology).

This enables:

1. **Personalized learning**, i.e. it tells me what **I don't know**, and how **I can apply it**. This is powerful.
2. **Learning on the go**, e.g. via voice while cycling or walking.
3. **Learning from untapped sources**. This includes: GitHub repos, research papers, open data registries, patent filings, earnings transcripts, subreddits, judgements or acts, [open data repositories](https://github.com/awesomedata/awesome-public-datasets) or [collections](https://www.data-is-plural.com/), and many more.

Take GitHub as an untapped source. I [asked O3](https://chatgpt.com/share/6804c78b-b370-800c-91c5-e46d0d9f521e):

> Go through the OpenAI Codex CLI repo on GitHub.\
> Teach me innovative, new, and surprising techniques or approaches or libraries I might not know about.\
> For each, explain what is interesting, how I might use it, and how this approach contrasts with alternatives.

This was a treasure trove, too! I learn about:

- [Ink](https://github.com/vadimdemedes/ink): React for CLI!
- [Zod](https://zod.dev/): schema validation
- [Creating firewalls](https://github.com/openai/codex/blob/main/codex-cli/scripts/init_firewall.sh)
- [Fuzzy path matching](https://github.com/openai/codex/pull/190)
- … and a **bunch** of other things

I [tried O4 Mini High](https://chatgpt.com/share/6804c7e1-9b6c-800c-9ea6-5d0ab5dcbb3b) and saw similar results. I felt O3 still gave me more personalized suggestions.

Let's see [what we can learn from pull requests on Codex](https://chatgpt.com/share/6805bff8-c46c-800c-a61c-335c498d748f).

> Go through all the pull requests that have been merged into OpenAI's codecs repository on GitHub. Pick the ones that would be most interesting to me. You can group a few if they are very related and give me the top 10 most interesting PRs that would be relevant for me. Also explain why these are relevant to me, how I might use them, and any interesting details about the way in which the PRs were written.

Soon, we won't just follow a lesson plan -- we'll have lessons built just for us. AI will track how we learn and adapt in real time. It'll feel like having a personal coach in your back pocket. That future starts now.

This also opens a door to endless curiosity. There's no limit to what we can explore. Curiosity **is** the competitive advantage, now.
