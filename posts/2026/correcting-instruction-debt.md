---
title: Correcting instruction debt
date: 2026-05-25T16:30:02+08:00
categories:
  - llms
  - how-i-do-things
description: A small calendar bug ("avoid holidays") created hidden work and led me to use ChatGPT — grounded in my own agent logs — to find the pattern, cross-check it, and convert the fix into three lines of AGENTS.md instead of three new habits.
tags: [agents-md, coding-agents]
---

Here's another AI-generated post, with _**Anand**_ editor notes. But I've also added my own version of the post below.

<!--
RESEARCH: https://chatgpt.com/c/6a13dc2a-4d28-83ec-ae9b-016cd00b13a9
BLOG: https://claude.ai/chat/17173628-db14-42a4-b9c4-1aff78d5edf3
-->

<section ai-disclosure="ai-generated" data-ai-model="claude-sonnet-4.6" data-ai-provider="Anthropic">

I told my "[find a free calendar slot](https://github.com/sanand0/scripts/blob/48a095e0a956841a8e395345d31f79b1ae99d4a6/freeslots.py)" script to "[Avoid weekends and holidays](https://github.com/sanand0/scripts/commit/a8f5fb9eb5640b828618a33f2c89252e67664487#r186420170)". Wednesday vanished. Turns out it's a Singapore holiday (_**Anand**: It's [Eid al-Adha](https://en.wikipedia.org/wiki/Eid_al-Adha)_), — irrelevant for the people I was meeting in other zones. **I'd debugged my own helpful rule.** (_**Anand**: What? What does "debugged my own helpful rule" even mean?_)

Annoying. But revealing. I went to ChatGPT — not to fix the script, but to think: (_**Anand**: True. I had no clue what to do._)

> Could you maybe interview me to figure out what direction I might want to take this train of thought in...? Just ask me two or three questions.

(The whole point was to _not_ take on more work myself.)

Two questions in, it named it: **instruction debt.** (_**Anand**: which is such a cool term that I'll keep it._)

> Not "bad instructions," because the original instruction was reasonable. The debt is created when a rule that once reduced cognitive load later creates invisible work, missed options, brittle behavior, or debugging cost.

That hit. The script obeyed too literally. I got no warning. Worst of all, I'd scored a self-goal — given my future self an instruction that would bother me, while believing I was being helpful.

---

I asked it to research further — and to mine my own agent logs as evidence. ([Local MCP](https://www.s-anand.net/blog/how-i-use-local-mcp/) runs bash; ChatGPT can read `~/.codex`, `~/.claude`, `~/.copilot` and run `~/code/scripts/agentlog.py` directly.) It came back with a taxonomy. I asked it to stress-test against more correction turns and **discard what didn't survive**. (_**Anand**: Basically, I said, analyze my logs._)

It did. The robust categories, each grounded in an actual correction I'd made:

- **Objective framing** — "don't base teachability on scores… base it on the pattern of errors." Wrong proxy. (_**Anand**: Oh, yeah, I was trying to find patterns of errors in student submissions._)
- **Evidence/modeling** — Ticketmaster classifier overfit on `venue_name`. Predictive, not causal. (_**Anand**: True. Stupid model said, "tickets in this stadium sell more" as if it were actionable._)
- **Constraint semantics** — the Singapore holiday. Hard filter where a warning would do.
- **State/action** — Darwinbox: "Click Clockin" clocked me _out_. No pre/post-state check. (_**Anand**: The button said "Clock in OR out". I was clocked in. It clicked, thinking that'll clock me in, without seeing that the button was already pressed._)
- **Representation/path** — blog migration: "ALL LINKS relative" broke nested URLs. (_**Anand**: Yeah, relative links in my blog have been problematic for 20 years._)
- **Validation** — OCBC PDF: row balances passed, totals failed by SGD 6.9M. (_**Anand**: I'm nowhere near this rich. Codex just messed up _badly_.)

ChatGPT's own self-critique was the best part:

> "Lack of carefulness" should not be a category. It is not actionable. (_**Anand**: No idea what this means!)

---

Then the pivot. It proposed a **60-line "Operating Contract"** for my `AGENTS.md`. I pushed back:

> The operating contract is WAY too long. I was thinking 1 line, not 60... fast and frugal heuristics that cover the majority of the scenarios, rather than hard-coding everything, is what we're suggesting coding agents do in the first place.

It came back with three lines. [I pasted them in verbatim](https://github.com/sanand0/scripts/commit/7be44855ac6063a364163181585b8eb5721fc469#r186421964):

```
For non-trivial tasks, define the user-visible invariant: "done means ___"; verify that invariant before claiming success.
Treat constraints as soft preferences unless safety, privacy, data loss, credentials, or the current request makes them hard; surface any constraint that filters, skips, blocks, or deletes.
Prefer simple, rerunnable changes: inspect real inputs/state first, use existing tools/libs, log counts/examples, and call out uncertainty.
```

Line 1 catches OCBC and clock-in. Line 2 catches the Singapore holiday. Line 3 catches the toil.

**Don't add the rule to your head. Add it to the file the agent already reads.** (_**Anand**: Oh, so totally true!_)

</section>

---

Actually, the first half of the above AI-generated post didn't really resonate with me. So let me explain in my own words what I did.

- I found that, for some reason, this Wednesday never appears when I ask for [find a free calendar slot](https://github.com/sanand0/scripts/blob/48a095e0a956841a8e395345d31f79b1ae99d4a6/freeslots.py).
- I asked Codex, "Why on earth is this happening?" It said, [because you told me to exclude holidays](https://github.com/sanand0/scripts/commit/a8f5fb9eb5640b828618a33f2c89252e67664487#r186420170).
- That got me thinking, where am I giving instructions that shoot me in the foot? And ChatGPT did a long, detailed analysis of my coding agent logs and came up with a bunch of examples and categorization.
- I didn't bother reading it. I told it in [Henry Kissinger style](https://www.google.com/search?q=henry+kissinger+is+that+the+best+you+can+do): can you do better?
- I didn't bother reading it again. I told it, "Just tell me what to put into AGENTS.md". I don't want to do the work every time. **YOU** do the work. Automate it!
- It gave me 60 lines. I said, "What rubbish! I can't review 60. Just 3, max."
- [I copied that into AGENTS.md](https://github.com/sanand0/scripts/commit/7be44855ac6063a364163181585b8eb5721fc469#r186421964).

> 1. For non-trivial tasks, define the user-visible invariant: "done means ___"; verify that invariant before claiming success.
> 2. Treat constraints as soft preferences unless safety, privacy, data loss, credentials, or the current request makes them hard; surface any constraint that filters, skips, blocks, or deletes.
> 3. Prefer simple, rerunnable changes: inspect real inputs/state first, use existing tools/libs, log counts/examples, and call out uncertainty.

The first makes _total_ sense. Define "done".\
The second makes _some_ sense - that's exactly what I did wrong with the calendar.\
The third is supposed to "handle my recurring style" - and _kind of_ makes sense, so I'll let it be.

![](https://files.s-anand.net/images/2026-05-25-correcting-instruction-debt.avif)
