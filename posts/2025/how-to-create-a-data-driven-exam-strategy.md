---
title: How to create a data-driven exam strategy
date: "2025-10-09T01:24:19Z"
lastmod: "2025-10-09T01:24:21Z"
categories:
  - education
  - llms
wp_id: 4232
---

![How to create a data-driven exam strategy](/blog/assets/tds-grades.webp)

Can ChatGPT give teachers data-driven **heuristics** on student grades?

I uploaded last term's scores from about 1,700 students in my [Tools in Data Science course](https://tds.s-anand.net/) and asked ChatGPT:

> This sheet contains the scores of students … (and explained the columns).
>
> I want to find out what are the best predictors of the total plus bonus… (and explained how scores are calculated).
>
> I am looking for simple statements with 80%+ correctness along the lines of:
>
> - "if ga1\_f + ga\_4f > x then you will not fail; this is true for 90% of the students" or
> - "your total will effectively be your p1\_f score, within plus or minus 5 marks; this is true for ~90% of the students" or
> - "if you get below 40% in ga3\_f then you will likely fail; 80% of the students who did so fail."
>
> Earlier predictors (GA1, GA2, maybe GA3) are more useful (to students) …
>
> Two kinds of students: Those who want to avoid failing and those who want to score high….
>
> .. give me the best student advice. Phrase it conversationally and include numerical evidence in simple language.

After a 30 minute conversation, ChatGPT delivered concrete, actionable advice:

**One-page student playbook**

If you're behind / "don't fail":

- **Immediate target:** **GA2 > 45** and **GA3 > 55**. That alone cuts fail risk to ~**16%**.
- If possible, push **>85/85** to get fail to **~8%**.
- Translation: stop skipping; get partial credit; move into the "safe" GA2/GA3 band.

If you're aiming for an **A**:

- **Path A1 (broad coverage):** **P2 + ET >= 180** > A ~ **35%** (n=169).
- **Path A2 (also broad):** **P1 + P2 >= 180** > A ~ **45%** (n=161).
- If early GAs are fine (GA2/GA3 >=70), **keep them steady**, but your **marginal effort** should go to **P2 and ET**.

If you're aiming for an **S**:

- **Path S1 (most reliable):** **P2 >= 90 + ROE >= 80** > S ~ **77%** (n=26).
- **Path S2 (elite):** **P2 >= 90 + ET >= 85 + ROE >= 80** > S ~ **91%** (n=11).
- **Simple rule of thumb:** **P2 + ROE >= 170** or **ET + ROE >= 160** > ~**70% S** with **0% fails** in those groups.
- Translation: **ace ROE**. Use P2 and ET as the second and third pillars.

---

**Students**: Don't study harder. Study what moves the marks. (Learning be damned!)

**Teachers**: Try this with **your** course data!

Full chat: <https://chatgpt.com/share/68e7034a-7340-800c-b259-0bd51715ad11>

[LinkedIn](https://www.linkedin.com/posts/sanand0_todays-exploration-data-driven-llm-advice-activity-7381923875992920064-Aeey)
