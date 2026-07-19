---
description: Maintain an active regression suite in evals.json to track LLM behaviors like unnecessary reframing, excessive clarification, and lost constraints. Use these tests to prune legacy system prompt rules as newer models improve.
tags: [llm-evals, llms, prompt-engineering, ai-workflows]
---

Sources:

- 18 Jul 2027. Created. Sources:
  - https://claude.ai/chat/380bc904-86bf-4008-870a-5e718837a159
  - https://chatgpt.com/c/6a5b09e7-71b0-83ee-8fc7-2198b0396bc2

A regression set lives in evals.json: cases where you should reframe, should not, should assume and proceed, and should ask one question — tracking unnecessary reframes, cosmetic reframes, invented intent, excessive clarification, and lost constraints. When newer models pass without a line above, prune it.
