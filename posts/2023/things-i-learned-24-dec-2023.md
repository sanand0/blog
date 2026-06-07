---
title: Things I Learned - 24 Dec 2023
date: 2023-12-24T00:00:00+00:00
categories:
  - til
description: I compared Mixtral-8x7b to GPT-4, studied DPO for fine-tuning, and took notes on Jeff Bezos’ leadership principles. I also found tools like Whisper-standalone for Windows transcription and Token Tally for estimating LLM token and GPU costs.
keywords: [dpo, mixtral-8x7b, jeff bezos, chatbot arena, faster-whisper, token tally, llm fine-tuning]
---

This week, I learned:

- [DPO](https://arxiv.org/abs/2305.18290) is a simpler alternative to RLHF for fine-tuning. Several [HuggingFace models use DPO for training](https://huggingface.co/search/full-text?q=DPO&type=model)
- [Name2Vec](https://github.com/foxcroftjn/CanAI-Name2Vec/) is a potential embedding for names.
- Google Knowledge Graph ID powers the Knowledge Graph. If it begins with /m/ it's the same as the FreeBase ID. This is now available as WikiData. e.g <https://www.wikidata.org/wiki/Property:P2671>
- I tried running Mixtral-8x7b locally (via Llamafile) and on [together.ai](https://api.together.xyz/playground/chat/mistralai/Mixtral-8x7B-Instruct-v0.1). It's good, but far from GPT 4.
- Generic computate-intensive algorithms eventually beat domain-specific tuning, because of Moore's law. [Ref](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
- The hidden brain podcast. the mystery of beauty
  - Evolution drove us to beauty as an efficient survival mechanism. Understanding the world is one such mechanism. Hence we enjoy maths and chess
- ⭐ [This leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard) included paid models like GPT4 and Claude and compared them with open models on HUMAN + system benchmarks
- Lez Friedman Podcast: Jeff Bezos
  - Build stuff that is is ubiquitous that other people take it for granted. The initial idea needs to be that obvious and easy. Like one click purchase or customer reviews
  - Build stuff that other people can build on. Internet makes startups possible. Infrastructure is about enabling others at scale
  - Decision making approaches: single person decides on two way doors. Deliberate as a team on one way doors
  - Conflict resolution: disagree and COMMIT. NO sniping, I told you so, malicious compliance. Avoid compromise. Avoid decision by attrition (most persistent wins).
  - People are inherently biased towards hierarchy. So the senior most person should speak last
  - We have a happiness bias. Contracted by choosing the unhappier options first
  - The map is not the territory. The metric is not the objective. We need metrics. But make sure you know why
  - See the world through the eyes of the customer. Use your own product. It's living their lives that makes customer obsession real. Jeff Bezos called their own customer care to see how long the actual wait time was. It was much longer than the metric reported
  - How to prioritize. whatever problems customers will still face in 10 years are the big problems. These are worth putting time into because they are stable in time
  - People working on big problems will never get down to the small problems. So have a dedicated team that works only on the paper cuts. It should be a dedicated team
  - We co evolve with our tools. We build tools and then our tools change us. It reprograms our brains
  - Cut out 10 minutes to the beginning of each meeting for people to read the material. They never reread anyway. This makes the meetings more productive
  - Powerpoint is designed for persuasion, not truth seeking. It is also easier for the author than for the reader. Prefer narratives that are focused on finding the truth and are easier for the audience though tougher for the author
- ⭐ [whisper-standalone-win](https://github.com/Purfview/whisper-standalone-win) provides a Windows binary for Faster-Whisper. It just needs [CUDA](https://developer.nvidia.com/cuda-downloads) and [cuDNN](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html) installed. Then `whisper-faster.exe video.mkv --language=English --model=medium` generates the transcript.
- LLM use cases by Benedict Evans
  - "Every text box on the internet will get an LLM"
  - "Infinite interns"
  - "Every UNIX function has become a company." "Every ChatGPT suggestion..."
- [llm360](https://www.llm360.ai/) publishes models along with training datasets.
- In [The Age of AI has begun, Mar 2023](https://www.gatesnotes.com/The-Age-of-AI-Has-Begun), Bill Gates says, "In my lifetime, I've seen two demonstrations of technology that struck me as revolutionary." The GUI (1980) and ChatGPT (2022).
- [Rubeus](https://github.com/portkey-ai/rubeus) is a HTTP proxy for multiple LLMs with load-balancing, fallbacks and retries.
- [GPTRouter](https://github.com/Writesonic/GPTRouter) is a Python interface for multiple LLMs with fallbacks and retries.
- ⭐ [Token Tally](https://tokentally.streamlit.app/) has an LLM Cost Tool that estimates GPU memory required and token cost across cloud providers.
