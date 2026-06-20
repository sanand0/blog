---
name: failure-redteam
description: Automatically stress-test plans, demos, claims, workflows, AI systems, code, data analyses, assessments, and recommendations by identifying likely failures, misuse, misunderstanding, edge cases, incentives, security/privacy risks, and lightweight mitigations.
keywords: [red teaming, premortems, ai safety, risk management, stress testing, adversarial testing]
---

When the user's immediate task could fail in a costly or embarrassing way, e.g. when:

- The task involves plans, demos, launches, client work, public claims, AI workflows, agents, code, data pipelines, assessments, governance, privacy, security, recommendations, or operational change.
- The answer could lead to bad decisions, client mistrust, unfair grading, security/privacy exposure, wasted effort, or a fragile system.
- The user asks for critique, review, risks, objections, edge cases, adversarial thinking, "what am I missing?", or "brutally honest."

Then, stress-test the answer without becoming negative or blocking action.

Find the failures before the audience, client, student, user, attacker, or production system finds them. Suggest lightweight fixes.

Rules:

- Assume it failed. Ask what probably went wrong.
- Attack the system, not just the model: people, incentives, data, UI, permissions, integrations, process, measurement, and downstream use.
- Prioritize plausible failures. Do not list every theoretical risk.
- Look for silent failures: outputs that seem correct but are wrong, stale, biased, incomplete, insecure, or unauditable.
- Check misuse and gaming. Ask how a student, user, employee, client, attacker, or model could exploit the design.
- Distinguish demo risk from production risk. Demos need credibility and safety; production needs ownership, monitoring, rollback, and controls.
- Pair each major risk with a prevention, detection, recovery step, or wording change.
- Add tripwires when useful: thresholds, tests, signals, review gates, or escalation points.
- Keep the main path alive unless the risk invalidates it.

When useful, add one compact note like:

```markdown
Main risk: <most plausible failure>
Fix: <lightweight mitigation>
Tripwire: <early signal or test>
Residual risk: <what remains>
```

Skip this note when it would add clutter.

Durable basis: premortems, red teaming, safety engineering, security review, postmortems, AI risk management, and adversarial testing. Better agents increase autonomy, integration depth, and blast radius; the need to anticipate failure and misuse increases rather than decreases.
