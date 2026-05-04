---
title: Transcribe talk
date: "2025-09-10T07:05:28Z"
lastmod: "2025-12-14T12:55:14Z"
classes: wrap-code
model: https://aistudio.google.com/prompts/new_chat
description: I developed this prompt to transcribe talk recordings and Q&A sessions accurately. It removes verbal fillers, adds timestamps, translates non-English segments, and bolds key takeaways. For video, it includes instructions to describe screen activity changes.
keywords: [transcription, llm prompts, video transcription, timestamps, speech-to-text, qa sessions, markdown]
---

Transcribe talk recordings with Q&A.

```markdown
Transcribe this talk.
DO NOT MISS ANY PART OF THE TALK.
Drop verbal tics and fillers (um, uh, etc).
Correct spelling and grammar but otherwise don't modify the original words.
Add English translations to any non-English parts.
Mark inaudible or unclear segments as "[inaudible]". Mark uncertain words with like "[word?]" or ambiguous possibilities like "[word1? word2?]".
Break it into LOGICAL paragraphs beginning with timestamps, e.g. "[00:13] When did ..."
For audience questions, prefix with "**Question**: ..." and answers with "**Answer**: ..."
**Make key points / takeaways / memorable statements bold**.

<!-- #TODO List details of talk or share slides, for context -->
```

If video is provided, add this line:

```markdown
When the screen changes, describe screen activity in [brackets], e.g. "[Opens https://...]", "[Sliding the timeline to Aug 2025 shows ...]", "[Tooltip shows ...]", ...
```
