---
title: Post-mortem of AI coding session
date: 2026-03-23T07:24:09+05:30
classes: wrap-code
description: I run blameless post-mortems on AI coding sessions using this prompt to document successes, analyze failures, and identify root causes. This process helps me refine environment settings and prompt structures to prevent recurring errors.
keywords: [ai coding, post-mortem, prompt engineering, root cause analysis, workflow optimization, llm feedback]
---

```markdown
Run a blameless post-mortem on this entire conversation to improve future performance.

1. Document the entire process so far (what you did, how, what you found, next steps, etc.).
2. List successes: techniques / approaches you discovered that worked well. Examples: tools, code snippets, prompt structures, planning techniques. Share what change to the environment / prompts will make it easier to repeat these successes in the future.
3. List problems faced: failures, inefficiencies and mis-alignments. E.g. commands that failed or behaved unexpectedly, corrections, more steps than necessary, where you adhered to the letter not spirit, took shortcuts that compromised quality, etc. Dig deep for root causes. Mention the PRACTICAL impact. Suggest pragmatic & safe fixes (if any) to prompts, skills, or environment (e.g. tools, .env) at a root cause level - preferably that resolve **entire classes/patterns of failures**, not just a specific instance.

Create or append to `notes.md` as `## Post mortem (%d %b %Y)` with today's date.
```
