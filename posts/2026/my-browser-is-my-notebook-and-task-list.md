---
title: My browser is my notebook and task list
date: 2026-11-10T15:10:47+08:00
categories:
  - how-i-do-things
description: I use Edge as both my workspace and TODO list, organizing 80-200 tabs with vertical tabs and groups, then extending it with extensions, bookmarklets, and scripts for notes, capture, and backups.
tags: [productivity, browser-extensions, bookmarklet, browser-tools]
---

Recently, I've started using my browser both as the primary workspace (slightly more than VS Code) as well as my TODO list. That's mainly due to better tab management and better tools.

### Tab Management

The first big shift was turning on [Vertical Tabs](https://explore.microsoft.com/en-us/edge/features/vertical-tabs) on Edge. Now, I can see and manage _far more_ tabs. Typically, I have 80-200 tabs open now.

The next big shift was using [tab groups](https://explore.microsoft.com/en-us/edge/features/tab-groups). With vertical tabs, this makes tabs like a folder.

Since I was accumulating too many tabs, I needed a management system. I decided to apply the same principle as my TODO lists:

1. All current work goes into a "WIP" tab, or task-specific category like Read, Lego, [TDS](https://tds.s-anand.net/), etc.
2. All previous week's WIP tabs are renamed "WIP YYYY-MM-DD" for that week.

![](https://files.s-anand.net/images/2026-11-10-browser-tab-groups.avif)

I also created a ["Tab Notes" extension](https://github.com/sanand0/tabnotes) to help me make notes on each tab, e.g. what I should do next, when I opened it, etc.

[![](https://github.com/sanand0/tabnotes/raw/main/submission-assets/final/hero.png)](https://github.com/sanand0/tabnotes)

... and updated my ["Anand Chrome Tools" extension](https://github.com/sanand0/anand-chrome-tools) that lets me change the title of a tab, telling me what I should do next.

![](https://files.s-anand.net/images/2026-11-10-browser-anand-chrome-tools-title.avif)

Over time, I didn't really need the extensions - the tab groups work well enough.

I also use an [`edge` CLI](https://github.com/sanand0/scripts/blob/8dc5fed1f8f5cbd34c984a12b35ec1c5929e248e/edge) that lets me export / import all my tabs. I run this daily to [backup my open tabs](https://github.com/sanand0/scripts/blob/8dc5fed1f8f5cbd34c984a12b35ec1c5929e248e/daily-activities#L148-L156). So, even if I close several tabs accidentally, I can restore most of them from yesterday.

Of course, a big unlock is that I [**use browser tabs as slides**](https://www.s-anand.net/blog/using-browser-tabs-as-slides/) almost exclusively these days.

### Tools

I find four capabilities really effective when extending browser capabilities.

1. [Bookmarklets](https://en.wikipedia.org/wiki/Bookmarklet) let me change _any_ site in almost any way.
2. [Extensions](https://developer.chrome.com/docs/extensions/get-started) let me do more - even changing the browser itself.
3. [Chrome Devtools Protocol (CDP)](https://chromedevtools.github.io/devtools-protocol/) lets me write external scripts that control the browser.
4. Browser profile data lets me write programs to access browser history, cookies, etc. even without controlling the browser.

Bookmarklets are a big part of how I extend my browser. I have a pretty extensive list of bookmarklets.

![](https://files.s-anand.net/images/2026-11-10-browser-bookmarklets.avif)

Some of the most used ones are:

- [AI Scrapers](https://tools.s-anand.net/ai-scrapers) - where I copy ChatGPT, Claude, or Gemini chats / prompts to save or pass to another agent.
- [WhatsApp Scraper](https://tools.s-anand.net/whatsappscraper/) lets me copy an entire WhatsApp thread as Markdown or JSON.
- [Meet Captions](https://tools.s-anand.net/meetcaptions) lets me save captions from Google Meet or Microsoft Teams. I can then ask AI "What should I say next?" and pass it the WIP file as context.
- [GMail header](https://tools.s-anand.net/gmail/) lets me copy the mail header to pass to an agent, e.g. "Reply to this email..."
- [Dark Mode](https://tools.s-anand.net/darkmode/) enables dark mode for GMial and Hacker News, which don't have this natively and I use a lot.

To make it easier to access these bookmarklets, I set up ["Anand Chrome Tools" extension](https://github.com/sanand0/anand-chrome-tools) so that <kbd>Ctrl + Shift + Space</kbd> acts like the command palette in VS Code. I can pick a bookmarklet to run, a tab to switch to, or a custom command (like setting titles).

I also summarize what I browsed each data as part of my [activities update](https://github.com/sanand0/scripts/blob/8dc5fed1f8f5cbd34c984a12b35ec1c5929e248e/activities.py) - which gives agents a bit more context about _when and why_ I browsed a tab.

---

It feels like I'm just scratching the surface of what's possible, actually. Now that agents can write most code I can imagine, imagination may be all we need.
