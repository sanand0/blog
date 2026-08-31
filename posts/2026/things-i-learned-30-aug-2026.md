---
title: Things I Learned - 30 Aug 2026
date: 2026-08-30T00:00:00+00:00
categories:
  - til
description: This week I switched from AnyDoc to Docling for PDFs, found a workaround for screenshots while using rofi, compared task-based AI benchmarks, and noted AWS's planned DuckDB acquisition.
tags: [benchmarking, ai-agents, developer-tools]
---

This week, I learned:

- I know that fact-checking 2000 page PDFs is error-prone, so'd do it manually for a few pages, then refine. Agents would know this if they've tried and failed and added it to their memory systems. So I intervene when agents don't remember well (increasingly rare) or I think they haven't seen it before (again, increasingly rare). My prompts guard against these - but I shouldn't habitualize these - they'll be needed less in future.
- [rofi](https://github.com/davatorium/rofi) - a Linux menu app I use for all kinds of things - makes it hard to take screenshots because it takes over focus and I can't send the `PrtSc` or other keys to the screenshot apps. So I use [`flameshot full --delay 3000 --path ~/Downloads/screenshot.png`](https://flameshot.org/) to take a screenshot (of the last region it used) 3 seconds later, and quickly activate `rofi` in-between. (The [docs](https://flameshot.org/docs/advanced/commandline-options/) say `flameshot full` captures the full screen. For me, it captured my last region.)
- ChatGPT can now connect to multiple GMail accounts in paid plans. [X](https://x.com/jxnlco/status/2093223754054922685?s=20)
- [AWS to acquire DuckDB](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws). DuckDB is one of my favorite tools today and is improving at a rapid pace. I guess that will continue in the short run - hope it lasts long enough for a worthy successor.
- I use [GoatCounter](https://goatcounter.com/) to track my website traffic. It doesn't capture domains (only paths), so I just use a [code snippet](https://github.com/sanand0/imdb/commit/9c235b25d80c92ec23d0939689ced889a0a8b142) to log `https://sanand0.github.io/SITE/...` as `/@SITE/...` - the `@` makes it easy for me to see that it's from a GitHub page.
- I switched from [anydoc](https://github.com/firecrawl/anydoc) to [docling](https://github.com/chronicle/docling) as my default PDF to Markdown converter. Docling is even better than AnyDoc #ForNow.
- Based on my Codex usage, [ChatGPT recommended](https://chatgpt.com/share/6a8bfcf3-57f8-83ee-b29d-87fb3a07a996) that I not create custom subagents (my setup already used subagents a fair bit last month), but rather, just use `default_subagent_model = "gpt-5.6-luna"` (which is a remarkably good model for its price #ForNow). <!-- https://chatgpt.com/c/6a8bf959-df54-83e8-ab71-9aa72f3d2150 -->
- [Artificial Analysis](https://artificialanalysis.ai/) hosts [several useful task-based evaluations](https://artificialanalysis.ai/evaluations/). Here are some the fronter leaders #ForNow: <!-- https://chatgpt.com/c/6a8bb008-c394-83ee-aa9b-439546f8cb1d -->
  - [GDPVal](https://artificialanalysis.ai/evaluations/gdpval-aa#:~:text=v2%3A%20Elo%20vs.-,Cost%20per%20Task,-GDPval%2DAA%20v2) is good for realistic tasks. Again, GPT 5.6 Luna models have captured most of the low-cost fronter.
  - [EnterpriseOps Gym](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa?eval-cost=score-vs-cost-per-task#:~:text=AA%3A%20Score%20vs.-,Cost%20per%20Task,-EnterpriseOps%2DGym%2DAA) is good for office tasks like emails, calendars, Teams/Drive, support tasks, etc. Interestingly, none of the OpenAI models are on the frontier. Claude Fable 5 and Gemini 3.5 Flash are at the high-end, but Kimi K3 (Max), Qwen3.7 (Max), GLM-5.2 (Max) lead the mid-end and DeepSeek V4 Pro / Flash lead the low-end frontier.
  - [TerminalBench 2.1](https://artificialanalysis.ai/evaluations/terminalbench-v2-1?eval-cost=score-vs-cost-per-task#:~:text=v2.1%3A%20Score%20vs.-,Cost%20per%20Task,-Terminal%2DBench%20v2.1) is good for coding tasks. The OpenAI models completely rule this frontier.
  - [Analyst Agent](https://artificialanalysis.ai/evaluations/aa-analyst-agent?eval-cost=score-vs-cost-per-task#:~:text=AnalystAgent%3A%20Score%20vs.-,Cost%20per%20Task,-AA%2DAnalystAgent%20score) is good for spreadsheet tasks ([using Python](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)). Gemini 3.7 Flash seems to be a _strong_ outlier on this frontier.
  - [Tau3](https://artificialanalysis.ai/evaluations/tau3-banking?eval-cost=score-vs-cost-per-task#:~:text=Banking%3A%20Score%20vs.-,Cost%20per%20Task,-%F0%9D%9C%8F%C2%B3%2DBanking%20score%20vs) is good for navigating unstructured data. GPT 5.6 Luna wins the bottom, DeepSeek V4 the middle, and Qwen 3.8 / GLM 5.3 take the top. Anthropic and Google are not even in the race.
  - [Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase?cost=elo-vs-cost-per-task#:~:text=Briefcase%20Elo%20vs.-,Cost%20per%20Task,-AA%2DBriefcase%20Elo) is good for building useful things from diverse messy data. Grok completely wins the mid-end with Anthropic dominating the high-cost frontier.
  - [APEX Agents](https://artificialanalysis.ai/evaluations/apex-agents-aa?eval-cost=score-vs-cost-per-task#:~:text=AA%3A%20Score%20vs.-,Cost%20per%20Task,-APEX%2DAgents%2DAA) is good for deeper knowledge work. GPT 5.6 Luna (Max) is a strong frontier outlier here.
- Task-based benchmarks seem more practical than token-based benchmarks. <!-- https://chatgpt.com/c/6a8bb2fa-e08c-83ee-91c5-852149476f44 -->
  - For example, rather than the [LM Arena ELO vs Cost](https://sanand0.github.io/llmpricing/), I would use [Terminal Bench 3.0](https://www.frontierbench.ai/?view=pareto) which clearly tells me to use Codex with GPT-5.6 Sol over Claude Code with Opus 5 / Fable 5; that GLM 5.3 with Claude Code might be excellent value for money as well when using APIs. #ForNow
  - I also did a rough calculation to see if the _$18 GLM subscription_ offers more than $20 ChatGPT Plus. Short answer: No, for my usage, Codex offers ~1.8x more value #ForNow. [ChatGPT](https://chatgpt.com/share/6a8bbfde-4a3c-83ee-ac80-c31630021fbf)
- Anthropic's Skill Creator Skill [now includes evals and A/B testing](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills) #ForNow to check if a skill actually does better. I've been doing this the hard way, e.g. with [impact of simple writing on thinking](https://github.com/sanand0/research/tree/main/simplification-prompt), [optimizing my ideation prompt](https://github.com/sanand0/research/tree/main/ideation-protocol-optimization), [optimizing my summarization prompt](https://github.com/sanand0/scripts/commit/7b1c11fd56c726cb796abfababfe31f9a9a2ec9f), etc.
- I switched from [markitdown](https://github.com/microsoft/markitdown) to [anydoc](https://github.com/firecrawl/anydoc) as my default PDF to Markdown converter. AnyDoc handles tables and other kinds of structures in PDF _much_ better #ForNow.

## Questions I was asked

[Week ending 30 Aug 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-08-30)

- **Question**: How hard was it to adapt your personal AI workflow to work?\
  **Answer**: I didn't try solving work problems. Rather, I took what I was solving personally with agents and tried finding where at work I can apply it. "I have a hammer, let me find all the nails."
- **Question**: If agents can do the coding, how do we teach the foundational blocks?\
  **Answer**: We don't care if they learn FastAPI, etc. Routing, authentication, interfaces, ... - THAT is more useful. So give them tasks that forces them to learn FUTURE foundational blocks FROM agents.
- **Question**: How do you monitor whether people are actually using reusable AI skills?\
  **Answer**: Read the agent session logs. A small script over Claude, Codex and Copilot histories can tell you which skills were actually used and how often.
- **Question**: How are you determining which AI spend is dumb?\
  **Answer**: Start with the highest-cost users and inspect the obvious outliers. Give the raw logs to an agent, ask why someone spent that much, tell users to make obvious optimizations, etc. before attempting sophisticated optimization.
