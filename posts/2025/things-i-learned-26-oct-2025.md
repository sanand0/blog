---
title: Things I Learned - 26 Oct 2025
date: 2025-10-26T00:00:00+00:00
categories:
  - til
description: I analyzed my LinkedIn network with ChatGPT and explored how agents can use self-generated code as memory. I also tracked browser agent use cases like form filling and using LLMs for convex optimization research.
tags: [vibe-coding, codex-cli, linkedin, gpt-5]
---

This week, I learned:

- Before founding a place to do good, work in a place that does good and learn. [Ben Werdmuller](https://werd.io/using-technology-skills-for-positive-change/)
- What should we teach when vibe coding becomes good enough for non-coders? [Ethan Mollick](https://x.com/emollick/status/1979627762903392362)
  - Problem decomposition
  - Clear communication & spec writing
  - Core technical foundations: file systems, access control, networking, APIs, version control, data structures, databases, deployment
  - Software development skills: Debugging, Testing, Refactoring, Design patterns, UI/UX
  - Project management: requirements, prioritization, scoping, ...
- Codex CLI tips:
  - `codex --add-dir $DIR` lets you write into $DIR
  - `codex --full-auto` is the equivalent of `codex --sandbox workspace-write --ask-for-approval on-request`
- Terse code is not necessarily easier or harder for LLMs to write. It's about how unusual (or not aligned with training data) the code is. [Gabi Teoduru](https://medium.com/@gabiteodoru/dont-force-your-llm-to-write-terse-code-an-argument-from-information-theory-for-q-kdb-developers-04077c5b7038)
- How are people using browser agents like Comet / Atlas? [Simon Willison](https://x.com/simonw/status/1980713097024401548)
  - Most popular: YouTube video summaries with timestamps
  - Most useful: Form filling: Government forms, data entry, repetitive bureaucratic tasks
    - Foreign language navigation: Applying for pension in Korea, navigating sites in other languages
    - Time reporting auto-completion
    - Insurance claims: Reading policy documents and drafting appeals (successfully got claim reimbursed in India)
    - Compliance training click throughs
  - Next most useful: Shopping / planning
    - Energy provider comparison - Comet checked current plan vs competitors on Check24, calculated exact annual savings per provider
    - Financial tracking: Finding Amazon orders, tracking Airbnb spending with refund calculations, analyzing bank transactions
    - Trip planning: Mapping 50-100 places on Google Maps automatically
  - Interesting: Airport shuttle discovery - Found shuttle that user missed in manual searching
- [HubFS](https://github.com/winfsp/hubfs) mounts GitHub repos on the file system. Every file system action directly works on GitHub via a REST API. Useful for some scenarios but less useful for note-taking than something like [GitDoc](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.gitdoc) which offers a delayed sync.
- [Ernest Ryu solved an open problem in convex optimization using ChatGPT](https://x.com/ErnestRyu/status/1980760351479328781). Quotes:
  - ChatGPT is now at the level of solving some math research questions, but you do need an expert guiding it.
  - ChatGPT was really effective at accelerating my progress. This work took about 12 hours, spread over 3 days. In hindsight, the proof is really simple.
  - But I iterated through so many other strategies that didn't pan out, and ChatGPT crucially helped to quickly explore and eliminate those dead-end approaches. Also, the key successful steps were suggested by ChatGPT.
  - ChatGPT did not produce the proof in a single prompt. The process was highly interactive. It generated many arguments, roughly 80% of which were incorrect.
  - Yet some were genuinely novel to me. Whenever I recognized a novel idea, whether correct or only partially so, I distilled the key insight and prompted ChatGPT to develop it further.
  - My contribution:
    - **Filtering out incorrect arguments** and accumulating a set of correct facts.
    - **Identifying promising new lines** of reasoning and guiding ChatGPT to explore them further
    - Recognizing when a strategy had been fully explored and **deciding when to move on**.
  - ChatGPT's contribution:
    - Producing the final proof argument.
    - Significantly accelerating my (or our) exploration of the many dead-end arguments, rapidly ruling out approaches that did not work.
- Comparing the GPT 4.1 and 5 models at all different of reasoning, I've switched my default from GPT 4.1 mini to GPT 5 mini (medium). Far smarter for a slightly higher cost. [Artificial Analysis](https://artificialanalysis.ai/?cost=cost-vs-intelligence&models=gpt-5-low%2Cgpt-5-minimal%2Cgpt-5-nano%2Cgpt-5-nano-minimal%2Cgpt-5-mini%2Cgpt-5%2Cgpt-5-medium%2Cgpt-5-nano-medium%2Cgpt-5-mini-minimal%2Cgpt-5-mini-medium%2Capriel-v1-5-15b-thinker%2Cgpt-4-1%2Cgpt-4-1-nano%2Cgpt-4-1-mini)
- `python -m pdb -c continue script.py` or `uv run -m pdb -c continue script.py` runs a script and drops into pdb on unhandled exceptions (post-mortem). [ChatGPT](https://chatgpt.com/share/68f9b890-ba0c-800c-8a29-48245a41ca5e)
- Technology removes constraints. We then do what we really value. [Claude](https://claude.ai/chat/f3a2606f-203c-41cc-b50f-62504483504f)
  - When writing became digitized, we stopped cared about spelling/handwriting for its own sake. Spelling bees and handwriting classes declined. "ur" is acceptable.
  - When fitness tracking became easy, many just track, few exercise more. Few people value exercise
  - When GPS became ubiquitous, we stopped learning geography. Most value arriving, not knowing
  - When photography became unlimited, most captured moments. Few perfected shots
- I had Codex scrape my ~2,000 pending invites on LinkedIn and asked ChatGPT to analyze it. Here are learnings: [ChatGPT, private](https://chatgpt.com/c/68f72899-5814-8320-9d02-88ce06257fd8)
  - Power-law. 5% of inviters account for ~42% of all common connections. Top 10 people alone for ~20%.
  - IITM student invites are high (~14%), but with 0-2 common connects, i.e. distant strangers.
  - EdTech is tiny in count but has the highest common connections per person (outlier-sensitive but real).
  - Among ≥20-commons, many hold VP/Head/Site-Lead titles in Data/AI or GenAI (not just recruiters).
  - GenAI people are 7-8% and steady across months. Not a useful signal to prioritize.
  - Premium ~ Senior. Premium accounts show ~40% senior titles vs ~29% for non-premium.
  - Finance invites have higher seniority rate and more common connects than healthcare.
  - Followers have higher common connections (~6 vs ~4).
- ⭐ Memory can be code. Agent memory is anything it choose to persist. Agents can write code on the fly to automate tasks, save them, and serve the code on the next request, potentially modifying the code as required. This is like the conscious mind saving a habit for the subconscious to execute fast.
- Finally: Microsoft Office has an agent mode that lets you talk to it and do stuff. [The Verge](https://www.theverge.com/news/787076/microsoft-office-agent-mode-office-agent-anthropic-models)
