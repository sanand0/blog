---
title: Local context repositories for AI
date: 2026-03-20T07:12:47+05:30
categories:
  - llms
  - how-i-do-things
description: AI agents become much more useful when they can access curated personal context repositories, because better local context leads to better idea selection and recommendations.
tags: [context-engineering, ai-agents, developer-workflow]
---

When people ask me for connections, I share my [LinkedIn data](https://www.linkedin.com/mypreferences/d/download-my-data) and ask them to pick.

This week, three people asked for AI ideas. I shared my local content with AI coding agents and asked them to pick.

![](https://files.s-anand.net/images/2026-03-20-local-context-repositories-for-ai.avif) <!-- https://gemini.google.com/u/2/app/b90eaeb839f3e493 -->

**STEP 1: Give access to content**. I use a [Dockerfile](https://github.com/sanand0/scripts/blob/7e1dc00d7e1fa36a9949a1e061c1b529928cc175/dev.dockerfile) and [script](https://github.com/sanand0/scripts/blob/7e1dc00d7e1fa36a9949a1e061c1b529928cc175/dev.sh) to isolate coding agents. To give access, I run:

```bash
dev.sh -v /home/sanand/code/blog/:/home/sanand/code/blog/:ro \
       -v /home/sanand/code/til:/home/sanand/code/til:ro \
       -v /home/sanand/Dropbox/notes/transcripts:/home/sanand/Dropbox/notes/transcripts:ro
```

This gives read-only access to my blog, things I learned, transcripts, and I can add more. (My transcripts are private, the rest are public.)

**STEP 2: Ask agents to scan content**. For [example](https://github.com/sanand0/talks/blob/c45b0e272708f82be50a1c48f10791bd0fee8e46/2026-03-18-iitm-office-of-institutional-advancement/prompts.md), I ask it to read:

> - Required blog posts related to LLMs `/home/sanand/code/blog/` (especially with the category `llms`)
> - Other relevant transcripts `/home/sanand/Dropbox/notes/transcripts` (especially extracted AI advice at `/home/sanand/Dropbox/notes/transcripts/extracts/ai/`)
> - Things I learnt at `/home/sanand/code/til/`

This makes it explicitly aware of the content and can use it to answer questions.

**STEP 3: Help it do better**. I often add "Use sub-agents as required", which reduces the context and lets them run more in parallel. I also point them to [post-mortems](https://github.com/sanand0/talks/blob/c45b0e272708f82be50a1c48f10791bd0fee8e46/2026-03-18-iitm-academic-council/ideas-post-mortem.md) for tips on scanning content effectively.

**STEP 4: Output as JSON**. JSON lets me write programs to convert to multiple other formats (e.g. HTML, markdown). I specify the fields I want, how I want them filled, and leave the rest to the agent. [Sample output](https://github.com/sanand0/talks/blob/c45b0e272708f82be50a1c48f10791bd0fee8e46/2026-03-18-iitm-academic-council/ideas/ideas.json).

---

This is not a new technique. It's just context engineering, roughly like:

- Connecting ChatGPT/Claude/Gemini/ to Dropbox/Google Drive/... and asking it to read the content.
- Enabling web search and asking them to search online.

But I can do this (kind of) safely on my local content and I can also teach it how to scan the content - which is a useful learning.

Next steps:

1. Add README.md to each directory on how to scan the content effectively.
2. Think about what content repositories I should add
3. Explore _combining_ content repositories cleverly (e.g. "Read my blog and apply lessons to my code.")
