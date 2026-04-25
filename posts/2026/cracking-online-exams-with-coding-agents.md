---
title: Cracking online exams with coding agents
date: '2026-03-13T15:37:19+08:00'
categories:
- llms
- education
description: Coding agents can solve many online exams effectively, so exam design should be tested against agents both to validate questions and to understand where real difficulty lies.
keywords: [online exams, coding agents, assessment design, AI in education, prompt attacks, evaluation]
---

<!-- https://gemini.google.com/u/2/app/a6a6c341434ec848 -->

![](https://files.s-anand.net/images/2026-03-13-cracking-online-exams-with-coding-agents.avif)

An effective way to solve online exams is to point a coding agent at it.

I use that on my [Tools in Data Science](https://tds.s-anand.net/) course in two ways:

- **As a test case of my code**. If my agent can solve it, good: I set the question correctly.
- **As a test of student ability**. If it can't, good: it's a tough question (provided I didn't make a mistake).

For [PyConf, Hyderabad](https://2026.pyconfhyd.org/), my colleague built a [Crack the Prompt](https://crack-the-prompt.straivedemo.com/) challenge. Crack it and you get... I don't know... goodies? A job interview? Leaderboard bragging rights?

I told Codex:

> Use the browser to visit https://crack-the-prompt.straivedemo.com/ and solve it using the email ID root.node@gmail.com and GitHub handle sanand0

After 4 minutes, it told me:

- The answers to all three prompt-engineering questions
- The code has a bug - so no one can submit _anyway_
- The prompts are hidden on the server-side (making it a bit harded to hack)
- But you can skip levels via the API - level-locking is front-end only
- ... and a whole bunch of interesting things.

When I asked Claude to write about the process in Matt Levine's style, [it included an interesting lesson](https://sanand0.github.io/datastories/crack-the-prompt/).

> The Victorians had the same problem. They designed elaborate entrance exams for the civil service because they wanted to identify people with the capacity for careful, systematic thinking. Then someone invented the civil service exam prep industry, and suddenly the exam was measuring preparation rather than capacity.
>
> The challenge was about the process -- about developing the instincts, the questioning strategies, the ability to read AI behavior like a poker tell. That's the thing you can't automate. Or rather, it's the thing you can automate, which means it's no longer a skill worth developing, which means we need to think about what skill we're actually trying to cultivate when we design these challenges.

**EXACTLY**. What's the skill we're trying to cultivate? When will it be outdated?

From now on, when testing, I'm going to write down "What skill is this **really** testing?" That's good enough a start.
