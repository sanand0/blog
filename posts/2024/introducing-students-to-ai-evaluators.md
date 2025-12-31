---
title: Introducing Students to AI Evaluators
date: "2024-11-29T04:14:07Z"
lastmod: "2024-11-29T04:14:09Z"
categories:
  - links
wp_id: 3754
---

![Introducing Students to AI Evaluators](/blog/assets/calvin-alien.webp)

In my [Tools in Data Science course](https://study.iitm.ac.in/ds/course_pages/BSSE2002.html) at IITM, I'm introducing a project that will be evaluated by an LLM.

[Here's the work-in-progress draft of the project](https://github.com/sanand0/tools-in-data-science-public/blob/tds-2023-t3-project2-wip/project-2-automated-analysis.md). It will [eventually appear here](https://github.com/sanand0/tools-in-data-science-public).

> Your task is to:
>
> 1. Write a Python script that uses an LLM to analyze, visualize, and narrate a story from a dataset.
> 2. Convince an LLM that your script and output are of high quality.

The second point is the interesting one. Using the LLM as the evaluator.

**Why are you doing this**? There are over 1,000 students in each term. Manual evaluation is not an option. Multiple choice questions are guessable. Programmatic evaluation takes effort to modify each time. LLMs seem like a good way to get intelligent evaluations with manageable effort.

**Will students accept it**? My guess is yes. The whole **objective** of the project is to convince the LLM. It's not evaluating you. You're tricking it into giving you marks. Sort of like [getting an LLM to say Yes](/blog/hacking-an-obnoxious-unhelpful-llm-to-say-yes/). A lot of educational and corporate evaluations will soon be done by LLMs. I may as well teach students how to game the system early.

**What if it makes mistakes**? I hope it will and we'll learn from it. The students will have the opportunity to test out (and get used to) the randomness in subjective evaluations. I'll have the opportunity to learn how to reduce these mistakes next time.

**What else will YOU learn**? I'm very curious about a whole bunch of things.

1. **How will students prompt it**? What analysis will they apply before passing data to an LLM? Will they ask open-ended or guided questions?
2. **How will they orchestrate the flow**? Will they use a linear flow or non-linear? Will it be deterministic or not?
3. **How will they hack it**? LLMs are very amenable to prompt injection. How will the students try and break out of my prompts?
4. **How will LLMs react to all this**? Where will they do a good job? Where will they fail? Which LLMs would work well in which case?

Since the code (and analysis) will be published on GitHub, I'll share the links. It might prove an interesting dataset in itself for future analysis.
