---
title: When the prompt is longer than the code
date: 2026-06-05T17:14:17+08:00
categories:
  - llms
description: I used Pi to build a tiny landing page where the prompts were longer than the 471-byte HTML output. This workflow helped me overcome starting friction and solve CSS centering while focusing on review over manual coding.
keywords: [pi, llms, css, html, web development, prompt engineering]
---

I used [pi](https://pi.dev/) to create a compact home page for [media.s-anand.net](https://media.s-anand.net/) using these prompts:

> Create `index.html` - a simple, elegant page that says that this page (media.s-anand.net) serves large media files for [Anand](https://www.s-anand.net/) - that's where they should look instead.

... followed by:

> Skip the part that says "Please visit ..."

... then:

> Shorten index.html to just 2-3 elegant rules of CSS. I want it MUCH smaller and simpler.

... and finally:

> Center vertically and horizontally.

These prompts ended up being larger than the 471-byte `index.html`:

```html
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>media.s-anand.net</title>
<style>
  body { min-height: 100vh; display: grid; place-content: center; margin: auto; font: 1.25rem/1.6 system-ui, sans-serif; }
  h1 { font-size: clamp(2rem, 8vw, 4rem); }
</style>
<h1>media.s-anand.net</h1>
<p>This domain serves large media files for <a href="https://www.s-anand.net/">Anand</a>.</p>
</html>
```

Not that this matters, because:

1. I didn't know what I wanted and having an AI coding agent generate a first draft helped with starting trouble and ideation.
2. I don't know how to center on the screen and this did it for me.
3. I am practicing the skill that matters - reviewing - and not the skill AI is taking over - writing code.
