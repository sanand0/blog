---
title: Things I Learned - 27 Oct 2024
date: 2024-10-27T00:00:00+00:00
categories:
  - til
description: I discovered LanceDB as a scalable ChromaDB alternative and explored Meta's image models. I also tested Gemini's code execution, analyzed audio diarization limitations, and compared AI development tools like Cursor, Bolt, and Replit for different skill levels.
tags: [gemini-api, cursor]
---

This week, I learned:

- [LanceDB](https://lancedb.github.io/lancedb/) is a more scalable alternative to ChromaDB. Written in Rust. Does not require a separate HSNW library.
- Meta has a bunch of image embedding models:
  - [DINOv2](https://github.com/roboflow/notebooks/blob/main/notebooks/dinov2-image-retrieval.ipynb) creates image embeddings (Apr 2023)
  - [ImageBind](https://research.facebook.com/publications/imagebind-one-embedding-space-to-bind-them-all/) is an embedding model for text, images, audio, and more (Jun 2023)
- Gemini has a [code execution API](https://ai.google.dev/gemini-api/docs/code-execution)!
- [0x0.st](https://0x0.st/) is an open API-based file upload + URL shortening service. You can dump files there temporarily.
- [noVNC](https://novnc.com/info.html) is a JavaScript VNC client. You can control a remote (virtual) machine from your browser.
- [Friend](https://www.wired.com/story/friend-ai-pendant/) is an always recording pendant that you can ask questions to.
- Anthropic's new Sonnet model is even better at code. Plus it has the ability to extract coordinates from images. [Ref](https://www.anthropic.com/news/3-5-models-and-computer-use)
- Gemini sort-of supports diarization. [Ref](https://cloud.google.com/vertex-ai/generative-ai/docs/prompt-gallery/samples/classify_audio_diarization). I tried it and it's OK but not perfect.
  - #IMPOSSIBLE LLMs cannot diarize reliably yet. (Gemini just guesses the speaker differences.)
- Replit is good for hobbyists, Cursor for developers, and Pythagora & Bolt for non-developers building business apps. [Ref](https://youtu.be/8fEdaXwdDl8)
