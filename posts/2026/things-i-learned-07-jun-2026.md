---
title: Things I Learned - 07 Jun 2026
date: 2026-06-07T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- `sudo resolvectl flush-caches` clears the DNS cache on Linux. Useful when you're changing DNS records and want to see the changes immediately. In my case, I was creating a Cloudflare tunnel to my laptop and wanted to test it quickly.
- Making something easy to verify makes it _much_ faster to train models on it. Arithmetic verification is easy - calculators can be deterministically verified. Chess verification is easy - Stockfish became easy to train. Code verification is easy - LLMs improved coding ability rapidly. Therefore:
  - Wherever we have environments that are easy to verify, AI will improve faster there.
  - To make AI improve faster in an area, build environments that are easy to verify.
- [MCP is getting simpler](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). A stateless HTTP protocol. Simpler OAuth. Plugins. No idea when it will land in Claude or ChatGPT, though. Worth checking after 28 Jun 2026 - after it is finalized.
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) is Microsoft's version of OpenClaw or [Gemini Spark](https://gemini.google/overview/agent/spark/).
- `git subtree` is a useful way of maintaining git repos inside git repos. For example, if you have a tool `tool-a` under a project. It's more light-weight than sub-modules, lets you commit at any point to the parent _or_ child, and is a built-in feature in `git`. <!-- https://chatgpt.com/c/6a1d25bf-49f4-83ec-8e02-5905a22f4fe0 -->
- [Gemma 4 12B is released](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) and seems almost as good as the 26B version. This is the class of models that makes it practical to run edge AI on phones. It's multimodal and reasonably smart (like frontier models were 12-18 months ago).
- I don't use Claude/ChatGPT Projects much. It offers 3 advantages: custom instructions, memory, files, and chats. Files aren't useful - I use my entire laptop as a file system via MCP. Instructions aren't useful - I can paste commonly used prompts with a click. Chats aren't useful - I have chat references enabled, so all past chats are accessible anyway. Memory isn't useful - I have memory enabled globally anyway. In short, I haven't discovered the power of projects that everyone's raving about. SKILL.md is more useful for me. <!-- https://claude.ai/chat/eb3bcf3e-f1f0-4d33-b5a2-14b09cbda189 -->
- [`repo`](https://gerrit.googlesource.com/git-repo/+/HEAD/README.md) is a Google/Android tool built on top of `git` that lets you manage multiple git repos. It sounded promising until I released it needs a `repo init` that creates a `.repo/` - which is more overhead that I'd like to keep.
- When using `<image onerror=...>` fallbacks, include `this.oneerror=null` to prevent infinite loops if the fallback image also fails to load. [RK](http://mvark.blogspot.com/2026/05/how-to-add-backup-image-in-html-when.html)
- One of the advantages of multiple agent (rather than a single agent loop) is: it's easier to change directions when wrong. Single loops get stuck. [Build Agents That Run for Hours](https://www.youtube.com/watch?v=mR-WAvEPRwE)
- Claude Code also supports [agent teams](https://code.claude.com/docs/en/agent-teams) where sub-agents can talk to each other rather than rely on the main agent to coordinate. Useful for parallel exploration. Anthropic lets Claude define "organizational policies" for agent teams best suited for the task (AI-native workflows). It also lets agents to push back on their scope, e.g. "This is too hard." [Build Agents That Run for Hours](https://www.youtube.com/watch?v=mR-WAvEPRwE)
- Claude Code has a `/background [prompt]` (or `/bg`) command that runs the current session the background. You can run `claude agents` as a separate command to [monitor agents](https://code.claude.com/docs/en/agent-view). (There's no equivalent in Codex yet.) This seems to be the future of agentic operations: a bunch of agents running that you monitor and steer through an agent view dashboard.
- Models are evolving. Therefore prompts evolved. Now harnesses also need to evolve. The workflows will also evolve. As a result, evaluations might be the (relatively) more stable assets. Datasets are likely to be the most stable ground truth.
- How to learn a new field fast:
  - Yes, it's possible to learn 50% of a field in 20 hours. [Josh Kaufman, "The First 20 Hours"](https://www.youtube.com/watch?v=5MgBikgcWnY) popularized it. The next 30% takes months and the last 20% takes years.
  - [Threshold concepts](https://en.wikipedia.org/wiki/Threshold_knowledge) are those that change your perspective and open up new ways of thinking.
  - Experts' knowledge is hard-wired and they can't identify nor teach threshold concepts naturally. Don't assume they can.
- ["We know more than we can tell."](https://www.google.com/search?q=Polanyi+%22we+know+more+than+we+can+tell%22) Polanyi's 1966 book "The Tacit Dimension" says that there's some knowledge that can't be verbalized. This [tacit knowledge](https://en.wikipedia.org/wiki/Tacit_knowledge), therefore, will be harder for humans and AI to learn.
