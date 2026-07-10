---
title: Things I Learned - 23 Mar 2025
date: 2025-03-23T00:00:00+00:00
categories:
  - til
description: I explored DeepSeek R1 training, how AI models are absorbing app capabilities, and fixing Windows symlinks for Hugging Face. I also discovered DuckDB's built-in notebook UI, Gemini’s YouTube API, and Karpathy-inspired note-taking workflows.
tags: [duckdb, gemini-flash, windows]
---

This week, I learned:

- If we can DESCRIBE what good looks like, training data is no gap. We can auto optimise models towards that. That's RLF. DeepSeek R1 side stepped the need for training data by creating reward functions and prompts. This tells the fine tuning process how to go correct as it goes along. [This video](https://www.linkedin.com/posts/devvret-rishi-b0857684_starting-today-you-can-build-your-own-custom-activity-7308141160357670912-Rwfy) is the first one that really help me understand what's going on.
- I was born in the Ananda year in the Tamil _and_ Telugu calendars. [ChatGPT](https://chatgpt.com/share/67dbcb41-209c-800c-9403-1eb4cd365ece)
- Andrej Karpathy's note taking mechanism is similar to mine, except I use Microsoft TODO. [Ref](https://x.com/karpathy/status/1902503836067229803)
  - I have 3 categories. Things I learnt, which I just note. Things to explore, which I can delegate, defer, drop, or do at any time. Things to do, which are the hardest and pile up.
- Alexander Doria shares an interesting perspective on the app space. [Model is the product](https://vintagedata.org/blog/posts/model-is-the-product)
  - Models are natively absorbing app capability and will become killer systems internalising workflows like Chat, Deep Research, Claude Code, Operator, etc. to wipe out the apps and workflow space. Models will "internalize" tool capabilities
  - Opinionated or focused training will be a lever and model providers will acqui-hire the successful trainers
  - API access from model providers will shrink. Selling tokens is not a viable business model given lowering costs
- The `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files. To support symlinks on Windows, you either need to [activate Developer Mode](https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development) or to run Python as an administrator.
- In Windows, you can enable offline files for any SMB share via: Control Panel → Sync Center → Manage offline files and turn on the feature. Then, in File Explorer, right‑click the mapped network folder or drive and select "Always available offline."
- OpenAI now supports [PDFs natively in the API](https://platform.openai.com/docs/guides/pdf-files?api-mode=chat). (Gemini has done so for a while)
- Anger is a trigger for change. "Either change yourself or the environment, else you'll be uncomfortable."
- [HocusPocus](https://tiptap.dev/docs/hocuspocus/introduction) allows live collaboration e.g. editing together
- [Block notes](https://www.blocknotejs.org/) is a notion like library for editor components. Converts to Markdown
- [Oxidizr](https://jnsgr.uk/2025/03/carefully-but-purposefully-oxidising-ubuntu) enables replacing Linux tools with Rust equivalents.
- [Emoji Kitchen](https://emojikitchen.dev/) lets you create stickers from emoji combinations.
- Another way of scaling LLMs is generating multiple options and self evaluating. [Eric Zhao](https://x.com/ericzhao28/status/1901704339229732874)
- `duckdb -ui` launches a DuckDB notebook. This is built into newer DuckDB releases
- [Monolith](https://github.com/Y2Z/monolith) downloads web pages as a single HTML file by embedding content.
- [Archgw](https://github.com/katanemo/archgw?tab=readme-ov-file) is an LLM proxy/router from the makers of Envoy proxy.
- There's an [annotated Terry Pratchett](https://www.lspace.org/books/apf/the-colour-of-magic.html)!
- Gemini API allows YouTube videos as a part. [Google](https://ai.google.dev/gemini-api/docs/vision?lang=python#youtube)
- agents.json is a proposal for discovery of agents on a site that enhances the Open API spec: [wild-card-ai/agents-json](https://github.com/wild-card-ai/agents-json)
- Since Gemini Flash 2.0 is now an image GENERATION model, interactive VISUAL fiction is now a cool possibility. People are using it in interesting ways:
  [Interleaved storytelling](https://x.com/OriolVinyalsML/status/1901328862656503826),
  [Memes](https://x.com/emollick/status/1901431681279475808),
  [Surrealism](https://x.com/emollick/status/1901370982557794658).
