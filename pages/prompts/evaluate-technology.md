---
title: Evaluate technology
date: "2025-09-20T09:27:45Z"
lastmod: "2025-12-07T12:16:08Z"
classes: wrap-code
---

Evaluate technologies on criteria I care about.

```markdown
Evaluate ...

- List all alternatives.
- Evaluate them on:
  - Popular: e.g. # contributors / users
  - Modern: Updated recently (date of latest release) + regularly (# releases last 12 months)
  - Admired: e.g. community feedback, expert reviews
  - Features: breadth of current features
  - Momentum: how fast are new features being added
  - Focus: Whet are the recent contributions about?
  - Cost: Open source self-hostable > Liberal free tier > Low cost > Expensive (mention actual costs)
  - Docs: Clear docs, examples, tutorials, FAQ, changelog
  - Light: Low resource usage
  - Speed: Fast performance, throughput (benchmark if available)
  - Easy: intuitive, easy installation + usage
- CLI tool additional checks:
  - Scriptable: extensive options for configuration, programmable SDK/API
  - CLI-configurable: Comprehensive configurability via command line options (without requiring config files)
  - Bundle: Single-binary > small bundle > large bundle
- LLM model additional checks:
  - Quality: based on evals (name+date+link)
  - Context: input size, output size
  - Size: model size, memory usage
- Library / framework additional checks:
  - Adoption: Rapid user growth & adoption in the last 6 months?
  - Plugins: size of ecosystem
  - Formats: breadth of input/output formats supported
- Platform / services additional checks
  - Export: How easily, completely, and frequently can we export data in an open format?
  - Pricing: Is the pricing simple, clear and stable according to users?
  - Stability: High uptime, low latency, likely to be around for years
  - Support: responsive support, active community

Recommend the top 3 options based on this evaluation.
Be rigorous. **Verify and cite sources with dates.** Prefer primary docs, changelogs, and benchmarks.
When unsure, state assumptions _up front_. If evidence is weak, **say so** and (if easy) propose ways to gather evidence.

List the GitHub repo (if available) for EACH technology evaluated, sorted by stars. Double-check to ensure you don't miss any. Use this format:

- [xojs/xo](https://github.com/xojs/xo): Opinionated, zero-config ESLint wrapper with strict defaults. Summary: delightful defaults and smooth “no config” UX; coverage derives from ESLint + curated plugins; development cadence modest; great if you want ESLint’s ecosystem without managing config.
- [repo-name](https://github.com/owner/repo-name): 1-line description. Summary of evaluation.

GENERAL PREFERENCES (use if applicable)

- CLI > Web app > Native app
- File formats: Fast + Popular > Open standards > Proprietary
- Data-driven configuration/declarative approaches > imperative code
- Modular > monolith
- Declarative outputs
- Browser-first JS + Python
- Cross-platform
- Stable APIs with migration path
```
