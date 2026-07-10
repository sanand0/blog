---
title: Things I Learned - 28 Apr 2024
date: 2024-04-28T00:00:00+00:00
categories:
  - til
description: I tested LLMs using Caesar cipher prompts, compiled a list of cheap cloud GPU services like Runpod, and learned how JSR handles package documentation. I also found that averaging embeddings is useful for processing long document inputs.
tags: [embeddings, deno]
---

This week, I learned:

- Tough prompt to test: `Gr brx vshdn Fdhvdu flskhu?` is a quick way to assess LLM capability. [Ref](https://www.s-anand.net/blog/a-quick-way-to-assess-llm-capabilities/)
- [Cheap cloud GPU services thread on Twitter](https://twitter.com/simonw/status/1780668642574897396) lists:
  - [Runpod](https://www.runpod.io/) (17)
  - [Vast.ai](https://vast.ai/) (17)
  - [Modal Labs](https://modal.com/) (8)
  - [fly.io](https://fly.io/) (4)
  - [LightningAI](https://lightning.ai/) (4)
  - [Colab](https://colab.research.google.com/) (4)
  - [AkashNet](https://akash.network/) (4)
  - [Lambda Labs](https://lambdalabs.com/) (4)
  - [ShadeFormAI](https://www.shadeform.ai/) (3)
  - [Mac Mini](https://www.apple.com/mac-mini/) (3)
  - [Tensor Dock](https://tensordock.com/) (2)
  - [Hetzner](https://www.hetzner.com/) (2)
  - [BrevDev](https://brev.dev/) (2)
- JSR lets you publish Deno packages that can be imported by npm [via](https://deno.com/blog/jsr-is-not-another-package-manager). It also auto-evaluates documentation and scores it! [via](https://jsr.io/docs/scoring)
- [Snowflake Arctic Cookbook explains how mixture of experts models work](https://medium.com/snowflake/snowflake-arctic-cookbook-series-exploring-mixture-of-experts-moe-c7d6b8f14d16)
- [A long list of LLM courses online](https://github.com/aishwaryanr/awesome-generative-ai-guide?tab=readme-ov-file#book-list-of-free-genai-courses)
- Embeddings can be averaged. So, to embed large documents, average the embeddings of their chunks! [OpenAI suggests this.](https://github.com/openai/openai-cookbook/blob/main/examples/Embedding_long_inputs.ipynb)
