---
title: Agents answer small questions from big data
date: 2026-06-18T20:12:04+08:00
categories:
  - llms
  - data
build: { list: never, render: always }
robotsNoIndex: true
description: I use AI agents to reconcile messy customer data in minutes, slashing timelines from weeks to seconds. When analysis becomes this cheap, you can skip massive projects and solve specific data quality issues by asking small, one-off questions.
tags: [ai-agents]
---

**OK, so agents can analyze data crazily fast.**

At the [EQT India AI & Cyber Summit](https://sanand0.github.io/talks/2026-06-16-eqt-data-stack-for-agents/), I asked 15 CIOs how long a customer-master reconciliation would take across 3 messy sources with different IDs, columns, spellings, missing fields, no common key, etc. [See the dataset](https://files.s-anand.net/pages/customer-masters-data/).

"A week to a month" was the median response.

We finished it in 6 minutes and 32 seconds during the workshop with a $20 ChatGPT account and a 30-second not-very-clever prompt. It reconciled origination, collections and CRM records into one customer master, with confidence scores, explanations, flagging 80% or less confidence for human review, and generated the [reconciliation report](https://view.officeapps.live.com/op/embed.aspx?src=https://files.s-anand.net/pages/customer-masters-data/reconciliation.xlsx).

For example, it matched "Amit Kumar Gupta" and "Amit K Gupta" and "AK Gupta" using phone, PAN and email. But it flagged "Arjun R." vs "A.D. Rao" with the same phone number and unknown PAN/email for human review, citing 70% confidence. I'd have merged it, but the room agreed with ChatGPT.

When I asked them the same question at the end, Almost _everyone_ reduced their estimate. In one case, by a _factor of 10_.

---

**But maybe the big deal is that we can ask smaller questions.**

The speed benefit is obvious. But interestingly, when **questions become cheap**, more questions are possible.

A one-off question like "is _this particular_ customer present in all 3 systems?" was too small for a data project. A full project takes a data lake, a data quality programme, a governance committee, a budget, a roadmap, a quarter, ...

Now you can just ask. Agents are able to source, clean, organize, and analyze with a few thousand tokens.

Some answers _will_ be wrong. That's OK. Earlier, the first wrong answer cost weeks. Now it costs minutes and a few cents.

---

One CIO raised the obvious objection: "I can't upload the data. InfoSec."

Fair. So we tried a local version. The agent could see metadata (column names) but not the full data. It worked perfectly fine, too.

---

**They're able to clean and organize data on the fly.**

I polled the audience about what blocked agents from analyzing data.

The blockers people listed, interestingly, were broken data, data quality, unstructured data, siloed knowledge, access, SOPs, and security. **Nobody** said the agents were not good enough.

Looks like the **bottleneck's moved away from AI and into data.** And it seems AI agents can fix some of these.

Not everything. Not magically. But the time and cost is so low it's easy to try things out.

---

**Why not try it?**

Let's ask small questions, point the agent at data, make it cite evidence, review it, and log the failures.

We might as well show results before asking for a project.

Please try analyzing _any_ data - and do let me know if it fails!

---

You can [see the summary, transcript, audio, and data](https://sanand0.github.io/talks/2026-06-16-eqt-data-stack-for-agents/) from the session.

![](https://sanand0.github.io/talks/2026-06-16-eqt-data-stack-for-agents/summary.avif)
