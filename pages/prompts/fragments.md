---
title: Fragments
date: "2025-11-12T03:04:36Z"
lastmod: "2025-12-28T16:09:56Z"
classes: wrap-code
---

Prompt fragments useful to add to other prompts

## Analysis notes

```markdown
As you analyze, note any interesting findings (patterns, anomalies, alternate perspectives, future explorations) in notes-v1.md.
```

## Best practices and ancient wisdom

```markdown
Research best practices from modern research and ancient wisdom.
```

## Binding constraints and slow variables

```markdown
Identify the binding constraints and slow variables — what governs here regardless of improvements elsewhere?
```

## Blog post

```markdown
Write in a crisp first-person blog voice: conversational, curious, and slightly mischievous, describing exactly what you did and what happened.
Be terse: short sentences, short punchy paragraphs, and occasional lists. Use simple words. Avoid corporate fluff and jargon. Max 300 words.
Use bold sparingly for scannability and italics to emphasize key insights. Divide sections with `---`. Avoid headings.
Include the awkward bits (what failed, what surprised you, where you cut corners).
Parenthetical asides for dry humor.
Pull out one non-obvious lesson. Admit uncertainty, and end with an insightful, practical recommendation.
Include links wherever relevant to sources, tools, code, etc.
Show key snippets of actual prompts & results verbatim in code blocks.
```

## Blog description and keywords metadata

```markdown
Generate a description and keywords as metadata for this blog post. Format:

description: ...
keywords: [..., ..., ...]

The description is a crisp one-sentence answer to: What is the main point or most useful takeaway here?
1 sentence, 20-40 words. Prefer concrete ideas over framing. Include distinctive methods, domains, tools, or concepts when central.

Keywords are the smallest set of search terms that would help an AI agent decide whether this content is relevant.
4-8 lower-case topic phrases. Avoid generic tags and redundant synonyms. No preamble, no markdown, no explanation.
```

## Book summary

```markdown
Comprehensively and engagingly summarize and fact-check, writing in Malcolm Gladwell's style (ELI15), the book:

Comprehensively and engagingly summarize, compare and fact-check, writing in Malcolm Gladwell's style (ELI15), the books:
```

## Brainstorming creative ideas

```markdown
- IDEATE prioritizing novelty over feasibility. Do not filter.
  - Choose 3–5 distinct people who'd see this differently. For each, generate 3 short candidate ideas.
  - Choose 2 UNRELATED domains and for each, extract 3 atomic structural rules, and use them to create 4 more candidate ideas.
  - List the 5 most obvious / conventional ideas across all candidates. Ban them, along with near-duplicates.
  - Merge all remaining ideas removing overlaps. Keep the set maximally diverse across mechanisms, users, and time horizons.
- CONVERGE:
  - Critique each surviving idea: what assumption must hold, why it is non-obvious, and why it may fail.
  - Score each idea on impact, novelty, and speed.
  - Recommend the best practical idea(s) and the best wildcard idea(s), explaining the non-obvious insight each is built on.
```

Older version:

```markdown
Choose 3–5 distinct ordinary personas who would see this problem differently.
For each persona, generate 3 short candidate ideas.
List the 5 most obvious / conventional ideas across all candidates. Ban them, along with near-duplicates.
Choose 2 unrelated domains. For each domain, extract 3 atomic structural rules. Use those rules to create 4 more ideas for this task.
Merge all ideas removing overlaps. Keep the set maximally diverse across mechanisms, users, and time horizons.
Critique each surviving idea: what assumption must hold, why it is non-obvious, why it may fail, and what makes it genuinely useful.
Score each idea on impact, novelty, ease, and speed.
Recommend 2 ideas: the best practical idea and the best wildcard idea, explaining why it beat the more obvious alternatives.
```

For brainstorming, ideation, evaluation, etc. [This uses](https://gemini.google.com/share/deaaeb543991):

1. Denial Prompting (Constraint-based generation): avoid the obvious ideas
2. Universe of Thoughts (Granular Decomposition): decompose unrelated domain rules and apply
3. Iterative Refinement (Adversarial Roles): critique each idea, then refine

<!--
https://gemini.google.com/app/16d01a74d131ee13
https://chatgpt.com/c/69cb9c74-8fe8-839b-968f-cfb93b29872c
https://claude.ai/chat/a9b0a7e6-add6-4a1e-ad5e-d6a4018edc5c
-->

Other styles: SCAMPER, TRIZ, lateral thinking, etc.

## Browsing history

```markdown
Based on my browsing history below, summarize what I did, grouping into logical groups like:

10:00 - 12:30: What I did in 1-2 sentences
12:30 - 13:00: Next activity
...

Ask me questions for whatever's unclear.
```

## Claude Code Chunk / Fragment data story

```markdown
IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, you MUST break this into parts, generating the .html in chunks or layered edits (keeping each chunk small, max 100KB of edits) and saving it, checking it, then updating it with the next iteration, and so on.
```

## Core concepts

```markdown
What are the core concepts, i.e. top NON-INTUITIVE well-established lessons/principles, of **\_\_**, knowing which, most of the rest of the field is derivable?

- Source comprehensively from authoritative sources.
- Pick the 10 that are mentioned repeatedly, have the highest applicability and usefulness, while being non-obvious.
- Fact-check each concept. Include references to authoritative sources.
- Write as a bulleted point. Explain each concept in a few simple sentences (ELI15) that are easy to understand intuitively.
```

## Draw Comic

```markdown
Draw this as a simple black and white line drawing comic strip with minimal shading.
Single panel.
Use clear speech bubbles with capitalized text.
```

## Demo explanation

Copy-paste content from an application to demo as Markdown. Then add this.

```markdown
Given this content from an application, how should I demo it and what should I point out as specific examples. Use concise bullets.
```

<!-- Example: https://gemini.google.com/app/cb939e416e331490 -->

## Draw Comic using Suggestion

```markdown
Give me ideas for a single panel comic that VISUALLY communicates the spirit of (or the central or key message of) the content below.
Pick a SINGLE point to convey.
Use simple ideas or analogies that are highly relatable and easily drawable and won't need text to explain.
It doesn't have to involve AI, robots, tech, etc. Simple, relatable analogies emphasizing the central concept are perfect.
Funny is good.
DO NOT DRAW. Just give me simple, funny ideas.
```

## Draw Infographic poster

```
Draw this as a visually rich, intricately detailed, colorful, and funny, infographic poster.
```

## Draw Sketchnote

```markdown
Draw this as a visually rich, intricately detailed, colorful, and funny, sketchnote.
```

## Draw Sketchnote (thinking)

```markdown
Draw this as a visually rich, intricately detailed, colorful, and funny, sketchnote.
Think about the most important points, structure it logically so that the sketchnote is easy to follow, then draw it.
```

## Draw Visual metaphor diagram

```markdown
Draw this as a visually rich, intricately detailed, colorful, and funny, visual metaphor diagram.
```

## Explain quotes

```markdown
Sing the beauty of these words, and their meaning.
(I don't really mean sing. I mean, write in a way that'd really make me appreciate the beauty.
But without going overboard. I mean, some wicked humor is always welcome!
In fact, I'd love for you to think about who some of the best authors are who achieve this balance and write in THEIR style.)
```

## Expert Lens

```markdown
Plan like an expert. In this context, first think about:

- What patterns would an expert in this field check / recognize that beginners would miss?
- What questions would an expert ask that a beginner would not know to?
- What problems / failures would an expert anticipate that beginners may not be aware of?
- What powerful & relevant mental models would an expert apply in this context?
```

I dropped the following:

- How would an expert analyze this? At each step, explain what they are looking for and why.
- Argue against this like a sceptic.
- What would change your mind?
- Ask me questions, Socratically, to discover the real need.

## Interactive explanation

Inspired by [Simon Willison's interactive explanations](https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/):

```markdown
Create an animated, interactive explanation of this.
Use smooth animation to help the user feel the flow.
Allow the user to pause, play, speed up, slow down, step forward/backward, or jump to any point in the timeline via a slider (like a video player).
Include clear explanation of each step with visual cues to highlight relevant parts and metadata/tags for the current step.
```

## Interactions, tooltips and popups

<!-- https://claude.ai/chat/038c0bea-8d76-4ea4-85ff-b0be231c2457 -->

```markdown
Use tooltips, popups, interactions, and animations as informative and engaging aids.

**Tooltips** are for:

- Context about non-obvious terms or phrases (only if relevant and useful)
- Additional context about references (where possible)
- Metadata and context about data points, table cells, chart elements, etc. (always)
- Guidelines:
  - On mobile, use tap-to-reveal with clear dismiss affordance (tap elsewhere or an × icon); auto-reposition to stay within the viewport.
  - Debounce on hover. Only 1 tooltip at a time.
  - Do not show tooltips where the tooltips add no meaningful value or additional information beyond the text.

**Popups** are for:

- Citations. Search for and include references. Cite the key point from the reference and link to it.
- Files. Link liberally to files as supporting evidence.
  - Clicking on file links should open the files in a popup, with a link to open the original in a new tab.
  - Syntax-highlighted if code
  - Show sortable for tabular data, gradient-coloring important numeric / categorical columns if that will help understand the context
- Data points. Provide extensive context for data points.
  - Wherever useful, clicking on data points, table cells, chart elements, etc. should open a popup that provides full context about that element.
  - Include narratives, cards, tables, charts, or even entire dashboards that answer what the user is likely to be curious about or wants to dig in for more details. E.g. context, examples, related metrics, trends over time, breakdown by relevant dimensions, etc.
  - Standardize the format of these popups so users know what to expect. Reuse popups by archetype.
- Guidelines: Trap keyboard focus inside. Contain scrolling. Show loading state when required. Use a consistent anatomy.

**Interactions** can include:

- Scrollytelling. As the user scrolls, trigger changes in charts, illustrations, narratives, etc. to guide them through the story.
- Sliders that allow users to adjust assumptions, scenarios, etc. and see the impact in real time. Keep input & output close - without scrolling.
- Interactive explainers that let the user step through a process, pause, play, speed up, slow down, step forward/backward, or jump to any point in the timeline via a slider (like a video player), with clear explanation of each step and visual cues to highlight relevant parts and metadata/tags for the current step.
- Transition on value change. Animate chart values between states (e.g., bar heights morphing) rather than jump-cutting.
- Streaming text to simulate LLM responses. Stream word-by-word, at ~4 words per second, with a controllable rate, using a blinking cursor at the end to show that it's still generating.
- Progressive reveal quiz. Ask user a question, reveal answer against their guess. Related to scenario forking: choose your own adventure style branching based on user choices.
- Comparisons. Pairwise comparisons, pinnable for comparison, swipe to compare, etc.
- Brushing and linking. Select a region in one chart to highlight related data nearby.
- Small multiples. Show a grid of small charts, letting user expand any SMOOTHLY into a full view - with more details.
- Filters & search.
- Also: Trails. Cursor morphing. Magnetic snapping. Intertial scrolling/panning. Contextual axis transitions.

**Animated SVGs** are for:

- Explaining processes, mechanisms, workflows, etc. The aim is to make users FEEL the process. One glance should give them an intuitive understanding of how it works, even before they read the accompanying text. Show how things are connected, what data flows from where to where, how elements, interact, etc.
- Guidelines: Use GPU-friendly rendering (transform, opacity). Sequence multiple animations deliverately. Respect `prefers-reducted-motion`.

**Principles** to follow:

- Meaningfulness: think carefully about what will be meaningful and useful for the audience to see, based on their objective. The goal is to help them understand and act.
- Visual quality: is critical. Use consistency, bold typography, contrast, visual hierarchy, progressive disclosure, repetition, alignment, information density calibration, and other principles of visual design - while also evaluating relevant visual format innovation.
- Responsive design: all interactions, tooltips, and popups work well on different screen sizes and devices.
- Accessibility: keyboard navigation, minimum contrast ratios, etc.
- URL-driven state: Slider positions, toggle states, and selected scenarios should be reflected in bookmarkable URL parameters.

**Errors to avoid**:

- Visibility: ensure nothing overlaps, get cut off, or becomes inaccessible because we can't scroll to it, etc.
- Performance: ensure loading is fast, latency < 100ms, even with large datasets or complex visualizations.
- Common bugs: tooltip/popup positioning during scroll / resize, z-index warefare, orphaned event listeners, etc.

Plan the design and layout carefully before coding. Sketch the information architecture, interaction inventory, design tokens, performance sensitive paths, responsive breakpoints, etc.
```

## List transcript insights / facts

Use ChatGPT - it's the most rigorous

```markdown
List every learning / interesting fact from the transcript in sequence.
```

## LinkedIn Post

```markdown
Max 3,000 characters (ideally less than 2,000). The first 200 characters should engage the reader honestly. (The aim is not to get clicks, but to entertain and educate - so it's perfectly fine to give the full answer upfront.)
```

## Meeting transcript summary

```markdown
Summarize the transcript, along with action items, to share with the attendees.
Write in the light style of Matt Levine reporting on this meeting.
```

## Meeting transcript fact list

```markdown
List every learning / interesting fact from the transcript in sequence.
```

## Photo coloring / upscaling

Nano-banana 2 finds it hard to follow instructions. "Pay extra attention to the faces and get the EXACTLY as in the original" worsens the result. So I just say:

```markdown
Upscale this image into a modern digital color photograph retaining EVERYTHING in the original perfectly.
```

## Pre-mortems

```markdown
What kills things like this?
If a year later this CLEARLY failed, how might that have happened?
What's the first thing that breaks with scale?
What's the biggest assumption that could fail?
Who loses if this succeeds, and how will they stop it?
What excuses abandon these?
How would one make this fail?
```

Alternative:

```markdown
Did you fully address both the letter AND spirit of my question?
List any shortcuts taken, corners cut, or ways you optimized for appearing correct rather than being correct.
What did I actually want vs what you provided?
```

## Read between Lines

Use on press releases, contracts, policies.

```markdown
Read between the lines and explore implications and trends
```

## Slide deck

```markdown
Convert this into a beautiful slide deck, McKinsey style with action titles. Just reading the titles should give the audience the entire message of the deck.
Follow the pyramid principle. The contents of the slide should prove the title.
Make the slides content rich, i.e. clear and self-explanatory with enough detail to help the audience understand without a narrator.
Use iconography, typography, stock images, etc. as appropriate.
Write as a single page HTML application.
```

For Gemini, to generate Google Slides, remove the last (HTML) line.

## Song narrative

```markdown
Create a narrative summarizing this article.
Narrate it rather than sing it.
Use a voice like Bobby McFerrin's, as if he were narrating rather than singing.
Keep the music MINIMAL, NO intro/outro music, and focus ENTIRELY on the voice.
```

## Style detection

```markdown
Think about whose style of writing would be the most engaging and informative to write the following content.
List options, mentioning their style, why they're suitable, and pick the best, with reason.
Then rewrite it in their style.
```
