---
title: Things I Learned - 20 Jul 2025
date: 2025-07-20T00:00:00+00:00
categories:
  - til
description: I explored Inevitablism and LLM chat interfaces while optimizing my CLI workflow with tools like eza and uv. I also detailed extensive Claude Code features, including memory management, custom slash commands, and integration with Sentry MCP.
tags: [claude-code, cli-tools, uv, mcp]
---

This week, I learned:

- [Inevitablism](https://tomrenner.com/posts/llm-inevitabilism/) is framing an argument as if it is the only logical choice in an inevitable future. Thereafter, the argument shifts to are there any alternative choices in that inevitable world, rather than whether that future is, in fact, inevitable.
- ⭐ LLM chat over data may leapfrog dashboards. This may be a trigger to kill redundant UI.
- A new wave of (liberal) colleges have emerged. Ashoka University, Krea, Plaksha (Mohali), Jindal University (Sonipat), FLAME University (Pune), Azim Premji University, Shiv Nadar University. Many of these accept IB students who are choosing to stay in India, instead of the earlier trend of studying abroad.
- `xh` is `curl`-compatible but adds JSON pretty‑print, colour, `--table` and can pass parameters like `xh post :8000/api question='When is the ROE?'`
- `dasel` is `jq`-compatible but supports YAML and TOML too
- `lazygit` is a 5-MB TUI that lets you stage/commit/push/diff in one screen
- `eza` is a modern `ls` replacement. I switched to this with `abbr --add l 'eza -l -snew --git --time-style relative --no-user --no-permissions --color-scale=size'`
- `jless` is `less` replacement for large JSON streams, with search & scroll
- `jc` is a JSON to table formatter
- `uv cache prune` removes only _unused_ cache entries and saves a fair bit of space. Mine trimmed 85 GB.
- Claude Code settings are in `~/.claude/settings.json` (personal) < `.claude/settings.json` (project) < `.claude/settings.local.json` (uncommitted personal) < CLI arguments. Explore `model`, `permissions`, `env`, `forceLoginMethod`. [Ref](https://docs.anthropic.com/en/docs/claude-code/settings) #ai-coding
- Claude Code loads memory from `~/.claude/CLAUDE.md` < `.CLAUDE.md` and from subdirectories _when required_. Run `/init` to auto-create it with repo-specific info! Mention `@file` to import. Beginning an input with `# ...` adds it to memory! Run `/memory` to view/edit memory files. [Ref](https://docs.anthropic.com/en/docs/claude-code/memory) #ai-coding
- Claude Code lets you type `\` then Enter at the end of a line to continue to the next line. Or, run `/terminal-setup` to bind Shift-Enter to insert a newline. #ai-coding
- Claude Code has built-in tools to read & write Jupyter notebooks (interesting), to run sub-agents (powerful), and to manage TODO lists (useful) [Ref](https://docs.anthropic.com/en/docs/claude-code/settings#tools-available-to-claude) #ai-coding
- `claude -p "query"` runs the query and exits, making it a _very_ powerful pipeline tool. E.g. `cat stream.jsonl | claude -p "..." --output-format json --input-format stream-json --max-turns 3 --dangerously-skip-permissions` [Ref](https://docs.anthropic.com/en/docs/claude-code/cli-reference) #ai-coding
- Claude Code has a `/review` command that requests a code review and a `/pr_comments` to view pull request comments [Ref](https://docs.anthropic.com/en/docs/claude-code/slash-commands) #ai-coding
- Claude Code lets you define custom slash commands at `~/.claude/commands/*.md` < `.claude/commands/*.md`. Use `@file` to reference files, `$ARGUMENTS` for arguments, and `!` for bash commands like `` DIR: !`pwd` ``. YAML frontmatter supports `allowed-tools:` and `description:` [Ref](https://docs.anthropic.com/en/docs/claude-code/slash-commands) #ai-coding
- You can drag & drop a screenshot or paste it into Claude Code! #ai-coding
- Claude Code lets you run `/compact Focus on code samples and API usage` (or mention it in `CLAUDE.md`) #ai-coding
- Claude Code activates extended thinking via these keywords: `think` < `think hard` < `think harder` < `ultrathink` [Ref](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-extended-thinking) #ai-coding
- Claude Code lets you set up [GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions) via `/install-github-app` so that any mention of `@claude` in an issue or a PR will trigger a CI job that does what you suggest. An alternative to [Jules](https://jules.google.com/) or [Codex](https://chatgpt.com/codex) #ai-coding
- Claude Code enterprise use is possible. It works with [Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock) and [Amazon Bedrock](https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock) [securely](https://docs.anthropic.com/en/docs/claude-code/security) and supports [usage monitoring](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage) #ai-coding
- Claude Code supports [proxies](https://docs.anthropic.com/en/docs/claude-code/corporate-proxy) and [LLM gateways](https://docs.anthropic.com/en/docs/claude-code/llm-gateway). The `apiKeyHelper` [setting](https://docs.anthropic.com/en/docs/claude-code/settings) can dynamically generate API keys #ai-coding
- Claude Code costs ~$6/day on average, and < $12/day for 90% of developers. [Ref](https://docs.anthropic.com/en/docs/claude-code/costs) #ai-coding
- [ccusage](https://github.com/ryoppippi/ccusage) summarizes Claude Code usage patterns from `~/.claude/` #ai-coding
- Interesting MCPs to explore:
  - [Sentry](https://mcp.sentry.dev/): fetch issues with stack traces and other useful debugging context
  - [Playwright](https://github.com/microsoft/playwright-mcp): automate browser
- [neomutt](https://github.com/neomutt/neomutt) is a convenient way for me to read my archived `.mbox` files. `neomutt -f $FILE.mbox` lets you browse an MBOX.
- IITM DoMS is a management school inside a technical institute. That lets MBA students learn to interact with geeks and create startups.
- Last year, LLMs were able to solve 3 JEE problems. This year, they were all-India Rank #4, and then beat AIR #1.
- India has 3% electric vehicle penetration. The highest (perhaps Norway) is 80%. The Indian Government is actively looking to phase in EVs. Charging points are being installed across the country.
