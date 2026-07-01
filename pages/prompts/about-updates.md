---
title: About Updates
date: 2026-06-30T19:27:24+08:00
classes: wrap-code
description: Update people summary pages based on transcripts every week
keywords: [mcp, personal-crm, transcripts, system-prompt, markdown]
---

<!--
  Prompt: https://chatgpt.com/c/6a433c6b-f598-83ec-b83f-97368077fd0b
  Test run: https://chatgpt.com/c/6a437148-3824-83ec-92a7-3e89c920143a
-->

````markdown
For the week ending Saturday ------ midnight (SGT), share updates to `~/Dropbox/notes/about/*.md` reading from @LocalMCP (without modifying files):

- `~/Dropbox/notes/transcripts/**/*.md`
- `~/Documents/data/s.anand@straive.com/{mail,calendar,chat}.jsonl`
- `~/Documents/data/root.node@gmail.com/{mail,calendar}.jsonl`
- `~/Documents/data/whatsapp/*.jsonl`

Inspect `~/Dropbox/notes/about/` files. Try to match each person to an existing file based on name, affiliation, and context.

If no matching file exists: create only if there are 3+ meaningful interactions across days/channels, or 1 exceptionally important interaction likely to guide future dealings, or a there's repeated meaningful interaction outside the week.
Name the file based on the Person Name and Affiliation (where guessable, else skip). For example: Khushi Kapoor BPB.

Add one `## YYYY-MM-DD - short topic` section for the week, newest near the top after stable profile notes, picking latest date in case of multiple conversations.
Include: substantial interactions that change how I should understand, work with, follow up with, or remember the person. Strong signals are: decisions, advice, critique, preferences, commitments, asks, opportunities, investments/startups, intros, conflict, personal context relevant to future interaction, repeated collaboration, or a person's distinctive operating style.
Exclude: logistics, "running late", calendar coordination, meeting/schedule changes, tactical travel/logistics, receipts/alerts/GitHub notifications, broadcasts, tiny group comments, generic FYIs, one-off detailed emails from students/strangers unless they become repeated interaction, and facts already captured unless the new item changes them.

For group transcripts, update a person only if they made a meaningful contribution, owned a decision/action, revealed a useful preference, or materially changed the direction. Do not credit everyone in the meeting.

For each proposed note, write concise 1-line bullets.
Each bullet should be useful later to Anand or an AI agent advising Anand.
Use the right number of bullets as the relationship signal warrants, not a fixed count. 5-8 is fine when there's very rich information.
Use more when the conversation materially changes how I should understand, work with, or follow up with the person.

Approach:

- Use a retrieval ladder: candidate table first from transcript frontmatter/filenames, existing `about/*.md`, and `transcripts/description.md`; deep-read only candidates that pass triage or are borderline.
- Do not use raw mention counts to create files. Prior transcript index/title hits and meaningful cross-channel evidence matter more than full-body `rg` hits.
- Use null-delimited file handling (`fd -0`, `xargs -0`, etc.) for all file loops because paths contain spaces.

Capture:

- what happened / what they asked / what was decided;
- what this says about the person's priorities, constraints, or working style; phrase it tentatively unless it's repeated or strongly signaled;
- open loops and follow-ups;
- reusable future guidance: "When working with X, do Y."

Avoid transcript summaries that belong in project notes. Person notes are for relationship memory and future interaction guidance.

Output format:

```markdown
# Person Name Affiliation

## YYYY-MM-DD - Topic

- ... (include compact source path(s) as evidence, e.g. `~/Dropbox/notes/transcripts/....md`)
- ...

# Person Name Affiliation

## ...

# Review

- Person Name: reason they may / may not be worth noting but need my judgment - mentioning other-period evidence if relevant.

# Skipped

- ... (compact list of high-volume false positives and why: logistics, notifications, minor group comments, etc.)

# Checklist

- [ ] Did not modify files.
- [ ] Checked whether a matching person file already exists, including aliases/spelling variants.
- [ ] `# H1` matches existing (or to-be) `~/Dropbox/notes/about/H1.md`
- [ ] Did not create files for one-off weak interactions.
- [ ] Did not summarize projects into every attendee's person note.
- [ ] Kept bullets concise and future-useful.
- [ ] Included source paths for every suggested edit.
```
````
