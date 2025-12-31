---
title: "The Surprising Power of LLMs: Jack-of-All-Trades"
date: "2025-08-27T01:59:08Z"
lastmod: "2025-08-27T01:59:10Z"
categories:
  - llms
wp_id: 4180
---

![The Surprising Power of LLMs: Jack-of-All-Trades](/blog/assets/Generated-Image-August-27-2025-8_53AM.webp)

I asked ChatGPT to analyze our daily innovation-call transcripts.

I used command-line tools to fetch the transcripts and convert them into text:

```bash
# Copy the transcripts
rclone copy "gdrive:" . --drive-shared-with-me --include "Innovation*Transcript*.docx"
# Convert Word documents to Markdown
for f in *.docx; do
  pandoc "$f" -f docx -t gfm+tex_math_dollars --wrap=none -o "${f%.docx}.md"
done
# Compress into a single file
tar -cvzf transcripts.tgz *.md
```

… and uploaded it to ChatGPT with this prompt:

> Here are transcripts from the daily call I (Anand) have with the innovation team that I lead. It is a .tgz of text transcripts as .md files.
>
> Your task is to
>
> 1. Discover a variety of non-obvious and surprising personality insights about Anand as well as team members, supported by evidence.
> 2. Recommend ways of improving the way in which these meetings are conducted.
>
> The transcription quality is average. Words are incorrectly transcribed. Factor that in.\
> Generate multiple hypotheses based on management, science, and ancient literature.\
> List and leverage multiple mental models while hypothesizing.\
> Test the hypotheses against the data and explicitly document which are valid and which are not.\
> If a hypothesis cannot be tested or the method of testing is not robust, note it and move on.\
> Share based on the strongest evidence and most robust evidence you find.

Here are two highlights from the analysis:

> Here’s what I did: I unpacked your 78 Markdown transcripts (≈298k words, 13 speakers, 13,005 utterances) and computed per-speaker metrics (turns, words, long monologues, question types, hedging, pronouns, action-ish statements, etc.).
>
> Mental models used below (and cited where applicable): Collective intelligence (equal turn-taking), Motivational Interviewing/OARS (open questions), Implementation Intentions (“who-what-when/if-then” planning), Psychological Safety, Brevity (Thirukkural), Parkinson’s Law, Goodhart’s Law, OODA loop.

Learnings:

- I spoke 39% of the words. My share is falling, but participation breadth is narrowing. Groups are smarter when talk is evenly distributed.
- I ask 6 questions per 1,000 words; 39% are open-ended. Teammates ask a higher share of open questions. Open questions are rising and support better joint problem-solving.
- The team hedges often (“I think,” “probably”). I hedge less—19 per 1,000 words. Hedging helps ideation, but slows decisions.
- Action statements are frequent (8 per 1,000 words), but only 1% include a date. High momentum; weak closure.
- Positive reinforcement shows up in 4% of my turns (“thanks,” “great,” “well done”).
- Meetings are getting wordier (+50 words a week). More depth, but more fatigue and decision drag.

The bigger lesson is about LLMs. A single analyst rarely mixes management, linguistics, and statistics at once. LLMs aren’t deep specialists, but they’re unusually capable **generalists**.

They handle **ambiguity** well. I should use them when I don’t yet know what to ask.\
They’re strong at **synthesis**. I should ask them to combine fields we rarely connect.

[LinkedIn](https://www.linkedin.com/posts/sanand0_i-asked-chatgpt-to-analyze-our-daily-innovation-call-activity-7366290000109322240-M8ns)
