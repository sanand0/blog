---
title: Things I Learned - 16 Aug 2026
date: 2026-08-16T00:00:00+00:00
categories:
  - til
description: I share practical discoveries about AI verification costs, Claude and ChatGPT behavior, VS Code dictation, JavaScript promises, fish shell, browser-based GIS, tool installation, and keeping personal logs simple and portable.
tags: [ai, claude, chatgpt, vs-code, javascript, developer-tools, gis, productivity]
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
