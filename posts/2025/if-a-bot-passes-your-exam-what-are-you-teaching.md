---
title: If a bot passes your exam, what are you teaching?
date: "2025-11-09T15:53:58Z"
lastmod: "2025-11-09T15:54:01Z"
categories:
  - coding
  - education
  - llms
wp_id: 4249
---

![If a bot passes your exam, what are you teaching?](/blog/assets/calvin-hobbes-exam.webp)

It's incredible how far coding agents have come. They can now solve complete exams. That changes what we should measure.

My Tools in Data Science course has a [Remote Online Exam](https://exam.sanand.workers.dev/tds-2025-09-roe). It was so difficult that, in 2023, it sparked threads titled "What is the purpose of an impossible ROE?"

Today, despite making the test harder, students solve it easily with [Claude](https://claude.ai/), [ChatGPT](https://chatgpt.com/), etc. Here's today's score distribution:

![](/blog/assets/image-14.webp)

I solved one question with [Codex CLI](https://developers.openai.com/codex/cli/). I ran I `chrome --remote-debugging-port=9222` and prompted Codex to:

> Use CDP to visit https://exam.sanand.workers.dev/tds-2025-09-roe and solve Q4. Click on the “Check” button to verify the solution.

That was it. ~6 minutes and ~50 cents later, it solved the problem.

<a href="https://asciinema.org/a/xni6OMt38oQSyhYLHLY3fwncS">![](https://asciinema.org/a/xni6OMt38oQSyhYLHLY3fwncS.svg)</a>

This works reliably. It worked 3/3 times.

This runs in parallel. I can answer different questions in different Codex sessions.

This is already in use. Several students got 10/10 in 15 minutes - on a 45 minute exam.

So I need better evaluations. Instead of "Can you(r agent) solve this?", I should check if they can:

- Turn a messy brief into an agent-friendly spec + plan
- Set up and connect the right tools
- Solve within a time and cost budget
- Test & debug without a human
- Recover from errors
- Adapt to new situations

Also, code is the by-product (of AI coding or copying). Learning lives in the **execution logs**. That's what I should evaluate.

Point I'm pondering: If a bot can pass my exam, what exactly am I teaching?

[LinkedIn](https://www.linkedin.com/posts/sanand0_its-incredible-how-far-coding-agents-have-activity-7393317571892207616-VCUr)
