---
title: Things I Learned - 03 May 2026
date: 2026-05-03T00:00:00+00:00
categories:
  - til
description: I found LiteParse for PDF parsing and explored GPT 5.5's high pricing. I learned about eigenquestions, tracking Claude usage via local OAuth tokens, and why AI agents change which parts of organizational ontology matter most.
tags: [gpt-5-5, claude-code, prompt-engineering, llm-pricing]
---

This week, I learned:

- [LiteParse](https://github.com/run-llama/liteparse) is a PDF to text library that you can run via `npx --package=@llamaindex/liteparse lit parse document.pdf`. [Simon Willison](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/)
- Always add indecisiveness, inaction, "other", "not applicable", etc. as an option to LLMs. They are trained for decisive responses and pattern matching, so we need to guide the the other way. [Martin Fowler](https://martinfowler.com/fragments/2026-04-14.html)
- GPT 5.5 is priced _twice_ that of GPT 5.4. No wonder my Codex usage is much higher than last month. [Simon Willison](https://simonwillison.net/2026/Apr/23/gpt-5-5/#a-few-more-notes-on-gpt-5-5). I am better off sticking to `medium` effort instead of the `xhigh` I usually use - it may not be required. [OpenAI](https://developers.openai.com/api/docs/guides/latest-model)
- "... the eigenquestion is the question where, if answered, it likely answers the subsequent questions as well." [Shishir Mehrotra & Matt Hudson](https://coda.io/@shishir/eigenquestions-the-art-of-framing-problems/eigenquestions-3)
- Claude Code stores the logged in OAuth token at `~/.claude/.credentials.json`. We can use that to fetch `https://api.anthropic.com/api/oauth/usage` and retrieve Claude usage and reset times. `uvx ccusage` does this automatically, but I prefer my own script.
- Ontology matters in the AI era. But some stuff matters more, and some less. <!-- https://claude.ai/chat/2f6fdf7e-9d32-4c45-ac8d-603d029aed5b -->
  - 🟢 MORE: Definitions: what "customer" means
  - 🟢 MORE: Constraints: e.g. "don't reclassify loans"
  - 🟢 MORE: Interactions: how to verify, coordinate, delegate, ...
  - 🔴 LESS: Creating ontologies: agents can do that.
  - 🔴 LESS: Completeness and rigor: agents tolerate uncertainty.
  - 🔴 LESS: Proprietary: agents can reverse-engineer.
- There are several industries / markets that MBA case studies rarely cover ([ChatGPT](https://chatgpt.com/share/69efcf7a-6bf0-83ea-86dd-36e115e7540c)): Kirana stores; Care (child care, elder care, domestic work); Faith (finance, food, media, education); Remittances; Gambling (lottery, sports betting, gacha); Scams & organized fraud; Counterfeiting; ... <!-- https://chatgpt.com/c/69efa7bb-f918-83ea-9bc5-e3f7231c75da + https://gemini.google.com/app/dc5ac9f4a4f44cf0 -->
