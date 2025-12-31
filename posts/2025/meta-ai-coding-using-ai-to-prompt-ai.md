---
title: "Meta AI Coding: Using AI to Prompt AI"
date: "2025-08-13T09:43:24Z"
lastmod: "2025-08-13T09:43:26Z"
categories:
  - links
wp_id: 4169
---

I'm "meta AI coding" -- using an AI code editor to create the prompt for an AI code editor.

**Why?**

- **Time**. The task is complex. If the LLM (or I) mess up, I don't want re-work. Review time is a bottleneck.
- **Cost**. Codex is free on my $20 OpenAI plan. Claude Code is ~$1 per chat, so I want value.
- **Learning**. I want to see what a **good** prompt looks like.

So, I wrote a rough prompt in `prompts.md`, told Codex:

> prompts.md has a prompt under the "# Improve schema" section starting line 294.\
> This is a prompt that will be passed to Claude Code to implement.\
> Ask me questions as required and improve the prompt so that the results will be in line with my expectations, one-shot.

Codex answered:

> I read the “Improve schema” section. A few specifics need your call so I can produce a single, precise prompt.
>
> - Masters vs layouts: Remove masters entirely and keep a `layouts[]`, or remove layouts and keep `masters[]` with `shapes` acting as the layout? The bullets conflict.
> - Shape registry: Confirm `.shapes` is an object map keyed by `id` at every level (root, master/layout, slide), not arrays. Ordering via `z` only?
> - Merge semantics: Confirm deep-merge precedence root.shapes < mid-level (master/layout).shapes < slide.shapes, by `id`. For arrays like `list.items`, replace (not concat)?
> - Theme flattening: Move `theme.colors` and `theme.fonts` to root as `colors` and `fonts`, or keep `theme` but allow root aliases? Which do you prefer?
> - Back-compat: Keep support for old schema, or drop and add a migration utility (CLI/script) to transform old→new? If keep, how long to maintain?
> - Version: Bump to `version: \"2.0.0\"` for the new schema?
> - Validation: Add a JSON Schema file and validate inputs in `slidegen.html()` (fast fail)? If yes, filename path e.g., `schema/slidegen.schema.json`?
> - Tests and samples: Update all decks in `tests/` (incl. `shapes-demo.json`) and `tests/index.html` to new schema only?
> - Overrides removal: Confirm `slides[].overrides` is removed entirely; all overrides via `slides[].shapes` only.
> - Any additional fields to normalize while we’re here (e.g., unify `unit`, enforce `%|px`, formalize border props)?
>
> Reply with your choices. I’ll then deliver a single, one-shot prompt for Claude Code with exact schema, merge rules, migration plan, test updates, and acceptance criteria aligned to your coding guidelines.

I replied:

> - masters versus layouts: I want you to remove masters entirely and keep a layouts[]. There currently are layouts inside masters, move them up to one level.
> - .shapes is not an object map currently. It SHOULD be an object map keyed by `id` at every level and not arrays and it should be ordered via z only.
> - The deep merge precedence that you have listed is correct.
> - For list.items replacement instead of concatenation is correct.
> - Since we are flattening the themes, we do not want theme at the root level and we do not want theme.colors/fonts aliases.
> - We do not want to support old schema.
> - We do not want to migrate from old schema.
> - We do not want to bump up the version.
> - We do not want to create a json schema file.
> - We do want to update all the tests including shapes-demo.json.
> - We do want to remove slides.overrides entirely, no other fields to normalize.
>
> If you have any other questions, please ask. Else update prompts.md

Codex gave an output. I reviewed it and sent one more prompt:

> Drop the house rules.\
> Allow the root .bg to be overridden by layouts[].bg to be overridden by slides[].bg -- and all the .bg values can be { fille, image, image\_fit }\
> layouts must be an object with the .id as key instead of a field. If any of this is unclear, please ask me. Else update prompts.md.

It finally settled on [this remarkable prompt](https://github.com/sanand0/slidegen/blame/de953817266357b00d80d4fa3e17def02e0de292/prompts.md#L296-L502).

This prompt was so clear it was **easy to review** **and** **easy for Claude Code** to follow (no inconsistencies).

I plan to use this technique more. You might want to try it, too.
