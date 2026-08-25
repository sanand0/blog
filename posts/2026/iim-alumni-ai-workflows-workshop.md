---
title: IIM Alumni AI Workflows Workshop
date: 2026-06-21T13:01:47+08:00
categories:
- llms
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7474328099581513729/
description: 'I ran an IIM Alumni workshop in Singapore on AI tools and workflows: transcribing recordings with Google AI Studio, verifying claims across models, and building reusable skills.'
tags: [ai-workflows, ai-agents, google-ai-studio, productivity]
---

The theme of yesterday's workshop for the IIM Alumni at Singapore was **Tools and Workflows** was:

Agents are getting smarter, so they know what to do.\
Tools agents can use are growing and are more powerful.\
This combinatorial explosion creates explosive possibilites.

This workshop covered the following six workflows:

1. **Leverage transcripts.** Use [Google AI Studio](https://aistudio.google.com/prompts/new%5Fchat) to transcribe non-sensitive recordings with a reusable ["don't miss anything"](https://github.com/sanand0/blog/blob/9763887917a006c8aa76b4fc60ed2202548bab6f/pages/prompts/transcribe-talk.md) prompt. AI Studio's record button is a ready-to-use transcriber.
2. **Simplify dense text** as a [comic](https://www.s-anand.net/blog/creating-comic-explainers/), an [infographic](https://notebooklm.google.com/), a [story](https://talks.s-anand.net/2026-05-23-ai-unboxed-context-engineering/). Image generation is now a tool call an agent runs for you. Then [compress it as AVIF on Squoosh](https://squoosh.app/) before you email it to a thousand people.
3. **Verify - cheaply.** Paste one suffix: _"Break this into key claims, mark certainty, flag the five highest-risk ones, and tell me how to verify or falsify each."_ Convert to a [skill](https://skill.md/) to automate. Cross-checking with multiple models took [error from 14% to 0.7%](https://sanand0.github.io/llmevals/double-checking/).
4. **Skills are assets.** A [skill](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) tells the agent "here's how _I_ do stuff." Build them slowly, edit them weekly, and they compound for years. No skills support in your tool? Keep them as copy-pasteable prompts.
5. **Brainstorm by forcing range.** [Ban the five obvious ideas; borrow from unrelated domains](https://github.com/sanand0/scripts/blob/d9fde4f5f169c1d465603e0cd6095db3fcdabad3/agents/ideation-protocol/SKILL.md); smash two random concepts together with the [Ideator](https://tools.s-anand.net/ideator/). Hallucination is a feature when you're being creative.
6. **[Schedule tasks](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt).** Weekly regulatory scans, daily meeting prep, market briefings - and even an ["unreasonable gesture"](https://www.s-anand.net/blog/prompts/unreasonable-gesture/) nudge. As AI hides the tech, human relationships gain value.

Here's the [talk video](https://youtu.be/H3GmGl1hzxM) and [full story + transcript](https://talks.s-anand.net/2026-06-20-ai-unboxed-tools-workflows/).

![](https://talks.s-anand.net/2026-06-20-ai-unboxed-tools-workflows/comic-page.avif)
