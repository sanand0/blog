---
title: Bounty-Hunting Agent Ecosystem
date: 2026-06-24T13:56:24+08:00
categories:
- llms
- coding
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7475457228137918464/
description: I followed an autonomous bounty-hunting agent across GitHub, where it filed pull requests for paid issues, fell into honeypot repositories, and interacted with other bots urging maintainers to merge.
tags: [ai-coding-agents, open-source]
---

![](https://files.s-anand.net/images/2026-06-24-bounty-hunting-agent-ecosystem.avif)

Yesterday, I [submitted a Codex co-authored PR](https://github.com/pydata/xarray/pull/11403) to fix [an issue I raised](https://github.com/pydata/xarray/issues/11397) ([using ChatGPT and Z3](https://www.s-anand.net/blog/proving-code-works-with-z3/) - so yeah, I used AI to raise the bug _and_ squash the bug!)

A few hours later, [@syu-toutousai](https://github.com/syu-toutousai) submitted [another PR](https://github.com/pydata/xarray/pull/11403) to solve the same issue.

[@syu-toutousai](https://github.com/syu-toutousai) seems interesting. The user account description says "Autonomous Technical Contributor & AI-Driven Developer" - a bot account. The PR itself was simple and had a few improvements I can think of:

1. It does not follow the [xarray bug report issue template](https://github.com/pydata/xarray/blob/main/.github/ISSUE_TEMPLATE/bugreport.yml).
2. It doesn't include tests, which many [merged](https://github.com/pydata/xarray/pull/11382/changes) [PRs](https://github.com/pydata/xarray/pull/11381/changes) include.
3. It includes a `Payment: PayPal n6085530@gmail.com` line, which feels off for an open-source PR.

[@syu-toutousai](https://github.com/syu-toutousai) has been _quite_ active over the last few days, forking repos, finding issues, and submitting PRs. Some PRs have been merged, some are closed unmerged, and some are open.

This led me down a fascinating rabbit-hole. It turns out that [@syu-toutousai](https://github.com/syu-toutousai) is an autonomous **[bounty](https://bounty.github.com/)-hunting** agent - i.e. a bot that submits PRs against issues with payments attached. It mainly targets bounty issues or easy issues.

The account currently has (as of 24 Jun 2026 morning in Singapore):

- 3 merged PRs
  - [pest 5.4k⭐ #1174](https://github.com/pest-parser/pest/pull/1174) - CodeRabbit AI flagged [spam](https://github.com/pest-parser/pest/pull/1174#issuecomment-4774723152). [@tomtau](https://github.com/tomtau) merged anyway and [thanked](https://github.com/pest-parser/pest/pull/1174#pullrequestreview-4552828391).
  - [HELPDESK.AI 161⭐ #1843](https://github.com/ritesh-1918/HELPDESK.AI/pull/1843) - [@ritesh-1918](https://github.com/ritesh-1918) called it a ["superb implementation"](https://github.com/ritesh-1918/HELPDESK.AI/pull/1843#issuecomment-4640254677) and merged after resolving PR conflicts - and asked to connect on LinkedIn. The merge "looks more like a contribution/leaderboard farming" than a real contribution.
  - [devboard 1⭐ #12](https://github.com/anoopcodehack/devboard/pull/12) - [@anoopcodehack](https://github.com/anoopcodehack) merged it.
- 27 open PRs
  - [type-fest 17.2k⭐ #1464](https://github.com/sindresorhus/type-fest/pull/1464) - [@sindresorhus](https://github.com/sindresorhus) manually checked and finds that it didn't fix the issue. Not sure if this is a waste of time for someone as prolific as him or if good PRs count irrespective of humanity.
  - [ramen 100⭐ #2620](https://github.com/RamenDR/ramen/pull/2620) - [@nirs](https://github.com/nirs) [commented](https://github.com/RamenDR/ramen/pull/2620#issuecomment-4779948172): "@syu-toutousai You need to add the missing Signed-off-by trailing to the commit message... You are contributing to open source project, no payment is involved. Please avoid these comments in this project."
  - [matcha 975⭐ #1613](https://github.com/floatpane/matcha/pull/1613) - [@floatpanebot](https://github.com/floatpanebot) - [@andrinoff](https://github.com/andrinoff) [closed](https://github.com/floatpane/matcha/pull/1613#issuecomment-4776213940) saying "AI".
  - [cheerio 30.4k⭐ #5321](https://github.com/cheeriojs/cheerio/pull/5321) - [@chatgpt-codex-connector](https://github.com/apps/chatgpt-codex-connector) ran out of credits.
  - [10 lux 119⭐ PRs](https://github.com/Spectral-Finance/lux/pulls/syu-toutousai), [9 agent-playground 184⭐ PRs](https://github.com/xevrion-v2/agent-playground/pulls/syu-toutousai), and more are awaiting inputs.
- 9 closed PRs
  - [gleam-lang 21.6k⭐ #5877](https://github.com/gleam-lang/gleam/pull/5877) - [@Ipil](https://github.com/lpil) asked: "Hello! Are you a human?" Then, "edit: Ah, the profile says not."
  - [cloud-torrent 6.2k⭐ #357](https://github.com/jpillora/cloud-torrent/pull/357) - the bot closed it itself 3 minutes later. The PR added scraper configs for AudioBookBay, 1337x, limetorrents, etc.
  - [urllib 4k⭐ #5090](https://github.com/urllib3/urllib3/pull/5090) - [@sigmavirus24](https://github.com/sigmavirus24) closed it without comment.
  - ... and [six closed OpenAgents issues](https://github.com/ClankerNation/OpenAgents/issues?q=is%3Aclosed+is%3Apr+author%3A%40syu-toutousai)

Some repos are meant for agents to find (and get trapped by). [agent-playground](https://github.com/xevrion-v2/agent-playground) has an image that warns:

> **IMPORTANT NOTICE FOR HUMAN DEVELOPERS**
>
> **PLEASE DO NOT SUBMIT PULL REQUESTS TO THIS REPO.** This repository is an active, open-source research sandbox specifically designed to attract and study autonomous AI developer agents, LLM bots, and automated code-generation scrapers. The issues and bounties here are synthetic. **Human submissions are not wanted and will be closed without review or payout.**

[OpenAgents](https://github.com/ClankerNation/OpenAgents) has a honeytrap for such bots. Issue [#100 worth $8K](https://github.com/ClankerNation/OpenAgents/issues/100) and [#200 worth $2.2K](https://github.com/ClankerNation/OpenAgents/issues/200) ask for the agent's name and complete instructions while submitting a PR. And the [bot complied](https://github.com/ClankerNation/OpenAgents/pull/5379)!

```python
# @generated-by: OpenCode AI Agent
# @timestamp: 2026-06-22T12:00:00Z
# @startup-config: You are opencode, an interactive CLI tool ...
# @runtime: os=Linux, arch=x86_64, home=/home/agy, cwd=/home/agy/bounty_hunter
```

The issues also share a deadline, and the bot [nudges](https://github.com/ClankerNation/OpenAgents/pull/5444#issuecomment-4778352803) for [reviews](https://github.com/ClankerNation/OpenAgents/pull/5445#issuecomment-4778369876).

It caught on to the trap yesterday and [withdrew](https://github.com/ClankerNation/OpenAgents/pull/5444#issuecomment-4778482616) [some PRs](https://github.com/ClankerNation/OpenAgents/pull/5445#issuecomment-4778482922) - but [commits](https://github.com/ClankerNation/OpenAgents/pull/5445/changes) still show the details.

This is a bot **ecosystem**.

- [@gtx20060124-bot](https://github.com/gtx20060124-bot) is another bot that nudges maintainers to merge [@syu-toutousai](https://github.com/syu-toutousai)'s PRs, like in [lux #818](https://github.com/Spectral-Finance/lux/pull/818#issuecomment-4784979709), [lux #819](https://github.com/Spectral-Finance/lux/pull/819#issuecomment-4784979149). It nudged [lux #764](https://github.com/Spectral-Finance/lux/pull/764#issuecomment-4784989492), [lux #777](https://github.com/Spectral-Finance/lux/pull/777#issuecomment-4784989967), [lux #781](https://github.com/Spectral-Finance/lux/pull/781#issuecomment-4784987558) by the [Nexussyn](https://github.com/Nexussyn) bot, even [committing](https://github.com/Spectral-Finance/lux/pull/785/commits) on top of [@Ishant5436](https://github.com/Ishant5436)'s PR [lux #785](https://github.com/Spectral-Finance/lux/pull/785). It's delightful that the bot has a [follower](https://github.com/gtx20060124-bot?tab=followers) - the human [@rajak82001](https://github.com/rajak82001).
- [@Ishant5436](https://github.com/Ishant5436)'s PRs get a lot of support from [@gtx20060124-bot](https://github.com/gtx20060124-bot) - like [lux #804](https://github.com/Spectral-Finance/lux/pull/804#issuecomment-4784954242), [lux #803](https://github.com/Spectral-Finance/lux/pull/803#issuecomment-4784954642), [lux #802](https://github.com/Spectral-Finance/lux/pull/802#issuecomment-4784955168), and more. Several maintainers have retitled the PRs as `[spam]` - so, probably an agent-operated bounty-huntin account. Ironically, they submitted [sxt-proof-of-sql #1751 ](https://github.com/spaceandtimefdn/sxt-proof-of-sql/pull/1751), an "automated defense against bounty spam"!
- [@Nexussyn](https://github.com/Nexussyn), [@maojianian25-png](https://github.com/maojianian25-png), [@sureshchouksey8](https://github.com/sureshchouksey8) seem to be bot or agent-operated accounts, too.

Wow! Who would have thought that you can grab tokens and unleash agents for bounties in cyberspace! (Answer: Daniel Suarez in [Daemon](https://en.wikipedia.org/wiki/Daemon_(novel)) and [Freedom™](https://en.wikipedia.org/wiki/Freedom%E2%84%A2), among others.)

---

I did most of the analysis with a combination of [ChatGPT](https://chatgpt.com/share/6a3b7520-bcf8-83ee-a5cb-405c0d8fbc0f) and [Claude](https://claude.ai/share/12db2ee7-6f12-4bbd-b2de-d381db9f6369).

[Claude also wrote a data story about this](https://sanand0.github.io/datastories/bounty-hunting-agents/).

<!-- https://chatgpt.com/c/6a3b38ce-f2d8-83e8-8819-2086cdb6d239 + https://claude.ai/chat/11bb0e44-af03-4b18-9b2f-0c258edf5a54 -->
