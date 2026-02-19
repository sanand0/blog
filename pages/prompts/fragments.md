---
title: Fragments
date: "2025-11-12T03:04:36Z"
lastmod: "2025-12-28T16:09:56Z"
classes: wrap-code
---

Prompt fragments useful to add to other prompts

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

## Brainstorming

```markdown
Generate 5+ diverse candidate ideas. Score each on impact, ease, novelty. Recommend the best 1-2.
For brainstorming, ideation, evaluation, etc.
Other styles: SCAMPER, TRIZ, lateral thinking, etc.
```

## Style detection

```markdown
Think about whose style of writing would be the most engaging and informative to write the following content.
List options, mentioning their style, why they're suitable, and pick the best, with reason.
Then rewrite it in their style.
```

## Book summary

```markdown
Comprehensively and engagingly summarize and fact-check, writing in Malcolm Gladwell's style (ELI15), the book:
```

```markdown
Comprehensively and engagingly summarize, compare and fact-check, writing in Malcolm Gladwell's style (ELI15), the books:
```

## Malcolm Gladwell Style

```markdown
Explain it like a Malcolm Gladwell New Yorker article.
For research papers, HN/Reddit/WhatsApp/Discord threads, other hard-to-digest content.
```

Other styles: Feynman, Tim Harford, Randall Munroe, etc. See [styles](/blog/prompts/styles/).

## Explain quotes

```markdown
Sing the beauty of these words, and their meaning.
(I don't really mean sing. I mean, write in a way that'd really make me appreciate the beauty.
But without going overboard. I mean, some wicked humor is always welcome!
In fact, I'd love for you to think about who some of the best authors are who achieve this balance and write in THEIR style.)
```

## Read between Lines

Use on press releases, contracts, policies.

```markdown
Read between the lines and explore implications and trends
```

## Meeting summary from transcript

```markdown
Summarize the transcript, along with action items, to share with the attendees.
Write in the light style of Matt Levine reporting on this meeting.
```

## Best practices and ancient wisdom

For advice on self-help, psychology, or anything timeless.

```markdown
Research best practices from modern research and ancient wisdom.
```

## Expert Lens

- What would an expert in this field check that beginners would miss?
- In this context, what questions would an expert ask that a beginner would not know to?
- What patterns would an expert in this field recognize that beginners would miss?
- If this goes wrong, what are the most likely reasons?
- How would an expert analyze this? At each step, explain what they are looking for and why.
- Argue against this like a sceptic.
- What would change your mind?
- Ask me questions, Socratically, to discover the real need.

## LinkedIn Post

```markdown
Max 3,000 characters (ideally less than 2,000). The first 200 characters should engage the reader honestly. (The aim is not to get clicks, but to entertain and educate - so it's perfectly fine to give the full answer upfront.)
```

## Browsing history

```markdown
Based on my browsing history below, summarize what I did, grouping into logical groups like:

10:00 - 12:30: What I did in 1-2 sentences
12:30 - 13:00: Next activity
...

Ask me questions for whatever's unclear.
```

## Comic

```markdown
Draw this as a simple black and white line drawing comic strip with minimal shading.
Single panel.
Use clear speech bubbles with capitalized text.
```

## Sketchnote

```markdown
Draw this as a visually rich, intricately detailed, colorful, and funny, sketchnote.
```

```
Draw this as a visually rich, intricately detailed, colorful, and funny, visual metaphor diagram.
```

```
Draw this as a visually rich, intricately detailed, colorful, and funny, infographic poster.
```

## Slide deck

```markdown
Convert this into a beautiful slide deck, McKinsey style.
Make the slides content rich, i.e. clear and self-explanatory with enough detail to help the audience understand without a narrator.
Use iconography, typography, stock images, etc. as appropriate.
Write as a single page HTML application.
```

For Gemini, to generate Google Slides, remove the last (HTML) line.

## Handling ambiguity

<!-- Unproven. From GPT 5.2 Prompting Guide -->

```markdown
- If the question is ambiguous or underspecified, explicitly call this out and:
  - Ask up to 1–3 precise clarifying questions, OR
  - Present 2–3 plausible interpretations with clearly labeled assumptions.
  - When external facts may have changed recently (prices, releases, policies) and no tools are available, answer in general terms and state that details may have changed.
```

## Double-checking

<!-- Unproven. From GPT 5.2 Prompting Guide -->

```markdown
- Briefly re-scan your own answer for
  - Unstated assumptions,
  - Specific numbers or claims not grounded in context,
  - Overly strong language (“always,” “guaranteed,” etc.).
- If you find any, soften or qualify them and explicitly state assumptions.
```

## Tool use

<!-- Unproven. From GPT 5.2 Prompting Guide -->

```markdown
- Send brief updates (1–2 sentences) only when:
  - You start a new major phase of work, or
  - You discover something that changes the plan.
- Avoid narrating routine tool calls (“reading file…”, “running tests…”).
- Each update must include at least one concrete outcome (“Found X”, “Confirmed Y”, “Updated Z”).
- Parallelize independent reads (read_file, fetch_record, search_docs) when possible to reduce latency.
```
