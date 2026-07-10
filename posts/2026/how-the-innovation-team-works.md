---
title: How the Innovation Team works
date: 2026-05-03T16:15:15+08:00
categories:
    - how-i-do-things
description: I analyzed 44 meeting transcripts to codify my innovation team’s 'demo-first' operating model. We prioritize 24-hour turnarounds, steering AI agents, and action over analysis. Use LLMs on your own recordings to identify hidden principles and bottlenecks.
tags: [information-management, ai-agents, film-analysis]
---

Based on 44 meeting recordings from February to late April 2026, here's how Straive's small team (3-6 people at any time, mostly freshers and interns) produce a continuous stream of client-facing demos across topics as diverse as image filtering, geospatial analysis, insurance contract verification, NFL medical scoring, OCR benchmarking, and song similarity clustering — often with a 24–48 hour turnaround from assignment to demo.

<!-- https://claude.ai/chat/01381de8-0037-4096-bd00-90f5a3c0b1b0 -->

<section ai-disclosure="ai-generated" data-ai-model="claude-sonnet-4.6" data-ai-provider="Anthropic">

Here is how the team works:

1. **Build demos, not products.** Every task traces to a specific client meeting with a known date. "Done" means good enough to show once to one audience — not production-ready. The moment a demo works, it gets shown; refinement happens only if the client asks for more.
2. **Show output first, always.** Start every update by showing the thing — not explaining what you did to build it. If you don't have output yet, say so in one sentence and then show where you are. Process is for after the food arrives.
3. **One person holds all client context.** The team lead attends client meetings, filters what matters, and translates it into specific buildable tasks. Team members build; they don't need to know why. This keeps work relevant and prevents wasted effort on misaligned output.
4. **Explore broadly, cut ruthlessly.** Multiple tracks run simultaneously — robotics, embeddings, OCR, formal logic — but anything that doesn't demo well gets dropped fast. The sequence is always: assign a loose exploration, see output quickly, deepen what works, kill what doesn't.
5. **Compress everything.** Small files, single HTML pages, 50KB images, 30-line YAMLs. This isn't aesthetic — demos need to load in bad hotel WiFi, repos need to clone in meetings, and files need to forward over email. Technical choices serve the demo context.
6. **Make pipelines reproducible after they work.** Once a demo runs, it needs shell scripts or CLI commands that reproduce it from scratch. No committed data, no manual steps, no "ask X how it works." If someone can't clone and run it, it doesn't exist as an asset.
7. **Operate AI agents, don't just use them.** The team's primary skill is steering coding agents — Codex, Claude Code, Copilot — toward specific outputs under specific constraints. When stuck, push harder ("drive it to death"), switch agents, or change the prompt. Don't wait for instruction on how to build something; use the agent to figure it out.
8. **Numbers, not observations.** Every story needs a specific number: 252 test cases passed, $22 for 2,300 slides, 40% cheaper per-deck vs. per-slide. Vague quality claims don't survive a client meeting. If a finding can be quantified, quantify it; if it can't, find a different finding.
9. **Action over analysis.** The output of every demo should answer "what do I do?" not "what do I know?" Sort students by who needs a call today, not by distress score distribution. Surface the critical failure in the warehouse footage, not a compliance percentage. The analysis can be one click away — it should never be the headline.

However, there are many improvements the team needs to make.

1. **The Single Point of Failure Problem** The entire team is dependent on Anand for direction, client context, task assignment, quality review, and stakeholder relationships.
2. **Missing: Taxonomy and Discoverability of Demos** The team produces dozens of demos, benchmarks, and data stories. There's a vague mention of a "catalog" and a "demo list" that Anand maintains, but it's personal and opaque.
3. **Missing: Explicit Knowledge Transfer Between Members** Team members work on parallel tracks with little cross-pollination. X's work on 3D benchmarking uses similar methodology to Y's UMAP work, but they don't reference each other's approaches. When Anand wants them to collaborate, he explicitly engineers it.
4. **The Presentation Quality Gap** Team members consistently make the same presentational errors across many months. Anand corrects these every time, but they recur because the corrections aren't being internalized or documented.
5. **Client Handoff Documentation Is Missing** Several demos reach clients without clear documentation of what was built, what the inputs were, and how to reproduce or extend it. Straive's pitch is "here is what AI can do for you" — but without handoff documentation, clients can't do anything with the demo.
6. **The Timing Problem on Model Choices** The team regularly uses outdated or suboptimal models, then switches when Anand notices. The team doesn't have a maintained "current best model for X task" reference. Each person relies on whatever they used last time or whatever they happen to know about.
7. **The Right Senior Mentorship for the Right Stage** Anand is simultaneously mentor, product manager, client liaison, and technical reviewer. This works but creates a bottleneck. More importantly, some of the most valuable mentorship happens late. The team would benefit from more structured "junior reviews senior's plan before execution" moments — not Anand reviewing output after, but Anand reviewing the *approach* before.

</section>

---

Every point is spot on and totally useful to me. The best part is that it just required me to paste the transcripts and ask it to analyze the team's structure.

**You can analyze your own team meetings too**. Paste a dozen transcripts into a good AI agent and ask it:

> Based on these transcripts, what are my team's principles and operating model? How should we improve and why? Share with specific examples from the transcript.

This is like hiring a $100/hr organizational consultant to attend your meetings and give you personalized feedback!
