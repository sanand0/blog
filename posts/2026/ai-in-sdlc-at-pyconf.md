---
title: AI in SDLC at PyConf
date: 2026-03-19T14:58:26+05:30
categories:
  - llms
  - coding
description: The strongest use of AI in software development is not isolated prompting but embedding models across the entire development loop from discovery to deployment and postmortem learning.
keywords: [AI in SDLC, software engineering, coding agents, process design, prompt reuse, developer workflows]
---

I was at a panel on [AI in SDLC](https://2026.pyconfhyd.org/) at PyConf. Here's the summary of my advice:

**Process**

- Make AI your _entire_ SDLC loop. Record client calls, feed them to a coding agent to directly build & deploy the solution.
- Record your prompts, run post-mortems, and distill them into `SKILLS.md` files for reuse.

**Prompting**

- Ask AI to make output _more reviewable_. Don't waste time reviewing unclear output.
- Prefer _directional_ feedback (feeling, emotion, intent) over implementational.
- _Also_ give AI freedom to do things its way. Learn from that - you'll be surprised.

**Learning**

- Prefer interns / outsiders over experts. They don't slow the process with preconceptions and leverage AI better.
- _Stop_ learning what AI does well. Learn what AI fails at - using AI. Keep re-assessing these.

**Adoption**

- Developer using AI are _still_ accountable for their code. (Agents might become accountable in the future.)
- Start with new projects: less competition, fewer preconceptions, lower risk.
- Start in domains where failure is OK, rather than making AI safe enough for high-risk domains.
- Create safe spaces where hallucinations don't matter and run experiments there to learn what AI can do.
- Plan for where AI'll be a year later. It's growing _very_ rapidly.

The full details of the panel discussion are at [Who Owns the Commit?](https://sanand0.github.io/talks/2026-03-15-pyconf-ai-in-sdlc/)

![](https://sanand0.github.io/talks/2026-03-15-pyconf-ai-in-sdlc/sketchnote.avif)
