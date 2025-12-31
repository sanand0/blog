---
title: When to Vibe Code? If Speed Beats Certainty
date: "2025-05-20T10:59:50Z"
lastmod: "2025-05-20T10:59:52Z"
categories:
  - coding
  - llms
wp_id: 4120
---

I spoke about vibe coding at [SETU School](https://setuschool.com/) last week.

<div class="video-embed"><iframe src="https://www.youtube.com/embed/ODXSDbY12dg" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Transcript**: <https://sanand0.github.io/talks/#/2025-05-10-vibe-coding/>

Here are the top messages from the talk:

**What is vibe coding**

It's where we ask the model to write & run code, don't read the code, just inspect the **behaviour**.

It's a **coder's tactic**, not a methodology. Use it when speed trumps certainty.

**Why it's catching on**

- **Non-coders can now ship apps** - no mental overhead of syntax or structure.
- **Coders think at a higher level** - stay in problem space, not bracket placement.
- **Model capability keeps widening** - the "vibe-able" slice grows every release.

**How to work with it day-to-day**

- **Fail fast, hop models** - if Claude errors, paste into Gemini or OpenAI and move on.
- **Don't fight sandbox limits** - browser LLM sandboxes block net calls; accept & upload files instead.
- **Cross-validate outputs** - ask a second LLM to critique or replicate; cheaper than reading 400 lines of code.
- **Switch modes deliberately** - **Vibe coding** when you don't care about internals and time is scarce, **AI-assisted coding** when you must own the code (read + tweak), **Manual** only for the gnarly 5 % the model still can't handle.

**What should we watch out for**

- **Security risk** - running unseen code can nuke your files; sandbox or use throw-away environments.
- **Internet-blocked runtimes** - prevents scraping/DoS misuse but forces data uploads.
- **Quality cliffs** - small edge-cases break; be ready to drop to manual fixes or wait for next model upgrade.

**What are the business implications**

- **Agencies still matter** - they absorb legal risk, project-manage, and can be bashed on price now that AI halves their grunt work.
- **Prototype-to-prod blur** - the same vibe-coded PoC can often be hardened instead of rewritten.
- **UI convergence** - chat + artifacts/canvas is becoming the default "front-end"; underlying apps become API + data.

**How does this impact education**

- **Curriculum can refresh term-by-term** - LLMs draft notes, slides, even whole modules.
- **Assessment shifts back to subjective** - LLM-graded essays/projects at scale.
- **Teach "learning how to learn"** - Pomodoro focus, spaced recall, chunking concepts, as in **Learn Like a Pro** (Barbara Oakley).
- **Best tactic for staying current** - experiment > read; anything written is weeks out-of-date.

**What are the risks**

- **Overconfidence risk** - silent failures look like success until they hit prod.
- **Skill atrophy** - teams might lose the muscle to debug when vibe coding stalls.
- **Legal & compliance gaps** - unclear licence chains for AI-generated artefacts.
- **Waiting game trap** - "just wait for the next model" can become a habit that freezes delivery.

[LinkedIn](https://www.linkedin.com/feed/update/urn%3Ali%3Ashare%3A7330549070744223745)
