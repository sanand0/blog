---
title: Rofi vs Kanata
date: 2026-03-01T15:25:48+08:00
lastmod: 2026-03-19T20:01:24+05:30
categories:
  - tools
---

<!--
Chats asking for Kanata use cases:
https://chatgpt.com/c/697d67a3-89d8-83a4-ad61-e905d2598abb
https://claude.ai/chat/b29d22da-6189-4c46-93b2-e64502fa6ee7
https://gemini.google.com/app/91a7e0c2ab8e1eae
-->

[Kanata](https://github.com/jtroo/kanata) might be the most useful tool I can't find a use for.

It's a cross-platform keyboard mapper. Some cool features:

- **Make any key a modifier**. Ctrl, Shift, Alt, etc. are modifiers. But we can make it so that pressing Space + I/J/K/L maps to Up/Left/Down/Right.
- **Chords**. You can map any _sequence_ of keys to anything else. For example, Alt + G, then C can type `git commit -m"Experimenting" [ENTER]`. Ctrl + M, then Down, can reduce the music volume by 10%.
- **Toggles**. Double-clicking Caps Lock activates capitalization for the current word, and once you type a non-letter, it turns off. Or double-clicking Ctrl can turn on "gaming mode" where WASD becomes arrow keys, and double-clicking again turns it off.
- **Tap Dance**. Double-clicking left-shift can turn on Caps Lock. Triple-clicking turns it off. Quadruple-clicking ...

... and there's _lots_ more.

Unfortunately, I have not been able to find a single use in practice. My main bottleneck is that I don't remember the shortcuts. So, instead, I use [rofi](https://github.com/davatorium/rofi).

[Rofi](https://github.com/davatorium/rofi) is a programmable menu launcher. The great thing is that I don't need to remember stuff. When I [map it to keyboard shortcuts](https://github.com/sanand0/scripts/blob/6c7ac7ab91ff726a60b700caf5808213fbb6032a/setup/media-keys.dconf#L45-L61), it pops up a menu and I pick what I need.

I use it to:

#1: **[Open any file](https://github.com/sanand0/scripts/blob/4e514e2128f25b78b3a7b0ad5324887b4d96161c/rofi-files.sh) or [browser tab](https://github.com/sanand0/scripts/blob/4e514e2128f25b78b3a7b0ad5324887b4d96161c/rofi-chrome-tabs.sh)** with `Ctrl + Alt + F`.
This is my most used shortcut. It replaces [Everything](https://www.voidtools.com/) for files, and [Chrome Search Tab](https://support.google.com/chrome/answer/2391819?sjid=6582210427121552745-NC#:~:text=find%20the%20specific%20tab) with a single shortcut.

![](https://files.s-anand.net/images/2026-03-01-rofi-ctrl-alt-f-files-browser.webp)

#2: **[Paste any prompt fragment](https://github.com/sanand0/scripts/blob/974d716338563f4a392a61bc67d66db1b99c8262/rofi-prompts.sh)** with `Ctrl + Alt + P`.

This is especially useful when adding a prompt fragment, like [Expert Lens](/blog/ai-expert-lens/) in the middle of a prompt, or [analyzing call recordings](https://github.com/sanand0/blog/blob/main/pages/prompts/analyze-call-recording.md) a dozen times a day.

![](https://files.s-anand.net/images/2026-03-01-rofi-ctrl-alt-p-prompts.webp)

#3: **[Edit the clipboard](https://github.com/sanand0/scripts/blob/974d716338563f4a392a61bc67d66db1b99c8262/rofi-clip.sh)** with `Ctrl + Alt + M` (for Markdown).

This is a killer feature. I often use it to:

- Copy from email/chat and paste it in ChatGPT as Markdown
- Copy from ChatGPT and remove the em-dashes and non-ASCII characters
- Convert Markdown to Unicode for LinkedIn
- Convert Markdown to rich test for pasting in emails or chat
- Creating a ChatGPT / Claude / Google AI mode link from a piece of text
- ...

![](https://files.s-anand.net/images/2026-03-01-rofi-ctrl-alt-m-markdown-clipboard.webp)

---

I'm still keen to find a use for Kanata, but for now, my use of Rofi will continue to grow.

---

**19 Mar 2026**: The [Compose key](https://crescentro.se/posts/compose-key/) is meant to combine two keystrokes to create a new character - which Kanata offers as a feature with _any_ key.
