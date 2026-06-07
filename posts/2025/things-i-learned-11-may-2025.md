---
title: Things I Learned - 11 May 2025
date: 2025-05-11T00:00:00+00:00
categories:
  - til
description: I discovered how double-checking LLM outputs can slash error rates and compared Anthropic's new search tool pricing. I also found snapdom for element capture, explored Gemini's prompt caching, and documented some prompt evaluation frameworks.
keywords: [snapdom, gemini api, anthropic, prompt engineering, llm evals, microservices, web search api]
---

This week, I learned:

- [snapdom](https://github.com/zumerlab/snapdom) is a fast, light, element capture alternative to [html2canvas](https://html2canvas.hertzen.com/) but doesn't work well with non-CORS images or iframes.
- [Sli.dev](https://sli.dev/) is a Markdown slide language. Similar to [Marp](https://marp.app/)
- Don't split your code into microservices until you need to scale. [Ref](https://nexo.sh/posts/microservices-for-startups/)
- Vibe coding is like getting others' code to work, which is exactly what most devs do. [Simon Willison](https://simonwillison.net/2025/May/8/ashley-willis/) #ai-coding
- Tofu Yakitori is a Japanese dish. It's like a dhokla. Marinated tofu cubes brushed with that sweet‑savory tare (soy, mirin, sake, a hint of sugar), then grilled until caramel‑charred. One of the better (tasty + different) dishes I've had recently. I used [ChatGPT](https://chatgpt.com/share/681d880f-5860-800c-ab21-68c07a25277a) to remind me of the dish name.
- Trust, attitudes and use of artificial intelligence surveyed ~1,000 people across 47 countries on their views on AI. [PDF](https://mbs.edu/-/media/PDF/Research/Trust_in_AI_Report.pdf)
  - Emerging economies trust and use AI more. It's an opportunity to leapfrog.
  - 26% of students use AI daily (vs 17% employees). Efficiency is the main benefit.
- Gemini APIs now have automatic caching for 75% cost reduction if message is >1K (Flash) or >2K (Pro) tokens. [Ref](https://ai.google.dev/gemini-api/docs/caching)
- YOLO is much better than Gemini at object detection. Use for pro-processing. [Ref](https://github.com/prudhvi1709/yolovsgemini)
- Using `[[n]]` is probably the best citation format for inline search references in RAG. [ChatGPT](https://chatgpt.com/share/681ca8c8-0570-800c-bd96-6b1970e98a36)
- ⭐ Double-checking is surprisingly efficient since LLM hallucinations are mostly uncorrelated. LLMs perform human tasks (e.g. classifying customer support messages) at ~85% accuracy. This might be unacceptable. But by asking 2 moderately correlated LLMs and double-checking discrepancies, we reduce automation by ~20% but reduce errors to 0.25%. Triple-checking reduces automation by ~25% but errors to under ~0.01%! [Ref](https://sanand0.github.io/llmevals/double-checking/)
- Anthropic introduces [web search in the API](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool) at $10 / 1K searches. Here's how it compares:
  - $0.1: [DuckDuckGo Search API (RapidAPI)](https://rapidapi.com/apiriot/api/duckduckgo-search-api/pricing) (monthly pricing)
  - $3: [Brave Search API](https://brave.com/blog/search-api-launch/)
  - $5: [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/overview)
  - $15: [SerpAPI](https://serpapi.com/pricing)
  - $10: [Zenserp](https://zenserp.com/serp-api-alternative)
  - $10: [Anthropic Web Search Tool](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool)
  - $25: [Bing Search API](https://www.microsoft.com/en-us/bing/apis/pricing)
  - $35: [Gemini API](https://ai.google.com/gemini-api/docs/pricing)
  - $35: [OpenAI API](https://openai.com/api/pricing)
- India attacked Pakistan!
- ⭐ When writing notes, summarize at the end of the day the learnings and next steps.
- GitHub does not let you control the cache duration, but there are many creative workarounds. [ChatGPT](https://chatgpt.com/share/6819df70-4310-800c-acdc-5b743e1cde31)
  - HTML meta tags: `<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">`
  - Use a [service worker](https://github.com/gzuidhof/coi-serviceworker) ([blog](https://dev.to/stefnotch/enabling-coop-coep-without-touching-the-server-2d3n))
  - Proxy through a CDN. Cloudflare, Netlify
  - Move to another static host: S3 + CloudFront, Heroku, Vercel, Surge, Firebase Hosting
- Notes from the [PromptEvals paper](https://arxiv.org/abs/2504.14738):
  - Good evals must be:
    - Objectively MEASURABLE (even if by an LLM). Otherwise, we won't know if it's right.
    - Directly RELEVANT to the input/prompt. Otherwise, we're not evaluating the input.
  - Typical evals fall into 6 categories
    - Structured output: Adhere to a schema (Markdown, HTML, DSL, JSON + Schema)
    - Multiple choice
    - Length constraints: N characters, words, sentences, list items, etc.
    - Semantic constraints: Exclude terms, topic relevance, follow grammar, etc.
    - Stylistic constraints: Style, tone, persona
    - Prevent hallucinations: Factual accuracy. Instruction following
