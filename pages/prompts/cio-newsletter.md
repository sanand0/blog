---
title: CIO Newsletter
date: 2026-07-27T17:58:28+08:00
classes: wrap-code
description: Prompt to identify topics to write about in my CIO newsletter.
tags: [prompt-engineering, generative-ai, enterprise-ai, data-science, decision-making, chatgpt, system-prompt]
---

```markdown
Find the best ideas for my next occasional email to CIOs and senior technology/data leaders.

First read and apply these skills on @LocalMCP: expert-lens, ideation-protocol, blind-spot, anand-objectives, decision-compression, evidence-provenance.

## 1. Calibrate the newsletter

Using personal Gmail via `gws`, find sent emails from `root.node@gmail.com` containing:

`you might have hinted you'd like such emails from me`

Read the newsletter emails, not merely the matching snippets. Infer:

- the audience;
- the recurring structure and tone;
- what counts as sufficiently important;
- topics already covered, so they are not repeated.

These are not AI-news roundups. The strongest emails usually begin with something I personally did, observed, measured, decided, or got wrong; provide inspectable evidence; derive one surprising enterprise implication; and give readers something concrete to try or reconsider.

## 2. Search my corpus

Search primarily after the latest matching newsletter, while allowing older material that was overlooked.

Use a staged search:

1. Scan indexes and recently modified files to identify at most 30 candidate sources.
2. Deep-read at most the 12 richest sources.
3. Re-open the best evidence to verify exact wording, numbers, dates, and provenance.

Prioritize:

- recent meeting transcripts and notes under `~/Dropbox/notes/` and ``~/Dropbox/notes/transcripts/`;
- `~/code/talks/README.md` and linked talks;
- `~/code/blog/description.md` and targeted posts;
- `~/code/til/README.md`;
- `~/code/llmdemos/config.json`;
- `~/code/llmevals/README.md`;
- email or chat only when it supplies a firsthand incident, reaction, decision, result, or failure.

Do not let public AI news become the core idea. Public sources may corroborate my evidence, but cannot substitute for it.

## 3. Gate every candidate

Keep an idea only when most of these hold:

- **Firsthand:** I did, observed, measured, decided, or materially shaped it.
- **Surprising:** it challenges a reasonable CIO assumption.
- **Consequential:** it could change an enterprise decision within the next 6–12 months.
- **Evidenced:** there is a concrete incident, number, artifact, failure, or audience reaction.
- **Exclusive:** a well-read CIO is unlikely to learn most of it from ordinary AI media.
- **Emailable:** it supports one focused story: incident → implication → practical move.
- **Shareable:** it is public, can be safely anonymized, or is clearly marked as requiring approval.

Reject generic trends, secondhand frameworks, routine project updates, unsupported opinions, thin rewrites of earlier newsletters, and impressive claims whose provenance cannot be recovered.

Explore broadly before ranking. Include 2–3 `IDEA`s: rich sources that may not yet support a finished thesis but are likely to provoke a better idea.

## 4. Output

Return 8–12 ideas, prioritized.

For each:

1. **Working title and one-sentence thesis**
2. **Opening incident or evidence**
3. **Why a CIO should care**
4. **Why this is uniquely me**
5. **Sources:** exact path, date, and useful line range or section; mention any public artifact available in the source
6. **Shareability:** PUBLIC / ANONYMIZE / APPROVAL NEEDED
7. **Missing evidence or weakness**
8. **Verdict:** WRITE NEXT / STRONG / IDEA / SKIP

Then provide:

- the top three in order, explaining why each narrowly beats the next;
- one attractive but generic idea rejected;
- one strong idea rejected because it is not sufficiently me;
- any important corpus area that could not be inspected.

Do not draft the newsletter. Be concise, skeptical, and specific. Never invent a result or imply external approval.
```

- 27 Jul 2026: Created. [ChatGPT](https://chatgpt.com/c/6a6725d0-00a8-83ec-be3b-573764e9e2c6)
