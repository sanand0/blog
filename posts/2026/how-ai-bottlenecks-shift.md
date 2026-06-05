---
title: How AI bottlenecks shift
date: 2026-06-05T13:59:11+08:00
categories:
  - llms
---

![](https://files.s-anand.net/images/2026-06-05-how-ai-bottlenecks-shift.avif)

I wrote about [my changing AI opinions](https://www.s-anand.net/blog/my-changing-ai-opinions/). At least some of this is because the industry is moving so fast that the bottlenecks keep shifting.

Here are four examples of how we AI couldn't do something (the bottleneck), but that became possible, and the bottleneck shifted - changing the way we work.

It's good to keep this in mind when thinking about AI.

**Coding**:

1. _"It can't write useful code. We can't get real help."_
   - But in [Sep 2022: GitHub finds Copilot developers are 55% faster](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/).
2. _"It writes code but doesn't know our codebase. We can't let it touch real projects."_
   - But in [Feb 2024: Gemini 1.5 Pro has 1M-token context ~ 30K LOC"](https://cloud.google.com/blog/products/ai-machine-learning/gemini-on-vertex-ai-expands). Cursor indexes code.
3. _"It understands the repo but can't ship a fix on its own. We can't hand it a whole issue."_
   - But in [Mar 2024: Devin solves 14% of SWE-bench - up from 2%.](https://cognition.ai/blog/introducing-devin). Verified SWE-Bench is now 70%+.
4. _"It ships fixes, but we can't review them fast enough or trust they're stable."_
   - [Oct 2024: DORA 2024 finds AI hurt both throughput and stability](https://dora.dev/research/2024/dora-report/).
   - **Now**: [Sep 2025: DORA 2025 finds is positive but stability stayed negative](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report).
   - **Now**: [Jul 2025: METR's RCT finds _experienced_ devs 19% slower](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/).

**Agents**

1. _"It does one step. We can't chain actions."_
   - But [Jun 2023: OpenAI function calling lets models invoke tools and return structured calls](https://openai.com/index/function-calling-and-other-api-updates/).
2. _"Every integration is bespoke. We can't connect it to all our systems."_
   - But [Nov 2024: Anthropic open-sources MCP, standardizing tool and data access](https://www.anthropic.com/news/model-context-protocol).
3. _"It can act and connect, but over a long task its errors compound. We can't trust a 20-step run."_
   - **Now**: [Mar 2025: METR finds autonomous task horizon doubling ~every 7 months. Reliability is a challenge](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/).
   - But Claude Mythos, with a ~16 hour reliable execution, might fix this.

**Enterprise knowledge work**

1. _"It only knows the public internet. We can't use it on our own documents."_
   - But [Sep 2023: Morgan Stanley's assistant uses ~100K internal documents](https://openai.com/index/morgan-stanley/).
2. _"It reads our documents but can't fit enough of them. We can't ask across the whole corpus."_
   - But [May 2023: Claude's 100K-token context](https://www.anthropic.com/news/100k-context-windows) and [Feb 2024: Gemini 1.5's 1M tokens](https://cloud.google.com/blog/products/ai-machine-learning/gemini-on-vertex-ai-expands) reduce chunking needs.
3. _"It runs on our data, but we can't trust it without a way to measure when it's silently wrong."_
   - **Now**: [the Morgan Stanley deployment relies on an eval framework](https://openai.com/index/morgan-stanley/) - evals are the bottleneck.

**Document processing**

1. _"It needs thousands of labeled samples. We can't stand up new doc types quickly."_
   - But [Sep 2023: Google Document AI extracts with limited-to-no ML training](https://cloud.google.com/blog/products/ai-machine-learning/mobilize-your-unstructured-data-with-generative-ai).
2. _"It learns fast but reads only text. We can't handle scans, charts, and tables."_
   - But [Sep 2023: GPT-4V](https://openai.com/index/chatgpt-can-now-see-hear-and-speak/) vision model and [May 2024: GPT-4o native multimodal](https://openai.com/index/hello-gpt-4o/) solved this.
3. _"It sees the page but can't understand long, layout-heavy documents. We can't trust it on real multi-page files."_
   - **Now**: [NeurIPS 2024: on MMLongBench-Doc, GPT-4o scored under ~50 on multi-page chart/table documents](https://arxiv.org/abs/2407.01523).
   - But Gemini 3.5 Flash, GPT 5.5, Claude 4.8 Opus, etc. have excellent vision and need to be tested.

<!-- https://claude.ai/chat/91d588c8-29d4-4b9d-bc3f-b4bd2e37d281 -->
