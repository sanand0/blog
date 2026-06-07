---
title: Things I Learned - 26 Nov 2023
date: 2023-11-26T00:00:00+00:00
categories:
  - til
description: I learned about GPT Vision for calendar extraction, the limitations of RAG versus fine-tuning, and using LlamaIndex for hierarchical retrieval. I also found tools for JSON repair, LLM evaluation metrics, and running local models with Ollama.
keywords: [gpt vision, rag, llamaindex, llmops, ollama, fine-tuning, openrouter, orca 2]
---

This week, I learned:

- This is an interesting GPT Vision API prompt from Simon Willison: "given this event flyer, create a link to add it to my Google Calendar". [Ref](https://www.newsroomrobots.com/p/breaking-down-openais-new-features)
- Quote from Jerry Liu: "GPT 4 is really good at complex reasoning". It's worth exploring what that means.
- Quote from Jerry Liu: "RAG is a hack". It's engineered, not machine learnt, so it's suboptimal. We need an ML way of creating the context. Maybe fine tuning can be a way of CREATING the right context. But RAG can handle deterministic stuff like access control.
- Open AI fine tuning API is not good at memorizing info the way it is exposed. But the Gorilla paper shows that fine tuning can actually memorize well.
- Learn ML optimization approach - LLMOps. Have an evaluation framework with metrics like weights and biases or tensorboard. Helps figure out where fine tuning helps and where RAG does. Soon, this will become important.
- Flat indexing of chunks is not the only way to store embeddings. LlamaIndex allows you to create hierarchies that you can traverse for retrieval
- Agents mimic programming primitives. Switch. While. Call a function. Print.
- [OpenRouter](https://openrouter.ai/docs#models) hosts several models and offers them as APIs!
- [Ragas metrics](https://docs.ragas.io/en/latest/concepts/metrics/index.html) evaluate quality of a RAG pipeline
- [Orca 2](https://www.microsoft.com/en-us/research/blog/orca-2-teaching-small-language-models-how-to-reason/) was trained on different reasoning techniques (e.g. step-by-step) and is as good as larger models
- Embeddings can help just re-rank regular search results. [Ref](https://txt.cohere.com/rerank/)
- Claude 2 Anthropic has a 200K context window but is still crap.
- [Video-Llava](https://github.com/PKU-YuanGroup/Video-LLaVA) can understand videos too.
- [CoVA](https://aclanthology.org/2022.ecnlp-1.11.pdf) scrapes web pages using LLMs and visual information.
- [jsonrepair](https://github.com/josdejong/jsonrepair) can fix JSON fairly well. [jsonformer](https://github.com/1rgs/jsonformer) wraps HuggingFace models to produce JSON. [Ref](https://twitter.com/jerryjliu0/status/1720127061917147376)
- Google has a model garden with lots of pre-trained and trainable models.
- [Gorilla LLM specializes in APPI calls](https://gorilla.cs.berkeley.edu/): Torch Hub, TensorFlow Hub, HuggingFace
- [GPT-4 does not do abstraction at human levels](https://arxiv.org/abs/2311.09247)
- Each of the GPTs / Prompts we create could be like a UNIX command prompt, and become a startup of its own
- [Llava Plus](https://llava-vl.github.io/llava-plus/) extends LlaVA with pre-trained vision models that make image editing better
- [Ollama](https://github.com/jmorganca/ollama) runs local LLMs
