---
title: LLM Model Cost Capability Strategy
date: 2026-08-01T09:43:46+08:00
categories:
    - llms
---

I track the cost vs capability of LLMs at [LLM Pricing](https://sanand0.github.io/llmpricing/) - the rough cost to read all Harry Potters (~1M tokens) vs the intelligence level on the [LMSYS Leaderboard](https://lmarena.ai/) - over time.

<div style="width: 100vw; margin-left: calc(50% - 50vw); width: min(100vw, 100rem); margin-left: calc(50% - min(50vw, 50rem)); margin-top: 1.5rem; margin-bottom: 2rem;">
  <iframe src="https://sanand0.github.io/llmpricing/" title="LLM Pricing" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="display: block; width: 100%; height: 820px; height: min(56rem, 92svh); border: 0; background: #f5f1e6;"></iframe>
</div>

Here's what the models' strategy evolution looks like.

Claude started at the mid-to-high end of the cost-capability frontier. Over time, they decided to specialize in the high-end, which they're doing well on.

<video controls autoplay loop muted playsinline preload="metadata" width="1600" height="1200" style="max-width: 100%; height: auto;">
  <source src="https://files.s-anand.net/images/2026-08-01-llmpricing-claude.webm" type="video/webm">
  <a href="https://files.s-anand.net/images/2026-08-01-llmpricing-claude.webm">Claude Cost-Capability Evolution</a>
</video>

Gemini began in the middle and rapidly pushed the low-end of the frontier. But now, it's focusing on the mid-end, which they're doing well on.

<video controls autoplay loop muted playsinline preload="metadata" width="1600" height="1200" style="max-width: 100%; height: auto;">
  <source src="https://files.s-anand.net/images/2026-08-01-llmpricing-gemini.webm" type="video/webm">
  <a href="https://files.s-anand.net/images/2026-08-01-llmpricing-gemini.webm">Gemini Cost-Capability Evolution</a>
</video>

OpenAI has always had models that cover the entire spectrum and the widest range. But currently, they don't lead the frontier at any end.

<video controls autoplay loop muted playsinline preload="metadata" width="1600" height="1200" style="max-width: 100%; height: auto;">
  <source src="https://files.s-anand.net/images/2026-08-01-llmpricing-gpt.webm" type="video/webm">
  <a href="https://files.s-anand.net/images/2026-08-01-llmpricing-gpt.webm">GPT Cost-Capability Evolution</a>
</video>

[Fable 5](https://claude.ai/share/6fab32f4-dbfb-491b-9c1d-3144778bb231) and [GPT 5.6 Sol](https://chatgpt.com/share/6a6d5143-a278-83ec-89f1-0d8276e7b52e) helped me with the analysis based on [this data](https://sanand0.github.io/llmpricing/elo.csv).

<!-- https://claude.ai/chat/acf12a02-4870-42e9-9d6b-a15c3ecffa95 + https://chatgpt.com/c/6a6d4cae-d588-83ec-a221-bfa047b752e0 -->
