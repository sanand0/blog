---
title: Things I Learned - 05 Apr 2026
date: 2026-04-05T00:00:00+00:00
categories:
  - til
description: I discovered useful Ubuntu window management shortcuts, compared jq and jaq for JSON formatting, and learned time-saving shell tricks. I also gained a clearer understanding of Diffie Hellman key exchange and observed GitHub Copilot's usage reset behavior.
tags: [ubuntu, jq, bash, github-copilot, linux]
---

This week, I learned:

- It's pretty convenient (on Ubuntu) to be able to move windows around desktops. Apart from the usual Super + Arrow keys to manage windows within a desktop, you can use:
  - Ctrl + Alt + Left/Right Arrow: Move desktops
  - Ctrl + Alt + Shift + Left/Right Arrow: Move window to desktop
  - Super + Shift + Arrow: Move window to another monitor
  - Super + Drag: Drag window from anywhere
- `jq . file.json` is an efficient way to pretty-print JSON files in the terminal. (Or `jaq . file.json`, which is ~30% faster.)
- GitHub Copilot monthly premium requests were _not_ reset at 12 am UTC
- [How Diffie Hellman Key Exchange Works](https://social.jvns.ca/@b0rk/116297197345549083) by Julia Evans is an _excellent_ explanation. Share a random number. A multiplies it by their private key and shares S*A. B multiplies it by their private key and shares S*B. They multiply the others' key with their secret key and they get S*A*B = S*B*A. Now _both_ of them have the same _new_ secret they can encrypt/decrypt with, but no one else knows, even though they shared everything publicly! This may be one of the **best** cool uses of math I've seen in a long time.
- [Shell tricks](https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/) I didn't know:
  ```bash
  # ALT + . cycles through the last arguments typed
  mv file.{txt,md}    # Move file.txt to file.md
  ls |& tee file.txt  # Pipe both stdout and stderr to tee
  ```
