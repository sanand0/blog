---
name: verification-gate
description: Run this by default as the final step after any non-trivial workflow — analysis, code, data work, a plan, a factual answer, a deliverable — before presenting it, even when not explicitly asked to verify. Skip it for trivial lookups, chitchat, and pure-tone tasks where there is nothing to be wrong about.
---

Verification is not re-reading to evaluate. It's getting an INDEPENDENT SIGNAL and changing only validated defects.

0. Scope it.
   If it's unfalsifiable or trivial, skip.
   If it's high stakes or irreversibile, go deep.
   Focus on the few claims the conclusion mainly depends on.

1. Reconstruct the spec — before checking the answer is right, check it answers the question.
   List the explicit asks, every stated constraint, and the implied success criteria. The most common failure is not being wrong but answering a nearby/easier question, or silently dropping a constraint. Flag any ask unmet or constraint dropped.
   If the task never defined what does _not_ count, infer the 2-3 tempting false victories and confirm the answer is not one. If it is, say so and name the exact remaining gap instead of smoothing it over.

2. Decompose into checkable units.
   Check against a multiple yes/no with reason checklist, not a single score or comparison.
   Split the output into atomic pieces: each number, factual claim, citation, code path, named entity (API / function / field / person), and load-bearing logical step. Tag each VERIFIABLE (has ground truth) or JUDGMENT (defensible, not provable).

3. Get an independent signal for every VERIFIABLE unit — re-derive, don't re-read.
   - Code / data: run it. Execute, hit edge cases, confirm it actually produces the claimed output. Recompute key numbers a _second_ way.
   - Facts / citations: refetch the source and confirm it says what you claim — not merely that it exists. Half-remembered and fabricated citations are the default failure here.
   - Arithmetic / units / conversions: recompute independently; check dimensions.
   - Names / identifiers: confirm the API, function, field, or spelling exists as written.

   A second _different_ route, or ground truth, counts. If all you can do is re-read and feel sure, it is **unverified** — mark it that way, don't launder it into "checked."

4. Hunt the known failure modes — don't ask "is this good?", try to find specific defects.

   For example, actively look for an instance of each:
   overclaiming past the evidence;
   stale fact (changed since cutoff);
   off-by-one or unhandled edge case;
   reversed causality or direction;
   plausible-but-wrong specific (exact figure, date, name);
   internal contradiction;
   an ambiguity you resolved silently in your own favor;
   a renamed hard part — an equal-difficulty subproblem labeled "routine", "the key", or "remaining work".

   This list is the floor: name the domain's own three most likely defects (judge position bias, leaked benchmark, unfair denominator, race condition, ...) and hunt those too.

5. Question the judge.
   You (and any human/LLM judge) may prefer the first option, longer answers, own family's style, and whatever is labelled "reference/human/baseline", etc.
   If possible, swap A/B order (or score both ways), don't reward length, use a different‑family judge, hide biasing labels, etc.
   (Sanity‑check the judge on an obviously wrong answer first. If it passes that, the judge is broken.)

6. Stress-test JUDGMENT units.
   You can't prove them — try to break them: the strongest counterargument, "what would have to be true," one disconfirming case. Down-rank anything that doesn't survive.

7. Fix only identified defects — then re-verify the fix.
   Revise only where steps 1–5 named a concrete defect with evidence. Found no error → leave it exactly as is; editing on a hunch usually injects error. Every changed unit is a new unit — run it back through step 3.

8. Report calibrated.
   State what you checked and how (executed / sourced / recomputed vs. merely reasoned), what survived, and what is still uncertain or unverified. Confidence tracks the _weakest load-bearing unit_, not the average. A clean pass is a real result — say "checked X, Y, Z; holds" plainly. Never report "verified" for anything you only re-read.

Hard rules:

- Re-derive, don't re-read. A second route or ground truth, or it stays unverified.
- Change only what you can name a defect for. Found no error → change nothing.
- Verify the load-bearing units; confidence = weakest link, not the average.
- Did it answer the question and keep every constraint? Check that before correctness.
- Prefer execution / source / recompute over "this looks right."
- "Unverified" is an honest, valid output. Don't manufacture problems to look thorough, and don't launder a hunch into a check.
- Proportional and bounded: stop once the load-bearing units are checked. Don't loop.
