---
title: Things I Learned - 05 Oct 2025
date: 2025-10-05T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- Wrong answers are useful if you discover why they said that. Conversation is a game where you CO-CONSTRUCT common ground. [Mike Caulfield](https://mikecaulfield.substack.com/p/when-wrong-llm-answers-get-you-to)
- BMTC hourly data from Bangalore Metro is available via RTI. [Vivek](https://github.com/Vonter/bmrcl-ridership-hourly)
- "Find evidence for and against" improves LLM responses far more than "Are you sure?" [Mike Caulfield](https://mikecaulfield.substack.com/p/is-are-you-sure-is-a-bad-follow-up)
- [SSH3](https://github.com/francoismichel/ssh3) is an emerging SSH alternative that's written on top of HTTP/3. It supports OAuth2, OpenID Connect, and HTTPS for certificates.
- Cholesterol has become a victim of its own success. We give statins to those with high LDL. So most people who have heart attacks have lower-than-natural cholesterol. Inflammation (HS-CRP) is now the strongest predictor of heart attack ([American College of Cardiology](https://www.empirical.health/blog/inflammation-and-heart-health/)). The usual stuff reduces HS-CRP: no sugar/carbs, veggies, nuts, green tea, turmeric/black pepper, weight loss, exercise, sleep, meditation.
- ⭐ The beginner mindset: scrub your instincts and don't let life experience cloud you. This takes effort. Hold on to naivette and escape cynicism. [The Knowledge Project: Barry Diller](https://fs.blog/knowledge-project-podcast/barry-diller/)
- Forecasts give comfort. They may not be good but they feel safer than instinct. [The Knowledge Project: Barry Diller](https://fs.blog/knowledge-project-podcast/barry-diller/)
- My laptop's mic is much better than my phone's mic, surprisingly. When recording conversations, it's better to leave my laptop open and record than use the phone's recording app.
- ⭐ Here are the major not-immediately-obvious LLM megatrends/superpowers I see.
  - Swarms. Ask for dozens of solutions in parallel. Merge, rank, auto-debate, converge.
  - Personalize at Scale. Create feedback, designs, excerpts/summaries, ... tailored to EACH person at scale.
  - Computer use. Agents operate UIs like a human (browser, apps).
  - LLM-as-a-judge. Use AI to validate ever-increasing AI generated output.
  - Synthetic data. Create realistic data for prototypes, testing edge cases, market research simulation, training data, ...
  - Code on demand. Ask for outcomes directly. Agents code _on the fly_ to get there, in data science, research, management, ...
  - Style transfer. Copy a master's style of drawing, coding, writing, ... creating an army of their apprentices.
  - Multi-modality. Native voice/video/screensharing and long-context perception
  - Citizen experts. Non-expertise is not a barrier. Amateurs can create expert-level films, music, software, reports, ...
  - Long-context LLMs. Growing context size lets us process entire repos, legal libraries, personal lifelogs, ...
  - Memory. Assistants learn per-person / per-team. Cuts prompt, builds knowledge.
  - Agent-to-Agent. Agents consuming content (e.g. `llms.txt`), agents calling agents (sub-agents, A2A protocol, ...)
  - Real-world tools. Write reports, send emails, shop online, use computer, control devices, ...
  - Jagged frontier. AI is great at certain things but terrible at others. This frontier is unknown and shifting rapidly.
  - Lethal trifecta. You can only have 2 out of these 3: private data, untrusted content, and external communication.
  - Edge/Private AI. Small models on private cloud compute.
  - Authenticity. What content is authentic? What's slop? What's fraud? Are AI twins liable?
  - AI Governance. Strict liability, transparency mandates, state control, ...
  - Not sure about or haven't seen enough of these:
    - Data / workflow as the moat
    - AI native business models
    - AI digital-divide
- ⭐ What I'd like to do next, maybe, is build a boutique "AI Studio". Small group of good people coding delightful AI problems. Something that doesn't scale.
- [GLM models can be used with Claude Code](https://docs.z.ai/scenario-example/develop-tools/claude). At $3/month and a quality close to Claude 4 Sonnet, this is a good deal. But the effort of adding a new subscription is too high for me. I'd rather use it via OpenRouter which is doesn't support an Anthropic API end point at the moment.
- [`typst`](https://github.com/typst/typst) is a good LaTeX alternative. Markdown-like syntax with fast rendering. Mostly useful for researchers using LaTeX. But publishers / journals don't accept typst often.
- [`libSQL`](https://github.com/tursodatabase/libsql) is an SQLite compatible fork with remote access, replication, ALTER TABLE to modify columns, random ROWID, etc. It supports the same externsions. The maintainers are working on [`turso`](https://github.com/tursodatabase/turso) - a SQLite compatible improvement with async, vectors, change data capture, etc. (still in alpha). But because of this, I'm a bit uncertain about the future of `libSQL`.
- ⭐ LLM benchmarks show a correlation of ~0.5, hinting at a common theme of intelligence. Correlations in coding & science are particularly high. [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3lzfm52q34k2n). Reminds me of [student marks correlations](https://www.s-anand.net/blog/correlating-subjects/). Strong correlation clusters (physics, chemistry, biology, mathematics, computer science) with the weaker correlations going down to ~0.5. What does it indicate? LLMs learn like people? Knowledge areas cluster? Humans write benchmarks like exams?
- [Dayflow](https://github.com/JerryZLiu/Dayflow) records your screen at 1 fps and uses Gemini to summarise your activity every 15 min. Has low CPU usage.
- ⭐ [Code Mode](https://blog.cloudflare.com/code-mode/) is a smart way to use MCPs and a very likely future direction. Using LLMs to write code to call MCPs rather than directly.
- Cloudflare supports an [AI Index](https://blog.cloudflare.com/an-ai-index-for-all-our-customers/) which will eliminate the need for a lot of custom RAG engineering.
