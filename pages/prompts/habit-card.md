---
title: Convert notes / tasks to habit cards
date: "2025-09-01T03:58:55Z"
lastmod: "2025-09-21T11:44:00Z"
classes: wrap-code
---

Generate habits to follow from reviews / post-mortems / notes.

```markdown
**Objective**: Perform a detailed analysis of a supplied behavioral note to optimize habit formation. This involves extracting objectives, verifying claims, proposing alternative methods, evaluating and ranking tactics, stress-testing, and producing a robust, testable habit card.

Begin with a concise checklist (3-7 bullets) of what you will do; keep items conceptual, not implementation-level.

**Instructions**: Parse the supplied note and follow each step sequentially, writing one section for each:

1. **Objective**. Identify objectives being pursued. If ambiguous, note plausible alternatives and specify ambiguity.
2. **Fact check**. Validate every assertion in the note. Flag unverifiable claims with explanation.
3. **Alternative**. Suggest and evaluate alternative methods (rival tactics).
4. **Evaluation**. Score and rank tactics by impact and effort.
5. **Habit**. Construct a habit card for the top tactic.
6. **Stress-test**. If necessary, revise the habit card for weak points. Assign flag levels (Low / Medium / High) for each risk category; update the habit card if any flag isn’t Low.
7. **Role play**. Run role-play scenarios. Summarize learnings and failure points to refine the habit card.
8. **Habit**. Write the final habit card as a single-level bulleted Markdown list with key phrases in **bold**.

After each substantive step, validate that results match the step's intent (e.g., confirm objectives are clearly tied to note, facts are mapped, habit card is actionable); promptly self-correct if validation fails.

<NOTE>
...
</NOTE>
```
