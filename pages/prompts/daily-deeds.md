---
title: Daily Deeds
date: 2026-07-27T19:44:00+08:00
description: Find out what I really accomplished last week.
classes: wrap-code
tags: [system-prompt, prompt-engineering, productivity, personal-data, ai-agents, personal-blog, ai-automation]
---

<!-- 26 Jul 2026: Source prompt - https://chatgpt.com/c/6a66b84b-41c4-83ec-b539-e65a08e910a5. The Claude Prompt was weak: https://claude.ai/chat/8dab40e3-9f59-4a86-a15c-b81544bef7f1 -->

```markdown
Help me answer: **"What did I REALLY accomplish?"** in the last 7 days until Saturday midnight (SGT).

The aim isn't to produce a time log, activity report, exhaustive chronology, or list of completed tasks.
It is to find out what really changed because of this week: in the world, in my trajectory, in other people, or in my sense of myself.

Use @LocalMCP bash/read. Do not run Claude, Codex, Gemini, or other AI agents.
I will update ~/Dropbox/notes/daily-deeds.md based on your output.

## What counts

Look for state changes such as:

- Something shipped, finished, adopted, decided, resolved, or stopped
- Significant movement against one of my stated goals
- A reusable asset, system, method, relationship, reputation, or capability that may compound
- A conversation or introduction that opened an important new opportunity
- A reaction - from me or someone else - that revealed impact or signficance
- A changed belief, newly discovered principle, or invalidated assumption
- A wrong direction killed, loss prevented, burden removed, or lingering loop closed
- A personally significant first, act of courage, relationship moment, delight, surprise, or state of flow
- Something small that future me may see as the beginning of something large

Do not rank by time spent, apparent effort, number of meetings, seniority of people involved, prestige, or monetary value alone.

One emotionally specific sentence in `daily-deeds.md` may matter more than twenty transcripts. Treat exact quotes, `:star:`, "wow," firsts, unusual behaviour, repeated later references, spontaneous delight, embarrassment, courage, and flow as strong (but not conclusive) personal importance signals.

Do not invent undocumented events. Instead, generate specific memory prompts that may help me recall them.

## Sources and search procedure

Search efficiently in two passes.

### Pass 1: Discover candidates

Start with:

- `~/Dropbox/notes/daily-deeds.md` -  see what I record/skip/miss and how I write.
- The current goals and status in `~/Dropbox/notes/goals-bucket-list.md` and `~/Dropbox/notes/@todo.md` and `~/code/blog/pages/skills/anand-objectives/SKILL.md`
- Transcript filenames within the date window under `~/Dropbox/notes/transcripts/`
- Emails via `gws` - both work (s.anand@straive.com) and personal (root.node@gmail.com)
- WhatsApp messages via `~/Documents/data/whatsapp`
- Dated completed and open entries in `~/Dropbox/notes/@todo.md`
- Overlapping `~/Dropbox/notes/about/week-*.md` files, using them as leads rather than trusting their ranking
- `~/code/talks/README.md`
- `~/code/datastories/config.json`
- `~/code/til/README.md`
- `~/code/blog/description.md`
- `~/code/README.md`
- `~/code/llmdemos/config.json`

Check file shapes and indexes before opening large files. Locate candidate files first, then read only relevant passages.

Use calendar, email, chat, WhatsApp, browsing history, and repository history only through targeted date/name/topic searches to verify candidates or detect state changes. Do not dump or broadly scan archives. Browsing time and meeting duration are not accomplishments.

Create a private raw list of roughly 20-40 possibilities before ranking.

### Pass 2: Verify and rank

For the strongest possibilities, find direct `path:line` evidence where available.

Judge each candidate separately on:

- **State change:** What is now different?
- **Goal movement:** Did it significantly advance an explicit or durable objective?
- **Leverage:** Can it compound through an asset, person, system, method, or reputation?
- **External evidence:** Did anyone adopt, approve, respond, quote, pay, publish, merge, invite, or change behaviour?
- **Personal importance:** Are there signs that I may remember or value it unusually strongly?
- **Durability:** Is it likely to matter three months from now?
- **Counterfactual:** Would omitting change the week's story?

Keep importance and evidence confidence separate. Small personal moments may be very important but low-confidence. Detailed meeting notes may be high-confidence but less important.

There'll be plenty of work-related content. Balance by probing deeper for personal life signals (family, relationships, health, body, play, service, art, courage, joy, and unusual experiences).

Include meaningful failures and closures - don't make the week look artificially successful.

## Output

Keep the entire response reviewable in about two minutes.

# What I may have REALLY accomplished

## Best current answer

Write three concise bullets representing your best current interpretation of the week. Phrase them as changes, not activities.

Prefer constructions such as:

- "I proved that..."
- "I moved ... from ... to ..."
- "I created ... that can now..."
- "I opened..."
- "I stopped..."
- "I discovered..."
- "I experienced..."

Do not simply say "I attended," "I worked on," "I discussed," or "I spent time."

## Candidate slate

List up to 10 candidates, most significant first. For each:

**1. Short candidate title** - Category: Outcome / Goal / Leverage / Seed / Learning / Closure / Moment

- **What changed:** One sentence.
- **Why it might matter:** One sentence explaining the possible long-term, goal, leverage, or personal significance.
- **Evidence:** Concise `path:line` references.
- **Your guess:** Importance: High / Medium / Wildcard. Evidence confidence: High / Medium / Low.

Use **Wildcard** for something that might be deeply significant but whose importance cannot be inferred reliably.

Do not fill all slots merely because they are available.

## What the record may have missed

Ask at most three highly specific memory questions derived from the week's actual events.

Good questions resemble:

- "After the [specific event], was there one audience remark or private conversation you kept replaying?"
- "During the trip to [place], did anything off-stage matter more than the scheduled event?"
- "You had [specific demanding sequence]. Was there a moment of fear, courage, delight, embarrassment, connection, or flow that the records would not show?"

Include:

1. One event-specific backstage or reaction prompt
2. One personal, relationship, body, play, or joy prompt
3. One quiet decision, failure, refusal, closure, or changed-belief prompt

Do not ask generic questions such as "Anything else important?"

## Goal movement

Mention only explicit goals that appear to have moved. Distinguish:

- **Outcome movement:** the goal itself advanced
- **Leading evidence:** behaviour or capability improved, but the goal did not necessarily advance
- **No reliable evidence**

Do not turn routine habit compliance into a headline unless something changed.

## Suggested `daily-deeds.md` additions

Provide copy-ready lines for items that are important and absent or weakly recorded.

Use this structure:

`- Day YYYY-MM-DD. [What changed]. [Exact reaction, why it mattered, or what it may enable].`

Preserve memorable exact words.

## Likely motion, not accomplishment

Optionally list at most two items that consumed visible activity but did not appear to change anything important. Explain briefly why you excluded them.

End with:

`Reply with Keep: ... / Drop: ... / Missing: ... and I will turn this into the final weekly answer.`
```
