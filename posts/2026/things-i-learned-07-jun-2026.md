---
title: Things I Learned - 07 Jun 2026
date: 2026-06-07T00:00:00+00:00
categories:
- til
description: This week I learned why easy verification accelerates AI, explored Claude Code’s agent teams and background agents, and found practical notes on MCP’s simplification, Gemma 4 12B, and git subtree.
tags: [ai-agents, claude-code, model-context-protocol, learning]
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

## Questions I was asked

[Week ending 07 Jun 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-06-07)

- **Question**: Who should attend the AI data stories workshop?\
  **Answer**: Everyone is welcome. The focus is how to get AI to tell data stories, and participants should have paid ChatGPT or Claude so it is hands-on.
- **Question**: When I can show anomalies and root causes, what should a forward deployed engineer actually deliver?\
  **Answer**: Don’t give me a tool, report, or “ability to analyze.” Tell me the action: these two agents cause the maximum problem, train or replace them, and here is the evidence.
- **Question**: Why do we need a CLI if we already have drag-and-drop or an API for publishing static reports?\
  **Answer**: The API is enough technically. The CLI reduces variation when five people or CI/CD jobs regenerate and publish outputs in different ways.
- **Question**: How should we handle infrastructure for sending tens of thousands of AI-personalized emails?\
  **Answer**: Don’t optimize prematurely. Send good emails to 80 or 200 people first, validate quality and compliance, then solve for 10,000 if the value is proven.
- **Question**: What happens after the FDE discovery and first moment of truth?\
  **Answer**: Move into discovery inventory, then execution and rinse-repeat. The point is not just to identify use cases; it is to keep solving them and turning the working patterns into capability.
- **Question**: Is the first agentic output just a broad design, not deployment?\
  **Answer**: Yes. What I described is the agentification of design. Deploy, maintain, continuously improve, and scale are separate phases with different bottlenecks and different agentic techniques.
- **Question**: Why is the agent approach different from just starting to use LLMs?\
  **Answer**: Gen 1 was writing code around LLM calls. Gen 2 was using LLMs for complex steps but still orchestrating everything yourself. Gen 3 is letting the agent/harness orchestrate the work.
- **Question**: Should we explain Gen 1, Gen 2, Gen 3 agent architecture to clients?\
  **Answer**: No. That is internal language. Externally, talk outcomes and workflows; internally, tell teams to start developing this way.
- **Question**: What is deployed AI?\
  **Answer**: It is not just a model or a demo. It is an agent or workflow connected to production systems, transaction data, verification, governance, KPIs, reporting, and human review where needed.
- **Question**: What enterprise architecture makes agents easier to deploy?\
  **Answer**: A registry of available data, tools, systems, and permissions. Once agents know what they can access and how, deployment becomes more like giving capabilities than building everything again.
- **Question**: How should I use your time on an AI productivity initiative?\
  **Answer**: Don’t give me status updates. Ask me a question where I can help; if I need context from the team, I’ll ask for it.
- **Question**: What organizational AI mindset shift are you wrestling with?\
  **Answer**: Moving teams from LLM API to harness, from CLI to MCP, and from software to outcomes. If a client’s intern can build the software in six hours, the value must be the business output, not the code.
- **Question**: How should we train a software developer shifting into GenAI prototype work?\
  **Answer**: Have him solve TDS once with a coding agent, then train harness configurability: hooks, plugins, workflows, sub-agents and shared skills. Also train use-case discovery and SME validation.
- **Question**: Are browser agents doing the same thing as turning websites into tools?\
  **Answer**: Yes. Treat browsers, APIs, command-line tools, action models, and specialized models as tools; the harness becomes the shell that pipes them together.
- **Question**: How should executives be introduced to AI before jumping into use cases?\
  **Answer**: Start with personal use, then citizen use, then enterprise use. Workshops beat trainings: make them solve something useful the same day so AI stops being abstract or threatening.
- **Question**: In the FDE model, who identifies the problems - the SME or AI?\
  **Answer**: Both, but AI does most of the first draft. The SME gives business context and prompts; the agent scans data and documents, proposes use cases, and should then solve them, not just list them.
- **Question**: Should you personally build the AI demos for the client?\
  **Answer**: No. The team should build them with Claude Code; I’ll help only when they hit challenges. Me building a demo gives a fish, not the fishing muscle we need to scale.
- **Question**: How are you using AI personally and what kinds of problems are worth solving?\
  **Answer**: I maintain an AI Bottlenecks log: every stuck, bored, overloaded, or messy moment becomes input. Ask AI how to solve it with AI, then turn the solution into an asset that compounds.
- **Question**: Are enterprises making a mistake by treating AI as just LLMs?\
  **Answer**: Yes. Upgrade the mental model from “LLM” to “harness”: the harness orchestrates tools, LLM APIs, deterministic computation, actions, governance, and eventually other model types.
- **Question**: Should we enforce a specific output format like a web app when asking agents to solve business problems?\
  **Answer**: Solve the problem first. Most end-users do not want a dashboard; they want a trusted answer in English that tells them what to do and why.
- **Question**: How should we scope an AI POC when the client wants data architecture, KPIs, code and semantic layers quickly?\
  **Answer**: Record the walkthroughs and make only a soft commit until you see the data. Ask what their own product manager would deliver from the same inputs, then deliver it faster and better.
- **Question**: How do we enable the whole team to get up to speed with AI?\
  **Answer**: Make everyone produce proactive AI-generated output useful to the client within a month. Review what worked, then convert repeated patterns into prompts, scripts, verifiers, access recipes, and shared assets.
- **Question**: What should I do when AI helps build something but I get stuck at the next deployment or review step?\
  **Answer**: Treat every stuck point as the next AI prompt. Write the bottleneck down, ask AI how to remove it, and spend your learning time only where AI still cannot help.
- **Question**: Is there any stable ground while AI tools and enterprise architectures keep shifting?\
  **Answer**: Yes: evals and test cases. Treat code and harness choices as depreciating assets; workflows matter more, and evals are the thing worth specifying.
- **Question**: How do we build robust AI systems when the technology keeps changing?\
  **Answer**: Shorten the payback period brutally. Don’t chase a feature that takes three months; use what is on a platter, build replaceably, and invest only when it pays back fast.
- **Question**: Should we solve production-scale reliability before committing to a new agent framework like ADK?\
  **Answer**: Only if the solution is easy now. If scaling, refactoring, or latency are not solvable on a platter, don’t burn months; let technical debt accumulate and build so components can be replaced later.
- **Question**: At what level should we abstract AI services from provider or agent-platform choices?\
  **Answer**: Ask at every decision: what happens when this is deprecated? Flexibility now means planning for model, harness, provider, and architecture replacement.
- **Question**: Should we invest in a separate traditional eval platform for AI systems?\
  **Answer**: Maybe premature. Benchmark creation is now cheap with coding agents; generic evals are thin, specific evals are specific, and continuous evals matter most once the system is in operations.
- **Question**: How do I get started when an AI problem looks too big?\
  **Answer**: Log exactly where you are stuck, paste that into AI, and iterate until one manual cycle works. Then automate that cycle and move the bottleneck forward.
- **Question**: If you were a forward deployed engineer today, what would you actually do?\
  **Answer**: Enter the client environment, inspect the data and digital exhaust, ask agents what problems stakeholders likely have, solve one, and send a “do this because of this” recommendation with evidence.
