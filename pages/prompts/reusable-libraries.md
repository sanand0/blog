---
title: Reusable libraries
date: "2025-09-10T07:05:28Z"
lastmod: "2025-09-21T11:44:00Z"
classes: wrap-code
---

From a folder sym-linked to multiple projects, identify reusable libraries and functions.

```markdown
# Role and Objective

- Analyze all .py, .js files under `./*/` updated in the last 90 days (skipping standard templates, boilerplate code, etc.) and update `./reuse.md` to:
  1. Suggest libraries that could improve code quality and reduce boilerplate.
  2. Identify reusable functions and opportunities for generalization.

# Checklist

Begin with a concise checklist (3-7 bullets) outlining your steps:

- Enumerate all specified files under `./*/`. Note: directories under `./` are symlinks.
- For each file, analyze for potential external library usage and reusable function candidates.
- Summarize findings by library and reusable function, grouping affected files.
- Alphabetize and format sections as specified before final Markdown output.
- Validate that all files are processed.

# Instructions

- For each file:
  - Identify code that could be replaced with modern, popular libraries.
  - Summarize findings by library and the files that could benefit from each.
  - Note any code suitable for extraction into reusable functions, generalize when feasible.
- Alphabetize libraries and functions in their respective sections.

## Sub-categories

### External Libraries

- List each identified library (bulleted, alphabetized).
  - For each, sub-list the affected file(s) (bulleted, relative paths).

### Reusable Functions

- For each reusable/generalized function (bulleted, alphabetized):
  - **Signature:** Provide as a Markdown code block.
  - **Docstring:** 1-line summary.
  - **Files Benefiting from This Function:** Bulleted list of relevant files.
  - **Library:** Markdown code block(s), indented.

# Agentic Operation and Verification

- Attempt an autonomous first pass using available information; escalate with a clarifying question only if ambiguities arise.
- After the analysis, validate that:
  - All findings are alphabetized in their sections.
  - Every file is categorized.
  - Output matches the required Markdown structure and section order.
- If success criteria are not met (e.g., missing or miscategorized files), self-correct and re-validate before finalizing output.

# Output Format

- All sections must be valid Markdown.
- Use unordered (bulleted) lists.
- Section order:
  1. Checklist
  2. External Libraries
  3. Reusable Functions

# Stop Conditions

- Stop when the updated Markdown file comprehensively reflects all findings, in the correct format.
- Escalate or ask for clarification if file access issues persist or ambiguities arise.
```
