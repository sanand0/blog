---
title: Protyping the prototypes
date: '2026-03-10T12:17:47+08:00'
categories:
- llms
description: Prototype iterations should improve not just the interface but the narrative around it, because better storytelling can make exploratory tools far more understandable and useful.
tags: [prototyping, data-stories, vibe-coding, data-visualization]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7437312601035927552/
---

I added a narrative story to my [LLM Pricing chart](https://sanand0.github.io/llmpricing/). That makes it easier for me _and_ others to tell the story of AI's evolution in the last three years.

<video controls autoplay loop muted playsinline preload="metadata" width="1400" height="800" style="max-width: 100%; height: auto;">
  <source src="https://files.s-anand.net/images/2026-03-10-llmpricing-screencast-crf55-fps5.webm" type="video/webm">
  <a href="https://files.s-anand.net/images/2026-03-10-llmpricing-screencast-crf55-fps5.webm">Video</a>
</video>

It was vibe-coded over two iterations.

In [the first version](https://github.com/sanand0/llmpricing/blob/467474abd9ebdb3051ba016ddc95bfed7da556c6/prompt.md#scrolly-v1), I prompted it to:

> Add a scrollytelling narrative. So, when users first visit the page, they see roughly the same thing as now (but prettier). As they scroll down, the page should smoothly move to the earliest month, and then animate month by month on scroll, and explaining the key events and insights in terms of model quality and pricing. Use the data story skill to do this effectively, narrating like Malcolm Gladwell, with the visual style of The New York Times, using the education progression as a framework for measure of intelligence (read prompts.md for context). Store the narrative text in a separate JSON file and read from it. This should control the entire narrative, including what month to jump to next, what models to highlight, what insights to share, and so on.

But there were two problems:

1. **Conflicting instructions**. "... with the visual style of The New York Times" conflicted with my current style.
2. **Incomplete instructions**. I wanted to begin with the exploration, not the narrative. I wanted to explain the axes first. I wanted smaller cards.

Both of them were solved in the [second version](https://github.com/sanand0/llmpricing/blob/467474abd9ebdb3051ba016ddc95bfed7da556c6/prompt.md#scrolly-v2), because this time, _I knew what I wanted_.

In other words, vibe coding isn't just helping me prototype, it's helping me prototype the prototype! Even if I don't know what I want, I can just ask for something and build on it.

This is a known benefit of lower costs. But, like the placebo effect and Hofstadter's Law, I'm surprised by it even when I know it.

---

An aside: Here's the [narrative](https://github.com/sanand0/llmpricing/blob/467474abd9ebdb3051ba016ddc95bfed7da556c6/narrative.json) it crafted:

- **How to read this chart**: The vertical axis is intelligence — mapped to the academic ladder on the right. Elo 1100 is high school freshman; Elo 1480 is tenured professor. The horizontal axis is cost: one million input tokens — roughly the entire King James Bible — priced from two cents to $75. **The upper-left corner is the dream: brilliant and cheap.** This is the story of how the world got there.
- **March 2023 — Year Zero**: March 2023. The entire AI landscape fits in a small cluster near the bottom of the chart. GPT-3.5 and Claude 1 are the state of the art — high-school-to-college-freshman intelligence that writes a fluent paragraph, then confidently invents a fact. Processing the King James Bible costs 50 cents to $8. These models can hold a conversation. **They cannot, reliably, hold an argument.** [LMSYS Chatbot Arena launches (May 2023)](https://lmsys.org/blog/2023-05-03-arena/)
- **November 2023 — The Leap**: November 6, 2023: GPT-4 Turbo. The chart jolts upward. Elo 1313 — college-junior level: coherent research papers, complex reasoning, output worth reading. **Price: $10 per million tokens** — about $14 to process all seven Harry Potter novels. Expensive, but for the first time the intelligence felt worth it. Enterprises stopped asking whether AI could help. They started asking how much they were willing to pay. [OpenAI DevDay announcement](https://openai.com/blog/new-models-and-developer-products-announced-at-devday)
- **February 2024 — The Split**: Early 2024: Anthropic launches Claude 3 in three tiers. Opus and Sonnet arrive February 29; Haiku a week later, March 7. Opus: entry-analyst capability at $15. Sonnet: similar quality at $3. Haiku: college-junior reasoning at $0.25. **A 60× price spread — same company, same training philosophy.** The intelligence market had learned to stratify, and every business began thinking in tiers. [Anthropic Claude 3 announcement](https://www.anthropic.com/news/claude-3-family)
- **June 2024 — The Summer Pivot**: June 2024 bent the economics permanently. Claude 3.5 Sonnet — strong manager level (Elo 1342) — arrived at $3 per million tokens: five times cheaper than Opus, four months later, at better quality. Meta’s Llama 3.1 405B matched it at $2, or free if self-hosted. Any CFO paying $15 for frontier AI could now pay $3. **The question changed from “can we afford AI?” to “what are we waiting for?”** [Claude 3.5 Sonnet launch](https://www.anthropic.com/news/claude-3-5-sonnet), [Meta releases Llama 3.1](https://ai.meta.com/blog/meta-llama-3-1/)
- **September 2024 — The Thinking Machine**: September 2024: OpenAI o1. It didn’t just answer — it reasoned. Before responding, it ran an internal monologue: checking its own logic, catching its own errors. **Elo 1388 — the biggest single-model quality jump since GPT-4.** It scored at or above PhD-expert level on GPQA Diamond, a benchmark of graduate-level science questions. Price: $15. For the first time, AI felt less like autocomplete and more like a colleague you’d genuinely consult. [OpenAI o1 system card](https://openai.com/index/openai-o1-system-card/), [GPQA Diamond benchmark results](https://arxiv.org/abs/2311.12022)
- **January 2025 — The Earthquake**: January 20, 2025. DeepSeek R1 matched o1-level reasoning (Elo 1398) at $0.55 per million tokens — **a 27× discount.** The announcement wiped $600 billion from Nvidia’s market cap in a single day. Silicon Valley assumed expensive compute was a moat. DeepSeek proved it was just a starting point. PhD-approaching reasoning for fifty-five cents per Bible. [Reuters: DeepSeek wipes $600B from Nvidia](https://www.reuters.com/technology/chinas-deepseek-sets-off-ai-market-rout-2025-01-27/), [DeepSeek R1 technical report](https://arxiv.org/abs/2501.12948)
- **Mid-2025 — The Race to the Top-Left**: By mid-2025, the upper-left corner was filling fast. Gemini 2.5 Pro delivered tenured-professor intelligence (Elo 1476) at $1.25 per million tokens. Flash models handled most enterprise work for 30 cents. Companies that had rationed AI to critical workflows were now running it everywhere. **The constraint was no longer cost or capability — it was imagination.** [Google Gemini 2.5 Pro launch](https://blog.google/technology/google-deepmind/gemini-model-updates-february-2025/)
- **February 2026 — Polymath Scholar**: The top models in early 2026 score above 1500 Elo — polymath scholar territory. A 1500-rated model beats a 1300-rated one in 76% of head-to-head matchups. GPT-4 Turbo launched at college-junior level (Elo 1313) in November 2023. Twenty-seven months later, Claude Opus 4.6 and Gemini 3.1 Pro sit at 1500+. **What cost $15 in 2024 is now beaten by models at one-seventh the price.** [LMArena Leaderboard](https://lmarena.ai/leaderboard)
- **So What Does This Mean?**: In 2023, reaching master’s-level AI for 100 analysts meant paying $30/MTok — roughly $135,000 a month. By 2026, models with higher capability cost $1–5/MTok: under $15,000 for better results. For most tasks — analysis, drafting, coding, research — models in the $1–3 range deliver more than enough. Save frontier models for your hardest problems. **The question is no longer what AI costs. It’s what you would build if intelligence cost a dime per Bible.** [McKinsey: The economic potential of generative AI](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai), [Sequoia: AI's $600B question](https://www.sequoiacap.com/article/ais-600b-question/)

---

Self-referentially, my answer to its last question: "what you would build if intelligence cost a dime per Bible" is "a scrollytelling narrative about intellegince costing a dime per Bible".

![](https://files.s-anand.net/images/2026-03-10-prototyping-the-prototypes.avif) <!-- https://gemini.google.com/u/2/app/6b7cf5190d354c87 -->
