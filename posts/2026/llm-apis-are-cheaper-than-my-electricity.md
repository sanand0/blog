---
title: LLM APIs are cheaper than my electricity
date: 2026-08-30T13:38:31+08:00
categories:
  - llms
---

Last week, I saw that [local agents are good but slow](https://www.s-anand.net/blog/local-agents-are-good-but-slow/).

Today, I [benchmarked](https://chatgpt.com/share/6a93c218-d264-83ec-9573-bfdf08ebe843) the speed and cost. On my NVIDIA RTX 2000 GPU, I can run [`gemma4:e4b-it-qat`](https://ollama.com/library/gemma4:e4b-it-qat) at ~60 tokens per second. That seems the best intelligence performance I can get right now.

It has an [Artificial Analysis intelligence index of ~9](https://artificialanalysis.ai/models/gemma-4-e4b-non-reasoning) without reasoning and 12 with reasoning.

So, if I run it for an hour, it'll save me the equivalent cost of about 8-12 cents in API calls.

| API model     |  Cost | AA Intelligence |
| ------------- | ----: | --------------: |
| Ministral 8B  |  8.8c |             9.0 |
| GPT-4.1 Nano  | 10.3c |             9.6 |
| Qwen3 14B     |  8.8c |            10.4 |
| Ministral 14B | 11.8c |            11.2 |
| Qwen3 32B     |  7.6c |            11.4 |

In Singapore, this costs about 2-2.5 cents per hour of electricity. So the net saving is about 6-10 cents / hour.

If I run it overnight, say for 10 hours, I can save about $0.6-$1.00 per day in API costs. Not much.

---

This reminds me of my cycle. When I bought it, I spent about S$ 350 and since my bus commute cost me ~S$3.5 daily, I would break even after ~100 days, or about half a year.

The RTX 2000 7GB, even today, costs at least $200 - so that's about at least 200 days payback. A bit worse than my cycle.

![](https://files.s-anand.net/images/2026-08-30-llm-apis-are-cheaper-than-my-electricity.avif)

---

Worse yet:

- Cloudflare hosts a better model, [gemma-4-26b-a4b-it](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/), at just $0.10 / MTok, making it cheaper than my electricity.
- OpenRouter offers [gemma-4-26b-a4b-it](https://openrouter.ai/google/gemma-4-26b-a4b-it:free) for free!

In short, I still can't find an economic reason to run the model locally.
