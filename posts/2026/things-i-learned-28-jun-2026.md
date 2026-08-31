---
title: Things I Learned - 28 Jun 2026
date: 2026-06-28T00:00:00+00:00
categories:
- til
description: I learned how Substack RSS feeds can reveal my reading, why Claude answers more briefly on mobile, how Cloudflare enables agent trial accounts, and how Git can ignore files outside .gitignore.
tags: [learning, ai-agents, python]
---

This week, I learned:

- Every Substack feed has an RSS feed at `https://your.substack.com/feed`. [Substack help](https://support.substack.com/hc/en-us/articles/360038239391-Is-there-an-RSS-feed-for-my-publication). I used this to scan my browsing history to identify Substacks I visit - and subscribed to [Marcus on AI](https://garymarcus.substack.com/) - an AI sceptic AI asked me to read about.
- Cloudflare let's agents create [temporary accounts](https://blog.cloudflare.com/temporary-accounts/) so that they can deploy and test. Enables trial and error - a powerful capability.
- "They're on mobile but this is substantiative enough to warrant length." I spotted this in Claude's thinking when prompting on mobile. So, if I ask Claude something on mobile, it will give me shorter responses by default. Clever design - but something to keep in mind. If I want some heavy thinking done by Claude, better to do it on desktop than try to give it conflicting instructions.
- [Giant Permissive Image Corpus (GPIC)](https://gpic.stanford.edu/) has 100 million Qwen tagged public images. Even as a simple searchable image catalog this has value. [Jeff Clark - Import AI](https://jack-clark.net/2026/06/01/import-ai-459-ai-oversight-is-difficult-scaling-laws-for-protein-folding-models-and-pricing-the-extinction-risk-of-ai-systems/)
- [Ethan Mollick](https://www.oneusefulthing.org/p/co-existence-and-the-end-of-co-intelligence) had an agent test his book summary against multiple LLMs as readers to find out how they would recommend it - and optimized. This is a great practical use of agents as consumers, and material for my [When Data is for Agents, Not Humans](https://hasgeek.com/fifthelephant/fifthelephant-2026-call-for-submissions/sub/when-data-is-for-agents-not-humans-RPJ3syxmspKua6ADd44mD6) workshop.
- [`kage`](https://github.com/tamnd/kage) is an easy CLI to clone websites and read offline. For example, `kage clone https://simonwillison.net/2026/Jun/ -o ~/tmp/site --scope-prefix /2026/Jun/ --max-depth 1` clones all Jun 2026 articles from Simon Willison's blog. Then `kage serve ~/tmp/site` serves it locally. While it's easy, the only time I need this is on a flight, and in that case, a local RSS feed app works better. I'm using [`newsboat`](https://newsboat.org/) for that.
- To me, the clearest [sign of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) from the [Wikipedia:AI or not quiz](https://en.wikipedia.org/wiki/Wikipedia:AI_or_not_quiz) was consistent paragraph lengths. I got the first 3/3 wrong, but once I used this heuristic, I got 6/7 right. Updated my [LLM Smells](https://github.com/sanand0/blog/commit/1f0535fef1bd6434b0b28804ef8fbb41ae1d8d91).
- The files `.git/info/exclude` and `~/.config/git/ignore` are also ignored by git, like `.gitignore`, but useful if you don't want to commit them into the `.gitignore` file. For example, `.DS_Store` makes sense only for Mac machines, not each repo. `.vscode/` makes sense only for VS Code users.  [Nelson Figueroa](https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/)
- [Justin Poehnelt](https://github.com/jpoehnelt), author of the brilliant [Google Workspace CLI `gws`](https://github.com/googleworkspace/cli/), was fired for it. There have been no updates for 3 months, but none may be required - it feels perfect. [X](https://x.com/JPoehnelt/status/2069482265953087602)
- [Lore](https://github.com/EpicGames/lore) is a centralized version control system for large binaries. If you have large binaries (e.g. images, videos, ...) that multiple people edit, it's better than Git LFS or Perforce. [ChatGPT](https://chatgpt.com/share/6a3bd941-7458-83ee-a61c-b145913b8cf3)
- [Deno Desktop](https://docs.deno.com/runtime/desktop/) lets you use JS to build desktop apps. I tried it. It's easy to install, compact to code, leverages familar web technology, and compiles to multi-platform binary. The binaries are a bit larger than I'd like, though - 80MB for a Hello World on Linux/Windows and ~70MB on Mac.
- Codex reported that `You have 2 usage limit resets available. Run /usage to use one.` [This thread](https://community.openai.com/t/flexible-rate-limit-resets-for-codex-and-a-method-to-get-a-reset/1383470) has context. After resetting, the next reset might be 7 days _after_ the reset, though [(source)](https://community.openai.com/t/flexible-rate-limit-resets-for-codex-and-a-method-to-get-a-reset/1383470/25).
- After having a child, _fathers_ are affected biologically, too. Testosterone drops, cortisol & prolactin & estrogen rise, the brain rewires for empathy and threat detection - and of course, there's less sleep. These sometimes lead to "Paternal Postpartum Depression" - something I didn't even know was a thing. The havoc kids wreak upon us! 🙂 [Gemini](https://gemini.google.com/share/a8b626f574ea)
- With AI writing more code, formal code proofs are becoming more accessible. You just need to ask a coding agent to prove / disprove a function. You can use: <!-- https://chatgpt.com/c/6a38c544-f850-83ee-b6f1-4a7ccfb9ba00 -->
  - [Z3](https://github.com/z3prover/z3) to find/prove whether a counterexample exists. Best default.
  - [Dafny](https://dafny.org/) to prove that code obeys a spec. Best for real algorithmic code.
  - [Alloy](https://alloytools.org/) to find loopholes in relational models, schemas, permissions, and workflows. Best for data.
  - [TLA+](https://lamport.azurewebsites.net/tla/tla.html) to check whether stateful, concurrent, or agentic systems can evolve into a bad state. Best for systems / workflows.
  - .. and there's a long tail of these.
- [Python is named after Monty Python](https://en.wikipedia.org/wiki/Python_(programming_language)#Naming), not the snake. I knew this, but forgot!
- Python now has multiple cross-platform app paths: [PyInstaller](https://pyinstaller.org/) and [Nuitka](https://nuitka.net/) for executables, [Kivy](https://kivy.org/), [Flet](https://flet.dev/), and [BeeWare/Briefcase](https://beeware.org/) for GUI/mobile/desktop apps, and [PyScript](https://pyscript.net/)/[Pyodide](https://pyodide.org/) for browser/WASM apps - a route that became more serious because Pyodide-compatible WebAssembly wheels can now be published directly to [PyPI](https://pypi.org/). <!-- https://chatgpt.com/c/6a389625-0390-83e9-a724-01cbeac4d40c -->
- On the one hand, AI is writing code, so there's no point learning Python. On the other hand, AI is writing code mostly in Python - so THAT's what you need to learn more. I think we should teach Python _using_ AI, that is, teach how to write and debug Python code _using_ AI. That'll end up teaching skills people will _really_ need. <!-- https://chatgpt.com/c/6a38968d-0194-83e9-9228-23b586e556d3 -->
- Computational thinking = Decomposition + Abstraction + Algorithm design + Pattern recognition.
  In AI, that translates to = Framing + Context engineering + Orchestration (harness engineering?) + Verification design. Maybe I'd add Assetization / Systems.
  <!-- https://claude.ai/chat/a4beee77-d7a3-4ee5-9b57-cea2a85f1e6d + https://chatgpt.com/c/6a38a93b-6f98-83ee-b61a-e74d427c405f -->

## Questions I was asked

[Week ending 28 Jun 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-06-28)

- **Question**: Why is building invoice generation the wrong next step after finding reconciliation errors?\
  **Answer**: Fix the wrong number inside the existing workflow. Don’t replace a working accounting system with new software just because you can generate a PDF.
- **Question**: In enterprise AI delivery, should the reusable accelerator be the large part and client customization the small part?\
  **Answer**: No. The common layer is usually thin; customization is the larger part because client environments and workflows vary.
- **Question**: Why not automatically send every prompt to ChatGPT and Claude in parallel?\
  **Answer**: Don’t remove all friction. Prompting is cheap; reading is the bottleneck. A tiny copy-paste cost stops me from generating outputs I will never review.
- **Question**: What are the most common corporate pushbacks to implementing AI?\
  **Answer**: Security, hallucinations, and cost—in that order.
- **Question**: Do forward deployed engineers need to be onsite?\
  **Answer**: No. They need access to the client environment and stakeholders; physical location is secondary.
- **Question**: Why ask the agent to solve the problem directly instead of first researching existing models?\
  **Answer**: Start direct. If it fails, break it into chunks. It saves time and tests whether the model has become smart enough to handle broader delegation.
- **Question**: What best practices should non-coders follow when vibe-coding enterprise products?\
  **Answer**: Don’t optimize the old software workflow. State the business goal, let the agent build whatever is needed, and review the output hard.
- **Question**: For a high-stakes EMS, should we deliver software or the decisions it produces?\
  **Answer**: Deliver decisions. Software, agent, and human together are the stack; price the outcome, not the code, tokens, or FTE effort.
- **Question**: How can we guarantee decisions if humans cannot be right every 15 minutes?\
  **Answer**: Treat it like a warranty. If the decision is wrong, don’t pay me; if it is right, pay X. Price in the error margin.
- **Question**: Should a high-stakes EMS use a deterministic mathematical model with an agentic layer on top?\
  **Answer**: Yes. What you know for sure goes into the program; what you don’t know stays with the agent or human. Benchmark both on the outcome.
- **Question**: How do you get yourself out of the loop instead of becoming the bottleneck?\
  **Answer**: Keep an AI bottleneck log. Every time I am stuck, I ask AI how to remove that bottleneck; “interview me” and “assetize this” are surprisingly effective.
- **Question**: In AI hiring, who should we hire when specific skills keep getting commoditized?\
  **Answer**: Hire flexibility, not fixed skill. The “best” data scientist, engineer, or product manager can become legacy in months.
- **Question**: How do we train sales and delivery leaders to speak credibly about AI solutions?\
  **Answer**: Don’t run classroom AI training. Run live solution labs where leaders use AI on a real workflow, build the first output, and draft what they will take to the client.
- **Question**: Can AI help me structure client pitches without depending on internal experts?\
  **Answer**: Yes. Feed it the messy conversation, files, links, and prior context. It won’t be identical to an expert, but it can produce above-average analyst output at scale.
- **Question**: What attitude helps people start using AI every day?\
  **Answer**: Don’t take AI too seriously. Its job is to serve you; give rough instructions, ask it to interview you when you’re unclear, and iterate.
- **Question**: Is clicking “Ask AI” a good signal that students are struggling?\
  **Answer**: Not by itself. Smart students may click it to save time. Combine it with performance and behavior data before deciding intervention.
- **Question**: Do forward deployed engineers just produce “insights on steroids,” or should they deploy AI into workflows?\
  **Answer**: They should move through stages: identify use cases, solve like an analyst, drive action, then embed it into production. Insight is only the first useful step.
- **Question**: How do we move from after-the-fact AI analytics to AI that prevents workflow errors?\
  **Answer**: Put the check where the data enters. Let the agent inspect current controls, propose guardrails or code, and turn recurring insights into monitored workflow.
- **Question**: Will enterprise AI deployments mostly live inside existing platforms rather than custom infrastructure?\
  **Answer**: Yes. Most deployments will happen where the data and workflow already live. Master the platform harnesses instead of building everything from scratch.
- **Question**: What do I do when I don’t even know the problem in a broad domain like rights?\
  **Answer**: That is the problem. Give the context to an agent and ask it to find, rank, validate, and build the easy use cases.
- **Question**: If clients can also use AI agents, what value do I add as a media expert?\
  **Answer**: If they could do it, they would have. Your value is harnessing agents with private data, schemas, validation code, skills, and test cases they don’t yet have.
- **Question**: Should we position our R&D product-plus-service offering as AI?\
  **Answer**: Maybe don’t. Use AI to serve more clients better and faster, but sell the outcome. The client neither cares nor needs the AI story.
- **Question**: What should I not do in GTM while selling AI plus services?\
  **Answer**: Don’t fight with your co-founder. Put someone in the US. Don’t be dogmatic: it is okay to do what the business needs.
- **Question**: Is there a case for building small language models for industry-specific process knowledge?\
  **Answer**: Use case, yes. SLM as default solution, no. Put a modern agent on the problem and let it choose tools; SLMs are usually expensive, depreciating, and behind frontier agents.
- **Question**: Is adding AI sentiment and renewal probability into CRM enough?\
  **Answer**: It is only half a step. Don’t give reps another signal; use bulk data to create watchlists, proactive calls, and specific actions.
- **Question**: Is a quick AI-built sponsorship visualization valuable for a new executive?\
  **Answer**: Useful once, but not enough. Executives need decisions: who pays most, what expires, what action to take, and how much money is at stake.
- **Question**: As a GenAI engineer, do I need deep ML knowledge?\
  **Answer**: Not as the main bet. If it is teachable and testable, AI will do it. Learn to define the problem, test the output, and use the model’s expertise.
