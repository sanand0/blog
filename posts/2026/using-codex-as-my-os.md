---
title: Using Codex as my OS
date: 2026-04-23T21:06:28-04:00
categories:
- llms
- coding
description: 'I use Codex as an operating system: it installs and runs programs, then debugs configuration failures itself. When my WhatsApp scraper broke after a UI change, Codex found and fixed the parser.'
tags: [operating-systems, ai-coding-agents, codex, agentic-workflows]
---

Increasingly, I'm using Codex (or other AI coding agents) as the "operating system" to run programs. That is, rather than directly run programs, I have the coding agent run the program.

Advantage: If the program breaks, or needs a configuration change, the coding agent debugs it and fixes it. I don't need to do anything.

This is particularly useful for installation. For example:

> Install demucs and run it against my music folder.

It's also useful for brittle scripts. When my WhatsApp scraper broke, I told Codex:

> The scraper was working fine but today, it fails. Find out what changed in the WhatsApp Web UI and fix it.

Codex researched and replied:

> The current scraper still finds the chat area and message rows, but its row-identity parser is now invalid. On March 28 the code assumed each message node had a packed `data-id` like:
>
> ```text
> true_<chat-id>@..._<message-id>
> false_<chat-id>@..._<message-id>
> ```
>
> Today, in the live WhatsApp tab, the visible message nodes still exist under `#main [role="row"]`, but `data-id` now looks like a bare message ID:
>
> ```text
> 3A4689CE2A81856D4BB0
> ACED689BB5C3115D3DD361F3520F9ECE
> ...
> ```
>
> Because `parseDataId()` only accepts the old packed format, it rejects every row, so `whatsappMessages()` returns `[]`, and the bookmarklet shows `Copy 0 messages`.
>
> WhatsApp appears to have split what used to be one overloaded field into separate concerns:
>
> - `data-id` now behaves like `messageId`
> - outgoing direction is likely encoded by DOM class (`.message-out`)
> - chat/thread id is no longer bundled into the row `data-id`

... and went on to share a "Recommended hardening plan for future breakages".

If coding agents can install, configure, write, run, test, and debug programs, "Agentic Operating Systems" are not nearby. We already have them.
