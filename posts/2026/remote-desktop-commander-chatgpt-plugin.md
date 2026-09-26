---
title: Remote Desktop Commander ChatGPT Plugin
date: 2026-09-26T17:37:46+08:00
categories:
- llms
description: I found the Remote Desktop Commander ChatGPT plugin, which lets ChatGPT access my computer, read and write files, and run commands. It also uses past chat context, making local coding feel like unlimited Codex.
tags: [chatgpt, mcp, chatgpt-usage]
---

The [Remote Desktop Commander ChatGPT Plugin](https://chatgpt.com/plugins/plugin_asdk_app_6a057d268ebc81919918d37eec718425) might be one of the most useful power-user plugins for ChatGPT. Here's how it works.

1. You install the plugin and log into [desktopcommander.app](https://desktopcommander.app/)
2. You run `npx @wonderwhy-er/desktop-commander@latest remote` on your machine
3. After that, ChatGPT can access your computer - read/write files, run commands, etc.

This is incredibly useful because that's like getting unlimited Codex usage. ChatGPT Chat doesn't charge by token usage. So you can write and run code on your machine without worrying about token limits. (This doesn't help so much with Claude - it charges the same for Chat and Code.)

Secondly, you can use the context of past chats and memories (or perhaps projects) - which Codex and Claude Code doesn't have.

[![](https://files.s-anand.net/images/2026-09-26-remote-desktop-commander-chatgpt-plugin.avif)](https://mcp.desktopcommander.app/)

I wrote a version of this plugin for myself - [mcpserver.py](https://github.com/sanand0/scripts/blob/8302d6266b295887e295d58cb6dd87a70c4828f7/mcpserver.py) - and it's been the most used plugin. Almost 70% of my chats (237 / 344) in August used this plugin.

Since I already have my plugin I probably won't be switching. Also, your data passes through a third-party, and their liberal free-tier (10K tool calls per month) might evaporate.

But this may be the most useful plugin for ChatGPT power users.
