---
title: Things I Learned - 24 May 2026
date: 2026-05-24T00:00:00+00:00
categories:
- til
description: I learned that Bitwarden may be heading toward a private-equity sale, Andrej Karpathy joined Anthropic, Qwen models trail the frontier, and I built a scraper to list Google-linked apps.
tags: [llms, google, transcription, open-source]
---

This week, I learned:

- BitWarden seems to be sneakily jacking up prices and going towards a PE sale. Might be time to shift out or self host. Sigh, I just migrated into it... [Source](https://blog.ppb1701.com/the-quiet-renovation-at-bitwarden)
- Andrej Karpathy has joined Anthropic. Likely to use Claude to build better Claudes - automating AI research. Also, it probably isn't a good time to build an AI education platform. [Claude](https://claude.ai/share/f9932e93-a632-4015-93f4-84359670f53c)
- The open-source Chinese models about 6 months behind frontier models. [Qwen 3.7-Max](https://qwen.ai/blog?id=qwen3.7) is [on par](https://arena.ai/leaderboard/text) with Claude 4.5 Opus (Nov 2025) and Gemini 3 Flash (Dec 2025).
- [Google basically became Gemini](https://blog.google/products-and-platforms/products/search/search-io-2026/). Entirely! I'm not sure there's a difference any more. Which means it will scrape websites and not send traffic through - just killing the search economy. But it's far more useful. [Claude](https://claude.ai/share/9f3f6172-2965-40a0-8b67-053a0769e455)
- I wanted a list of sites I log into with my Google Account. [Google's Linked apps](https://myaccount.google.com/connections) page does that. Unfortunately, I can't find a way to use [Google Takeout](https://takeout.google.com/) to export that data. So I wrote a [scraper](https://github.com/sanand0/scripts/blob/deb4c1ecbc93e03511ca264ce14d2977d01b7d90/googleconnections.py) which can be [single-shot prompted](https://github.com/sanand0/scripts/blob/deb4c1ecbc93e03511ca264ce14d2977d01b7d90/prompts/googleconnections.md) these days.
- As long as you remember to exhale, your chances of recovery from being ejected into space is pretty good for the first 15-60 seconds. [Gemini](https://gemini.google.com/share/4a15b461a2d3)
- I don't understand half the comments I read on LinkedIn. Earlier, I was able to separate good from bad. Now, I'm not sure if what I read is actually insight or idiocy. Is the AI use making their comments too smart or making my brain too dumb?
- "Pax Memoriae": peace of memory. Putting past conflicts to rest. The best part of it was, I learnt the phrase by typing "Pax" into VS Code and wasn't sure what to write next. Before I could search for it, GitHub Copilot completed it. I searched for what it meant, and it was _so apt_!
- Children's vision is worse than adults, but filter less and absorb ore irrelevant information than adults. This is useful for learning and surprise detection, but costly for focus, speed, and relevance. [ChatGPT](https://chatgpt.com/share/6a0aae2f-9b64-83ec-8db5-00c2f3a465b0)
- The word phobia comes from the Greek god of fear, Phobos, which is the name of one of Mars' moon. Deimos, the other moon, is the Greek god of dread/terror. They're the children of Ares (Mars), the god of war. Nice planet.
- On WhatsApp, I can type `@Meta AI` and then `/imagine` to have it draw an image. The quality is OK - not great, not terrible.
- Surprising but GPT Realtime Whisper (<a> new model) isn't as good as the older open-source Whisper models. Also, Gemini 3 Flash Preview is as good at transcription as Gemini 3.1 Pro Preview for up to medium-length text. [LLM Audio Transcription benchmark](https://pythonicvarun.github.io/llm-audio-transcription-benchmark/)
- Google Maps typically shows me a cycling time of 30 minutes when it take me 40 minutes and a walking time of 40 minutes when it take me 30 minutes. Either I walk much faster and cycle much lower than the typical person or Google Maps is not well calibrated to Singapore and India.

## Questions I was asked

[Week ending 24 May 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-05-24)

- **Question**: How do you give Claude and ChatGPT the same context?\
  **Answer**: Manually first. Type in one, paste into the other, attach the same files. Crude, but it works.
- **Question**: How do you structure prompts well?\
  **Answer**: Don't over-engineer. Write roughly, reuse, tweak when it fails, and store what you repeat.
- **Question**: How do you use AI to improve prompts?\
  **Answer**: Run post-mortems over conversations: what prompt would have improved this? Then simplify because post-mortems overfit and models change, making micro-changes less useful than broad intent.
- **Question**: What is MCP?\
  **Answer**: Model Context Protocol exposes tools and programs so agents can use them. Powerful, but not beginner material for a 2-minute explanation.
- **Question**: What are skills or SKILL.md?\
  **Answer**: On-demand permanent prompts. Use them for expert workflows where the base model typically fails out-of-box.
- **Question**: Once stored, do skills become context?\
  **Answer**: Yes, on demand. The model sees skill names and descriptions, then loads the right skill only when relevant.
- **Question**: How do you protect against hallucinations?\
  **Answer**: Make outputs falsifiable. Ask for evidence, quotes, links, checklists, tests, samples and independent challenge; use one model to red-team another.
- **Question**: Why do models get worse in long chats?\
  **Answer**: "Context rot" is known behavior. Start a new chat and carry forward a summary, memory or copied context.
- **Question**: Why can't ChatGPT retrieve old answers from memory/search?\
  **Answer**: You're probably not doing anything wrong. Chat search is weak; don't treat chat history as a serious knowledge system. Rename chats with keywords and search.
- **Question**: Are wrappers above LLMs a superior way to use AI?\
  **Answer**: Yes. They're called harnesses. ChatGPT and Codex are harnesses on top of the GPT models. Raw models are intelligence; harnesses give them tools, files, memory and workflows.
- **Question**: Which engineering domains look most ripe for AI?\
  **Answer**: Manufacturing, electronics and PCB design, 3D printing, CAD, and civil. Anything codified in software with an API or MCP-like control surface becomes automatable.
- **Question**: Why is engineering so ripe for AI?\
  **Answer**: The codification of engineering. Once the work already happens inside controllable software, an agent can observe, operate, and iterate.
- **Question**: Is a PhD topic safe when AI progress makes work obsolete so fast?\
  **Answer**: The bar has moved. What was a PhD three years ago may now be a freshman-with-AI project; choose bigger, faster, more foundational problems.
- **Question**: If AI can code and simulate, what are engineers and designers supposed to do?\
  **Answer**: Teach delegation. Give students problems where AI is unavoidable; they learn what to hand off and where the human jagged edge remains.
- **Question**: Is synthetic data versus real data the right framing?\
  **Answer**: No. Treat it as a continuum: start with real data, jitter it using realistic behavioral rules, and use synthetic edge cases to stress-test models.
- **Question**: What metric tells us whether an AI answer is good?\
  **Answer**: Three checks: are the inputs enough to answer, does (LLM) rubric think the answer is good, and ultimately, do the end users like it and find it useful?
- **Question**: What AI tools should we start using?\
  **Answer**: Just a few ChatGPT Plus ($20) monthly subscriptions are a good start. Don't buy specialized tools or annual licenses until people prove usage and value.
- **Question**: There is a lot of pressure on us to do AI; how should we explore what is possible personally and professionally?\
  **Answer**: Workshop mode, not discussion mode. Get hands-on, do real tasks, and feel what is possible and what is not.
- **Question**: If we double-check across five agents, is it one LLM with five methods or different models?\
  **Answer**: Both work. Same model with different prompts is useful; different models add diversity and usually improve consensus.
- **Question**: If you fire five models, aren't you paying five times per query?\
  **Answer**: Technically yes, but cost is collapsing. Use cheaper models for cross-checking; for most business questions, verification is now cheaper than manual rework.
- **Question**: How do you keep consistency when model versions change?\
  **Answer**: LLM Ops. Run automated eval suites before any model/version switch; don't silently promote a model just because it is new.
- **Question**: What about factual consistency when an LLM confidently gives a wrong answer?\
  **Answer**: Ask it for links with verbatim citations. You can programmatically check if the link and citation exist, and use another LLM to catch bad reasoning.
- **Question**: Should we build the knowledge graph first or start with agents?\
  **Answer**: Parallel. Agents deliver value immediately; knowledge graph and data engineering mature alongside with use.
- **Question**: How does a CTO manage a thousand agents?\
  **Answer**: Not as a thousand apps. Build one agent operating system or enterprise agent platform; each agent is a versioned configuration with registry, evals, observability, rollback and ownership. Azure Agent Registry might be an example.
- **Question**: Should the deliverable be software or the output of the software?\
  **Answer**: Prefer the output of the software. Software is WIP pipeline we keep improving; the client buys an outcome, not a depreciating asset that "their intern can build with Claude Code."
- **Question**: When the model misunderstands a prompt, how do we improve next time?\
  **Answer**: End with a post-mortem prompt: what did you misunderstand, what context was missing, and how should I prompt next time? Store that learning.
- **Question**: How do we decide whether AI-suggested use cases are valuable?\
  **Answer**: Don't sell use cases. Convert them into concrete actions backed by evidence, then email the business asking whether those actions matter.
- **Question**: Should we train custom models for film or design generation?\
  **Answer**: No. Frontier models improve too fast. Start with prompt engineering, reference images, image search, workflow automation, and human review. Train only when there is proprietary data, repeated demand, and a clear advantage - which is almost never.
- **Question**: Is hardware or physical engineering more AI-proof?\
  **Answer**: Better protected. AI accelerates design, simulation, planning, and documentation; physical experimentation, procurement, instrumentation, and validation still need humans.
- **Question**: How should I personally learn AI?\
  **Answer**: Use AI for everything. Record where it fails. That failure log becomes is where human expertise is needed - and is what we should teach.
- **Question**: How can engineering research leverage agentic AI?\
  **Answer**: Use AI to find what to research, do the literature search, do the actual research, write-up the research, verify the research, find publications, revise based on review comments, ... Practically every part of the chain.
- **Question**: Does AI kill creativity?\
  **Answer**: It redefines creativity. What we thought was creativity may die and these are the lower levels, but new higher levels forms emerge.
