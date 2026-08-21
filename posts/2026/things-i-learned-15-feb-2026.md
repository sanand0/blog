---
title: Things I Learned - 15 Feb 2026
date: 2026-02-15T00:00:00+00:00
categories:
- til
description: I learned how to concatenate compatible files directly with ffmpeg, add icons to terminal listings using Nerd Fonts, and briefly tried Maple Mono in VS Code before returning to Fira Code.
tags: [ffmpeg, developer-tools, vs-code]
---

This week, I learned:

- `ffmpeg` lets you concatenate files without needing a separate input file. `ffmpeg -i "concat:input1.ext|input2.ext|input3.ext" -c copy output.ext` works as long as the files use the same codecs and parameters.
- There is a psychological phenomenon where we "overlay" old images of people we haven't seen in decades onto their current selves, making it hard to distinguish between someone who is 30 and someone who is 70. [Gemini](https://gemini.google.com/share/1348ea514d1e)
- Most modern `ls` tools like [`eza --icons`](https://github.com/eza-community/eza) or [`lsd`](https://github.com/lsd-rs/lsd) support icons if the terminal font supports icons, like [Nerd Fonts](https://www.nerdfonts.com/). For example, this: `` shows up as a GitHub icon and `󰌻` as a LinkedIn icon. The [Nerd Fonts Cheat Sheet](https://www.nerdfonts.com/cheat-sheet) is a good place to search for these. You may need to download a [supporting font](https://www.nerdfonts.com/font-downloads).
- I just replaced [Fira Code](https://github.com/tonsky/FiraCode) with [Maple Mono](https://font.subf.dev/en/) as my default font on VS Code. Like Fira Code, the ligatures are great, but there are extra ligatures like [TODO] or [ERROR], _connected italics_, nerd font support, variable font weights, and more. Via [lobste.rs](https://lobste.rs/s/ahca9t/maple_mono_open_source_monospace_font). (**Update**: Maple Mono is _much_ harder to read than Fira Code, so I switched back. But it's a nice idea.)
