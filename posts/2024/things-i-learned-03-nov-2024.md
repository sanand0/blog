---
title: Things I Learned - 03 Nov 2024
date: 2024-11-03T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- Indian companies with 30+ employees MUST have 2.5%-15% of their employees as apprentices. [Ref](https://chatgpt.com/share/67249206-3be0-800c-a2c3-d1dab166f180)
- [Textnow](https://www.textnow.com/) and [TextFree](https://textfree.us/) provides a free phone number (like a virtual SIM). (But TextFree has more ads.) Keep using to avoid deactivation. No guarantee of retaining the number.
  - Some banks don't accept TextNow for verification SMS. But voice call is OK.
  - [Tello](https://www.tello.com/), [Red pocket](https://www.redpocket.com/) are cheap MVNOs with $5/month voice plans.
  - [Metro by T-Mobile](https://www.metrobyt-mobile.com/) and [Cricket](cricketwireless.com) are other MVNOs.
  - [MintMobile](https://mintmobile.com/) and [US Mobile](https://usmobile.com/) have $15/month and $8/month data plans.
- The scientific discoveries that might have remained undiscovered for long if not for their discoverers [Ref](https://chatgpt.com/share/6722ec5e-56b8-800c-b869-3c09f10ad685)
  - Newton's discovery of the universal law of gravitation
  - Einstein's discovery of General Relativity
  - McClintock's discovery of Transposable Elements: genes that can turn physical characteristics on and off
  - Mullis' invention of the PCR that makes billions of DNA copies rapidly
- [VibeCheck](https://arxiv.org/abs/2410.12851) can predict a model based on its vibes 80% of the time.
- [/llms.txt](https://www.answer.ai/posts/2024-09-03-llmstxt.html) is a proposal to standardize `/llms.txt` files as a way to share LLM prompts.
  - [Jina AI Meta Prompt](https://docs.jina.ai/) is an example
  - [Remotion system prompt](https://www.remotion.dev/docs/system-prompt) is an example
  - <https://docs.fastht.ml/llms-ctx.txt>
  - <https://docs.fastht.ml/llms-ctx-full.txt>
- [structuredClone](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone) deep clones objects in JS
- [F5-TTS](https://github.com/SWivid/F5-TTS) clones voices with just 15-second samples.
- Rust has crazy low memory usage too. Spawning thousands of child processes is common and OK these days. [Ref](https://github.com/pretzelhammer/rust-blog/blob/master/posts/rust-in-non-rust-servers.md)
- SetInterval is a good idea in cyborg scraping. [Ref](https://til.simonwillison.net/twitter/collecting-replies)
- GH CLI is quite good for deployment too, like Wrangler CLI. Enabling pages, setting secrets, etc.
- Restic is a CLI backup tool. Just like git. Works well with rclone.
- [NotebookLlama](https://github.com/meta-llama/llama-recipes/tree/main/recipes/quickstart/NotebookLlama) is an open source podcast generator like NotebookLM
- Pragmatic Podcast (I forgot which one)
  - Automate changelogs for your codebases. Convert past commits into attractive release notes automatically
  - AI is going to be the consumer of many tools and logs. Build converters for these
  - Speed of validation such as linting, testing, etc. will allow LLMs to iterate faster and WILL become more important
- Via Soumya Ranjan
  - Vision embedding is useful in agile modeling
  - Vision embedding models with SAM, Grounding Dino by meta, Alibaba does good stuff
  - Vision embedding is more useful in batch than real time
  - Embedding subtraction with vision embedding models like Dino
- AI code editors are not good with large code bases today. Keep the refactoring exercises to below 1000 lines. Also evaluate the ease of setting it up locally
- Deepseek Janus is a 1.3b model that can generate both text AND images (and also supports vision)
- [Cohere Multimodal Embed v3](https://cohere.com/blog/multimodal-embed-3) is available on Azure.
- Elevenlabs lets you create voices with a prompt. No need to even clone one!
- Runway Act One creates expressive character performances
