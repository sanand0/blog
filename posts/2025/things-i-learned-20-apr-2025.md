---
title: Things I Learned - 20 Apr 2025
date: 2025-04-20T00:00:00+00:00
categories:
  - til
description: I learned about devcontainers and GitPod for portable coding, OpenAI’s o3/o4 tool capabilities, and Marp’s morphing animations for Markdown slides. My notes also cover zero-day options, financial AI limitations, and practical advice for starting a consultancy.
keywords: [devcontainers, gitpod, marp, openai o3, zero-day options, deepcoder, webcontainers, marimo]
---

This week, I learned:

- The [`devcontainers.json`](https://containers.dev/) spec encapsulates everything you need to get a codebase running for development - as opposed to production. E.g. VS Code extensions, linters, etc.
- Practical use for GitPod are:
  - Make quick edits to repos that are not on your system (e.g. other people's repos, or via others' machines.)
  - Run public workshops with a full coding environment.
  - Give students assignments that have dependencies pre-installed.
  - Collaborate on a work-in-progress codebase with my team.
  - Share POCs with clients or public allowing them to edit it.
  - Allow teams to install remote AI code extensions (e.g. Windsurf) that may be blocked inside the corporate firewall?
- AI coding can teach us new tech. For example I learned that `tqdm.pbar` can print logs while showing progress. It's worth noting such learnings until it becomes a habit. #ai-coding
- If English is the new coding language, should prompts be versioned? Or at least stored, perhaps in a PROMPTS.md? #ai-coding
- `marimo new "prompt"` generates an entire new notebook using your prompt. [Video](https://youtu.be/sXiR5YX-tiE)
- Google Sheets now has an `=AI(prompt, [range])` function [Help](https://support.google.com/docs/answer/15820999)
- [Codex](https://github.com/openai/codex) is more a proof-of-concept for agentic coding than a coding tool. #ai-coding
  - You can't run commands. Only prompts. You need to exit codex to run commands. So you can't use it like a shell, e.g. like [Warp.dev](https://www.warp.dev/).
  - It doesn't index local code. It runs commands to figure out stuff.
  - Code diffs and applying changes are clunky.
  - The output is hard to read with text scrolling.
  - `codex.md` can only handle 32K.
- ⭐ [O3 and O4](https://openai.com/index/introducing-o3-and-o4-mini/) have built-in tool use covering all of OpenAI's tools, including containers. This allows them to manipulate images and natively understand them improving vision capabilities dramatically.
- GPT 4.1 can handle videos
- Notes from discussion with [Balaji T](https://www.linkedin.com/in/balaji1975/):
  - Zero-day options are options that expire on the same day. They are priced low. It's almost just a gamble or a lottery ticket. But since the price is low, retail investors can invest.
  - NIFTY is one of the largest markets for zero day options, surprisingly. There are several college grads who trade writing Python scripts.
  - CoreWeave has taken over all the compute from OpenAI. Though the stock price has fallen, buying CoreWeave is the closest equivalent to buying OpenAI pre-IPO.
  - However, every OpenAI product lost money, despite their 75% discounted compute from Microsoft. (With CoreWeave, the cost would be higher.) So their profitability depends on wiping out competition long-term.
  - For investment research companies (hedge funds, VCs, etc.) increasing the number of companies they research is an advantage. So using AI for research is key. However, the quality of LLMs is too poor for financial analysis accuracy. We need better LLMs for spreadsheet analysis.
  - We suffer from the [Gell-Mann's amnesia effect](https://en.wikipedia.org/wiki/Gell-Mann_amnesia_effect) with LLMs. "You read a newspaper article in your field and find it's rubbish. You turn the paper and believe it's perfectly accurate on the next page".
  - Domain expertise will therefore become even more valuable in the near future.
  - People don't like AI being forced down their throats. MAS is forcing AI down banks whose execs are forcing it down the org. Bankers and analysts are grumbling about this.
- I visited [SUTD InspireCon 2025](https://www.sutd.edu.sg/events-listing/inspirecon-2025/). Here were some exhibits that caught my eye.
  - A path marking app that uses cameras to draw a heatmap of people's walking paths. Popular tracks are redder.
  - Using drones for machine inspection.
  - Portable immigration devices that let you scan passports, face recognition, fingerprint, mic/speakers, etc.
  - Using accelerometer to detect unsafe gait and improve walking habits.
  - UImagine: a web app builder. Interestingly, they used [Webcontainers](https://webcontainers.io/) to run Node in the browser!
  - Training a drone to follow a person
  - Credibility detection via micro facial expressions
  - PitchMe: providing real-time feedback to pitches / presentations
  - Zetesis: a platform for people to ask questions during a lecture or meeting (independent of Zoom, Meet, etc.)
  - Tinyeqn: helps grade student assignments
- The dynamic between domain experts and coders has changed. Now, rather than domain experts pitching ideas to developers who build the apps, developers are creating interfaces that allow the domain experts to shape the app. [Ref](https://www.dbreunig.com/2025/04/10/the-domain-experts-are-drivers.html)
- Since even the cheapest LLMs do a good job of converting unstructured text into a JSON schema, for all practical purposes, adding a full text search on top of any structured API is a trivial exercise. (Of course, it can't handle complex questions but that's what agents are for.) [Ref](https://simonwillison.net/2025/Apr/9/an-llm-query-understanding-service/#atom-everything)
- ⭐ Marp supports [bespoke transitions](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md) which includes morphing animations. This can create a [bar chart race](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#example) just using Markdown!
- Nick Lansley, who I know from my work with Tesco, wrote a great article that includes [advice for aspiring consultants](https://www.linkedin.com/pulse/10-years-ago-today-i-exited-from-my-27-year-career-tesco-nick-lansley-imvde/):
  - Re-connect with ex-colleagues
  - Leave on good terms with your employer
  - Have a 6-12 month financial buffer
  - Hire an accountant / legal advisor to set up your business
  - Focus on what you enjoy
  - Have a 30-second elevator pitch
  - Build a brand with blogs, social media, or talks
  - Create a portfolio to reinforce your skills
- DeepCoder is currently the best 14b coding model, i.e. best if you want to code while on a flight. [Ref](https://www.together.ai/blog/deepcoder) #ai-coding
- `docker model run` can run models. Currently, only on Docker Desktop on Mac [Ref](https://docs.docker.com/desktop/features/model-runner/)
