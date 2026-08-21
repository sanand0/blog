---
title: When LLM prices fall 10x every year
date: '2026-02-20T09:25:45+08:00'
description: 'I explore what happens if LLM prices keep falling 10x every 11-12 months: within two years, models could be 100x cheaper, enabling faster, more reliable automated coding workflows.'
tags: [forecasting, llm-pricing, ai-coding, ai-workflows]
---

<!--
https://claude.ai/chat/f0070b78-0653-4172-9906-b6b96b8986dc
https://gemini.google.com/app/939d6b2d87fbe085
https://chatgpt.com/c/6997b88f-f754-83a4-9fa6-362f56c0c3d4
-->

In Feb 2024, Claude 3 Opus was the best model, at $15/MTok.\
In Jul 2024, GPT 4o Mini reached that quality at 10% of the price.\
In Dec 2024, DeepSeek v3 reached that quality at 1% of the price.

<video width="1337" height="724" style="max-width: 100%; height: auto;" controls autoplay loop muted>
  <source src="https://files.s-anand.net/images/2026-02-20-llm-pricing.webm" type="video/webm">
  <a href="https://files.s-anand.net/images/2026-02-20-llm-pricing.webm">Video</a>
</video>

[See the interactive version](https://sanand0.github.io/llmpricing/)

If the price continues to fall 10x every 11-12 months or so (and [it](https://claude.ai/share/dd426a79-1bfe-4a5c-94d1-ffc407de6040) [has](https://gemini.google.com/share/6c55131f1dcd) [been](https://chatgpt.com/share/6997ba52-ff64-8003-aa43-7e8d12818c66)), then in a year, a Claude 4.6 Opus like model will cost 1/10th of the $5/MTok today, and in 2 years, 1/100th of that.

(We'll be using better models, of course.)

But 2 years isn't far away. If Opus 4.6 were 100x cheaper, I could do 100x of what I could do with it today. What would we do with it?

If we assume that they'll become 100x _faster_ as well (and that's an important assumption), and the reliability will continue to improve, then:

- **LLM LSPs**. _Language servers_ could be LLMs. Hover over a squiggly line to understand a bug it spotted, right click and fix. Move on.
- **LLM pre-commit hooks**. Write docs, write and run tests, refactor - automatically before you commit.
- **Continous refactoring**. LLMs auto-refactor the code, run tests, and commit better code.
- **Auto-fix from logs**. Log analysis -> Test case -> Fix -> Deployment can be automated.
- **Pick best option**. LLMs generate 30 diverse options for each task, test all, and pick the best. E.g. What's the best language / framework for this? What's the better visual design? What should I build?
- **Live docs**. LLMs auto-update docs every commit.
- **Adversarial workflows**. LLMs continously run adversarial test cases to break the code, and fix it.
- **Build & discard, don't buy**. Most tools are easier to create than purchase. They're also easier to throw away. To hell with code quality!
