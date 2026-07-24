---
title: Talk Event Scan
date: 2026-07-24T12:00:00+08:00
classes: wrap-code
description: Scan for events I should speak at or attend, and update the registry of events.
tags: [ai-workflows, prompt-engineering, chatgpt, public-speaking, productivity]
---

Run on ChatGPT, weekly.

```markdown
Run a weekly scan for events I should speak at or attend. Today's date and all action dates should use Singapore time.

Read from @LocalMCP without modifying files. Give me registry changes that I can copy into:

`~/Dropbox/notes/talk-event-list.tsv`

## Understand me first

Read and apply, as relevant:

- `~/Dropbox/notes/talk-event-list.tsv` - talk registry
- `~/Dropbox/notes/talks.md` - talk ideas, proposals and preparation
- `~/code/talks/README.md` and relevant talk transcripts - delivered talks and formats
- my current calendars via `gws`
- the `anand-objectives`, `reframe-question`, `expert-lens` and `blind-spot` skills
- If required: `~/Dropbox/notes/people.md`, relevant `about/*.md`, and recent relevant transcripts - how I learn from and connect with people

State which calendars and personal sources you successfully checked.

## Find events

Search official event, CFP and registration pages for:

- events occurring in the next 9 months;
- CFPs open up to 12 months ahead.

Prioritize Singapore, Chennai, Bangalore, Hyderabad, and remote events. Consider Mumbai, Delhi for valuable opportunities, other locations only for unusually valuable opportunities.

Search beyond AI and technology events. Also find open trade-, domain- and function-specific events where AI creates a useful angle for that audience - for example education, journalism, design, publishing, government, HR, product, consulting, finance, healthcare, manufacturing, law, or investment.

For a non-AI event, do not propose a generic "AI is transforming this field" talk. Identify a specific workflow, decision, risk, experiment or new capability that would matter to that audience and could produce an evidence-rich, useful session.

Do not penalize an event because it requires new material. Expanding my portfolio of talks, experiments and relationships is part of the objective. Reward new material when it could become a reusable asset.

## Constraints

I never pay to attend or speak.

Use these cost values:

- `free` - attendance is explicitly free;
- `free_if_speaker` - accepted speakers receive free access;
- `paid` - I would have to pay;
- `unknown` - not verified.

Do not recommend `paid` events. Recommend `free_if_speaker` events only for speaking. Keep high-value `unknown` events as watch items until cost is verified.

Prefer open CFPs and public registration over invitation-only events.

Remind me at a useful action date, normally:

- 14-21 days before a CFP closes;
- early enough to register before capacity or free places disappear;
- immediately, if an important opportunity is discovered later than ideal.

## Rank by value

Consider:

- fit with my objectives and interests;
- strength and specificity of the AI angle;
- learning value;
- relationship value and quality of likely participants;
- opportunity to test an idea with an audience;
- potential to create a reusable talk, experiment, benchmark, dataset, demo or relationship asset;
- reach and credibility;
- novelty relative to my existing audiences and portfolio;
- openness and likelihood of acceptance;
- calendar and travel fit;
- preparation and travel effort;
- commercial noise.

Do not recommend an event merely because it is large, prestigious or contains "AI" in its title.

Include at least one strong wildcard outside my usual communities when one exists.

## Use the registry to avoid repetition

Read all existing registry rows before searching.

Identify the same event using its existing `event_id`, canonical official URL, or normalized event name + year + city. Never create a duplicate row for another page belonging to the same event.

Silently recheck relevant active events, but mention a previously registered event in the report only when:

- its action date is now due;
- a deadline, date, location, format, cost, availability or URL changed;
- an unknown fact was resolved;
- my calendar or travel fit materially changed;
- new information materially changes its priority;
- I explicitly need to reconsider it.

Otherwise, suppress it completely.

Do not change a registry row merely to record that it was checked again. Update it only when a material field, status, action or next-review date changes.

Keep past events in the registry as history. Mark them `expired`, `attended` or `spoke`; do not delete them merely because they have passed.

Add a researched event to the registry when it is:

- worth recommending or watching; or
- a plausible recurring candidate whose rejection should be remembered.

Do not add obviously irrelevant search results.

## Registry schema

Fields:

- `event_id`: stable lowercase identifier such as `2026-containerdays-singapore`. Preserve it forever.
- `event_name`
- `organizer`
- `start_date`
- `end_date`
- `city`
- `country`
- `format`: `in_person`, `online` or `hybrid`.
- `event_type`
- `domains`: short semicolon-separated terms.
- `audience`
- `official_url`
- `cfp_url`
- `cfp_deadline`
- `registration_url`
- `registration_deadline`
- `cost_status`
- `recommendation`: `speak`, `attend`, `both`, `watch` or `skip`.
- `ai_angle`
- `why_for_me`
- `priority`: `1` highest through `5` lowest.
- `status`: `discovered`, `watching`, `action_due`, `submitted`, `registered`, `invited`, `rejected`, `skip`, `expired`, `cancelled`, `attended` or `spoke`.
- `next_action`
- `action_due`: when I should act or be reminded - not necessarily the final deadline.
- `next_review`: when the event should next be reconsidered if no action is currently due.
- `first_seen`: preserve the original value.
- `last_changed`: update only after a material change.
- `confidence`: `high`, `medium` or `low`.
- `notes`

Rules:

- Dates: `YYYY-MM-DD`; leave unknown dates blank.
- Use only official canonical URLs where possible.
- Fields must contain no tabs or line breaks. Use semicolons within fields.
- Keep `ai_angle`, `why_for_me`, `next_action` and `notes` concise.

## Output

### 1. Recommended actions

Show only events that are:

- **NEW** - newly discovered and worth my attention;
- **DUE** - action is timely now;
- **CHANGED** - material facts or priority changed.

Rank by value, not by deadline alone. Do not fill a quota. Return at most 10.

For each, give:

1. Tag: **NEW**, **DUE** or **CHANGED**
2. Event, date, location and official link
3. **Speak**, **Attend**, **Both** or **Watch**
4. Exact next action and recommended action date
5. CFP or registration deadline, where applicable
6. Cost status
7. Why it matters specifically to me
8. A specific AI angle or session idea for this audience
9. Calendar and travel fit
10. Confidence

For a **CHANGED** event, emphasize what changed rather than repeating its full earlier rationale.

### 2. Registry changes

Output only the applicable sections:

#### ADD

Provide complete new rows without the header. I will append them.

#### REPLACE

Provide complete replacement rows without the header. Prefix each row outside the TSV block with the `event_id` it replaces, or group them in a TSV block whose first column is the existing `event_id`. I will replace the matching rows.

#### DELETE

List `event_id<TAB>reason`. Delete only duplicates, erroneous identities or rows merged into another event - not expired events.

If a section has no changes, omit it. Never reproduce unchanged rows.

### 3. Scan summary

Briefly state:

- how many existing events were silently suppressed because nothing changed;
- how many new events were investigated but rejected without registry entry;
- important gaps, such as inaccessible calendars or unverified cost;
- where the search may need broadening next week.

If nothing deserves action, say so. Still provide registry changes when facts or statuses need updating.
```

- 23 Jul 2026: Created. Sources:
  - https://chatgpt.com/c/6a61a82b-bc80-83ee-a02c-ab8f7e1db9dc
