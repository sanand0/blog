---
title: MCP vs Shell
date: 2026-08-08T07:02:28+05:30
categories:
- llms
description: I tested ChatGPT on large email tasks using its Gmail plugin, a local MCP server, and Codex. The results showed both the value of well-tested tools and agents' ability to loop at scale.
tags: [mcp, command-line, ai-agents, chatgpt]
---

![](https://files.s-anand.net/images/2026-08-08-mcp-vs-shell.avif)

I'm a fan of the [Code Mode approach](https://blog.cloudflare.com/code-mode-mcp/) - i.e. letting agents run code rather than narrow functions. Many people agree: [CircleCI](https://circleci.com/blog/mcp-vs-cli/), [Perplexity](https://palma.ai/blog/mcp-vs-cli-not-the-same-thing), etc. In fact, [mcp2cli](https://github.com/knowsuchagency/mcp2cli) gives MCPs a CLI interface.

I feel the main reason is UNIX composability. I can run CLI commands in a loop, pipe them, etc.

I tested it out on ChatGPT. ChatGPT has an `@Gmail` [Plugin](https://chatgpt.com/features/plugins/). I build a [Local MCP Server](https://github.com/sanand0/scripts/blob/main/mcpserver.py) that exposes my CLIs, including [`gws` (Google Workspace CLI)](https://github.com/googleworkspace/cli). I gave it 3 tasks in a single prompt:

1. **Mailbox-scale commitments**: Using only @SOURCE, scan my work email from the past 6 months. Find every commitment I made that appears to require follow-up.
2. **Communication analytics**: Using only @SOURCE, analyze my work email from the past 12 months. Identify the 20 people I interact with most.
3. **Cross-thread project reconstruction**: Using only @SOURCE, reconstruct everything material about $CLIENT from my email over the past year, including relevant attachments.

The @Gmail plugin did _surprisingly_ well. After 19 minutes:

1. 🟢 It scanned 373 sent messages "containing commitment language", then checked replies, and gave me a prioritized list of 8 items. Good ones.
2. 🔴 It said "I can't do this reliably", but shared a few clusters of relationthips.
3. 🟢 It clearly reconstructed the client timeline.

The @LocalMCP plugin had issues. I'm wrapping `gws` inside a developer MCP plugin, and:

- ChatGPT has to send large files back and forth from `gws` via an MCP interface, rather than just read it.
- ChatGPT's restrictions didn't allow it to read the retrieved files - maybe because it was a developer plugin.

Clearly, I know less and mess up more than I think - better to use well-tested well-maintained tools and interfaces.

But anyway, I said: "ChatGPT, use `codex` on @LocalMCP to process the files from `gws`." That took 39 minutes:

1. 🟢 It scanned far more messages and gave me 10 unresolved items.
2. 🟢 It managed to scan all contacts and give me the top 20.
3. 🟢 It clearly reconstructed the client timeline.

The quality and scale of the latter are certainly better.

But my main learnings is: **don't underestimate agents' ability to loop**! They can iterate for long - mode like code than humans.
