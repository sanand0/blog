---
title: Things I Learned - 12 Jan 2025
date: 2025-01-12T00:00:00+00:00
categories:
  - til
description: I explored measuring developer productivity with DX Core 4, experimented with smolagents and CLIProxyAPI for coding agents, and looked into modern Redis alternatives and the enduring dominance of SQL in the database landscape.
tags: [sql, developer-productivity]
---

This week, I learned:

- [Measuring developer productivity with the DX Core 4](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/) is a framework for measuring developer productivity. It encapsulates other frameworks like DORA, SPACE, and DevEx.
- [Can LLMs write better code if you keep asking them to “write better code?](https://minimaxir.com/2025/01/write-better-code/) A delightful exploration of how Claude 3.5 Sonnet keeps optimizing and adding features to improve code. My takeaway: repeatedly applying a prompt gives us interesting new directions to explore.
- Wednesday comes from Wōdnesdæg - named after Odin (or Woden).
- [CLIProxyAPI](https://help.router-for.me/) seems a good way to allow any CLI coding agent (Codex, Claude Code, etc.) to work with any provider (e.g. Gemini, OpenRouter, etc.) The documentation needs a few more examples, but it's usable.
  - `mise x github:router-for-me/CLIProxyAPI -- cli-proxy-api` starts a local server that proxies requests.
  - Create a [`config.yaml`](https://help.router-for.me/configuration/basic.html), update the keys, and configure your coding agent, e.g. [Codex](https://help.router-for.me/agent-client/codex.html) to use it.
  - It's also a good way to see what prompts are being sent by the various harnesses.
- [smolagents](https://huggingface.co/blog/smolagents) is a new agents library from HuggingFace. It seems simple enough to use.
- [whisper-flow](https://github.com/dimastatz/whisper-flow/) does real-time speech transcription!
- [Switchboard-1](https://catalog.ldc.upenn.edu/LDC97S62) is a labelled audio corpus with ~260 hours of speech. It has ~2,400 calls among 500+ speakers in the US.
- [Cloudflare tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/create-local-tunnel/) is like ngrok but more permanent. It's a bit more complex, too. But given CloudFlare's liberal free tier, it's a good, viable option for long-term local hosting.
- John Wheeler: "We live on an island surrounded by a sea of ignorance. As our island of knowledge grows, so does the shore of our ignorance." A great way to understand how ignorance actually grows as you learn more.
- [`justhtml`](https://pypi.org/project/justhtml) is a fast enough pure Python fully HTML5 compliant library. For a faster, mostly compliant solution, [`html5-parser`](https://pypi.org/project/html5-parser/) with `lxml` works.
- There is little reason to use Redis. There are several clones you can use. [Databases in 2024: A Year in Review](https://www.cs.cmu.edu/~pavlo/blog/2025/01/2024-databases-retrospective.html)
  - [Microsoft's Garnet](https://microsoft.github.io/garnet/)
  - [KeyDB](https://docs.keydb.dev/) (only Linux)
  - [ValKey](https://valkey.io/) (only source)
  - [DragonFly](https://www.dragonflydb.io/) (only Linux)
  - [ReDict](https://redict.io/) (only Linux)
- Every few years, something comes along trying to replace relational databases and SQL, and gets absorbed. [YouTube](https://youtu.be/8Woy5I511L8)
  - Key value stores. People soon realize they need more features, e.g. indices.
  - MapReduce systems. Most MapReduce vendors put SQL on top of SQL. Then the Hadoop market crashed. (But HDFS, S3, distributed storage systems are a good idea)
  - Document Databases. JSON. SQL absorbed that. SQLite 3.45+ supports even JSONB. DuckDB, of course, has JSON.
  - Column Databases. Again, these introduced SQL.
  - Graph Databases. SQL:2023 introduced graph queries via SQL/PGQ (Property Graph Queries). DuckPGQ beats Neo4J
  - Array Databases. SQL:2023 adds SQL/MDA which allows for matrix operations. But specialized databases might make sense in this category.
  - Vector Databases. Every DB is adding support for this.
- [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany) is a benchmark of real-world [tasks](https://github.com/TheAgentCompany/TheAgentCompany/tree/main/workspaces/tasks) like:
  - [Arranging a meeting room](https://github.com/TheAgentCompany/TheAgentCompany/blob/main/workspaces/tasks/admin-arrange-meeting-rooms/task.md)
  - [Analyze a spreadsheet](https://github.com/TheAgentCompany/TheAgentCompany/blob/main/workspaces/tasks/ds-answer-spreadsheet-questions/task.md)
  - [Add a Gitlab wiki page](https://github.com/TheAgentCompany/TheAgentCompany/blob/main/workspaces/tasks/sde-add-wiki-page/task.md)
- Salvatore Sanfilippo (antirez - Redis) finds DeepSeek v3 comparable with Claude 3.5 Sonnet. [YouTube](https://www.youtube.com/watch?v=_pLlet9Jrzc)
  - He also passed a paper and his code to compare them. A useful prompt. [YouTube](https://youtube.com/clip/Ugkx3JUGaspeLA2U2U68zSRyB2rPJ-PnCUXR?si=xCoIu5bxaFntSymm)
