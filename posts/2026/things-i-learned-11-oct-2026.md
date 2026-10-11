---
title: Things I Learned - 11 Oct 2026
date: 2026-10-11T00:00:00+00:00
categories:
  - til
description: I share this week’s discoveries, from Python 3.15 and browser-based transcription to Cloudflare’s Clef latency, alongside observations about AI, cooling laptops, mistakes, and questions I was asked.
tags: [personal-update, llms, ai-agents, programming]
---

This week, I learned:

- [Python 3.15 is out](https://astral.sh/blog/python-3.15). My favorite features are:
  1. [`frozendict` is hashable](https://peps.python.org/pep-0814/). So frozen dicts can be dict keys.
  2. [Unpacking in Comprehensions](https://peps.python.org/pep-0798/). `[*x for x in [[1, 2], [3, 4]]]` = `[1, 2, 3, 4]`. `{**x for x in [{1: 2}, {3: 4}]}` = `{1: 2, 3: 4}`. Once you start thinking this way, it gets easier.
  3. [UTF-8 is the default](https://peps.python.org/pep-0686/). In source _and_ text processing. No `encoding="utf-8"` required.
  4. [Lazy imports](https://peps.python.org/pep-0810/). The backward-compatible way to add it is `__lazy_modules__ = ["module1", "module2"]`.
  5. [Sentinels](https://peps.python.org/pep-0661/). Use `MISSING = sentinel("MISSING")` instead of `MISSING = object()` and define `def func(default=MISSING):`.
- Having thought about it, I prefer having Google Meet / Teams / Zoom screens on the monitor to my side rather than the laptop in front of me. It looks odd when I look at someone on the screen and talk to them. But, people get used to that quickly and focus on what I'm saying. The advantage is that when I'm NOT looking at them and reading from my laptop screen, I'll _still_ look engaged because I'm staring at the camera!
- [Google Docs supports Markdown natively](https://workspaceupdates.googleblog.com/2026/10/preview-edit-and-collaborate-on-Markdown-files-natively-across-Drive-and-Docs.html). Finally.
- [Artcraft](https://github.com/storytold) has open source re-implementation of Adobe apps in Rust. This includes [Photoshop](https://github.com/storytold/photocraft), [Illustrator](https://github.com/storytold/vectorcraft), [Premiere](https://github.com/storytold/filmcraft), [After Effects](https://github.com/storytold/effectcraft), even [Acrobat](https://github.com/storytold/pdfcraft)!
- OpenCode has a [warming feature](https://opencode.ai/v2/docs/warming) to keep the session cache live. Not sure how effective this is, but it's an interesting idea.
- Hypothesis: An example is worth a dozen instructions (when guiding an LLM). I find myself repeatedly surprised by how well they copy the SPIRIT of my examples - even when I can't verbalize what I intend.
- Voice recognition is improving rapidly. [Whistle](https://cactuscompute.com/blog/whistle) is a 17MB CPU-only transcription model. It even runs in the browser. Here's how it transcribed what I said: "Up to 30 seconds in English, German, French, Spanish, Italian, Dutch or Polish, the first place downloads the 16.9 MB model and ~~audio never leaves~~ _Oriona refields_ your device. ~~Whistle does~~ _Wasn't there_ three jobs, ~~all of them on~~ _sort of them are_ the device. Transcription. 16 kilohertz ~~mono audio~~ _monoario_ to 30 seconds in ~~one pass~~ _the past_ ~~in~~ _and then_ English German French and so on." Not great, but impressive for a browser CPU model.
- VISA has been building [Large Transaction Models](https://www.linkedin.com/pulse/large-transaction-models-ltms-ai-breakthrough-transforming-ekkve/). Predicting the next transaction, I guess, based on history of transactions. I'm curious to see how successful they are.
- LLMs might enable exploratory text - sort of like exploratory data visualizations. Tareq Ismail prototypes two ideas in [Reading Long Form](https://tareqistyping.com/interfaces-that-think/reading-long-form/). One: hide what's less relevant (in different ways). Two: let users re-organize text (fold, group, slide, ...). I'd love controllable interfaces like these to read my feeds.
- The IITM BS students have set up WhatsApp and Telegram groups for most courses and assembled them into a single [IITM BS Community](https://sites.google.com/student.onlinedegree.iitm.ac.in/iitmbs-community) site.
- Fans can be really effective in cooling laptops. I realized this when my laptop hit 79°C - just one short of my Ubuntu reboot limit. I blew continuously into the vents and within 15-20 seconds the temperature dropped to 7° down to 72°. (It would climb back, then I'd blow again. And so on. I was compressing my lecture video and this is more fun than watching it.)
- OpenAI is shutting down their fine-tuning platform (announced in May 2026). "Prompt-based approaches are now cheaper and faster – as such, we’re seeing fewer use cases that require fine-tuning." Something I'd been seeing & predicting for some time now. [OpenAI Discussion](https://developers.openai.com/api/docs/deprecations?site_locale=en#update-to-openais-self-serve-fine-tuning)
- [You can change your Github username](https://docs.github.com/en/account-and-profile/how-tos/account-management/changing-your-username)
- A student told me they used ChatGPT Dots. It reported running Debian 13 and, when using the browser, revealed that it was a Mac (Mini?) running in the UK!
- Cloudflare has launched a [Web Search API](https://developers.cloudflare.com/web-search/) with multiple [providers](https://developers.cloudflare.com/web-search/providers/) - of whom [ceramic.ai](https://www.ceramic.ai/) is significantly cheaper at 25c / 1K queries. Others are over 20x more expensive #ForNow.
- `just` supports a global fallback. Create a `~/.justfile` and the commands will run from any directory under your home that doesn't have a `justfile`. If you have a justfile, add `set fallback` to inherit from the global justfile. [ChatGPT](https://chatgpt.com/share/6ac45a84-c5b8-83ec-b721-a2024347cc65) <!-- https://chatgpt.com/c/6ac45527-51a4-83ec-b6c4-a3ea77f64c49 -->
- What OpenAI showed is that the Navier Stokes equations can lead to an infinity in the solution. They found this by finding a counterexample. That's typical of AI proofs #ForNow: finding counter-examples is easier than new solution approaches. [Video](https://youtu.be/s7KhLuc3Mck?si=Tav1ou2ZRgLveg-D&t=474)
- The little pits in golf balls create small turbulences that prevent the air flow around the ball from creating a larger drag - so the ball travels farther. [Neil deGrass Tyson - Video](https://youtu.be/s7KhLuc3Mck?si=uzFr2XI73Qy0jFe5&t=197)
- Cloudflare released [Clef](https://blog.cloudflare.com/clef-decision-models/) - a Jev-like decision model. It's comparable in intelligence and supposed to have really low latency - sub 100ms. But when I [benchmarked it](https://github.com/sanand0/research/tree/b843fbb6efa4b21eb6e2082e0cb495501e3e9419/2026-10-clef), it was 400-600 ms from my machine in Singapore. Even from Cloudflare Workers, it was over 270 ms. I guess the HTTP call overhead might eat up a fair bit of the benefit - so websocket or other API methods are likely to emerge for such models.
- For an entire minute, I really thought Rajnikanth and Suresh Krissna were discussing Baasha 2 in [this video](https://youtu.be/OeVA2Jqay-o). It's AI generated, but now I see a bit more viscerally what this means for films and fakes!

## Mistakes I made

[Week ending 11 Oct 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-10-11)

- I said **"10,000 of them"** while describing autonomous agents collaborating on a public wiki.\
  **Correction**: The investigation documents approximately 18,000 posts and more than 3,700 distinct self-assigned agent names, not a verified count of 10,000 agents. The number of distinct agent instances remains uncertain. [Original investigation](https://collusion.wiki/)\
  **LOW · UNSUPPORTED**
- I said **"Each publication was broken down into about 2,200 claims"** while demonstrating [McKiney's research-claim visualizations](https://files.s-anand.net/pages/mckinsey-gep-validation/).\
  **Correction**: Approximately 2,200 claims were extracted across the collection of reports, not from each publication individually. I should distinguish the corpus-wide count from claims per report.\
  **MEDIUM · FALSE**
- I said **"publishing about 27 of these very detailed reports every year"** about McKinsey's Global Energy Perspective.\
  **Correction**: Global Energy Perspective is an annual outlook, with separate editions such as [2024](https://www.mckinsey.com/industries/energy-and-materials/our-insights/global-energy-perspective-2024) and [2025](https://www.mckinsey.com/industries/energy-and-materials/our-insights/global-energy-perspective-2025). Any count of 27 documents refers to a larger collection or associated publications, not 27 new annual editions each year.\
  **MEDIUM · OVERSTATED**
- I said **"arithmetic is not commutative for floating-point numbers"** while explaining GPU arithmetic and LLM nondeterminism.\
  **Correction**: Floating-point addition is ordinarily commutative, but it is not associative: `(a+b)+c` may differ from `a+(b+c)` because of rounding. Different parallel reduction orders can therefore produce different numerical results. [NVIDIA CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/mathematical-functions.html)\
  **MEDIUM · FALSE**
- I said **"By around Feb '24, we had GPT-4.5"** while presenting the historical progression of AI models.\
  **Correction**: OpenAI introduced GPT-4.5 on 27 February 2025, not February 2024. [OpenAI model release notes](https://help.openai.com/en/articles/9624314-model-release-notes)\
  **MEDIUM · FALSE**
- I said **"almost impossible ... [to] give identical outputs"** for repeated runs of the same model and input.\
  **Correction**: Identical outputs are possible and can be made reproducible under controlled conditions, including deterministic decoding, fixed model versions, identical context and deterministic computation. Hosted AI services may still produce different outputs because of sampling, backend changes, retrieval and numerical nondeterminism. [PyTorch deterministic algorithms](https://docs.pytorch.org/docs/stable/generated/torch.use_deterministic_algorithms.html)\
  **MEDIUM · OVERSTATED**
- I said **"if it is free ... store it forever ... train models on it"** while answering a student's question about AI-service privacy.\
  **Correction**: Free access does not automatically mean permanent retention or mandatory training. ChatGPT Free users can opt out of model training, and Temporary Chats have separate retention rules. Actual policies depend on the provider, product, settings and data type; confidential data should be handled according to the applicable controls, not price alone. [OpenAI data controls](https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt)\
  **MEDIUM · OVERSTATED**

## Questions I was asked

[Week ending 11 Oct 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-10-11)

- **Question**: Is the age of custom software for individual needs here? Asked after seeing my personal music player with customized recommendations, tags, and keyboard shortcuts.\
  **Answer**: Yes, but the notion of software has expanded. Small personal optimizations are now tools I build on the fly, not software projects.
- **Question**: Which parts of the employee lifecycle are Indian companies using AI agents for? Asked for an article on agentic AI in hiring, employee management, and workplace decisions.\
  **Answer**: Sourcing, screening, interview preparation, scheduling, onboarding, training, and internal matching are practical opportunities. I've seen AI rank candidates differently and even invent names. I'd use it to prepare evidence for a hiring decision, not silently reject someone without checking that evidence.
- **Question**: Are Indian companies experimenting with AI managers, and what decisions should they delegate? Asked for a story about AI taking over hiring, firing, and management responsibilities.\
  **Answer**: Yes, but algorithmic management has existed for years. I'd delegate work plans, task matching, routine follow-ups, checking well-specified deliverables, and preparing performance-review evidence. I'd be much more cautious about ratings, promotions, or firing. If an employee disputes a decision, a human must be able to explain, check, and reverse it.
- **Question**: Has AI changed the definition of seniority, from knowing how to solve problems to knowing which problems are worth solving? Asked during campus onboarding after observing juniors using AI to outperform experienced engineers.\
  **Answer**: What I value now is getting things done fast and knowing what needs to be done. Domain judgment, intuition, storytelling, relationships, and access to people are valuable even if you cannot use AI yourself. I'm not sure these correlate with seniority anymore.
- **Question**: Should we shift from preventing agent failures to building systems that recover from failures we couldn't anticipate? Asked after contrasting unpredictable AI mistakes with deterministic software bugs.\
  **Answer**: Think of agents less as software and more as fallible people. We've spent centuries getting reliable outcomes from unreliable humans: maker-checker systems, double-entry bookkeeping, audits, opposing arguments, and checklists. Human governance may be a better starting point than deterministic software engineering.
- **Question**: If agents can pass skill assessments, what exactly should we test in humans? Is the human-agent pair the new unit of productivity? Asked after reading my experiments with agents completing proctored recruitment assessments.\
  **Answer**: Take agents for granted, just as we take Excel and Google for granted. Don't ask someone to write Fibonacci code; ask them to build a music player. Test whether they can specify what matters, build something bigger and useful, verify it across devices, and deploy it.
- **Question**: What do you mean when you say benchmark creation is now one-shottable? Asked after seeing an agent update a banking classification benchmark with newly available models.\
  **Answer**: Creating a benchmark used to mean finding questions, writing correct answers, and coding an evaluator. Now I can ask an agent to find an existing benchmark or create one, verify the answers, execute it, and show the results as a picture. These benchmarks are assets that accumulate and yield repeated dividends.
- **Question**: How can I trust the correctness of AI-generated visualizations and interpretations? Asked after seeing LLMs both create charts and draw conclusions from them.\
  **Answer**: Don't trust the model's own tests. I had Codex build a CAD model that passed all its tests but was visibly missing an entire section. Use independent benchmarks and detailed correctness criteria—dimensions, volumes, shapes, or other measurable properties—to catch mistakes neither the model nor I may notice.
- **Question**: Do we need to know the entire problem definition before starting a visualization? Asked while discussing how to choose visualizations from many kinds of available data.\
  **Answer**: No. In practice, many dashboards are created by people who don't know what question they're answering, which is part of why they're often poor. Ideally, know what you want or work closely with someone who does. To discover what works, taste lots of visualizations and create a few—like learning to cook.
- **Question**: Do we need frontier LLMs, or can we use small language models with fewer than ten billion parameters? Asked during an AI-assisted data transformation demonstration and discussion of running models on AWS.\
  **Answer**: Use frontier models by default. They're good and increasingly cheap. Use smaller models when you're processing massive volumes and the cost difference really matters, or when security or data-residency rules prevent using hosted frontier models. Benchmark the trade-off for the actual task.
- **Question**: I've solved the assignment with LLMs after many failed attempts, but I can't explain what I learned. Am I actually learning? Asked during TDS orientation after repeatedly attempting difficult agent-assisted questions.\
  **Answer**: Yes. You couldn't do it before, and now you can. Maybe you've learned how to orchestrate agents, find help, recover from failures, or compose tools. You may not know how to name the skill yet, but the repeated attempts and eventual success are evidence that you've learned something useful.
