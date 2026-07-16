---
title: Tacit is just un-instrumented
date: 2026-07-13T20:43:33+08:00
categories:
  - llms
description: Tacit knowledge is just un-instrumented data. Use a simple framework comparing the cost of trial against the speed of verification to identify which skills and roles in your organization are most vulnerable to AI automation.
tags: [automation, ai-automation, future-of-work, management, generative-ai]
---

At [The Curzon Hotel](https://maps.app.goo.gl/VKT8FiANmzsehMHJA), my key card didn't work. But every time I went to the reception, they'd send a bellboy who would use the _same_ key card, jiggle it a bit, pull it in and out a few times, and the door would open.

Every night. For five nights. I just couldn't get the knack of it.

I've been at the other end of this. People often reach out to me saying, "Anand, this software isn't working." Then I go do the _same_ thing they did, and it works. (Sometimes, I just need to watch them do it and it works.)

It's an intangible skill, I guess.

That gave me some food for thought. This is _exactly_ the kind of skill an AI cannot pick up, right? I mean, jiggling keys, physical world, tacit knowledge, precisely the kind of things that would be AI proof.

So I asked Claude Fable for its opinion. "Can AI pick up the key knack?"

"It already has." Claude said. Apparently, opening locks is one of the most studied problems in robotics.

The only reason opening the key feels hard to learn is because we didn't / couldn't put it in words. But a sensor on his hand would. **Tacit is just un-instrumented**. Once we measure it, it becomes training data.

As long as something is cheap to try and fast + clear to verify, it doesn't matter how "physical" it is - we can build a model around it.

|                        | Cheap to try | Expensive to try |
| ---------------------- | ------------ | ---------------- |
| Fast + clear to verify | Pottery      | Surgery          |
| Slow + vague to verify | Friendships  | Mergers          |

<section ai-disclosure="ai-generated" data-ai-model="claude-fable-5" data-ai-provider="Anthropic">

This applies to organizations firms in different ways.

| Organization             | **Automate** (cheap to try, clear to verify)                | **Cut the cost of trying** (expensive to try, clear to verify)                                      | **Cut the cost of verifying** (cheap to try, vague to verify)                            | **Keep human** (expensive to try, vague to verify)   |
| ------------------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **Insurance**            | Photo-based simple claims                                   | Fraud investigations (proven or not) → AI triage of which cases to open                             | Underwriting rule tweaks (losses mature in years) → early-warning loss indicators        | Risk appetite; reinsurance structure                 |
| **Asset mgmt**           | Rebalancing, index tracking (tracking error verifies daily) | Large trade execution (implementation shortfall is measured) → execution simulators                 | Stock picks (skill or luck? takes years) → forecast scoring, attribution                 | Private-market deals; manager selection              |
| **Waste mgmt**           | Route optimization; robotic sorting                         | Fleet electrification pilots (cost per route is clear) → route and energy simulation                | Recycling awareness campaigns → bin-level contamination sensors                          | Landfill siting; 30-year municipal contracts         |
| **Logistics**            | Routing, load planning, ETAs                                | Network redesign, e.g. a new hub (cost-to-serve verifies in months) → digital twin of the network   | Driver incentive tweaks (retention causality is murky) → cohort telemetry                | Building capacity ahead of demand                    |
| **Healthcare equipment** | Visual defect detection on the line                         | Clinical trials (clear endpoints, millions per try) → in-silico trials, device digital twins        | Hospital sales messaging (committee sales, vague attribution) → pipeline instrumentation | Ten-year platform bets (R&D + regulation + adoption) |
| **Card processor**       | Transaction fraud scoring (millions of labeled tries a day) | Core platform migration (latency and uptime verify instantly) → shadow and parallel runs            | Fee and pricing tweaks (merchant churn is slow, confounded) → churn cohorts              | Betting on new payment rails                         |
| **Scientific publisher** | Integrity checks, formatting, metadata                      | Replicating a paper's results (re-run the code and data; verdict is clear) → automated re-execution | Desk rejections (did we reject a breakthrough) → track the fate of rejects               | Open-access business model transition                |
| **Virtual school**       | Auto-grading; tutoring on known-answer problems             | Full course production (completion and scores verify fast at scale) → AI-drafted courses            | Engagement nudges (engagement isn't learning) → better assessment                        | Accreditation; university partnerships               |
| **Physical school**      | Timetabling, worksheets, admin                              | Campus expansion (enrolment verifies) → demand modeling                                             | Classroom pedagogy tweaks (education's replication crisis) → proper assessment           | School culture and head succession                   |

Or at a role level.

| Role            | **Automate** (cheap to try, clear to verify)            | **Cut the cost of trying** (expensive to try, clear to verify)                                         | **Cut the cost of verifying** (cheap to try, vague to verify)                           | **Keep human** (expensive to try, vague to verify) |
| --------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **CMO**         | Ad copy variants (CTR verifies in hours)                | National campaign launches → test with synthetic consumers, test markets                               | Brand and content posts ("half my advertising is wasted") → brand-lift measurement      | Repositioning the company                          |
| **CFO**         | Reconciliations, close, variance commentary             | Refinancing and hedging moves (P&L verifies) → backtests, scenario sims                                | Forecasts (cheap to issue, never scored) → track accuracy, Brier-style                  | M&A; capital allocation                            |
| **CHRO**        | Policy Q&A, payroll queries                             | Comp restructuring (offer acceptance, attrition verify in months) → model before rollout               | Training programs (nobody knows if they worked) → real skill assessments                | Succession; senior hires; culture                  |
| **CIO**         | Code with test suites                                   | System migrations and cutovers → staging, canary, parallel runs                                        | Developer productivity tooling (adopted cheaply, impact unclear) → DORA-style metrics   | Build-vs-buy platform bets                         |
| **CRO (Sales)** | Lead scoring; outreach drafts (reply rates verify fast) | Enterprise pursuits (win/loss is clear, each pursuit costs months) → rehearse against simulated buyers | Relationship nurturing (coffee now, payoff unclear when) → pipeline telemetry per touch | Key-account and channel strategy                   |

The common pattern here is:

|                        | Cheap to try         | Expensive to try                |
| ---------------------- | -------------------- | ------------------------------- |
| Fast + clear to verify | Automate high-volume | Build simulators                |
| Slow + vague to verify | Capture data         | Spend on leadership development |

Keep in mind that this is at a task-level, not role-level. A single role may span the entire spectrum of tasks.

</section>

<!-- https://claude.ai/chat/e76b43b0-d59e-46d1-a575-7afeebf05901 -->
