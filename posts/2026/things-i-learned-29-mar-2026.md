---
title: Things I Learned - 29 Mar 2026
date: 2026-03-29T00:00:00+00:00
categories:
- til
description: I learned about Meta and YouTube's addictive-design fines, the growing “LLM psychologist” job title, OpenAI's Astral acqui-hire, faster AI chips, and practical patterns for AI coding agents.
tags: [personal-update, llms, ai-coding-agents, hardware-trends]
---

This week, I learned:

- [The Kids Should See This](https://thekidshouldseethis.com/) - great collection of videos for curious people. [Thej](https://thejeshgn.com/2026/03/27/weekly-notes-13-2026/)
- A jury fined Meta and YouTube $4.2m and $1.8m for building addictive features in their products. That's a first. [NY Times](https://www.nytimes.com/2026/03/25/technology/social-media-trial-verdict.html)
- "I think AI-type tools will actually revolutionize the experimental side of math, where you don’t care so much about individual problems and the process of solving them, but you want to gather large-scale data about what things work and what things don’t." [Terence Tao](https://www.dwarkesh.com/p/terence-tao#:~:text=gather%20large%2Dscale%20data)
- The [hedonic treadmill](https://en.wikipedia.org/wiki/Hedonic_treadmill) (which roughly quantifies a Buddhist principle) says that we revert to a [happiness set point](https://en.wikipedia.org/wiki/Hedonic_treadmill#Happiness_set_point) (which varies by individual). Worse, those who experience a high kick (e.g. a lottery) don't get enough kick from normal wins (contrast effect) -- [Interactive explainer](https://gemini.google.com/share/9e8a904b34bb). <!-- https://gemini.google.com/app/b676e7571e5cbc85 --> The happiness neutral
- As of today, a [LinkedIn search for "llm psychologist"](https://www.linkedin.com/search/results/people/?keywords=%22llm%20psychologist%22) lists 9 people. I'm not alone!
  - [Anand S](https://www.linkedin.com/in/sanand0/), LLM Psychologist, Singapore, Singapore
  - [Anshul Saxena, PhD](https://www.linkedin.com/in/analyticsanshul/), AI Advisor & Trainer | Technology Strategist | LLM Psychologist | Currently teaching humans, machines & business to work smarter through Generative AI and Quantum Computing | 15+ Years Experience, Pune, Maharashtra, India
  - [Charitarth (Chad) Sindhu](https://www.linkedin.com/in/chadofficial/), LLM Psychologist / Fractional Business & AI Workflow Consultant/ Digital Nomad, Tokyo, Japan
  - [Lancelot Salavert](https://www.linkedin.com/in/lancelotsalavert/), LLM Psychologist, Barcelona, Catalonia, Spain
  - [Lior Dor(Durahly)](https://www.linkedin.com/in/lior-durahly/), Team Lead | Bug Banisher | Ex 8200, Tel Aviv District, Israel. Past: R&D Team Lead and **LLM** **Psychologist** at Superwise | A Blattner Tech Company
  - [maxime bodereau](https://www.linkedin.com/in/maximebodereau/), Lead Creative Art Director | UX Forensics | Ai LLM Psychologist | Visual Alchemist | Codesmith | Brandologist | Full Stack Designer, Nantes, Pays de la Loire, France
  - [Mei Chen 🦋](https://www.linkedin.com/in/chenml/), LLM Psychologist | Lead Product Engineer | Delivering Agentic Experiences, Toronto, Ontario, Canada
  - [Shoshannah Tekofsky](https://www.linkedin.com/in/shoshannahtekofsky/), LLM Psychologist at AI Digest, Zwolle, Overijssel, Netherlands
  - LinkedIn Member, LLM, psychologist, mediator, Prague, Czechia
- [OpenAI acquired Astral!](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/). This will likely slow down the new wonderful tools accelerating the Python ecosystem. Like with [PromptFoo](https://openai.com/index/openai-to-acquire-promptfoo/) and [OpenClaw](https://steipete.me/posts/2026/openclaw), this seems to be about talent. The "acqui-hire" mode seems a _clear_ niche career path now, and an alternative to getting hired (you get a much higher salary) or getting acquired (you take on much higher risk).
- [quickjs-emscripten](https://www.npmjs.com/package/quickjs-emscripten) lets you run isolated JS code securely in the browser, CloudFlare workers, NodeJS, and Deno. It compiles to WASM. @sebastianwessel/quickjs is a higher-level TS wrapper. [Simon Willison](https://github.com/simonw/research/tree/main/javascript-sandboxing-research)
- [Manyana](https://bramcohen.com/p/manyana) is a CRDT based version control system. It sounds like a good idea but I'm sceptical because merge conflicts are a "what should I do" problem more than "how". With [agents doing more merge conflict management](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/), I am not sure this will offer a concrete benefit - but probably no harm either.
- [LLMs are able post-train LLMs on new topics](https://posttrainbench.thoughtfullab.com/). They're improving fast. [Jack Clark](https://jack-clark.net/2026/03/16/importai-449-llms-training-other-llms-72b-distributed-training-run-computer-vision-is-harder-than-generative-text/)
- [Vibe Coding Fixer](https://www.linkedin.com/search/results/people/?keywords=vibe+coding+fixer) and [AI Slop Cleaner](https://www.linkedin.com/search/results/people/?keywords=ai+slop+cleaner) are real job descriptions - which are morphing into enterprise offerings. But I still seem to be the only official [LLM Psychologist](https://www.linkedin.com/search/results/people/?keywords=llm+psychologist)
- Notes from [AI Services - Wrong Mental Models, Right Moment](https://mtrajan.substack.com/p/ai-services-wrong-mental-models-right):
  - AI services has 3 markets. Automatable work: vanishes in 2 years. Human-in-the-loop work: sustains. Judgement-driven: grows in importance.
  - YC: don’t sell access to a tool for $50 a month, use the AI yourself and sell the finished work for $5,000.
  - Sell output. Price on outcome. Sell to business, not IT.
  - Sell accountability: proven success, with your guarantee.
  - Sell authenticity: a brand story representing uniqueness, character, ... or whatever... something people respect.
- Data transfer between GPU and memory is a bottleck and three approaches are emerging. [#](https://mtrajan.substack.com/p/inference-blindness)
  - [Taalas](https://taalas.com/the-path-to-ubiquitous-ai/) is etching LLMs into the chip. Llama 8b runs at 17,000 tok/s (H200 is at 230 tok/s).
  - [d-Matrix](https://www.d-matrix.ai/announcements/d-matrix-unveils-corsair-the-worlds-most-efficient-ai-computing-platform-for-inference-in-datacenters/) is moving compute into SRAM memory chips. 30,000 tok/s for Llama 70b. Cerebras and MatX are similar: memory-oriented.
  - [FuriosaAI](https://furiosa.ai/blog/lg-ai-research-taps-furiosaai-to-achieve-2-25x-better-llm-inference-in-production-vs-gpus) minimizes data movement. Groq and Sambanova are similar.
  - But in the long run, commodity technology usually beats integrated stacks.
- [GPT 5.4 Nano ($0.2/MTok) and Mini ($0.75/MTok)](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) are good options for bulk OCR, transcription, etc. as cost and quality comparable alternatives to Gemini Flash Lite and Gemini Flash. [They can describe 75K photos for $50](https://simonwillison.net/2026/Mar/17/mini-and-nano/). Both models are better than GPT-5 Mini on most benchmarks.
- Cool [AI coding agent git prompt fragments](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/):
  - Use git bisect to find when this bug was introduced: ...
  - Find and recover my code that does ...
  - Sort out this git mess for me.
  - Rewrite history removing ...
  - Split the last commit into multiple commits grouped logically.
  - Start a new repo at ... and build just this module ... based on ... with a similar commit history copying the author and commit dates.
- [Campaigns Are Knowledge Workers and the Tools Just Caught Up](https://matthodges.com/posts/2026-01-07-ai-agents-campaigns/). A powerful framing. I saw this in action a few days ago when a friend was able to automate an outbound campaign with Claude Code.
- [EARS (Easy Approach to Requirements Syntax)](<https://www.google.com/search?q=EARS+(Easy+Approach+to+Requirements+Syntax)&oq=EARS+(Easy+Approach+to+Requirements+Syntax)>) is a simple structure for requirements. For [example](https://github.com/github/spec-kit/issues/1356), "Users should be able to drag tasks between columns. The app needs to work offline too. Handle errors gracefully." becomes the following - which AI can convert to and is easier to spot errors in. State machines and decision tables are useful alternatives, too.
  - **REQ-001** (Event): When the user drags a task card to a different column, the system shall update the task status to match the destination column.
  - **REQ-002** (State): While the application is offline, the system shall store task updates in local storage.
  - **REQ-003** (Event): When the application reconnects, the system shall synchronize locally stored updates with the server.
  - **REQ-004** (Unwanted): If synchronization conflicts occur, then the system shall display a resolution dialog to the user.
- As of now, avoid using Claude.ai to create (large) visualizations. It runs forever and exhausts credits without generating anything. Claude Code works much better for this.
