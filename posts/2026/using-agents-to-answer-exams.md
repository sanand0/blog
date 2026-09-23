---
title: Using agents to answer exams
date: 2026-09-23T10:53:03+08:00
categories:
- llms
- education
description: I used Codex CLI to complete a proctored iMocha practice exam while I watched. It finished despite flawed questions and zero reported violations, suggesting hiring tests must assess agent use and verification.
tags: [ai-agents, recruitment, codex-cli]
---

Our recruitment team asked me to review hiring questions for analysts and data scientists. These were on [iMocha](https://imocha.io/) - a proctored assessment platform.

I logged in. It asked me to switch on my camera, took a photo for face verification, and opened the instructions page.

### Agents can solve exams

I told Codex CLI (running GPT 5.6 Luna Medium):

> https://test.imocha.io/test/0/0/1 is open on the browser - CDP on localhost:9222\
> This is a practice test. Solve it. Log progress and results in notes.md.

After 11 minutes, it came back with:

> Completed the practice test and logged everything in notes.md.
>
> General section: 10/10 attempted and submitted.\
> Coding section: submitted; grader showed formatting-related failures.\
> MySQL section: passed.\
> Uploaded report: formal_sales_report.txt\
> Practice flow finished and redirected away from iMocha.\

There were a few things it struggled with. For example:

- **Unusual radio buttons**. Codex learnt that it needs to click, then verify if the page actually shows the radio buttons as checked.
- **Auto-formatting**. The code editor re-formats text while typing. Codex learnt: "For small code, click, `Control+A`, and type; for larger code, set `monaco.editor.getModels()[0].setValue(source)` and inspect the resulting source before compiling."

So I told it to:

> Document learnings about how to use the imocha.io tests in an imocha-test/SKILL.md - compatible with how skills loaded in projects.

Then:

> Click "Start Test" and solve the test.

12 minutes later, it did. I just watched it, staring at the webcam, while eating an apple.

<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/AxXQhSehfbw" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

### Proctoring may need revision

Interestingly, the proctoring report shows no problems. It took pictures of me (maybe every minute or so) and since it was the same person with no one else present, it assumed all is well.

![The Proctoring Report shows 0 Total Violations.](https://files.s-anand.net/images/2026-09-22-using-agents-to-take-exams-proctoring-report.avif)

![While I was eating an apple](https://files.s-anand.net/images/2026-09-22-using-agents-to-take-exams-anand-apple-1.avif)
![... and the agents was coding.](https://files.s-anand.net/images/2026-09-22-using-agents-to-take-exams-anand-apple-2.avif)
![](https://files.s-anand.net/images/2026-09-22-using-agents-to-take-exams-anand-apple-3.avif)
![](https://files.s-anand.net/images/2026-09-22-using-agents-to-take-exams-anand-apple-4.avif)

In other words:

- At least _this_ app isn't AI agent proof yet
- If someone were telling me what to type from outside the field of vision, it wouldn't work.

I was later told by our recruiting team that many of these exams are conducted in testing centers where agents aren't allowed - in which case, online proctoring might not be required in the first place.

### Questions banks have errors

For example:

- One question asked how to filter a Pandas table. Luna used' `query()`, which worked when executed, but iMocha marked it wrong.
- One compound-interest question had four answer choices. **None were correct.** Luna picked one and got the mark anyway.
- One reasoning question gave facts about robins and sparrows, then asked what we could conclude about finches. **Nothing about finches followed from the facts given**, but the test still had a "correct" answer.
- One SQL question asked to join salary history and department history. Luna gave an answer that iMocha accepted, but that was a **wrong join** that could assign an old salary to the wrong department!

These questions were probably drawn from a question bank. My lessons:

1. Question banks have errors
2. Agents can cheaply check quality
3. I need to control my temper. When our recruiting team asked, "So, Anand, should we use agents to quality-check questions?" it took me a few deep breaths to control my blood pressure and ask sweetly, "What do _you_ think?"

### We need better questions

Many questions test things like writing SQL / Python scripts for simple tasks. Agents do these _very_ well.

Maybe we still need to test for these. But let's reduce it and instead add new types of questions, like:

1. **Use agents well**. Give them hard tasks like "Analyze this _large_ dataset", "Deploy an app", etc. that check if they can use agents well. (Not everyone can.)
2. **Verify agent output**. Give them results with errors ranging from blatant to subtle. Can they spot them all (with or without agents)?
3. **Test new skills** that are important in the AI era.
   - Do they speak well? "Upload a 1 min audio/video answering why we should hire you."
   - Are they diligent? "Mail careers@example.org a week later to follow up."
   - Do they take ownership? "Your answer to Q5 above had this mistake: ___. Why did that happen?"
   - Do they show initiative? "Create a GitHub repo and get 20 stars before the exam ends."

### Testing infrastructure needs to change

I realized that it's harder for recruiters to change and easier for the testing infrastructure to enale these. Specfically:

- **Question banks** need to change: picking from a "Gen AI skill" question bank is easier for recruiters.
- **Testing software** needs to change: to detect AI use as well as selectively allow it for questions where it's required.
- **Test centers** need to change: to allow and enable agent usage for specific exams.
