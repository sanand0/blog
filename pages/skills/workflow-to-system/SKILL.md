---
name: workflow-to-system
description: Automatically detect when a one-off request is really a repeatable workflow, then propose the smallest reusable system - template, script, spec, state file, checklist, prompt, CLI, repo structure, automation, or operating rhythm. Use for repeated work, coding/data tasks, agents, personal knowledge workflows, demos, assessments, and operations.
keywords: [workflow engineering, system design, templates, automation, state management, checklists]
---

When the user's immediate task reveals a repeatable pattern, e.g. when:

- The user repeats or references a recurring task: briefs, demos, prompt patterns, skills, assessments, reports, data pipelines, sync scripts, personal knowledge search, client prep, or artifact generation.
- The task uses files, folders, scripts, CLIs, calendars, emails, transcripts, repos, spreadsheets, Markdown, JSON, HTML, or dashboards.
- The answer includes steps that could become a checklist, template, command, state machine, spec, or automation.
- The user is doing agentic work where prompts, specs, logs, tests, and outputs should be reusable.

Then, turn repeated effort into reusable machinery without over-engineering.

Capture the workflow. Standardize the inputs and outputs. Preserve state and provenance. Automate only where the payoff is clear.

Rules:

- Solve the immediate task first. Do not let system-building hijack the user's request.
- Prefer the smallest reusable form: checklist before template, template before script, script before app.
- Make inputs and outputs explicit. Name the files, fields, commands, folders, schemas, or artifacts involved.
- Preserve state when the workflow may continue later. Use small IDs, state files, logs, dates, or status markers where useful.
- Keep provenance attached. Record where inputs came from, what was changed, what was assumed, and what needs verification.
- Design for agents and humans. A good workflow should be easy to run manually, easy for an agent to follow, and easy to inspect after.
- Add tests or checks when errors are likely. Use sample inputs, dry runs, validation rules, diffs, or review gates.
- Avoid premature automation. If the task is rare, ambiguous, or still changing, suggest a reusable prompt or checklist instead.

When useful, add a small note like:

```markdown
Reusable pattern: (name)
Use when: (trigger)
Inputs: (files/data/context)
Output: (artifact/result)
Next system step: (checklist/template/script/state file/spec)
```

Skip this note when it would add clutter.
