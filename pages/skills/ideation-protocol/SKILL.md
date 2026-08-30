---
name: ideation-protocol
description: Brainstorm creative, novel, non-obvious ideas or options for an open-ended problem and narrow them to a recommendation. Not for writing prose, research, explanation, summaries, or questions with one right answer.
---

Use all three phases: FRAME, DIVERGE, and CONVERGE.
Keep candidates to one line and spend words on finalists.

- FRAME. Name the prize: a FIX (something must work; most business briefs) or SURPRISE (new ways to see or do; briefs that say invent, imagine, or name no owner or metric). Weight every later choice by the prize. Then list the 5-7 ideas a smart generalist would offer within 30 seconds (the mode). Ban them and their thin disguises. No later idea may reuse their core mechanism.
- DIVERGE prioritizing novelty over feasibility. Do not filter yet.
  - Name 4-6 independent dimensions a solution could vary on (e.g. mechanism, actor, who pays, timing, what is removed or inverted). Generate one-line candidates covering dimension combinations no candidate covers yet.
  - Pick 2 UNRELATED domains. Extract 3 proven mechanics from each. Create candidates that depend on a borrowed mechanic to work; drop any where the borrowing is decoration.
  - Give every candidate a typicality score from 0.0 to 1.0: how likely a typical AI assistant is to suggest it for this brief. At least half the pool must score below 0.3.
  - Merge overlaps by causal mechanism, not wording. Keep 3-5x as many ideas as you finally need, maximally spread across mechanisms, users, and time horizons.
  - If the merged pool crowds into 1-2 mechanism families, run one more generation pass restricted to the neglected families before converging.
- CONVERGE.
  - For a FIX, first state the binding constraint: the one bottleneck that, if moved, moves everything else. Gate by the prize.
    FIX: keep only candidates with a stated causal path - change X, which causes Y, which moves the bottleneck - or which show the bottleneck itself is wrong.
    SURPRISE: keep the lowest-typicality candidates that still name the mechanism that makes them possible.
    No magic steps either way.
  - For each survivor: the one assumption that must hold, who adopts it and why they keep using it, and the cheapest observation that would falsify it.
  - Select by pairwise knockout on one question. FIX: most consequential if it works AND most likely to survive contact with reality AND wins even when everyone uses a powerful AI agent. SURPRISE: most changes how you see the problem AND could actually be built. Do not use rating scales; ratings cluster while comparisons discriminate.
  - Recommend the best practical idea(s) and the best wildcard idea(s): state the non-obvious insight each depends on and the first cheap test that would confirm or kill it.

The numbers above are defaults, not constraints.
Skip, repeat, or expand sub-steps if it'll improve diversity or the final choice.
