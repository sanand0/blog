---
title: Things I Learned - 29 Sep 2024
date: 2024-09-29T00:00:00+00:00
categories:
  - til
description: I explored using Pyodide for browser DOM access and PyMuPDF4LLM for converting PDFs to Markdown. I also compared AVIF to GIF compression, experimented with Opus audio encoding, and researched Anthropic’s contextual retrieval methods for improved RAG performance.
tags: [avif, ffmpeg, rag]
---

This week, I learned:

- Pyodide can access the DOM and JavaScript in the browser
- [Jupyter Lite](https://jupyter.org/try-jupyter/lab/) lets you run Jupyter notebooks in the browser
- AVIFs is about 10X better than GIFs. I tried creating one via [EZGIF AVIF Maker](https://ezgif.com/avif-maker/) and the .avifs file created was 15X smaller!
  `ffmpeg -i input.gif -c:v libaom-av1 -crf 30 -b:v 0 -cpu-used 4 -tiles -an output.avif`
- Claude 3.5 thinks `.opus` is the best format to compress audio. It used `ffmpeg -i audio.wav -c:a libopus -b:a 16k -application voip -vbr on -compression_level 10 audio.opus`
- API coding best practices [Source](https://erikbern.com/2024/09/27/its-hard-to-write-code-for-humans.html) via [Simon Willison](https://simonwillison.net/2024/Sep/27/erik-bernhardsson/):
  - Always add screenshots to the Readme. They never break.
  - Always add every example. Human think in examples.
  - Avoid defaults and be explicit unless 99% of the usage is with the default.
  - Make the feedback loops incredibly fast.
  - Make deprecations easy for users to deal with.
  - Keep objects immutable.
- [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/) can convert PDFs to Markdown. It handles tables, too.
  - 04 Oct 2024. [PDF-Extract-Kit](https://github.com/opendatalab/PDF-Extract-Kit) does PDF layout, formula, table, and OCR extraction using various models.
  - 04 Oct 2024. [llmsherpa](https://github.com/nlmatics/llmsherpa) extracts PDF layout, tables, not OCR
- When evaluating feasibility of technology with LLMs always ask for multiple options and pick from those. [Simon Willison](https://youtu.be/6U_Zk_PZ6Kg?t=4444)
- [Gemini supports audio natively](https://ai.google.dev/gemini-api/docs/audio?lang=rest)
- Google Vertex AI has an [OpenAI compatible API](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/call-vertex-using-openai-library) but it works only for some models. Anthropic and Gemini are not compatible.
- When you paste HTML into Excel, it automatically changes the font of the cell to match the content in the HTML!
- Aptos is the new default font in Office - replacing Calibri.
- Anthropic's [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) says:
  - Use BM25 in addition to embeddings to match rare terms (e.g. identifiers)
  - Add a context to each chunk's metadata (generate it with a cheap LLM) and pass it to the summarizing LLM
  - Reranking helps with cost AND accuracy. Use [Cohere](https://cohere.com/rerank) or [Voyage](https://docs.voyageai.com/docs/reranker)
- [Sentient](https://github.com/sentient-engineering/sentient) lets you control the browser via Python in natural language
