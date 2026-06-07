---
title: Things I Learned - 28 Jan 2024
date: 2024-01-28T00:00:00+00:00
categories:
  - til
description: I investigated OpenAI's tactics for system prompt compression and recursive book summarization. I also explored llm-guard for output validation and compared using Google Docs versus email for facilitating collaborative commentary on long-form essays.
keywords: [openai, prompt engineering, recursive summarization, llm-guard, google docs, content validation]
---

This week, I learned:

- ⭐ [OpenAI's prompt engineering strategies](https://platform.openai.com/docs/guides/prompt-engineering/strategy-split-complex-tasks-into-simpler-subtasks) are an excellent start for prompt engineering. A few lessons:
  - Use detailed system prompts, often containing the entire instruction set, if it won't change over the course of a conversation.
  - "... summary of the prior conversation could be included as part of the system message" is an interesting history compression tactic.
- [OpenAI summarizes books](https://openai.com/research/summarizing-books) by recursively summarizing sections and maintaining a running commentary of the summary so far.
- Dan sends Google documents with essays instead of emails. This allows people to comment on it. But commenting is a culture and not many people do it. Adriano does it a lot and we'll. Dan and Adriano actively converse on GitHub issues
- [llm-guard](https://llm-guard.com/) is an LLM content validation tool.
