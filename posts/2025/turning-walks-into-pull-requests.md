---
title: Turning Walks into Pull Requests
date: "2025-05-30T05:16:52Z"
lastmod: "2025-05-30T05:16:54Z"
categories:
  - coding
  - llms
wp_id: 4135
---

![Turning Walks into Pull Requests](/blog/assets/jules.webp)

In the last few days, I'm coding with [Jules](https://jules.google.com/) (Google's coding agent) while walking.

Here are a few pull requests merged so far:

- [Add features via an issue](https://github.com/sanand0/tools/pull/5)
- [Write test cases](https://github.com/sanand0/saveform/pull/2)
- [Add docs](https://github.com/sanand0/tools/pull/8)

**Why bother?** My commute used to be audiobook time. Great for ideas, useless for deliverables. With ChatGPT, Gemini, Claude.ai, etc. I was able to have them write code, but I still needed to run, test, and deploy. [Jules](https://jules.google.com/) (and tools like [GitHub Copilot Coding Agent](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/), [OpenAI Codex](https://openai.com/index/introducing-codex/), [PR Agent](https://github.com/qodo-ai/pr-agent), etc. which are not currently free for everyone) lets you chat clone a repo, write code in a new branch, test it, and push. I can deploy that with a click.

Fifteen minutes into yesterday's walk I realised I'd shipped more code than in an hour at my desk (even with LLMs)!

**Workflow**

1. Open [Jules](https://jules.google.com/) via browser on phone, connect wired headset.
2. **Prompt** (by typing or speaking) the change to make. It reads the repo, creates a plan and writes code.
3. It runs any existing test suites in a sandbox. Repeats until all tests pass.
4. I have it publish a branch, go to [GitHub Mobile](https://github.com/mobile) and create a PR.
5. Back home, I review the output and merge.

There are 3 kinds of uses I've put it to.

**#1. [Documentation](https://github.com/sanand0/tools/pull/8)** is the easiest. Low risk, high quality, boring task. Here's a sample prompt:

> This repo has multiple directories, each with their own standalone single page application tools.
>
> If a directory does not have a README.md, add a concise, clear, USEFUL, tersely worded one covering what the tool does, the various real life use cases, and how it works.
>
> If a readme already exists, do NOT delete any information. Prefix this new information at the start.
>
> Avoid repeating information across multiple README files. Consolidated such information into the root directory readme.
>
> In the root directory README, also include links to each tool directory as a list, explaining in a single sentence what the tool does.

**#2. [Testing](https://github.com/sanand0/saveform/pull/2)** is the next best. Low risk, medium quality, boring task. Here's an example:

> Run the tests in this repo. Go through the code and see what parts of the code are not covered. Understand the logic and see what kinds of user scenarios are not covered. Add test cases to cover these in the same style as the existing code.
>
> Write MINIMAL, ELEGANT code.

**#3. [Coding](https://github.com/sanand0/tools/pull/5)** may not be the best suited for this. High risk, medium quality, and interesting. But here's a sample prompt:

> Fix <https://github.com/sanand0/tools/issues/3>
>
> - Allow the user to enter just the GitHub @username, e.g. @sanand0 apart from the URL
> - Add crisp documentation at the start explaining what the app does
> - Only display html\_url (as a link), avatar\_url (as an image), name, company, blog, location, email, hireable, bio, twitter\_username, public\_repos, public\_gists, followers, following, created\_at, updated\_at
> - Format dates like Wed 28 May 2025. Format numbers with commas. Add links to blog, twitter\_username, email
> - Add "Download CSV" and "Copy to Excel" buttons similar to the json2csv/ tool

Automated tests are a great way to reduce AI coding risk, as [Simon Willison suggests](https://simonwillison.net/2025/May/28/automated-tests/). I need to do more of this!

**Wins & Losses**

- **Good**: 1 walk = one merged PR. Even with LLMs, it used to take me 2 hours. Now, it's about half an hour of reclaimed walking "dead time".
- **Good**: Test-first prompting caught a sneaky race condition I’d have missed.
- **Bad**: Told Jules “add docs” without saying “don’t overwrite existing.” It politely destroyed my README. Manual revert ensued.
- **Bad**: Front-end tasks need visual QA; I'm still hunting for a zero-setup UAT preview on mobile.

The industry echoes the pattern: GitHub’s new Copilot agent submits draft PRs behind branch protections [1]; Sweep auto-fixes small tickets but can over-touch files [2]; Microsoft’s own engineers found agents flailed on complex bug fixes [3].

**But…**

- **Isn’t this risky?** Maybe. Branch protections, CI, and human review stay intact. Agents are like a noisy junior devs who never sleep.
- **Is the diff readable?** If not, I have it retry, write more reviewable diffs, and explain clearly in comments & commit messages.
- **Does it have enough context?** I add all the context clearly in the issue or the prompt. That can take some research.
- **Security?** The agents run inside repos you give it access. Prompt injection and exfiltration **are** possible risks, but **only** if it accesses external code / websites.

**How to start**

1. Pick a low-stakes repo with solid tests.
2. Pick an agent. [Jules](https://jules.google.com/) has 5 tasks/day free for now. Or pay and use [GitHub Copilot Coding Agent](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/), [OpenAI Codex](https://openai.com/index/introducing-codex/), etc. Or self-host [PR Agent](https://github.com/qodo-ai/pr-agent), etc.
3. Write a failing test.
4. Go for a walk and talk.
5. Merge (or laugh) on return.
