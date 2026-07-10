---
title: IIM Bangalore PGP Interview Panel
date: 2026-03-17T06:42:32+05:30
categories:
  - education
description: AI can help interviewers rapidly extract sharper questions from dense applicant materials, improving evaluation when time is too short for careful manual review.
tags: [interviews, admissions, evaluation, higher-education]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7439864413735714816/
---

![](https://files.s-anand.net/images/2026-03-17-iim-bangalore-pgp-interview-panel.avif) <!-- https://gemini.google.com/u/2/app/2ff4c1dd6c10b1d7 -->

Yesterday, I was part of an IIM Bangalore interview panel at Hyderabad, along with Professor Subhabrata Das and Debajyoti. Panels typically comprise of two faculty and an alumni, and handle 8 interviews in the morning and eight in the evening, though in our case, we had 9 each.

As we arrived, we were given a USB drive with the student's resume, statement of purpose, and other documents that they had submitted, which included employment contracts, declarations, letters of recommendation, etc., depending on the student. Each interview was approximately 20 minutes. Luckily, Dr Das set a timer for 18, so we didn't go too far beyond.

There was practically no time to read the documents before each interview, so I used Claude with the following prompt to suggest questions.

```markdown
In the context of the below, suggest deep, probing questions that will reveal the suitability of the attached candidate for IIM PGP.

Feel free to search online for additional information about the candidate.
```

...followed by

1. The instructions email from IIMB
2. The attachment in the email
3. Claude's earlier advice on how to evaluate candidates based on the above. This included suggestions to:
   - **Probe for internal consistency**: "Your SoP says X but your job history suggests Y. Explain."
   - **Probe for authenticity**: stuff that coaching can't teach. (It gave candidate-specific questions.)
   - **Probe for social sensitivity**: "You're from village X. Where does your aspiration help / hurt whihc segments of your village?"
4. The candidate's documents (resume, statement of purpose, etc.)

It helped that there were three panelists. That gave me time to screen the questions and understand the good ones - while others asked their questions.

**DISADVANTAGE**: You have to spend time reading the questions. Not all questions are great. Hallucinations exist (It said one candidate had a claw-back in their employment contract - they didn't.)\
**ADVANTAGE**: You pick up little-known stuff. One wrote a monthly salary instead of yearly and didn't know it. The gaps in the resume, the dips in transcripts, etc. surfaced instantly.

Initially, I just read out some questions.\
Then I tried using my own judgement.\
Then I went back to Claude's questions.\
It took a while to learn how to use it well.

---

The interview questions idea came from Claude. It also suggested:

- **Transcribe real time and pop-up questions**. I wish I could and I'm sure it'll happen soon.
- **Review scores & transcript with Claude**. I did almost exactly that!

I told GitHub Copilot CLI (I had credits) running Claude 4.6 Sonnet (a sensible model):

> You are evaluating candidates for the PGP Program at IIM Bangalore.\
> Read interview-guidelines.md fully to understand the process and criteria.
>
> Then, go through each candidate's folder. These contain:
>
> - notes.md: interview notes
> - documents.md: documents submitted (converted from the PDF in that folder).
>
> Primarily based on the notes (using documents.md for reference - no need to read PDFs), evaluate all candidates on the criteria mentioned in interview-guidelines.md.
>
> Plan like an expert interview evaluator first. In this context, first think about:
> - What patterns would an expert in this field check / recognize that beginners would miss?
> - What questions would an expert ask that a beginner would not know to?
> - What problems / failures would an expert anticipate that beginners may not be aware of?
> - How would an expert analyze this? At each step, explain what they are looking for and why.
>
> Document and plan your process in eval-copilot-claude/plan.md.\
> Then, analyze students (use sub-agents as required) and document your analysis and evaluation in eval-copilot-claude/evaluation.md.

It reviewed all 18 candidates summarizing their background, work-experience, and interview scores along with strengths, concerns, and notable moments, with an evaluation summary.

This serves as a good cross-check, I think. So I told it to:

> Compare the ratings against my ratings (and notes) in README.md.\
> Sort the candidates based on the difference between my ratings vs your (normalized / scaled from 1-10) ratings.\
> For the biggest differences, analyze the reasons for the differences.\
> Specifically, what might I have missed in the candidate that I should take a closer look at?\
> Append this to eval-copilot-claude/evaluation.md.

I ran this on Copilot as well as Claude. We agreed on the best candidate. No question about that. Interesting!

This revealed some interesting observations. I seem to:

- **Ignore social insensitivity and artistic ability**. Most likely because I lack both. Note to self: I'm blind to, and hence devalue, what I'm not good at.
- **Value genuineness far more than analytics**. I rated one candidate with _terrible_ analysis skills as only a marginal reject. Claude rejected them outright. This is true for another candidate, too. But I rejected fakers outright.
- **I calibrate for preparation**. I expect more from those with more experience, with more interview preparation, etc. Not a bad thing - just an observation.

---

In short:

- **AI is great for preparation**. I should make it easier to feed it context.
- **AI is great at post-mortems**. I need to budget time for this.
- **AI can help _during_ discussions**. I need to figure out the technology for this.
