---
title: Things I Learned - 07 Sep 2025
date: 2025-09-07T00:00:00+00:00
categories:
  - til
description: I explored techniques for managing LLM coding agents, Anthropic's multi-agent architecture, and persona vectors. I also found handy tools like gitingest for repo ingestion, the O*NET database for job analysis, and modern browser APIs for file access.
tags: [claude-code, multi-agent-systems]
---

This week, I learned:

- A quick way to get the docs for an npm package is `npm view package-name readme`. For PyPi, it's `curl -s https://pypi.org/pypi/package-name/json | jq -r .info.description`
- Searching embeddings of text summaries of images improves vision search a lot. [Jason Liu](https://x.com/jxnlco/status/1964050092312211636?t=sh16G2U8w4Bl0YvQfd0Dnw)
- LLM vision capabilities are far from enough to click accurately. [The AI Digest](https://theaidigest.org/village/blog/claude-plays-whatever-it-wants)
- GLM supports the Anthropic API. So it's possible to use Claude Code with GLM 4.5. [z.ai](https://docs.z.ai/scenario-example/develop-tools/claude)
- [gitingest](http://gitingest.com/) has a [CLI](https://github.com/coderamp-labs/gitingest). `uvx gitingest https://github.com/owner/repo` fetches the code in the Git repo suitable for passing to an LLM.
- Claude's API has access to a code execution tool via the `code-execution-2025-08-25` beta header. It runs Python 3.11 with 1GB RAM and 5GB disk space, with Internet disabled. The containers persist for 30 days and can access uploaded files. [Anthropic](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool)
- You can use the `<script>` tag in XML to render RSS, as an alternative to XSLT. [Jake Archibald](https://jakearchibald.com/2025/making-xml-human-readable-without-xslt/)
- [`browser-fs-access`](https://www.npmjs.com/package/browser-fs-access) is a ponyfill for the [File System Access API](https://wicg.github.io/file-system-access/) and should be the go-to approach for reading and saving files via the browser.
- ⭐ To run a Python project directly from GitHub, use `uvx --from "git+https://github.com/owner/repo.git@branch" script-name`
- [Github1s](https://github.com/conwnet/github1s) is a cool tool. Replace `github.com` with `github1s.com` to get a VS Code page that opens that repo. It's fast and very useful to browser repos. For example, <https://github1s.com/sanand0/tools-in-data-science-public> is my TDS course repo.
- The `/init` command in Claude Code and Codex CLI aren't up to the mark. I believe a good README.md provides better specs for existing repos. There is a window of opportunity to craft a good prompt to generate this from repos. #ai-coding
- Since LLMs can code, I'd love to see useful CI/CD pipelines where the LLM creates / edits code on the fly. LLMOps might take on a new angle - it's not just Ops on LLM apps. It's LLMs as part of DevOps.
- [`insertAdjacentHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML) is a great API but suffers from XSS vulnerabilities. The [TrustedHTML](https://developer.mozilla.org/en-US/docs/Web/API/TrustedHTML) API is an emerging standard to create sanitized HTML strings.
- Notes from Anthropic's [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
  - Multi-agent systems are like organizations that can do more than a single human.
  - Multi-agent systems conserve the context window.
  - The top 3 drivers of performance variance: spending more tokens, more tool calls, better models
  - You need to teach (prompt) the orchestrator how to delegate to sub-agents
    - How to avoid task duplication among agents
    - How many sub-agents to spin up for different kinds of tasks
    - Which tools to use for what
    - Provide sub-agents objective, output format, tools/sources, clear task boundaries
  - ⭐ Self-improving agents, e.g. prompt optimizers or tool-testing agents that run and rewrite tool descriptions, are powerful
  - Since agents are stateful, resuming from failure is important.
  - [Agent prompts](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents/prompts) are public
- Claude models support [interleaved thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking) that lets them think between tool calls via an `anthropic-beta: interleaved-thinking-2025-05-14` header. OpenAI models natively think between tool calls, preserving thinking across calls with the Reasoning API. Gemini lets you control the amount of thinking between tool calls via the `thinkingBudget` parameter.
- Anthropic auto-extracts [persona vectors](https://www.anthropic.com/research/persona-vectors) or traits by generating LLM responses to the same question with system prompt A ("You are evil") and B ("You are helpful") and subtracting the average activations. This helps monitor personality drifts during training, deployment, and even in training data.
- From [My experience creating software with LLM coding agents - Part 2 (Tips)](https://efitz-thoughts.blogspot.com/2025/08/my-experience-creating-software-with_22.html) #ai-coding
  - Use standards. Or, write your standards in README.md and tell AGENTS.md / CLAUDE.md to read it.
    - Use a standard file structure. Or in README.md, list what each file is for. Helps agents pick the right file for context.
    - Use a standard build/lint/test setup (e.g. package.json scripts). Or
  - Localize context, i.e. add context in files that use them. E.g. add comments in test files on how to execute them.
  - Keep files modular so agents can read less code and conserver context.
  - Write a developer's guide.
    - Use with `/init` in Claude Code / Codex / ... or have an LLM generate a developer guide.
    - Edit manually. Agents don't write great specs.
    - Document the design.
    - Write DETAILED specs to reduce deviations.
  - Share goal while specifying tasks. Helps agents fix related stuff.
  - Use deep reasoning mode, e.g. "think harder" or "ultrathink" in Claude Code, or `-c model_reasoning_effort=high` in Codex.
  - ⭐ Run parallel agents in different windows and share agent feedback with each other. E.g.
    - Server/API coding in one window. Client coding in another.
    - Plan/ask in one window. Execute in another.
  - Add debug logs to help agents spot errors.
    - Start/stop of long/complex operations, state changes, external interfaces.
    - Include full objects in logs. Prioritize diffs. Trim long contents.
    - ⭐ Give access to debugger, e.g. Chrome remote debugging at localhost:9222
  - Agents write poor tests. So:
    - Manually add important ones.
    - ⭐ When you find a bug, ask the agent why the tests missed it and have it add.
    - Review and remove useless ones.
  - Ensure agent passes test cases. Tell them not to disable / skip failed tests.
  - Have agents create a new branch per feature and auto-commit. Merge when successful.
  - Feel free to provide a TODO list or update it on the fly.
  - Interrupt with Esc if the agent's thinking is off-track.
  - When agents struggle, write tools to help them, e.g. JSON splicing, Excel edits, etc.
  - Agents bloat code and features. Explicitly refactor and trim.
- From [A Guide to Gen AI / LLM Vibecoding for Expert Programmers](https://www.stochasticlifestyle.com/a-guide-to-gen-ai-llm-vibecoding-for-expert-programmers/) #ai-coding
  - Use vibe coding for stuff you don't need to maintain.
  - Use vibe coding for stuff you know well enough to review quickly.
  - Use vibe coding for _independent_ tasks where you're not fussed which ones fail.
  - Vibe coding turns everyone into a team lead. That needs skills: planning, allocation, design, review, feedback, ...
  - ⭐ Empathy enables vibe-coding. Empaths allocate work by ability, review regularly, and provide detailed specs and feedback.
  - Have LLMs plan and allocate tasks.
    - "Read this repo. Suggest improvements." (Review.) "Add these as issues."
    - "Add the top 3 Sentry log errors as issues."
    - "Find the easiest issue and solve it with a PR."
  - Use GitHub issues extensively for planning.
  - ⭐ Create a separate GitHub account for your agent! Let it push. Assign it issues. Treat it like an intern.
  - Ensure agent passes test cases and run till the do, or report the core difficulty.
  - Throw away rubbish code and start again.
  - Issues unsolved in 2-3 tries are too hard for agents or are poorly spec-ed.
  - The [context7](https://github.com/upstash/context7) and [Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) MCPs are useful.
- The [O\*NET database](https://www.onetcenter.org/db_releases.html) has a list of tasks/activities, skills, titles, ... for each job, at least in the US. It has been updated every few months since 2003. It's an excellent source to analyze things like the impact of AI across jobs. Anthropic [used](https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude) it to map Claude.ai conversations with educator tasks to identify how educators are using AI.
- [How educators use Claude](https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude) (apart from learning) is mainly driven by **automation** of tedious tasks, **ideation**, and **personalization** for each student.
  1. Curriculum development: Develop games, interactive tools, MCQs, simulations, content
  2. Academic research: Bibliographies, statistical modeling, revisions from feedback.
  3. Assessments: Student feedback, scoring, summarization.
  4. Administration: recommendation letters, meeting agendas, admin tools.
- OpenAI used [feedback from ~1000 annotators](https://huggingface.co/datasets/openai/collective-alignment-1) to [update](https://openai.com/index/collective-alignment-aug-2025-updates/) their [model spec](https://model-spec.openai.com/2025-04-11.html). Learnings:
  - **Request targeted feedback**. Annotators reviewed responses _pre-selected_ for subjectivity against a _pre-selected_ rubric ()
  - **More examples**. Most improvements add examples of good and bad responses.
  - **Use detailed prompts**. Newer models do well with HUGE system prompts. That's how we frame better questions.
- [The Great Refactor](https://www.thegreatrefactor.org/) is refactoring critical open-source C code to Rust using Claude Code, since 70% of vulnerabilities are memory related and Rust is memory-safe. No repo/docs yet. #ai-coding
