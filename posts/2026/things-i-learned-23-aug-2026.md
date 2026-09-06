---
title: Things I Learned - 23 Aug 2026
date: 2026-08-23T00:00:00+00:00
categories:
  - til
description: I learned about DuckDB 2.0's CONNECT command, EQ-Bench's model-behavior comparisons, how ChatGPT Work layers on Codex, and running Gemma 4 locally, with reflections on AI, work, and taste.
tags: [llms, ai-agents, coding-agents, prompt-engineering]
---

This week, I learned:

- [DuckDB 2.0](https://duckdb.org/2026/08/17/duckdb-20-highlights) adds a `CONNECT` command that can connect to databases like MySQL, PostgreSQL, etc. making DuckDB the only DB client I need.
- [EQ-Bench](https://eqbench.com/index.html) evaluates models on capabilities like: does it follow direction, does it challenge you, how good are its insights, does it build rapport, etc. Very interesting to see that the Gemini models are the most "yielding" to your pressure  and "validating" your beliefs (Anthropic's are the least) while OpenAI models are the most "directive" (give concrete actions) #ForNow. There are other benchmarks such as [Creative writing](https://eqbench.com/creative_writing.html) which Opus 5, Kimi K3, and GPT-5.6 Sol lead #ForNow.
- OpenRouter offers several [models at a discount](https://openrouter.ai/collections/discounted-models). #ForNow, [GPT-5.6 Sol](https://openrouter.ai/openai/gpt-5.6-sol) is at a 50% discount, [DeepSeek v4 Pro](https://openrouter.ai/deepseek/deepseek-v4-pro) at 62%, and [Gemini 3.7 Flash](https://openrouter.ai/google/gemini-3.7-flash) at 75% discount. There's also a [Free Models](https://openrouter.ai/collections/free-models) collection that #ForNow includes [Nemotron 3 Ultra](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free) and more.
- For a few years, I've been feeling useless, that I don't contribute anything tangible to my organization. No measurable metric I've improved. Today, it strikes me that this is a _good_ thing if I don't want to be fired. As AI eats up more of our work, measurable contributions naturally shrink (AI does more, you do less/different work), and the vague "Oh, he's probably doing some good" is a safer bet than "He contributed 10% to this metric last year, this year it's 1%, can we justify his cost?" (I'm sure marketers will come up with a good term to cover this feeling of uselessness that is actually a good thing.)
- ChatGPT Desktop - Work is a layer on top of Codex #ForNow (which I sort-of expected, but the session logs confirm this). It _adds_ instructions that cover: <!-- https://chatgpt.com/c/6a85538f-7f48-83e9-a6b0-fc5cfbe09600 -->
  - Memory: from `memory_summary.md`, `MEMORY.md`, rollout summaries, and saved skill notes. Recheck decaying ones, mention if unverified.
  - Folders: Temo work in `work/`, final in `outputs/`, local files use absolute paths.
  - Coordination: How to start, fork, inspect, message, wait for, rename, ... Codex tasks, how to use subagents.
  - Automations: Available tools for reminders, schedules, monitors, follow-ups, and wake-ups.
  - Knowledge management: known project → memory; specialist task → skill; external object → connector; subtask → subagent; recurring work → automation; finished artifact → Work UI primitive.
  - Presentation: Use shell/scripts internally but hide it, describe outcomes in user terms.
  - Apps/Connectors: Gmail, Drive, GitHub, Dropbox, etc.
  - Skills: via `SKILL.md`
- Neither ChatGPT Work nor Claude Work can read the ChatGPT / Claude chat conversations. But the chat conversations can access past conversations via "Memory". That's a pity, and one of the reasons I'm more often on "chat" than on "work" - it can refer to my past chats automatically, which helps build a kind of unstructured knowledge base. The other reason is that, at least on ChatGPT, chat does not consume usage limits #ForNow. ChatGPT work and Claude - both chat _and_ work - consume usage limits.
- Weird that there's a "make a lot of money" button and nobody's pressing it (take your SaaS, make it headless, let agents use it, charge per interaction esp for enterprises). [Thariq](https://x.com/i/status/2089844723691479333)
- AI is accelerating discoveries in cyber (definitely) and maths (reasonably) but not as much in algorithms. [METR](https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/)
- "Match your prompt style to the desired output." [Clear guidance from Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#control-the-format-of-responses) that "The formatting style used in your prompt may influence Claude's response style." [OpenAI says something similar](https://model-spec.openai.com/2026-08-18.html#be_professional) - adapting implicitly to the user's tone. But this is not a very strong signal - examples are better guides.
- [Why model routing must be in the harness](https://x.com/_AbhaySinghal/status/2088361241928732705). Makes perfect sense. "Only the harness can judge when a model switch is worth the cache miss." I'm sure some popular harness (like OpenCode, Codex, Claude Code) will enable an "auto model" mode that'll pick and change the model by itself by the end of the year.
- Microsoft Print to PDF can, sometimes, [generate PDFs with no highlightable](https://learn.microsoft.com/en-ie/answers/questions/2359651/words-in-print-to-pdf-documents-cant-be-highlighte) or [selectable text](https://learn.microsoft.com/en-us/answers/questions/3894700/microsoft-print-to-pdf-makes-text-unselectable-in) - all fonts get converted to paths. A crude solution is below. This is a poor solution but often good enough for an LLM to process. (Of course, if you're passing it to an agent, you could just upload the file and it'll figure it out.)
  ```bash
  sudo apt install ocrmypdf tesseract-ocr
  ocrmypdf --output-type pdf input.pdf ocr.pdf
  pdftotext ocr.pdf -
  ```
- When my train neighbor started talking to me (asking personal questions but was self-aware, rambling but was partly interesting), I asked if he was an extrovert. He said "No". People who talk a lot can still be introverts if they're: <!-- http://localhost:8080/sessions/pi%3A01a00f16-9425-7f0c-9952-9c3f7e7cab9d -->
  - socially competent (like me at work)
  - in "performance mode" (like me when I'm on stage)
  - are high energy and engaged by topics (maybe him - or me when, like now, when I just HAVE to tell the flight attendant Ollama + Gemma 4 + Pi answering a psychology question is a delight!)
  - ambiverts (maybe him)
  - not self-aware and are mistaken (maybe him)
- `ffmpeg` can embed subtitles. `ffmpeg -i video.webm -i subtitles.srt -map 0:v -map 0:a? -map 1:0 -c:v copy -c:a copy -c:s srt -metadata:s:s:0 language=eng -metadata:s:s:0 title="English" -disposition:s:0 default output.mkv` adds `subtitles.srt` to `video.webm` and creates `output.mkv` with embedded subtitles. Note: On VLC, MKV works better than WEBM if you want to embed subtitles. On the browser, you need to use the `<video>` tag with a `<track>` tag to display subtitles. <!-- https://chatgpt.com/c/6a8294f9-59c4-83ee-8a80-cee9b33beaae -->
- `ffmpeg` can _burn_ subtitles. `ffmpeg -i video.webm -vf "subtitles=subtitles.srt" -c:v libvpx-vp9 -crf 30 -b:v 0 -c:a copy output.webm` re-encodes the video with subtitles added to the video.
- `ffmpeg` can offset subtitles. For example: `ffmpeg -itsoffset 10 -i input.srt -c copy output.srt` creates `output.srt` with subtitles starting 10 seconds later than `input.srt`.
- When I hear my father's tales from his childhood, I'm struck by how much India moved forward in half a century on child mortality, consumerism, and communication (mobiles). Also surprising are what feels the same: legal system, travel (trains made it easy), food (tasted better, then), entertainment (theatres made it easy), gardening, education (scholarships made international study more accessible than I thought),
- I asked ChatGPT how I adapt my message based on the audience. It discovered that I tailor messages to the audience's (A) Objectives (B) Examples (C) Expertise - e.g. tell vs ask (D) Risk appetite. But what's distinctive is that I often surrender, i.e. I don't defend my view, but drop it and run with _their_ framing. <!-- https://chatgpt.com/c/6a8265ad-8688-83ee-8675-254ca6b0428e -->
- "People with taste are picky. The only way to make money is by satisfying those who can’t discern quality." [Adrian Hanft](https://medium.com/swlh/the-zombie-mobile-b03932ac971d). I've been telling people that taste is our differentiator against AI. And yes, it's a fickle differentiator. I mean, how do you build a taste that thousands or millions will adopt? Or... is taste marketed more often than organically adopted, in which case, persuasiveness matters more than taste? But either way, unless most people disagree with you, you're building conformity, not taste.
- On a flight, I tried `ollama launch pi --model gemma4:e4b-it-qat`. It's a reasonably sensible model. Power consumption is high, though. I was at about 8 watts with ~7 hours of battery life. While running, power spiked to ~50W (1.5h) and settled down to ~12W (4h) when idle. The `llama-server` process consumes some CPU/GPU even when idle, but I couldn't get it back to the ~8W even after `ollama stop`. (It eventually _did_ return to 8W after an hour. Not sure why.) When I tried again on 21 Aug, it went up from 8W (8h life) to 28W (3h life) and back to 8W, so looks like when idle, it _doesn't_ consume power. I look forward to using local LLMs more!
- Pain is good. Struggle is good. Stretch is good. Not new. But worth reminding, worth seeking.
- [T3 Code](https://t3.codes/) is a coding agent orchestrator. It lets you "remote control" multiple coding agent sessions across systems. The ecosystem of tools _around_ coding agents is growing. Observability, e.g. [AgentsView](https://github.com/kenn-io/agentsview), is one such area.

## Questions I was asked

[Week ending 23 Aug 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-08-23)

- **Question**: How do I safely let an agent modify my files when it could get things wrong?\
  **Answer**: Make backups and let it work on a copy. Try it five or ten times; once it repeatedly earns your trust, gradually remove the safety net.
- **Question**: When should I turn an ad-hoc agent workflow into automation?\
  **Answer**: If I run it once every two months, I don't mind the agent writing the code again. If it's every two weeks or two days, save the script and automate it.
- **Question**: How do we decide which agents to train when client problems keep changing?\
  **Answer**: Decouple the agent from the skill. Keep the skill intelligence agnostic - it's not about correcting agent errors but about transferring context it won't have. Keep a central folder of skills with one-line descriptions; whichever agent people use can scan it and pick the relevant skills.
- **Question**: Which part of the current agentic AI narrative is overhyped?\
  **Answer**: GraphRAG is definitely overhyped. Prompt engineering is outdated; harnesses and agentic loops are not overhyped yet.
- **Question**: To make agentic software development scalable, do we need a standard framework or just give everyone Cursor and let them figure it out?\
  **Answer**: Install Cursor for everyone and let them figure it out. Share lightweight enterprise guidelines as skills, but give every instruction an expiry date and a small benchmark so you can remove it as agents learn to handle it themselves.
- **Question**: If frontier video models fail on physics and action scenes, how should we fine-tune them with our proprietary video data?\
  **Answer**: Don't solve the physics problem; solve a much narrower action-block problem. Build reusable filtering and fine-tuning pipelines so the next frontier model can replace the base model and you train only on what it still cannot do; no manual annotations.
- **Question**: Will AI take all the tech jobs in the next five to six years?\
  **Answer**: Yes. And so what? AI will take a significant number of existing jobs, and we'll create new ones because our desires and competition don't disappear; figure out which new work takes you further before your neighbor does.
- **Question**: How did you come up with this conceptual clarity about what to do?\
  **Answer**: I didn't. Pretend to have clarity, ask AI everything and use its answers, then do it so often and fail repeatedly that you get a feel for what works. Quantity beats quality like crazy.

## Mistakes I made

[Week ending 23 Aug 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-08-23)

- I said **Claude Code auto mode made the risk of unintended actions "negligible," and later said "as of this month, it won't make a mistake" with a "90% chance" it would preserve undoability.**\
  **Correction**: I was far too confident and invented a probability I could not support. Agent safeguards are probabilistic. Anthropic's own auto-mode evaluation reported a 17% false-negative rate on real "overeager" dangerous actions. For destructive local operations I should still use backups/version control, limit permissions and retain review where the blast radius matters. Evidence: [Anthropic — How we built Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode?_bhlid=bb5b0c065a6a8790a89389462f16ab1ea5010c5e&utm_source=chatgpt.com)\
  **HIGH · OVERSTATED**
- I said **"there is no difference between Codex and ChatGPT Work" and that Work is essentially Code with a lighter, more marketable name.**\
  **Correction**: Work uses Codex technology, so the overlap is real, but they are distinct experiences. Work is aimed at longer multi-step research, analysis and deliverables; Codex remains specialized for software development and has separate workflows/history. Evidence: [OpenAI — Introducing ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/?_bhlid=b229619b8c31d33de07faa7f27a4a4f2202c57cd&utm_source=chatgpt.com) [OpenAI — ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275/?utm_source=chatgpt.com)\
  **MEDIUM · OVERSTATED**
- I said **"1960s is when Studio Ghibli starts trying to catch up" with Disney.**\
  **Correction**: Studio Ghibli was established in 1985. Evidence: [Studio Ghibli — company history](https://www.ghibli.jp/profile/?utm_source=chatgpt.com)\
  **LOW · FALSE**
- I said **"I'm yet to find a use case where fine-tuning is worth it ... Zero. Out of thousands of use cases ... it was never worth it" and "in neither case is fine-tuning useful."**\
  **Correction**: "I haven't personally found an ROI-positive fine-tuning case yet" would have been defensible; "never useful" is not. Fine-tuning remains a standard adaptation technique even for open-weight models; Meta's official Llama cookbook includes fine-tuning and parameter-efficient fine-tuning recipes. Evidence: [Meta — official Llama Cookbook](https://github.com/meta-llama/llama-cookbook?utm_source=chatgpt.com) [Meta — Llama fine-tuning overview](https://github.com/meta-llama/llama-cookbook/blob/main/getting-started/finetuning/LLM_finetuning_overview.md?utm_source=chatgpt.com)\
  **HIGH · OVERSTATED**
- I referred to **"ChatGPT's share price" falling** if a privacy controversy were real.\
  **Correction**: OpenAI was not publicly traded, so there was no public ChatGPT/OpenAI share price to fall. I should have referred to OpenAI's private-market valuation, tender/share price, investor appetite or commercial impact. Evidence: [Reuters — OpenAI's planned IPO](https://www.reuters.com/business/openai-expects-go-public-within-next-year-information-reports-2026-06-10/?utm_source=chatgpt.com)\
  **MEDIUM · FALSE**
- I said **Meta's glasses can record someone "without you getting even an inkling or a notification."**\
  **Correction**: Meta's AI glasses have an outward-facing capture LED that blinks while photos or video are being captured; current models disable the camera if the LED is covered or disabled. The indicator may be easy to miss, but there is one. Evidence: [Meta — AI glasses privacy and capture LED](https://about.fb.com/news/2026/07/metas-ai-glasses-your-questions-answered/amp/?utm_source=chatgpt.com)\
  **MEDIUM · FALSE**
- I said **Alexa sends audio to Amazon only if you say "Alexa."**\
  **Correction**: The wake word is the normal trigger, but it is not an absolute rule. Follow-Up Mode allows requests without repeating the wake word, and Amazon says Alexa can sometimes mistake unrelated speech for a follow-up request. Evidence: [Amazon — Alexa Follow-Up Mode](https://digprjsurvey.amazon.com/csad/help/node/GX7EJ9WHEPYBV94J?utm_source=chatgpt.com) [Amazon — Alexa FAQs](https://digprjsurvey.amazon.com/csad/help/node/201602230?utm_source=chatgpt.com)\
  **MEDIUM · OVERSTATED**
- I said **"In India, most children are born on 1st June, which is the admission cutoff date for most schools."**\
  **Correction**: There is a real historical June-1 anomaly in **recorded** dates of birth in parts of India: when exact birth dates were unknown, some schools/parents used June 1 for admission records. That does not mean most Indian children are actually born on June 1, and the cutoff is not universal nationwide. Evidence: [Times of India — “Admit it, June 1 isn't your real b'day”](https://timesofindia.indiatimes.com/city/ahmedabad/admit-it-june-1-isnt-your-real-bday/articleshow/711643.cms?utm_source=chatgpt.com)\
  **LOW · OVERSTATED**
