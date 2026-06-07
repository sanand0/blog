---
title: Things I Learned - 25 Aug 2024
date: 2024-08-25T00:00:00+00:00
categories:
  - til
description: I discovered Hermes 3's special reasoning tokens, Lumentis for transcript documentation, and the 27% reuse threshold for Anthropic’s prompt caching. I also noted that LLMs write better code in Markdown than JSON and explored Copilot's system prompt.
keywords: [hermes 3, prompt caching, anthropic, lumentis, cursor.ai, copilot, karya.in]
---

This week, I learned:

- [Karya.in](https://karya.in/) is creating high quality datasets. Suhel mentioned them
- [An 8-year old uses Cursor.ai to code](https://x.com/rickyrobinett/status/1825581674870055189)
- [Hermes 3 has special tokens](https://www.arxiv.org/pdf/2408.11857) like `<SCRATCHPAD>, <RESTATEMENT>, <THOUGHT_*>, <PYDANTIC_SCHEMAS>, <SCHEMA_*>, <REASONING>, <INNER_MONOLOGUE>, <PLAN>, <EXECUTION>, <REFLECTION>, <THINKING>, <SOLUTION>, <EXPLANATION>, <UNIT_TEST>`, etc. This extends the capability dramatically.
- [Lumentis](https://github.com/hrishioa/lumentis) creates docs from transcripts and text
- [LLMs write worse code in JSON than Markdown](https://aider.chat/2024/08/14/code-in-json.html)
- [Copilot's system prompt](https://labs.zenity.io/p/stealing-copilots-system-prompt) calls a `search_enterprise(query: str)` tool and a `hint(M365Copilot_language: str)` tool as assistants.
- [Anthropic Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) is 90% cheaper to use and 25% costlier to create. So if there's a 27% chance it'll be re-used, cache it.
