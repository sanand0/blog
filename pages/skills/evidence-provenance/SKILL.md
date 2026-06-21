---
name: evidence-provenance
description: Automatically improve trust, auditability, and reuse by separating facts, assumptions, inferences, sources, confidence, and verification. Use for research, client claims, data analysis, AI outputs, technical recommendations, public writing, and anything that may be reused or shown to others.
metadata:
  sources:
    - https://chatgpt.com/c/6a34fe2f-6128-83ee-bf7f-895e2d0ab39b
---

When the user's immediate task depends on evidence, e.g. when:

- The answer includes factual claims, recommendations, rankings, numbers, dates, laws, prices, technical capabilities, current information, or client-facing claims.
- The task uses files, data, transcripts, spreadsheets, code outputs, logs, emails, web pages, PDFs, or AI-generated outputs.
- The output may become a demo, leadership note, public post, slide, assessment, workflow, policy, or reusable prompt.
- The user asks for confidence, verification, sources, citations, auditability, reproducibility, lineage, exceptions, or "are you sure?"

Then, make the answer reliable enough to act on without drowning it in citations.

Separate facts from assumptions. Preserve where claims came from. Say what was checked, what was inferred, and what still needs verification.

Rules:

- Solve the user's task first. Add provenance only where it improves trust or prevents misuse.
- Label the important claim types: source-backed, user-provided, inferred, assumed, unknown.
- Cite or reference load-bearing evidence. Do not add decorative citations.
- Check freshness when facts can change. Use exact dates when relative timing matters.
- Preserve source meaning. Summarize faithfully; quote sparingly; use file names, line references, cells, commands, or outputs when useful.
- Record material transformations: filters, joins, thresholds, heuristics, prompts, models, tools, or human decisions.
- Give confidence only with a reason. Say what would change the answer.
- Prefer reproducible evidence: code, commands, formulas, tests, queries, logs, or reviewable artifacts.
- Never fake provenance. If something is from memory, say so or verify.
- Keep the evidence layer proportional. A risky external claim needs more support than a private working note.

When useful, add one compact note like:

```markdown
Evidence: <source/input checked>
Assumption: <what must be true>
Confidence: <high/medium/low + why>
Verify before external use: <specific check>
```

Skip this note when it would add clutter.

Durable basis: provenance modeling, audit trails, scientific reproducibility, requirements traceability, model/dataset documentation, risk management, and verification/validation. Better models increase output volume and downstream dependence; they do not remove the need to know what a claim rests on.
