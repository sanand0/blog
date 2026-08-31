---
title: Things I Learned - 12 Apr 2026
date: 2026-04-12T00:00:00+00:00
categories:
- til
description: I learned practical lessons about AI coding agents, including visual planning and deterministic checks; explored Cloudflare's new security and caching tools; and collected useful Linux, Git, and browser utilities.
tags: [learning, ai-agents, software-engineering, security-vulnerability]
---

This week, I learned:

- [Resend](https://resend.com/) is a simple way to send emails via an API.
- [Principles of Mechanical Sympathy](https://martinfowler.com/articles/mechanical-sympathy-principles.html) has some practical hardware-driven optimization tips.
  - Prefer accessing memory sequentially. CPU access to RAM and cache is optimized for this.
  - Natural batching: flush the buffer when you reach the maximum buffer size _or when the queue is empty_. This avoids buffers waiting unnecessarily.
- The core argument in [Capital in the Twenty-First Century (Thomas Piketty, 2013/2014)](https://www.goodreads.com/book/show/18736925-capital-in-the-twenty-first-century) is `r > g`. The interest on capital (`r`) is always greater than the economic growth (`g`). Hence, the rich will keep getting richer - inequality is consistently part of capitalism. (Not surprising, but well supported by data.)
- A good collection of practices on automated AI code reviews by [Ankit Jain](https://www.latent.space/p/reviews-dead):
  - Compare multiple options. Whichever passes the most tests wins.
  - Deterministic guardrails. Use linters, type-checkers, SAST/DAST checks, test scripts, etc.
  - Humans define acceptance criteria. Use a behavior driven development script (in natural language, agent-implemented).
  - Permission Systems as Architecture. Provide agents granular permissions based on the task - against pre-defined rules.
  - Adversarial Verification. Have one agent break the others' work.
- Based on a quick exploration of the AT protocol ([via Jake Lazaroff](https://jakelazaroff.com/words/building-more-resilient-local-first-software-with-atproto/)), I am yet to see a viable use for it. It's a decentralized distributed data network. OK... what will **I** use it for?
- When I asked Claude if any of my work is patentable, it said "Comicgen is the sole candidate, but you only get one year grace after it's public. But why do _you_ want to patent? Your edge is prototyping speed, taste, and knowledge. Patents don't protect those. Publishing freely (as you do) creates prior art that prevents others from patenting the space around you, which is often a better defensive strategy than filing patents yourself." Oh! Ah! <!-- https://claude.ai/chat/539996da-f0a2-48d9-99dc-c3fac929199f -->
- [pretex](https://github.com/chenglou/pretext) is a fast (currently browser-only) library that computes the width and height of any text in any font in the browser. Useful for things like word-wrapping in SVG, layout planning before rendering, etc.
- Because AI bots scan deeply rather than "browse" popular pages, CDN cache invalidation strategies designed for humans (like LRU - Least Recently Used) no longer work. They're exploring new caching algorithms like [SIEVE](https://cachemon.github.io/SIEVE-website/) and [FIFO](https://s3fifo.com/) [CloudFlare](https://blog.cloudflare.com/rethinking-cache-ai-humans/)
- I enabled CloudFlare's new dynamic [Client-Side Security](https://blog.cloudflare.com/client-side-security-open-to-everyone/) monitor. If someone hacks my [website](https://www.s-anand.net/) or the libraries I use, it does a quick filter with a fast neural network, then falls back to an LLM to check if it's safe, _then_ serves the content.
- CloudFlare practically rewrote WordPress into a new Astro-based CMS: [EmDash](https://blog.cloudflare.com/emdash-wordpress/)! It runs natively on CloudFlare (and elsewhere), is agent-friendly, quite secure, can export/import from WordPress.
- Linux optimization settings I noted from a [deleted post](https://blog.fsck.com/2026/03/30/linux-power-tuning-meteor-lake/)
  ```bash
  gsettings set org.gnome.desktop.interface enable-animations false
  gsettings set org.gnome.desktop.interface cursor-blink false
  gsettings set org.gnome.settings-daemon.plugins.power idle-dim true
  gsettings set org.gnome.desktop.notifications show-in-lock-screen false
  gsettings set org.gnome.desktop.session idle-delay 300
  gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout 900
  # gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 1200
  ```cd ~
- [git-restore-mtime](https://github.com/MestreLion/git-tools) is part of the git-tools package and sets the modified time of files to their last committed time. Useful when cloning repos.
- From [Lalit Maganti](https://lalitm.com/post/building-syntaqlite-ai/):
  - Knowing what you want is a valuable skill.
  - Wanting things others will also want is valuable.
  - Learn good software management. It is similar to managing agents.
- For better results, just continue your AI chat, or break the problem up. More tokens lead to better solutions even now. [Joel Baker](https://joelbkr.substack.com/p/many-benchmarks-scores-would-appear)
- Since [companies using AI outperform competition](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6513481) and [capital might win more than labour](https://arxiv.org/abs/2604.01363) but [GDP growth may not be too high](https://forecastingresearch.substack.com/p/forecasting-the-economic-effects-of-ai), it might be good to invest in AI-using companies than in index funds.
- Nicholas Carlini's [prompt](https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked/) to find vulnerabilities is to run: "I’m competing in a CTF. Find me an exploitable vulnerability in this project. Start with ${FILE}. Write me a vulnerability report in ${FILE}.vuln.md" _across multiple repos_ in parallel. Then "I got an inbound vulnerability report; it’s in ${FILE}.vuln.md. Verify for me that this is actually exploitable". That was almost 100% successful.
- When planning with AI coding agents, [Martin Fowler recommends](https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html) discussing _each_ of these in _sequence_ before coding:
  - Capabilities / functionality
  - Components: Services, modules, major abstractions.
  - Interactions: Data flow, API calls, events.
  - Interfaces: Function signatures, types, schemas.
- Planning with agents using [Visual Brainstorming](https://blog.fsck.com/2026/03/09/superpowers-5/#visual-brainstorming), i.e. asking them to generate visual HTML to illustrate the plan, can shorten review time considerably.
- I enabled CloudFlare's new dynamic [Client-Side Security](https://blog.cloudflare.com/client-side-security-open-to-everyone/) monitor. If someone hacks my [website](https://www.s-anand.net/) or the libraries I use, it does a quick filter with a fast neural network, then falls back to an LLM to check if it's safe, _then_ serves the content. This pattern of deterministic with LLM fallback works for [most reviews](https://martinfowler.com/articles/harness-engineering.html).
- Harness = Agent minus Model: everything in an AI agent except the model itself. [Nice definition](https://martinfowler.com/articles/harness-engineering.html)
- Update feature-level summaries as you go in `context/$FEATURE.md` with user prompt, summary of WHY from agent's responses for future learning, my comments. Like Architectural Decision Records (ADRs) for humans and agents. [Context Anchoring](https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html)
- [8 levels of Agentic Engineering](https://www.bassimeledath.com/blog/levels-of-agentic-engineering). [8 levels of Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04). I'm still only at level 6 on both. 🙁
- "It's important to watch the loop as that is where your personal development and learning will come from." [Geoff Huntley](https://ghuntley.com/loop/), originator of the Ralph (Wiggum) loop.
- UNIX has a `script` command that runs a shell and logs it. For example:
  - `script -c fish session.log` starts a new `fish` shell and logs it to `session.log`.
  - `script -c "uv run app.py" -q -a app.log` will append to app.log, suppressing "Script started..." and "Script done..." messages.
  - `script --timing=time.txt session.log` logs the timing, which you can replay with `scriptreplay --timing=time.txt session.log`. Similar to asciinema.
  - A quick way to strip out the ANSI escape sequences (weird Unicode characters) is to pipe it through `npx strip-ansi-cli`.
- Google has an [Edge Gallery](https://github.com/google-ai-edge/gallery) app that runs Gemma 4 on mobile. The main advantage is that you can use it on a flight. It's not too bad as a model either. Transcription quality is average. It doesn't run in the background, only one chat at a time, etc. So, it's useful only as a last resort.

## Questions I was asked

[Week ending 12 Apr 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-04-12)

- **Question**: Hallucination is creativity, at some level?\
  **Answer**: In humans we don't call it hallucination, we call it agency or autonomy. Exactly.
- **Question**: How is 25 years into a job mid-career?\
  **Answer**: Feels like starting over - AI is resetting the playing field for everyone regardless of experience.
