---
title: Things I Learned - 21 Jul 2024
date: 2024-07-21T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- [GPT For Work](https://gptforwork.com/help/gpt-for-sheets/gpt-functions/all-available-functions) has a set of useful spreadsheet LLM functions
- [Xata](https://xata.io/docs/rest-api) offers a free PostgreSQL tier with REST API
- Mamba now uses mambaforge as the default installation, i.e. conda-forge is the default and only channel!
  - Update: 6 Jun 2025. Mambaforge is sunset as of 29 Jul 2024. Conda-forge now uses Miniforge as the standard installer [Ref](https://conda-forge.org/news/2024/07/29/sunsetting-mambaforge/)
    conda-forge.org. Users should switch to Miniforge instead.
- nginx supports a load-balancing method `least_conn` which is _far_ better than the default round-robin.
- #IMPOSSIBLE LLMs cannot provide a bounding box of objects in images. (Maybe Florence 2 can). Update: Mar 2025. Gemini has [good timestamps and bounding boxes](https://simonwillison.net/2025/Mar/25/gemini/)
- Models gently grow in capability. It helps to maintain an impossibility list that steadily gets invalidated. [Ref](https://www.oneusefulthing.org/p/gradually-then-suddenly-upon-the)
- [Github Copilot internals](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals.html) walks through how Copilot constructs its prompts
