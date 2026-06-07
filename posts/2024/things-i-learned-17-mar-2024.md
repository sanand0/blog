---
title: Things I Learned - 17 Mar 2024
date: 2024-03-17T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- DuckDB is 2-10 times faster than Pandas. ClickHouse is supposedly faster but doesn't run on Windows.
- [Claude 3 Haiku input costs is $0.25/MTok](https://www.anthropic.com/api). That's half the GPT-3.5 cost. If it's of comparable quality, it's worth switching.
  But [Claude 3 Opus is comparable to GPT-4](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard) and twice the cost, so not worth it.
- [Tavily is a search API for LLMs](https://docs.tavily.com/docs/tavily-api/introduction)
- Interesting [model garden models](https://console.cloud.google.com/vertex-ai/model-garden)
- There are sites you TRULY cannot scrape even in the browser because of the `isTrusted` read-only property of events that you can never set to true. Oracle Service Cloud checks for isTrusted in mouse actions.
