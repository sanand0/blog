---
title: Things I Learned - 02 Feb 2025
date: 2025-02-02T00:00:00+00:00
categories:
  - til
description: I learned about JavaScript's Temporal object, appending hidden data to PDFs, and using embeddings for ML classification. I also explored AI-driven business models, including zero-employee companies, and how compute dominance shapes global AI power.
keywords: [temporal api, webassembly, machine learning, embeddings, zero-employee companies, inflation, ai product management]
---

This week, I learned:

- You can add any content at the end of a PDF file. It's ignored. It's an interesting way to send additional information (or just blow up the file size if you don't like them.)
- [JavaScript introduces a `Temporal` object](https://developer.mozilla.org/en-US/blog/javascript-temporal-is-coming/) that will replace the `Date` object.
- You can use embeddings as the input to a classical ML classifier. This can improve classification a lot. [Nomic](https://docs.nomic.ai/atlas/cookbook/building-image-classifiers-with-atlas)
- As AI software becomes more common, demand for AI product managers will grow. Also as a proportion of people in an organization. https://www.deeplearning.ai/the-batch/issue-284/
- Control of chips and GPU compute is what will likely be the gameplay to control AI dominance globally. [Dario Amodei](https://darioamodei.com/on-deepseek-and-export-controls)
- Bring LLMs to the table. One mode of collaboration is using LLMs as **ACTIVE** participants, i.e. they CONTRIBUTE. For example, in a video call. A workshop. A classroom. A presentation. Have the LLM provide input **DIRECTLY** to a group of people.
- Environment shapes ambient thoughts. Working in a hospital will give you ideas about how to use LLMs in hospitals, for example. People you are working / ENGAGING with are perhaps the biggest drivers.
- The cost of a cream biscuit packet in India has fallen about 25 _times_, i.e. about as fast as inflation, between 1981 - 2024. Effectively, the absolute price has not changed. How do I know this?
  - [In 1981, a cream biscuit packet cost Rs 25](https://youtube.com/clip/UgkxCF90vppUV01qz0Wila-9meADPord26kc?si=3LLQ5fgRzwG_wUO-)
  - [In 2025, it's available for Rs 21](https://www.amazon.in/Sunfeast-Dark-Fantasy-Bourbon-120g/dp/B0BSX9N69D/)
  - [India Inflation Calculator](https://www.in2013dollars.com/india/inflation/1981?amount=25) - a rare inflation calculator with annual inflation rates baked in - shows that Rs 25 in 1981 is equivalent to Rs 540 in 2024. That's about 25 times more than the Rs 21 it costs today.
- [A WebAssembly compiler that fits in a tweet](https://wasmgroundup.com/blog/wasm-compiler-in-a-tweet/) deconstructs a piece of JS that creates a tiny WebAssembly calculator. It's a great walk-through of JavaScript compression tricks and how WebAssembly works. [Simon Willison](https://simonwillison.net/2025/Jan/25/a-webassembly-compiler-that-fits-in-a-tweet/#atom-everything)
- Brandon Sanderson has a [series of YouTube videos](https://www.youtube.com/watch?v=-6HOdHEeosc) where he teaches a course on magic systems.
- When using AI coding agents, CLI beats APIs. Simpler models are able to use the CLI more reliably than APIs. [Simon Willison](https://simonwillison.net/2026/Jan/17/jeremy-daer/)
- I was exploring new business models enabled by LLMs. [Here are some thoughts](https://chatgpt.com/share/6795b30f-35d4-800c-9863-285a852afe7b):
  - **1. Autonomous Multi-Sided Marketplaces**. AI-powered platforms coordinate complex services with minimal human oversight—think “Uber for Everything, but the platform sets pricing dynamically, schedules both supply and demand, and resolves disputes algorithmically.
  - **2. Collective Intelligence Ecosystems**. Communities pool data, expertise, and AI models to tackle shared problems—like an open-source “GitHub for AI, but with embedded micropayments or tokenized incentives to reward contributors whenever the models are used commercially.
  - **3. Zero-Employee Companies**. Fully automated software entities—legal frameworks might allow an AI to manage services, pay taxes, and sign contracts. These “companies only hire humans as needed, on-demand, for edge cases AI can’t handle.
  - **4. Context-Aware Knowledge Platforms**. Imagine a Wikipedia that not only retrieves static info but also tailors each page in real time to the reader’s personal context, language level, and preferences—generating content on the fly. User feedback loops train the system to improve.
  - **5. Data Cooperatives / Data DAOs**. Groups collectively own their data and license it to AI companies on a revenue-share basis. Individuals have a direct financial stake in how their shared data is leveraged, voting on permissible use cases.
  - **6. Personalized Service Layers**. Similar to GitHub’s “forking model, but for entire user experiences. Each user can clone and customize an AI service (whether it’s a personal grocery shopper or a content curator) and can share or monetize improvements with the broader network.
