---
title: Things I Learned - 13 Oct 2024
date: 2024-10-13T00:00:00+00:00
categories:
  - til
description: I discovered how LLM planning time rivals massive parameter increases, compared text-to-speech pricing, and tested DuckDB's function chaining. I also explored Deno 2's Node compatibility, Marimo notebooks, and efficient Python Docker builds using uv.
keywords: [duckdb, deno, marimo, text-to-speech, llm, uv, docker, pypi]
---

This week, I learned:

- [DuckDB supports function chaining](https://duckdb.org/docs/sql/functions/overview.html#function-chaining-via-the-dot-operator)
- [DuckDB lets you create functions = macros](https://duckdb.org/docs/sql/statements/create_macro.html)
- [HTML for People](https://htmlforpeople.com/) is a nice introduction to HTML.
- [FlightRadar24](https://www.flightradar24.com/) lets you watch airplanes live.
- [sq](https://sq.io/) is like `jq` but for SQL.
- [Deno 2](https://deno.com/) is fully backward compatible with Node! [via](https://deno.com/blog/v2.0)
- O1 is good at solving problems where the solution is easy to verify and generating options helps get closer to the solution
- Reverb ASR does diarration as well as transcription. It seems the state of art right now.
- Gemini Flash and Gemini Flash 8b can be fine-tuned at zero cost. Inference is at the same price! [Ref](https://ai.google.dev/pricing)
- Flux 1.1 Pro is released. I tried my Calvin & Hobbes test on it. Not great. ImageGen3 is better, ChatGPT is the best. [Ref](https://www.s-anand.net/blog/image-generation-gets-better-at-comics/)
- Revisiting text to speech models. Nothing much has changed since July 2024.
  - OpenAI TTS: $15/1M chars [Ref](https://openai.com/api/pricing/)
  - Deepgram Aura: $15/1M chars [Ref](https://deepgram.com/pricing)
  - Azure AI Speech: $15/1M chars [Ref](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/)
  - Google TTS Neural2: $16/1M chars [Ref](https://cloud.google.com/text-to-speech/pricing?hl=en)
  - AWS Polly Neural TTS: $16/1M chars [Ref](https://aws.amazon.com/polly/pricing/)
  - Cartesia Pro: $50/1M chars [Ref](https://www.cartesia.ai/pricing)
  - Elevenlabs Scale: $300/1M chars [Ref](https://elevenlabs.io/pricing)
- GitHub co-pilot workspaces let you code using your mobile with AI and deploy it at one shot
- If you need an Ubuntu Docker container with Python, install it via uv rather than compiling from source. [via](https://mkennedy.codes/posts/python-docker-images-using-uv-s-new-python-features/)
- [VTracer](https://www.visioncortex.org/vtracer/) is an open source library (and tool) to convert raster images to SVGs. [via](https://simonwillison.net/2024/Oct/7/vtracer/)
- If you want to create a `console.llm()` function, a browser extension is the best way, because some pages have Content-Security-Policy that block eval, form submission, fetch from other domains, and script execution.
- [PyPi lets you publish from GitHub Actions](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) without a token. Also from Gitlab.com CI/CD and Google Cloud.
- [ActiveState](https://en.wikipedia.org/wiki/ActiveState) which made ActivePython, ActivePerl, etc. made these products paid for commercial use around 2013 after a series of acquisitions.
- [Marimo](https://marimo.app/) supports:
  - Publishing any notebook to static.marimo.app as a static app
  - Creating a SINGLE link that embeds the ENTIRE notebook in the URL!
  - Runnable via `uvx marimo edit`
- [Parables on the Power of Planning in AI](https://youtu.be/eaAonE58sLU): Giving models about 30 seconds of thinking time consistently improves results - as much as increasing parameter size by a factor of 1,000 to 100,000!
  - This works particularly well for verifiable results (code, math, etc.)
  - Technique: Ask an LLM hundreds of times at low temperature and pick the most common one. (Google's Minerva used this on the MATH dataset.)
  - Better Technique: Ask an LLM hundreds of times. Pick the best solution based on an evaluation metric (reward model)
  - Better Technique: Apply a reward model at EACH step of the process. OpenAI's "Let's Verify Step by Step"
- [Late chunking](https://jina.ai/news/late-chunking-in-long-context-embedding-models/) is an interesting approach to adding context to embeddings. (I don't understand it, but it's cheap and effective.)
- [DeepInfra offers embedding models as APIs](https://deepinfra.com/models/embeddings) at about 0.5 to 1 cent per MTok in an OpenAI compatible API.
  It also supports [text-to-image models](https://deepinfra.com/models/text-to-image) like flux.dev and
  [speech recognition models](https://deepinfra.com/models/automatic-speech-recognition) like Whisper.
- [Jake Heller](https://www.youtube.com/watch?v=eBVi_sLaYsc):
  - "One of the things we learned is (an LLM app) after it passes passes frankly even 100 tests, the odds that it will do, on any random distribution of user inputs, the next 100,000 100% accurately is very high."
- OpenAI's O1 is like Daniel Kahneman's System 2 thinking - as against other LLMs' System 1 thinking.
- [Continue.dev](https://www.continue.dev/) is another AI coding editor. It supports OpenRouter. So now I have heard good things about:
  - Github Copilot
  - Cursor
  - Cody
  - Continue.dev (supports OpenRouter)
  - Aider (supports OpenRouter)
  - Maybe:
    - Codeium
  - Not:
    - Amazon Q Developer
