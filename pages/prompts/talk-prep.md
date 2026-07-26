---
title: Talk Prep
date: 2026-07-24T16:00:00+08:00
classes: wrap-code
description: "Prepare an announced talk/workshop once the forum, audience, topic, and description are known. Use for audience research, session and exercise design, demos, page copy, announcement posts, pre-session engagement, scripts, and cheat sheets."
tags: [talk, workshop, learning, communication, research]
---

```markdown
Give me ideas to prepare for this talk / workshop:

Serve three beneficiaries, in order (flagging conflicts):

- the audience (genuinely useful),
- me (read past conversations and relevant skills, build compounding assets), and
- the host (carry their message forward).

Treat the session as a room-sized activity and experiment, not a classroom.
Make the room discover something worth remembering and leave evidence behind.

## Research audience and my work

Research the audience beyond generic personas fail and demographics using:

- Organizer and planning call transcripts, emails, chats, etc. Rank by who knows the audience best and weight accordingly.
- The audience's live work: portfolio, projects (and their weight), workflows, current assumptions.
  Find and research a few real attendees' actual work: input mode, real anxieties, actual skill gaps.
  Use online sources and @LocalMCP as required.
- Peer sessions at the venue: match their norms, then position AGAINST the rest of the program. Cover what no other speaker there will.
- The named people - host, moderator, co-panelists. Research them; draft questions to feed the moderator.
- How I actually run sessions: `~/Dropbox/notes/talks.md`, `~/code/talks/**/transcript*.md`.

Research my work that will be relevant to the audience:

- Read @LocalMCP for my blog, TIL, talks, workshops, transcripts, notes, email/chat, code, ...
- Run a broad pass to discover themes I've explored over the last year or so. Filter for relevance. Then deep-dive into the most relevant ones.
- Ideate/brainstorm on what to cover. Drop weak ones, follow any new ideas that emerge, and share options.

## Suggest content ideas

- What are assumptions this room holds that I, uniquely, can make them question in front of their eyes?
  What experience or evidence could change it? What they should do differently after?
- What in my work (blog, ~/code, past talks, experiments) will enable this? Remember: if an agent can do it, it's not a differentiator.
  Filter by utility (useful frequently) x novelty (can't learn it elsewhere) x engagement.

## Suggest delivery ideas

How I might deliver the content? Here are some ideas, but don't limit yourself to these:

- What can they commit BEFORE a reveal: predict, rank, choose, attempt, set a prior, ...
  Then test live, compare, ask what changed their mind and what evidence still would.
  I can create/update/analyze surveys DURING the session, dynamically, using `~/code/liveform/`.
  You can generate a `form.yaml` where relevant.
- Pre-register my prediction too. Instrument before/after (survey, dot stickers, liveform).
  Design so either outcome - including a null result or a broken demo - is a finding worth publishing.
  Transparent, un-rigged experiments only.
- Use the audience's own material as substrate: their problems, data, exams, themselves.
  Or synthetic data so realistic "they'd be convinced it's literally their data."
  The surprise stat about THEIR institution beats a generic one.
- Fit the format:
  talk - predict or judge a live case;
  workshop - do, share, critique, then apply to a NEW case;
  dialogue/panel - decide in groups, then attack another group's decision.
  Don't over-prepare a dialogue into a presentation.

## Assetize

How I can build compounding assets for myself and the audience? For example?

- What's a live coding/analysis/... activity I could perform that will build something truly useful for them AND me AND others?
- What modular demos/cases/datasets/activities could I give them?
  Why - what's their purpose, surprise, learning? What's the friction, fallback, and priority?
  How do we let them pick, or signal interest and need?
- How can we make it EASY for THIS cohort?
  E.g. voice-first for non-typists, paste-a-link activities, pre-built pages, no blank canvas, ...
  But let people look and think before sending them to a device.
- What's the backup if the network dies?
- What's the last thing they should feel or do?
- What's the pre-engagement - e.g. WhatsApp? What's low effort (paste a link, type a few words), high wow, personally useful?
  What's the sequence over days? E.g. a priming message ("most people find at least one error").

How can the session build artifacts useful to participants and a compounding asset for me?
Suggest ideas for these.

Note: The talk summary will be saved in `~/code/talks/<date-slug>/`: recording + transcript, prompts.md, story, techniques, chats.
See the workshop-followup skill. Transfer test: recall LATER, apply ELSEWHERE, explain WHY, know when WRONG.

## Guidelines

- Give me options to pick from unless there is a clear winner. Don't pre-filter.
- Use simple language and tell me linearly, step-by-step, how to run the session.
  Explain what to prepare inline, with context.
  Avoid cross-references that make me jump around.
- Do not share the timing break-up. Do not share actual datasets/cases/code.
```

- 25 Jul 2026. Revised in my words. #TODO But still not good enough. See https://chatgpt.com/c/6a640f4a-d2f4-83ec-a78e-f4ff08df353c + https://chatgpt.com/c/6a64392b-d058-83ec-b718-032ec6aa1615
- 21 Jul 2026. Created. Sources:
  - https://claude.ai/chat/16349a22-f2dc-4f8a-b337-8c76963cbac7
  - https://chatgpt.com/c/6a5c87c3-d3d0-83ee-b3e3-639b7f66e83b



- Things #TODO from https://chatgpt.com/c/6a48d8ac-4450-83ec-9fd9-13e30456215f?mweb_fallback=1
  - Design the final test before designing the talk. After this section, given a case they have not seen, what should they be able to decide—and explain?
  - Measure transfer. End every important section with one unseen case: What would you do? Why? How confident are you? What could make you wrong?
  - Make exercises require a judgement, not merely an operation. Not "transcribe this" but "would you use dictation, transcription or uploaded audio? what's the privacy risk / failure mode?"
  - Create a liveform. Make predictions before with confidence %.
