---
title: Things I Learned - 27 Jul 2025
date: 2025-07-27T00:00:00+00:00
categories:
  - til
description: I evaluated my data science skills against O3, built an image tool using Codex, and explored India's tech community builders. I also learned about DuckDB’s embedding joins, GitHub Sponsors Explore, and the 'udm=14' trick for clean Google searches.
tags: [duckdb, codex, o3, india]
---

This week, I learned:

- Here are some tech community builders in India. [ChatGPT](https://chatgpt.com/share/688787c8-a0b0-800c-8be1-0c18a9c4f23e)
  - Atul Chitnis (Bengaluru) – FOSS.IN and Linux Bangalore
  - Dr. Nagarjuna G. (Mumbai) – FSF India and ILUG Bombay
  - Rushabh Mehta (Mumbai) – FOSS United & ERPNext Community
  - Kiran Jonnalagadda & Zainab Bawa (Bengaluru) – HasGeek Tech Conferences
  - Kenneth Gonsalves (Nilgiris/Tamil Nadu) – Indian Python Community (deceased)
  - Thejesh GN (Bengaluru) – DataMeet Open Data Community
  - Varun Aggarwal (Delhi) – ML-India (Machine Learning Forum)
  - Prashant Sahu (Pune) – Pune AI Meetup
  - Akshay Dashrath (Bengaluru) – BlrDroid Android Group
  - Vikrant Singh (Bangalore) – ReactJS
  - Sankarshan Mukhopadhyay – Mozilla India and Wikimedia tech outreach
  - Neependra Khare (Bengaluru) – Docker/Kubernetes Meetup
  - Atul Jha (Bengaluru/Hyderabad) – OpenStack & CNCF Communities
  - Aseem Jakhar & Ajit Hatti (Delhi/Pune) – null Open Security Community
  - Rohit Srivastwa (Pune) – ClubHack and Hackerspaces
  - Anubha Maneshwar (Nagpur) – GirlScript Developer Network
- Digital Public Infrastructure initiatives in India scale if there's a clear use case _and_ centralized orchestration. [Prof R Srinivasan](https://newsletter.iimbaa.com/from-upi-to-ondc-the-role-of-centralised-orchestration-in-dpi-success/)
- The distance between the end of the thumb and little finger, when fullet stretched, is ~9 inches. Between the thumb and pointer, when at a right angle, is ~6 inches. I checked this today - and it's right. A useful rule of thumb for measurement - literally. [Vasuki](https://www.linkedin.com/in/vasuki-seshadri/), ~1985
- [GitHub Sponsors Explore](https://github.com/sponsors/explore) shows you which developers code most of your dependencies. You can sponsor them. I sponsored [isaacs](https://github.com/sponsors/isaacs) who maintains [node-tap](https://node-tap.org/) and [sindresorhus](https://github.com/sponsors/sindresorhus) who maintains several NodeJS packages for $50/month each.
- [markmap](https://markmap.js.org/) looks like a promising JS-based interactive mindmap from Markdown. More interactive than [Mermaid Mindmap](https://docs.mermaidchart.com/mermaid-oss/syntax/mindmap.html#an-example-of-a-mindmap).
  - [mind-elixir](https://github.com/ssshooter/mind-elixir-core) is another option that lets you edit mindmaps and serialize in its own format
  - [jsmind](https://github.com/hizzgdev/jsmind) is yet another but docs are in Chinese
  - [elkjs](https://github.com/kieler/elkjs) seems a good option for laying out nodes in an architecture-style flow diagram
- ⭐ O3 seems a better data scientist than I am. [Based on my Google Searches](https://sanand0.github.io/datastories/google-searches/), I have 3 persona: developer, AI-builder, and India/Singapore geo-culturist. A great example of an analysis from O3 that's better than anything I could have come up with. [ChatGPT](https://chatgpt.com/share/6883b1eb-dc14-800c-8be8-87cb559e69e2)
- ⭐ Fast review of AI be a powerful skill _and_ enabler. I built an [Image Editing tool](https://tools.s-anand.net/imagegen/) with [Codex](https://chatgpt.com/s/cd_6885abae24a0819195e7536480909260) in ~4 hours, with 11 prompts taking 3.5 - 7.5 minutes each. 3 hours human review, 1 hour LLM coding. I'm 3X slower at reviews while AI will keep improving. [ChatGPT: Faster LLM review techniques](https://chatgpt.com/share/6885b832-3d00-800c-87eb-7e49f8999c8d) #ai-coding
  - Auditize: citations, rationale, output screens, diffs, test results, risks, unknowns
  - Auto validate. Evals, tests
  - Prioritize. High z-values, big-useful-surprising areas
- At the [VizChitra Birds of a Feature session](https://hasgeek.com/VizChitra/2025/schedule/whose-analysis-is-it-anyway-the-role-of-ai-and-humans-in-data-analysis-and-visualization-XvyZtNt5RsAhTENMsQvFLj), here's what people said AI enables:
  - Complementary skills enable a team of 1. Non-coders can code. Non-domain people get insights from data
  - Solves starting trouble. It offers a first draft
  - Generation. New ideas (reduces blind spots), scenarios, non-existent people, new data, new persona for surveys
  - Hyper-personalization. Parts of YouTube relevant for THIS asset manager. Implication of data for _me_
  - Automated scaling. Generate 1,000 images. Evaluate 1,000 assignments
  - Saves time: debugging, research, validation, documentation, copywriting
  - New ways of working. Loading event schedules into my calendar
- [Qwen-Code](https://github.com/QwenLM/qwen-code) is a fork of Gemini CLI and uses [qwen3-coder](https://github.com/QwenLM/Qwen3-Coder) -- a model that can also be used with Claude Code and Cline. The model is not anywhere near as good as Claude 4 Sonnet. The app is costlier than using Claude Code directly. #ai-coding
- The LLM industry seems to have matured quickly. Early adopters who are open to understand the generic capabilities of LLMs through demos are somewhat saturated. The early majority have come in. They aren't interested in generic capabilities. They're looking for solutions that solve _their_ specific problem. Soon the late majority will come in asking for _existing_ solutions that have already solved their problem for many others. [ChatGPT: Creating demos for majority](https://chatgpt.com/share/6885b87b-b30c-800c-8c4e-a5c4218b9906)
- [Claude for Financial Services](https://www.anthropic.com/solutions/financial-services) is an agentic version of Claude available on AWS & Google marketplaces tuned for financial services analysis. [Video](https://youtu.be/5zd7m3Rh5B0)
- [catbox.moe](https://catbox.moe/) is a file hosting service that you can upload a file to without any API key. It's an alternative to [0x0.st](https://0x0.st/). Both can be used for images. Catbox retains files indefinitely and openly publishes costs - might last longer. 0x0 deletes files between 1-12 months based on size.
- Agents face 3 problems: compounding errors, quadratic costs, and poorly designed tools. Start with small scope & strong reviews while you solve these problems. [Betting Against Agents](https://utkarshkanwat.com/writing/betting-against-agents/)
- **Leadership and vision will matter more**. LLMs iterate fast. They can think for longer. So tasks where people need to work longer independently than LLMs can are what humans will be needed for. That requires understanding the objective. So leadership and specifically vision transfer will become more valuable. You need to be able to tell people what to do well enough that they can work independently for _weeks_.
- Having LLMs go through engineering drawings, floor plans, etc. and understand them, find problems, etc. is an emerging use case. People are using Veo 3 to convert a floor plan into a 3D walk through too.
- Digital adoption is slow partly because of a skill gap. "Old-timers" are slow to let go of traditional approaches.
- Video recordings are used in manufacturing to evaluate quality (e.g. wafer inspection, assembly inspection, component presence) using AI. An interesting by-product of this data is that they can also measure productivity, task time.
- "Common sense is a specialization". That's something I said accidentally when seeing that some schools/colleges tend to produce more broad, sensible thinkers (e.g. Naval College @ Goa) while others produce more narrow-thinking specialists (e.g. engineering colleges).
- Three groups control the financial economy. To sell sustainability services, you need to have sold to one of them. via [Sundeep](https://www.linkedin.com/in/sundeeprm/)
  1. Banks, who will sell a loan against anything they can insure, and look to insurers for long-term thought leadership.
  2. Insurers, who will insure anything they can re-insure, and re-insurers, who look at real-estate trends as a stable long-term asset
  3. REITs who own the majority of the world's real-estate
- We could think of a copilot as an (agentic) LLM chat interface for an artifact. E.g. Code pilot (Claude Code. Cursor.). Data analysis copilot (Google Colab, sort-of. ChatGPT). That allows us to imagine tools that will create/edit artifacts. Here are some I've encountered as a demand.
  - Documents. E.g. Docsearch, GPTs, Microsoft Copilot, Gemini
  - Slides. E.g. Microsoft Copilot, Gemini
  - Sheets. E.g. Microsoft Copilot, Gemini
  - Code. E.g. Cursor, Claude Code
  - Database. Create DB schema, ER diagrams, synthetic data, ingestion scripts, etc.
  - Data (analysis). E.g. Datachat, Google Colab, Marimo
  - Posters. E.g. Postgen
  - Shell. E.g. Warp
  - Topic modeling. E.g. classify
  - Surveys. E.g. Personagen
  - APIs. E.g. [apiagent](https://sanand0.github.io/apiagent/)
  - Drug regulatory submissions.
  - Contracts (risk).
  - Manufacturing SOPs.
  - Curriculum.
  - Data quality.
  - Support tickets.
  - Dashboards.
  - IaaC / DevOps.
  - Video campaigns.
  - Resumes.
  - Patents.
- CLI optimization for LLMs will likely emerge. More CLIs (and wrappers / hooks in the shell) will improve output and error contexts for LLMs, e.g. printing current directory, caching slow outputs, suggesting alternate commands, etc. [Ref](https://www.notcheckmark.com/2025/07/rethinking-cli-interfaces-for-ai/)
- Frequent commits with linting & building seems like a good AI coding strategy, especially for Claude Code. [Ref](https://www.notcheckmark.com/2025/07/rethinking-cli-interfaces-for-ai/) #ai-coding
  > To keep Claude Code in line on my project, I’ve relied heavily on linters, build scripts, formatters, and git commit hooks.
  > It’s pretty easy to get Claude Code to commit often by including it in your CLAUDE.md, but it often likes to ignore other commands like “make sure the build doesn’t fail” and “fix any failing tests”.
  > All my projects have a .git/hooks/pre-commit script that enforces project standards. The hook works really well to keep things in line.
- Google Apps Scripts are actually a web apps platform in JavaScript more than a macros equivalent. [Ref](https://github.com/tanaikech/taking-advantage-of-Web-Apps-with-google-apps-script)
- ⭐ DuckDB supports joins based on embedding similarity and even hybrid similarity! [Ref](https://duckdb.org/2025/06/13/text-analytics.html)
- Human persuasion techniques like Cialdini's work well with LLMs [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3luawqzljzc2d)
- [gitwatch](https://github.com/gitwatch/gitwatch) is a clean way of auto-committing & pushing files into GitHub. It effectively converts GitHub into a Dropbox-like service.
- Adding [`?udm=14`](https://udm14.com/) to Google Search URLs removes AI mode and other clutter. [Ref](https://tedium.co/2024/05/17/google-web-search-make-default/)
- ⭐ Never embed LLM‑generated summaries without a disclaimer, source links, and flag‑as‑wrong feedback button. Build a fast appeal/edit pipeline _before_ release. via [Death By AI](https://news.ycombinator.com/item?id=44615801)
