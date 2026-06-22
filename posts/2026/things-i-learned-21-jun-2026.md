---
title: Things I Learned - 21 Jun 2026
date: 2026-06-21T00:00:00+00:00
categories:
  - til
description: I share techniques for mental closure in conversations and steering AI agents mid-task. I also cover ug search shortcuts, VS Code fixes, and why harness engineering is the new bottleneck for AI quality.
keywords: [ug, codex, harness engineering, mental closure, vs code, git, skill transfer]
---

This week, I learned:

- It doesn't always take time to learn or convey things. (Early trust can be built instantly, e.g. vulnerability.) At first, experts don't know how to make skills explicit. But trainer effort could compress 10X via evals, practice loops, and feedback. Learner elapsed time would compress less. <!-- https://chatgpt.com/c/6a36144d-0d3c-83ee-a149-b8fbdef6b7e1 -->
- Everyone has something worth discovering, but not every conversation is worth my time right now. So, meet new people with trust, attention, and [good questions](https://www.s-anand.net/blog/questions/). Continue if there's emotional / intellectual stimulation (surprising, interesting, moving, connecting, energizing, challenging), else exit warmly with respect. <!-- https://chatgpt.com/c/6a35f088-8554-83e8-aa0f-1b06541c16d4 -->
- To avoid getting overwhelmed in ultra-interesting conversations, mental closure helps. During the conversation, pause, name, reflect, and close. "Wait, you're saying X. I should do Y. I'll reflect/act tonight." or "Wow, let's sit with that for 5 seconds. You mean X. I feel Y. I'll drop." After the conversation, summarize: "What struck me were X1, X2. I'll plan Y1, Y2 and drop Z1, Z2." Then take a short break. <!-- https://chatgpt.com/c/6a35f088-8554-83e8-aa0f-1b06541c16d4 -->
- Setting `"markdown.editor.updateLinksOnPaste.enabled": false` might fix the delay / freezing (infinite spinner) issue when pasting Markdown in VS Code.
- The bottleneck to quality of AI output has shifted from model quality to harness quality (and this is not obvious to many people). It is important, therefore, to optimize harness usage rather than prompts usage, i.e. harness engineering over context engineering.
- I use `ug --smart-case --bool -Q --sort=rtime` to interactively search for text in files. It's like VS Code search-across-files. Here are the shortcuts I find useful:
  - `Alt-g`: Glob (filter files to search in)
  - `Alt-[ or ]`: Decrease or increase context (lines before / after)
  - `Alt-w`: Word match toggle
  - `Alt-c`: Count lines toggle
  - `Alt-u`: Ungroup - show lines once even if multiple matches
- Using AI for health seems to have reached a tipping point. Three people have pitched an idea in this space to me in the last three days.
  One is a managed personal health provider who wants to tie-up with hospitals to gather data to improve AI health advice.
  Second is an enterpreneur who wants to enable the Indian Govt to use AI to improve public health - given the low proportion of trained doctors in public hospitals.
  The third is a colleague who is uploading personal health reports, fitness data, DNA data, wearable data, etc. and suggest daily habits such as fitness, nutrition, sleep, medication, etc. to optimize health.
- Changing the topic (e.g. asking a question) instead of answering a question is powerful. It lets you decline requests, avoid sensitive topics, ignore boring ones, learn rather than teach, and bring in your agenda - all at one shot. I need to un-practice my 40-year habit of answering questions. (This is selfish. I forgive myself.)
- bolt.diy seems like a browser-embeddable coding agent. That is, you can add bolt.diy to your web page and have it build apps. That might be a pretty powerful upgrade to generative UI - where pages build themselves based on the user input. <!-- https://chatgpt.com/c/6a215c52-4cb4-83ec-aeac-f937e3aab34a -->
- Codex has a few new features in the last few months.
  - Codex can generate images and have voice conversations.
  - `/goal` sets an overall session goal to avoid getting side-tracked.
  - `/side` is like Claude Code's `/btw` - for a side task while the main task continues.
  - `/resume` lets you switch to any previous session.
  - `/keymap debug` lets you edit the keymap and inspect what keystrokes the terminal sends.
  - `@` lets you mention files, directories, skills, _and_ plugins.
  - `Ctrl+R` works, lets you pick a previous prompt.
  - `Ctrl+O` copies the last answer as Markdown.
  - Hooks are stable. `PreToolUse` lets you log every tool, `SessionStart` lets you inject repo-specific rules.
  - MCPs with `readOnlyHint` can run in parallel.
  - `codex doctor` diagnoses environment issues.
  - `codex remote-control` lets you remotely control Codex, making it a server.
  - Codex Python SDK is better and you can have Codex run as a back-end more smoothly.
- To change others' behavior, **embody** (not preach) it **visibly** and **consistently**, make it **easy to copy**, and **ask without forcing**. It takes time, though. [ChatGPT](https://chatgpt.com/share/6a35f1ae-27ec-83ee-9e3c-2f079cbff277) <!-- https://chatgpt.com/c/6a35f040-277c-83e8-9e4f-54ac2f28e345 -->
- Governance is how groups keep promises when things (people, incentives, environment, pressure) change. A simple way to explain what governance is to someone who doesn't understand why governance matters, and guide on when it _does not_ matter. <!-- https://chatgpt.com/c/6a32bc0d-9460-83ee-9d9d-de391c5a4282 -->
- Forward Deployed Engineers are the next evolution of data scientists, IMHO. AI can do data science. Data scientists will likely act as the "Human As An Interface" (HaaI) to business, proactively identifying and solving problems - a space business analysts traditionally occupied. Of course, business analysts will likely do the same without needing data scientists to help. But since AI replaces data scientists more than business analysis, I expect that the % of data scientists who become FDEs will be higher than business analysts.
- The value of data exported from software is high. For example, your email, social posts, CRM / HRMS / ERP dumps, service tickets, purchases, notes etc. These let you create a personal / organizational digital brain. Hence proprietary solutions will make exports harder and open solutions will emerge.
- To live-preview any publicly accessible Excel file, you can embed or link to `https://view.officeapps.live.com/op/embed.aspx?src=YOUR-URL`
- The Codex app can now use the browser much better and faster since last week if you enable "Dev mode" [OpenAI](https://x.com/OpenAIDevs/status/2065226355495895521). THis uses CDP - which is more efficient than screenshots - and is something Codex CLI has been doing for many months.
- In Codex, Claude Code, etc. you can submit a prompt _while_ the agent is working to _steer_ it, i.e. after it completes a turn (e.g. a tool call) it will factor in the prompt. You can also queue it. Neither of these is available on ChatGPT or Claude.ai, though it's such an important feature. On ChatGPT, submitting another prompt stops the previous run and the agent continues with the new prompt.
- By default, git uses `~/.config/git/ignore` or `%USERPROFILE%\git\ignore` as the global `.gitignore`. You can override that with `git config --global core.excludesFile PATH`. [StackOverflow](https://stackoverflow.com/questions/7335420/can-i-use-a-global-user-profile-scope-gitignore-file)
