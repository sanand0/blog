---
title: Things I Learned - 26 May 2024
date: 2024-05-26T00:00:00+00:00
categories:
  - til
description: I explored home networking and LLM infrastructure, discovering WiFi 6 beam-forming, Predibase's competitive pricing for fine-tuned models, RunPod's serverless vLLM endpoints for HuggingFace models, and Portkey's utility as an AI model router.
tags: [vllm]
---

This week, I learned:

- My home WiFi is on WiFi 6. This supports beam-forming which increases range by "focusing" on devices!
- [Predibase](https://predibase.com/pricing) lets you run fine-tuned models at the same price, on a per-token basis. 25c/MTok up to 21B models. That's sames as Claude 3 Haiku, but with fine-tuning.
- [RunPod's vLLM endpoint](https://docs.runpod.io/category/vllm-endpoint) lets you run any HuggingFace LLM with an OpenAI API priced on usage (serverless) not on idle time. "Autoscaling to 0".
- [Portkey](https://portkey.ai/) is an LLM router
