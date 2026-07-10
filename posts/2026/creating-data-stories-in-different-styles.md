---
title: Creating data stories in different styles
date: 2026-01-09T17:20:00+08:00
categories:
  - experiments
  - llms
  - visualisation
classes: wrap-code
description: I used Claude and GPT to generate data visualizations in distinct expert styles, like the Wall Street Journal and Shirley Wu. Prompting AI for multiple style transfers is a powerful shortcut for finding the best way to tell a data story.
tags: [data-visualization, llms, style-transfer, claude, prompt-engineering, data-storytelling]
---

**TL;DR**: Don't ask AI agents for _one_ output. Ask for a **dozen**, each in the _style_ of an **expert**. Share what works best.

---

AI agents build apps, analyze data, and visualize it _surprisingly_ well, these days.

We used to tell LLMs _exactly_ what to do. If you're an expert, this is still useful. An expert analyst can do better analyses than an AI agent. An expert designer or data visualizer can tell an AI agent _exactly_ how to design it.

But you're not an expert in _everything_.

Instead, "style transfer" experts.

LLMs are trained on the styles of experts across the world. Tell them to adopt an expert's style. That's a shortcut to improve output quality. It won't be as good as that expert, but likely better than you.

---

For example, [Linux Foundation leaderboards](https://insights.linuxfoundation.org/leaderboards) evaluates open source projects - are they active, who's behind it, do they follow security best practices, what's their popularity, etc.

[Varun](https://github.com/PythonicVarun) use [GitHub Copilot](https://github.com/copilot) with [GPT-5 mini](https://platform.openai.com/docs/models/gpt-5-mini) to [scrape](https://github.com/PythonicVarun/LinuxFoundation-Leaderboards-Analysis/blob/master/scraper.py) the [data](https://github.com/PythonicVarun/LinuxFoundation-Leaderboards-Analysis/tree/master/datasets) Then, he had [Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5) create data visualizations in **[five different styles](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/)**:

1. A **[Wall Street Journal](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/wall-street-journal-style)** style. [Prompt](https://github.com/PythonicVarun/LinuxFoundation-Leaderboards-Analysis/blob/master/datastory/PROMPTS.md#1-wall-street-journal-style)
2. **[Malcolm Gladwell + NYT](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/malcolm-gladwell-style)** style, i.e. written in Malcolm Gladwell's voice (who writes for the New Yorker), but with the New York Times' visual style. This ability to remix is powerful. [Prompt](https://github.com/PythonicVarun/LinuxFoundation-Leaderboards-Analysis/blob/master/datastory/PROMPTS.md#2-malcolm-gladwell-style-nyt-graphics)
3. The **[Polygraph / The Pudding](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/polygraph-style)** style. We aren't specifying a single publication here, but providing multiple publications, allowing it to mix and match from those. [Prompt](https://github.com/PythonicVarun/LinuxFoundation-Leaderboards-Analysis/blob/master/datastory/PROMPTS.md#3-polygraph--the-pudding-style)
4. From **[Shirley Wu](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/shirley-wu-style)**, who is a data artist, allowing us to go to the style of a specific individual. [Prompt](https://github.com/PythonicVarun/LinuxFoundation-Leaderboards-Analysis/blob/master/datastory/PROMPTS.md#4-shirley-wu-style)
5. An "**[open source data adventure](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/animated-style)**". That's not a publication or a person, but a theme. [Prompt](https://github.com/PythonicVarun/LinuxFoundation-Leaderboards-Analysis/blob/master/datastory/PROMPTS.md#5-animated-style-professional-adventure)

[Same input. Five different styles](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/).

For example, while [The New York Times](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/malcolm-gladwell-style/) comes up with transitional scatter plots (which are _great_ for rich interactive explorations):

[![](https://files.s-anand.net/images/2026-01-09-data-story-styles-nyt.webp)](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/malcolm-gladwell-style/)

... [Shirley Wu](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/shirley-wu-style) comes up with these hidden gems, focusing on the _smaller_ projects that have a remarkably diverse contributor base.

[![](https://files.s-anand.net/images/2026-01-09-data-story-styles-shirley-wu.webp)](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/shirley-wu-style)

Or, while [The Wall Street Journal](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/wall-street-journal-style/) opens with the state of the economy:

> The open-source software that underpins trillions of dollars in global commerce is showing signs of strain.

... [Malcolm Gladwell](https://pythonicvarun.github.io/LinuxFoundation-Leaderboards-Analysis/malcolm-gladwell-style) opens with perspective:

> In the spring of 2023, a small project called CBT Tape caught my attention. Three contributors. That's it. Yet they had pushed 3,414 commits in twelve months—a rate of **1,138 commits per person**. To put that in perspective: a "normal" project sees perhaps 20-30 commits per contributor annually.

---

At least for the next few years, the ROI is less from expertise. It's more from _style_.

Try out different styles. Learn to guide AI towards your preferences. Pick what works best.

And share!
