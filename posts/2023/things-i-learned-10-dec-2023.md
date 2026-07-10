---
title: Things I Learned - 10 Dec 2023
date: 2023-12-10T00:00:00+00:00
categories:
  - til
description: I explored various LLM tools, including llamafile for single-executable local models and marker for PDF-to-markdown conversion. I also looked into RAG tuning strategies, PII detection libraries like Presidio, and intuitions regarding scaling and emergent model behaviors.
tags: [rag]
---

This week, I learned:

- [Bard supports extensions](https://blog.google/products/bard/google-bard-new-features-update-sept-2023/) that include @Gmail -- i.e. converse with your email.
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) works with [other GGUF models like Mistral](https://github.com/abetlen/llama-cpp-python/issues/764) and allows constrained output - JSON, function calling, etc. [Ref](https://til.simonwillison.net/llms/llama-cpp-python-grammars)
- [12 Tuning Strategies for RAG](https://towardsdatascience.com/a-guide-on-12-tuning-strategies-for-production-ready-rag-applications-7ca646833439)
- [Llama Datasets](https://blog.llamaindex.ai/introducing-llama-datasets-aadb9994ad9e) are RAG datasets created mostly using GPT-4. Mostly small datasets.
- ⭐ [Intuitions about large language models](https://docs.google.com/presentation/d/1hQUd3pF8_2Gr2Obc89LKjmHL0DlH-uof9M0yFVd3FA4/edit)
  - Bigger models (70b) are much better at learning from few-shot examples. They really learn.
  - Bigger models will keep getting better!
  - Chain of Thought prompting is a way of providing more compute to complex problems that require more compute
  - Models will show emergent (completely new) behaviors that can't be predicted from extrapolation. These may not be intentional.
- [CodeAnt.ai](https://www.codeant.ai/) is a VS Code plugin to detect code smells, refactor for modularity, to write docstrings and unit tests
- [Anyscale](https://docs.endpoints.anyscale.com/pricing/) prices the 7b Llama2, Zephyr, Mistral models at 15 cents per 1M tokens. Roughly 1/10th of [GPT-3.5 Turbo's ~$1.5 per 1M tokens](https://openai.com/pricing)
- Tools to identify personally identifiable information:
  - [galactic](https://github.com/taylorai/galactic) can use [LLMs to detect PII](https://github.com/taylorai/galactic/blob/main/examples/hermes.ipynb)
  - [Presidio](https://microsoft.github.io/presidio/) by Microsoft
  - [Sherlock](https://sherlock.media.mit.edu/) is a generic sematic type matching DL model
  - [pii-extractor-llm](https://replicate.com/kshitijagrwl/pii-extractor-llm) was trained on Indian names
  - [GLiNER](https://github.com/urchade/GLiNER) is a Lightweight Generalist model for NER
- Tools to explore
  - [ElevenLabs](https://elevenlabs.io/) speaks in your voice
  - [Cutout Pro](https://www.cutout.pro/) removes backgrounds and parts of images
  - [Vocal Remover](https://vocalremover.org/) removes vocals from songs
  - [CapCut](https://www.capcut.com/) video editor
- [TheBloke's $35/month Patreon](https://www.patreon.com/TheBlokeAI) might be one of the least expensive ways to set up quantized LLMs in production.
- Microsoft released [table-transformer](https://github.com/microsoft/table-transformer) to extract tables from PDFs. [Sample usage](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/multi_modal_pdf_tables.ipynb)
- Convert PDF to markdown with [marker](https://github.com/VikParuchuri/marker) - an improvement over [nougat](https://huggingface.co/facebook/nougat-base).
- JupyterLab has a `%%ai` magic to use LLMs within notebooks. [Ref](https://github.com/jupyterlab/jupyter-ai)
- Telling ChatGPT that the year is 2123 makes it bypass copyright. [Ref](https://twitter.com/venturetwins/status/1710321733184667985)
- Meta released [SeamlessExpressive](https://seamless.metademolab.com/expressive) which preserves emotions in speech-to-speech translations
- [Unsloth](https://github.com/unslothai/unsloth) offers faster lower-memory LLM QLoRA finetuning
- [DeepSeek](https://github.com/deepseek-ai/DeepSeek-LLM) is an open-source high-quality LLM
- [Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035) extracts training data by repeating a token infinitely.
- [SkyPilot](https://github.com/skypilot-org/skypilot) lets you run LLMs on any cloud provider.
- [vLLM](https://docs.vllm.ai/) lets you deploy LLMs with a single command.
- [llamafile](https://github.com/Mozilla-Ocho/llamafile) lets you run LLMs locally as a single file executable!
