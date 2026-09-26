---
title: Editorial Slop
date: 2026-09-26T08:56:17+08:00
categories:
  - interesting-experiences
description: 'I compare my submitted article with the published version, finding broken sentences, fake hyperlinks, poor HTML headings, and a pompous summary: editorial changes that caused more damage than good.'
tags: [content-strategy, digital-media, journalism]
---

My article [Redesigning the Operating Model: Shifting from AI Tool Rollouts to Workflow Integration](https://cxotoday.com/corner-office/redesigning-the-operating-model-shifting-from-ai-tool-rollouts-to-workflow-integration/) appeared on CXOToday two days ago. Here's how it happened.

**29 May 2026**: [Palash](https://www.linkedin.com/in/palashbhattacharjee/) mailed me that we have an "Email interaction opportunity with [Digital Terminal](https://digitalterminal.in/)" and they shared six questions:

1. What are the key reasons behind this “last-mile problem” in scaling AI to production?
2. While much of the focus is on models and tools, how critical are content readiness and data quality in determining whether AI delivers real business value?
3. (... and so on.)

_He'd already drafted the responses_ and "sharing below the link for your feedback and approval."

A few hours later I replied, saying I'd rather write my own article. [Here it is](https://docs.google.com/document/d/1PAJz-fc69tz3LoJCmTNMyluJnzCayWmmFttcZu-KcbA/edit) ([Markdown](https://github.com/sanand0/blog/blob/main/pages/notes/2026-05-29-digital-terminal-interview.md)):

> You're welcome to share mine with my name.
> Or you can share the earlier version with anyone else's name - **not mine**.
> Either option works for me.

Palash preferred my version and shared it.

---

**24 Sep 2026**: 12 weeks later, the [article appears](https://cxotoday.com/corner-office/redesigning-the-operating-model-shifting-from-ai-tool-rollouts-to-workflow-integration/), and with a few differences - 🟢 good and 🔴 bad. They:

1. 🟢 Added a title
2. 🟢 Changed `--` and `-` to em-dashes: `—`; also the double quotes `"` to smart quotes `“` and `”`; single quotes `'` to apostrophes `’` (which is interesting because I told my agent to remove those to avoid it sounding agent-y).
3. 🔴 But failed to fix my punctuation. For example, a missing full-stop in `... fundamentally redesigned workflows In a separate workplace report...`
4. 🔴 Also added paragraph breaks mid-sentence. This happened thrice. For example, here's one broken sentence:

   ```
   High risk

   actions need approval.
   ```

5. 🟢 Removed a duplicate question and my `Anand:` quote prefixes.
6. 🟡 But prefixed a two paragraph summary that's more pompous and jargon-y than me.
7. 🔴 Removed every hyperlink and changed it into underlined text that _looks_ hyperlinked but isn't. My links were to McKinsey, NIST, and arXiv. None are clickable.
   - The underlining is sometimes unbalanced. In `(McKinsey & Company)`, the opening paranthesis isn't underlined, but the closing is.
   - The links are sometimes split into multiple underlined segments. `A Survey of` and `Data Agents` are two separated underlined blocks - though it used to be one link.
8. 🔴 Added poor / unsemantic HTML markup. All six interview questions are encoded as `<h6>` headings directly under the article, not H2/H3. There is also a stray final `<p>&nbsp;</p>` after the article.

On the margin, this may be more damage than good. "Editorial slop", I guess.

![](https://files.s-anand.net/images/2026-09-26-editorial-slop.avif)

PS: I make more mistakes than any editor and hate being called out. But I don't mind. I'm a _happy_ hypocrite.

PPS: I'm not moralizing "Humans generate slop too, so don't blame AI", etc. I'm more mature for that. I'm just saying, "Hee hee, you made a boo-boo 🙂".
