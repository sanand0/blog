---
title: Using Codex to improve Codex
date: 2026-03-01T18:26:13+08:00
categories:
  - llms
  - tools
---

![](https://files.s-anand.net/images/2026-03-01-using-codex-to-improve-codex.avif)

Instead of learning and applying [new Codex features](https://developers.openai.com/codex/changelog/), I asked it to analyze my sessions and tell me what I'm under-using.

```markdown
I'd like you to analyze my Codex sessions and help me use Codex better.

sessions/ has all my past Codex sessions.

Search online for the OpenAI Codex release notes for the latest features Codex has introduced and read them - from whatever source you find them.

Then, create a comprehensive catalog of Codex features.

Then, analyze my sessions and see which feature I could have used but didn't and make a comprehensive list.

Then summarize which features I should be using more, how, what the benefits are, and with examples from my sessions.

Document these in one or more Markdown files in this directory. Write scripts as required. Commit as you go.
```

It did a thorough job of [listing all the new features](https://github.com/sanand0/datastories/blob/8b7c71230900698ec424ba7e888f4deb74ac6ac6/codex-session-analysis/CODEX_FEATURE_CATALOG.md) and [analyzing my gaps](https://github.com/sanand0/datastories/blob/8b7c71230900698ec424ba7e888f4deb74ac6ac6/codex-session-analysis/CODEX_SESSION_GAP_ANALYSIS.md).

[**Read the full story**](http://sanand0.github.io/datastories/codex-session-analysis/)

Here's the summary: I'm using new models immediately, but not the new features of Codex. For example:

- **Parallel execution**. Yesterday, I ran ~103 tool calls without the new [spawn_agents_on_csv](https://developers.openai.com/codex/changelog/#github-release-290476287) feature from last week, which would have saved a _lot_ of time running in parallel.
- **Permissions**. Last week, I ran a script that asked me for permissions 7 times towards the end. Instead, I could have used `/permissions` to set early permissions.

The best part is that it could just add a few instructions to my `AGENTS.md`:

```markdown
Run multiple independent reads in parallel.
For 20+ tool calls, maintain update_plan throughout.
For long-running commands/tests, delegate via sub-agents and report checkpoints.
If blocked by permissions, ask me concise choices.
If sandbox/config gets in the way, use /permissions and /debug-config early.
```

---

Now, the beauty is that **the tool optimized itself**. I don't even need to learn how to optimize it!
