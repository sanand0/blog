---
title: Things I Learned - 16 Aug 2026
date: 2026-08-16T00:00:00+00:00
categories:
- til
description: I learned how fish can treat command output as file input, VS Code has built-in dictation, and AI work needs a measured verification tax. I also thought about reciprocal attention.
tags: [ai, developer-tools, javascript, productivity]
---

This week, I learned:

- [psub](https://fishshell.com/docs/current/cmds/psub.html) is a neat `fish` option to treat command outputs like file inputs. E.g. `diff (sort a.txt | psub) (sort b.txt | psub)`
- More anchor points on how much text to ask AI for: <!-- https://chatgpt.com/c/6a7ee0c5-75d8-83ee-aede-388d8f14a2eb -->
  - ... in 200-300 words (about 1 book page)
  - ... in ~1 A4 sheet (~500 words)
  - ... in ~3 minute of conversational Grade 8 reading (~500 words)
- I usually log things in a single file rather than split things into yearly, monthly, etc. A single file is more portable, scannable, and, for human logs, gives a feeling of accomplishment. I split when the file gets so unwieldy that it actually hurts - which is a good thing because it means I'm actually using it (maybe?) - and splitting beforehand may be good planning but is also premature optimization, adding friction to a nascent, fragile process. (This idea is pretty generalizable.)
- Claude models launched after 2 Aug 2026 "weaves an imperceptible watermark directly into the text itself. You won’t see it, and it doesn’t change the meaning, quality, or readability of Claude’s response." [How Claude marks AI-generated content](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content).
- [VS Code has built-in dictation](https://code.visualstudio.com/docs/configure/accessibility/voice#_dictate-in-an-editor). It uses `nemotron-3.5-asr-streaming-0.6b` by default #ForNow, and it's pretty good. I expect I'll use it a lot more, since most of my typing is in VS Code anyway. <kbd>Ctrl + Alt + V</kbd> toggles dictation. Dictation is also supported in the terminal and is trained to recogni
- I had an interesting moment today when I asked ChatGPT to identify which of my ChatGPT conversations were the most effective. I gave it access to my computer and it started using the browser to scrape itself so aggressively that I stopped it from it banned itself! <!-- https://chatgpt.com/c/6a794e02-1eb0-83ec-bbbb-00406cc1d56d -->
- [GeoLibre](https://web.geolibre.app/) looks like a full-fledged GIS. It's [open source](https://github.com/opengeos/GeoLibre) and runs directly in the browser.
- When installing tools with `mise`, if it messes up the platform, you can explicitly specify it. For example: `mise use -g 'github:pranshuparmar/witr[asset_pattern=witr-linux-amd64,bin=witr]@latest'`. [Mise Docs](https://mise.jdx.dev/dev-tools/backends/github.html#asset-pattern)
- I saw this snippet from Claude Code: `await Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 3000))]);` That waits for up to 3 seconds for the fonts to load. Didn't know about [Promise.race()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race) before. It's different from `Promise.any()` in that `.race()` will return the first _result_ while `.any()` will return the first _success_.
- Measure the verification / follow-up tax in your AI work. AI does things fast. _You_ have to take the next step. It helps to tag items with how long they'd take to verify or action. We do for specification, because we have to do that _now_, _before_ telling AI. But I typically ignore the deferred tax.  <!-- https://chatgpt.com/c/6a78a9e7-f6a4-83ec-834a-feaca6ea088b -->
- A theme is emerging: "Human attention needs reciprocity. If you ask for someone's attention, first demonstrate your own effort." Example: "people really don't like when a coworker's chatgpt contacts them asking for help with a task, even when they'd be perfectly happy doing that same work if asked by that coworker." [Greg Brockman](https://x.com/gdb/status/2083435180392673714)

## Questions I was asked

[Week ending 16 Aug 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-08-16)

- **Question**: What should a strong data scientist actually build in an AI-native delivery model?\
  **Answer**: Assume he is training an AI to replace him. He should not build the thing himself; he should direct the agent, apply his judgment over a few iterations, and leave behind a portable system you can benchmark and rebuild simpler, better and faster.
- **Question**: If two people are iterating on an AI-native delivery workflow, what collaboration setup do they need?\
  **Answer**: Shared files solve most of it. Keep data, code, skills/prompts and notes in folders with the right permissions; Google Drive or OneDrive is enough for now.
- **Question**: If we're debating whether a course is even necessary anymore, how do we transition it for AI?\
  **Answer**: Start with a single class that's full AI, a single exam that's full AI, one step at a time.
- **Question**: Instead of hiring more developers, should I take fewer people and spend the difference on premium AI seats?\
  **Answer**: Experiment with a few people, not everyone. Treat AI as an extra headcount slot, but radically raise the output expected; getting that productivity happens only when you need that productivity.
- **Question**: Should we self-host open models to reduce LLM costs?\
  **Answer**: Do the math: machine cost per hour versus useful inferences per hour and compare it with the API. Cost alone probably isn't enough; privacy is a much better reason to self-host.
- **Question**: How do you build a QA agent that tests developers' work and reports back?\
  **Answer**: Don't build the agent first. Tell a coding harness the outcome—find requirements, create tests, run them and report—and do it manually 5–10 times; automate only after you know what you actually want.

## Mistakes I made

[Week ending 16 Aug 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-08-16)

- I said **"The data is secure everywhere. All of them have solid enterprise contracts"** and that choosing an AI tool for company data was not really a technical question.\
  **Correction**: Enterprise AI offerings can have strong security, but their data handling is not interchangeable. It depends on the exact product, plan, tenant configuration, retention and training settings, connectors, geography and contract. Microsoft explicitly says Copilot controls vary by subscription; OpenAI and Anthropic make separate commitments for their business/commercial products. I should check the approved product and its actual controls rather than assume equivalence. Evidence: [Microsoft — Copilot enterprise data protection](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection) [OpenAI — Enterprise privacy](https://openai.com/enterprise-privacy/) [Anthropic — commercial-product training policy](https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training)\
  **HIGH · OVERSTATED**
- I said **GitHub is where you take version-controlled software and "save it publicly."**\
  **Correction**: GitHub repositories can be public or private; GitHub Enterprise also supports internal repositories. Version control does not imply publishing the code. When explaining this to a beginner, I should explicitly distinguish Git from GitHub and repository visibility. Evidence: [GitHub Docs — About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)\
  **LOW · FALSE**
- I said **animation "started" in the 1930s with *Snow White and the Seven Dwarfs*.**\
  **Correction**: *Snow White* was a landmark, but animated features predate it. *El Apóstol* was released in 1917, and *The Adventures of Prince Achmed* from 1926 is the earliest surviving animated feature. My visualization was a filtered view of popular IMDb titles, not a history of when animation began. Evidence: [BFI — animated features before Snow White](https://www.bfi.org.uk/features/lesser-spotted-british-animated-feature-film)\
  **LOW · FALSE**
