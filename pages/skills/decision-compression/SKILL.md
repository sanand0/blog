---
name: decision-compression
description: Automatically compress broad answers into the decision, recommendation, rationale, tradeoff, and next action. Use for recommendations, prioritization, research synthesis, strategy, planning, reviews, rankings, and large-context requests.
---

When the user's immediate task could sprawl, e.g. when:

- The user asks for recommendations, prioritization, research synthesis, strategy, planning, tradeoffs, ranking, review, "what should I do?", "what matters?", or "what am I missing?"
- The answer contains many options, caveats, dimensions, or next steps.
- The user is likely to use the answer in a meeting, client discussion, workshop, decision, or implementation.
- The user provides a large body of context and expects judgment.

Then, reduce the answer to the decision it supports.

Lead with the recommendation. Keep the decisive reason. Name the tradeoff. End with the next action.

Rules:

- Identify the decision. What will the user do differently after reading this?
- Recommend before explaining. Do not make the user assemble the answer from evidence fragments.
- Rank when there are options. Default criteria: impact, speed, demoability, evidence strength, strategic fit, reversibility, and risk.
- Separate now, next, and later. Good but non-urgent ideas should not crowd the answer.
- Name what to ignore. Remove distractions, false precision, premature work, and low-value branches.
- Keep only caveats that could change the decision.
- Prefer reversible learning steps when uncertainty is high.
- State what would change the recommendation.
- Do not end with a vague menu. Give one concrete next action unless the user asked for exploration.

When useful, add one compact note like:

```markdown
Recommendation: (best move)
Why: (decisive reason)
Do next: (one action)
Ignore for now: (distraction)
```

Skip this note when it would add clutter.

Durable basis: decision quality, bounded rationality, structured tradeoffs, checklists, OODA-style loops, lean experimentation, and cognitive-load reduction. Better agents create more options and more detail; decision value still comes from framing, prioritizing, and committing to action.
