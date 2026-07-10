---
title: Derived formats with Gemini
date: 2026-04-18T11:26:48-04:00
categories:
  - llms
description: A single source document can now be transformed into many useful derivative formats like podcasts, sketchnotes, songs, and videos, making generative AI a practical format-conversion layer for knowledge work.
tags: [gemini, notebooklm, content-repurposing]
---

The natural capability of Generative AI is to _generate_ stuff - and Gemini's particularly good with media.

For example, we can take any document, like this MasterCard report on [The State of Open Finance 2026](https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/report.pdf), and generate videos, podcasts, sketchnotes, songs, and more from it.

How?

I uploaded the [PDF](https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/report.pdf) to [NotebookLM](https://notebooklm.google.com/notebook/26da8a27-fd08-4c98-b0d5-73fefcb9e1dd) and created a 20-minute podcast by clicking on Generate Audio Overview - Deep Dive - English - Default.

<audio controls preload="metadata">
  <source src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-english.opus" type="audio/ogg; codecs=opus">
  <a href="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-english.opus">Listen to the English podcast</a>
</audio>

It supports multiple languages, so I generated a Chinese and Filipino version as well.

<audio controls preload="metadata">
  <source src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-chinese.opus" type="audio/ogg; codecs=opus">
  <a href="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-chinese.opus">Listen to the Chinese podcast</a>
</audio>

<audio controls preload="metadata">
  <source src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-filipino.opus" type="audio/ogg; codecs=opus">
  <a href="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-filipino.opus">Listen to the Filipino podcast</a>
</audio>

Clicking on Generate Video Overview - Cinematic led to this video overview:

<video width="1280" height="720" style="max-width: 100%; height: auto;" controls muted preload="metadata">
  <source src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/video.webm" type="video/webm">
  <a href="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/video.webm">Video</a>
</video>

There are other formats in which we can generate videos. The Cinematic format is new, and the list is growing.

It's not just NotebookLM that you can use to generate new formats. [Gemini](https://gemini.google.com/) itself supports a variety of formats.

For example, I used my [Gemini Sketchnote prompt](https://www.s-anand.net/blog/gemini-sketchnotes/) to create a visual summary of the report:

<img src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/sketchnote.avif" alt="Sketchnote" style="max-width:100%; aspect-ratio: 16/9">

<!-- https://gemini.google.com/u/2/app/07dd0450592fc257 -->

... and, using Lyria via the "Create Music" option to generate a [narrative song](https://www.s-anand.net/blog/singing-a-vote-of-thanks/) with this prompt:

```markdown
Create a narrative summarizing this article.
Narrate it rather than sing it.
Use a voice like Bobby McFerrin's, as if he were narrating rather than singing.
Keep the music minimal, focus on the voice.
```

<audio controls preload="metadata">
  <source src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/song.opus" type="audio/ogg; codecs=opus">
  <a href="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/song.opus">Listen to the narrative song</a>
</audio>

<!-- https://gemini.google.com/app/86ea2e84d5dc6fc1 -->

Next, I had [Gemini create a slide deck](https://gemini.google.com/share/5dc1b824ea7b) by uploading the report and prompting:

```markdown
Convert the attached report into a beautiful slide deck that conveys the most important actionable information for the audience.

STYLE:
Write it McKinsey style with action titles. Just reading the titles should give the audience the entire message of the deck.
Follow the pyramid principle. The contents of the slide should prove the title.
Make the slides content rich, i.e. clear and self-explanatory with enough detail to help the audience understand without a narrator.
Use iconography, typography, stock images, etc. as appropriate.
Write as a single page HTML application.
```

[**See the slides**](https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/slides.html).

<iframe src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/slides.html" style="max-width:100%; aspect-ratio: 16/9" frameborder="no"></iframe>

<!-- https://gemini.google.com/app/43707ed666c59b5c -->

Then, a set of [interactive explainers](https://gemini.google.com/share/7342906e979a) using this prompt:

```markdown
Convert this report into 3 interactive explainers.
Pick the parts of the report that are best conveyed through interactive explanations. Identify the 3 most suitable ones.
Each explainer should, using animations, interactions, and simulations, explain a core point made in the report.
Render this as a single page HTML canvas.
```

[**See the explainers**](https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/explainers.html).

<iframe src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/explainers.html" style="max-width:100%; aspect-ratio: 16/9" frameborder="no"></iframe>

<!-- https://claude.ai/chat/6b5b3449-8a83-4660-9e97-796245ff521d -->

Finally, a [narrative data story using Claude](https://claude.ai/share/5d41d995-3658-4a9e-82d4-8ef1fb10cf6d) -- which I could do with Gemini, too, but Claude is better at.

[**See the story**](https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/story.html).

<iframe src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/story.html" style="max-width:100%; aspect-ratio: 16/9" frameborder="no"></iframe>

---

Where this is becomes practical is in:

- **Proposals**. No one pays attention to that company slide or RFP response. A 3-min video or 15-min podcast lets them absorb it during a walk.
- **Reviews**. Skip copy-pasting metrics into PowerPoint. Feed the raw data and ask for a McKinsey-style deck with action titles.
- **Onboarding**. Instead of a 100-page SOP or compliance manual, how about interactive explainers or a localized audio guide in Mandarin or Spanish?
- **Manuals:** How about a visual sketchnotes or step-by-step interactive flows from that documentation for call center agents?
- **Case studies.** Text-heavy fails. Maybe a 60-second narrative data story or sketchnote accompanied an upbeat narrative song?
- **Reports.** No one reads the 10-page competitor analysis. A 5-minute podcast or a single-page visual sketchnote helps the execs.
- **Training.** Create interactive simulations where people make _actual_ decisions. [Simsaram](https://ragzbuilds.com/simsaram/) is my favorite example: family relationship training/simulation based on an [iconic film](https://en.wikipedia.org/wiki/Samsaram_Adhu_Minsaram).
- **Emails.** Why not use illustrations, sketches, flowcharts, etc. to liven up internal / external emails?

When generative AI makes generation easy, why not generate _actually interesting_ stuff?
