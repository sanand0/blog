---
title: Case Study
date: 2026-07-29T11:03:15+08:00
classes: wrap-code
description: Create a training pack for analysts to build intuition
tags: [data-science, data-analysis, ai-in-education, decision-making, evaluation, ai-agents]
---

```markdown
Create a training pack to help analysts (business analysts, data scientists, strategy consultants, forward deployed engineers, etc.) improve their investigative judgment.

Success for the analyst is not recovering the hidden truth you designed. It is making the best evidence-based judgment available from the materials. Design and score for that.

First, formulate the underlying dynamics - the hidden mechanisms, reasons, processes - e.g.

- why the processes are not/poorly/wrongly documented
- why the data is stored, structured, and labelled the way it is
- why it has the quality issues that it does
- what are the underlying unstated organizational dynamics, etc.

Discovering some or all of these would be key to the analyst's success in the exercise. Don't state these dynamics directly anywhere the analyst can see. But they may be partly mentioned, disputed, denied, euphemised, or misunderstood by people who each see only a part of it. That is how it works in real-life.

For each dynamic, plan two or more independent channels through which an analyst can detect it (a data pattern, a silence in a thread, a timeline that doesn't line up, a form field abandoned mid-year), and at least one innocent explanation that fits any single channel on its own. Also plant anomalies that mean nothing - in real-life, not everything is a clue, and we want to train for the intuition to tell the difference.

Create an instructor-only `case.yaml` that includes all of this as the primary context. Include entities, systems, timeline, people, the process (how was it designed, documented, believed to run, actually runs), the dynamics and where and how each dynamic plays a role.

Record every anomaly in the pack in case.yaml, marked as: designed and critical / ambient noise / benign quirk / accidental defect. Fix the accidental defects.

Generate every artifact below from `case.yaml` to avoid ACCIDENTAL contradictions.

Create realistic documents and datasets that an analyst will likely get when investigating a process like below. This includes:

- Documents explaining the process. Reflect real-life, where some processes are undocumented, poorly documented, or wrongly documented.
- Datasets.
  - Both structured (spreadsheets, SQL dumps, geospatial, proprietary formats, ...) and unstructured (text, images, documents with a mix, audio, video, ...).
  - This may include large transactional/reference data as well as smaller datasets, across a variety of realistic formats.
  - Think about how organizations realistically store data.
    There are underlying historical and organizational reasons for why their data evolved the way it did.
    In real-life, datasets have varying quality, based on the process of collecting and processing them.
    Datasets are often sourced from multiple systems and processes.
    The nature of gaps / errors / other quality attributes typically reflect the underlying sources.
  - Use a format only if this organization would likely produce it and it serves an exercise - not just for variety.
  - For large transactional data, Use a fake data generator skill when available.
    Write seeded generator scripts rather than static files.
- Supporting material.
  This may include emails, chat logs, meeting transcripts, system logs, people profiles, etc. that are usually passed to an analyst for context.
  In real-life, these supporting materials are windows into and reflections of organizational structure, politics, constraints, etc.
  How it is said, and what is unsaid, is often more important than what is said.
- People the analyst can question.
  Add the profiles to `data/`.
  Include instructor-only notes explaining what each person knows, believes, is wrong about, and would rather not say. Enough for an instructor (or AI agent) to role-play them and answer questions like them.
  Deciding whom to ask, and what, is a critical skill. That's how analysts go beyond incomplete / incorrect briefs.

The same pack can be used for multiple exercises. Include exercises, each containing:

- Objective - a page explaining their task.
  Realistically, these may be loosely, incompletely, or wrongly defined, or unsolvable without additional data or context, etc.
  This, too, needs to reflect real-life based on a hidden dynamic.
  Where the brief is wrongly framed or underdetermined, analysts should reframe it, say what's missing, ask for it, and act safely under uncertainty. If they do that, that's a success, not failure.
  Don't make something wrong in every objective. Deciding whether to dig is part of the training.
  Mention who the objective is for, how long it should take, which tools (e.g. AI agents) are allowed, and what output to submit.
  Require an evidence table - claim | source | confidence - and the hypotheses they rejected, with why. Without this, we can't differentiate between judgment and lucky guesses.
  Some exercises can be small: one artifact, ten minutes, "does anything here smell wrong?" - including some where the answer is no.
  Intuition comes from many quick exercises with fast feedback, not just from one long case.
- Rubric - not shared with the analyst, but explaining to the instructor:
  - What the analyst needs to discover in order to succeed in the exercise - mentioning the relevant dynamic.
  - How to evaluate the analyst's work.
    Share this as a prompt that can be shared with an expert or an AI agent.
    The prompt will be shared along with the same inputs passed to the analyst (documents, datasets, supporting material, this exercise's objective) as well as the dynamics.
    The prompt should clearly explain the steps to evaluate the analyst's work and the scoring rubric along with evaluation criteria and clear definitions of what constitutes a good/bad response, with an emphasis on the hidden dynamics that the analyst needs to discover.
    Because the evaluator is handed the dynamics, say explicitly: score the evidence and reasoning first, THEN the conclusion.
    A well-supported alternative conclusion can score as high as the intended one.
    But the intended conclusion asserted without evidence should not score high.
    You can use the tone, omissions, timing, and other "non-verbal" aspects of the response as a signal, but treat that as hypotheses needing proof.
  - Write behavioural anchors for each score level.
  - Then write test submissions for this exercise, as an analyst would write them - not as someone who knows the answer. For example, if a "good" submission clearly states the dynamic, that's unrealistic. Recommended submissions:
    1. Strong: real evidence, traced to files, calibrated, some things still open.
    2. Polished but shallow: confident, well written, restates the brief, no evidence.
    3. Right conclusion without evidence - a lucky guess.
    4. A different conclusion that the evidence actually supports.
    5. Says the evidence is insufficient, and asks for the right things.
    6. Treats a decoy as a finding.
       Target what this rubric is most likely to get wrong.
  - For each submission, write what the evaluator should return:
    its expected rank against the others (a band for each dimension, not an exact score),
    and the specific text in the submission it must cite for that score.
    We'll test the evaluator based on whether it gets the right rank using the cited reasons.
    Exact numbers vary between evaluators and are not a fair check.

Generate this pack as a set of files with this structure:

- `README.md` - for the instructor, containing a full overview of the case, including the underlying dynamics, explanation of the data. An instructor reading this for the first time would understand everything they need to know about running this training exercise. Layer this. Begin with an overview, an explanation of the dynamics, a walkthrough of the data, a list of exercises and what they uncover and how to evaluate them. Then go into the details of how each dataset was generated and what dynamics it reflects.
- `case.yaml` - instructor-only source of truth. Everything else is generated from it.
- `data/` - for the analyst, containing all documents and datasets to be shared with the analyst. Nothing here (including metadata, hidden sheets, comments, ...) should reveal the dynamics DIRECTLY
- `src/` - generator scripts and seeds, so the pack can be rebuilt and re-seeded for the next cohort.
  Not all `data/` needs to be generatable - some of them can be hand-crafted or downloaded or constructed in any way.
- `exercise-<exercise_name>/` - one folder for each exercise, containing:
  - `README.md` - for the instructor, explaining the exercise, why it was chosen, how it was designed, the underlying dynamics it is designed to uncover, why this rubric was chosen, and how to evaluate the analyst's work. Assume they have read ../README.md and nothing else. End with a debrief - which cues were diagnostic, which were misleading, what an experienced analyst would notice early, and what not to generalise from this case - and a hint ladder, from directing attention, to suggesting a test, to revealing part of the mechanism.
  - `objective.md` - for the analyst, explaining the task
  - `rubric.md` - for the instructor, shared as a prompt explaining how to evaluate the analyst's
    work for this exercise.
  - `tests/`
    - `submissions/{01,02,...}.md` - analyst-facing only, neutral names
    - `expected.md` - what each one tests, expected rank, bands, required citations

The evaluator receives `objective.md`, `data/`, the dynamics, `rubric.md`, and ONE submission - never `expected.md` and never a second submission. It scores blind. Rank is derived afterwards by comparing its independent scores.

Also describe - don't build - three variants of this case in the README: same symptom with a different cause, same cause showing up through different evidence, and a control where the documented process is broadly right and the anomaly is benign. Intuition transfers through contrast, not through repetition of one case.

The aim is not to make the exercise easily solvable - quite the opposite. We're training for INTUITION - that sixth sense that comes from experience and pattern recognition, where they smell something is off and know to dig deeper. Design for this.

Hard, though, not unfair. The difficulty should come from conflicting evidence, ambiguity and incomplete access - not from sheer volume, obscure formats, or one buried clue.

Run these checks before you finish, and list every one in the README with its result:

- Write the perfect path for each exercise: the artifact-by-artifact chain from brief to finding.
  If you can't write it, it's unfair rather than hard. Rewrite the exercise.
- If you think a strong AI agent can solve an exercise one-shot while a human would take hours, the difficulty is either volume/effort (move it into contradiction and ambiguity) or clues that are too loud (make each channel innocent on its own). State and fix it.

Generate the actual files, not descriptions of them.
Report which checks you ran and what failed.
Don't say a check passed unless you ran it.

Use the context below to create the training pack.
Anonymize real organizations, people and identifiers from the context.
This context may not be directly related to the training pack. It may contain irrelevant details, objectives, tasks, etc. Just use this as the organizational context to base the training pack on.

<CONTEXT>
</CONTEXT>
```

<!--

- 29 Jul 2026: Created. Sources:
  - Mainly: https://claude.ai/chat/6343dcc1-3bac-4cf8-86cb-c7873a733125
  - Supported by: https://chatgpt.com/c/6a69500d-cc78-83ec-897e-ebe039031f91
-->
