---
title: Google Meet captions as a local transcript recorder
date: 2026-05-16T13:32:06+08:00
categories:
  - coding
  - how-i-do-things
  - llms
description: A tiny Google Meet bookmarklet can stream live captions into local Markdown, making meeting transcripts agent-readable without waiting for platform exports.
keywords: [google meet captions, bookmarklet, local transcripts, markdown, file system access api, agent-readable meetings]
---

![](https://files.s-anand.net/images/2026-05-15-google-meet-captions-tool.avif)

I'm a man of simple needs. All I want is: when I'm on [Google Meet](https://meet.google.com/), I turn on captions. I wanted to click a bookmarklet and save those captions into a local Markdown file. (So that an AI agent can guide me from it.)

Hence, [Google Meet Captions](https://tools.s-anand.net/gmeetcaptions/). The code is in [`gmeetcaptions/`](https://github.com/sanand0/tools/tree/main/gmeetcaptions). Drag the button to your bookmarks bar. Join a Meet. Turn on captions. Click it.

You get a tiny panel with two buttons: **Copy** and **Start Recording**.

[The bookmarklet](https://github.com/sanand0/tools/blob/main/gmeetcaptions/gmeetcaptions.js) writes this kind of Markdown:

```markdown
# Meeting title

- **Meeting code**: abc-defg-hij
- **Started**: 5/15/2026, 8:00:00 AM
- **Participants**: Alice, Bob, Carol

---

## Alice [0:12]

Good morning everyone.

## Bob [0:18]

Let's get started with the agenda.
```

That's it. No server. No extension. No login. No API. Just a [bookmarklet page](https://github.com/sanand0/tools/blob/main/gmeetcaptions/index.html), a [script](https://github.com/sanand0/tools/blob/main/gmeetcaptions/script.js), and local browser APIs.

---

**BUT**: Google Meet captions are live and unstable.

A sentence may appear as:

```markdown
mic, so,
```

Then a second later become:

```markdown
mic, So that's a new person. Okay.
```

Then become:

```markdown
mic, So that's a new person. Okay. Hey. oh, but,
```

If I simply append every change, the transcript becomes garbage. So the bookmarklet keeps updating the active speaker turn until it becomes stable. The implementation uses a [`MutationObserver`](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver) plus a one-second polling fallback. After four unchanged polls, it treats the turn as final.

The tests are in [`gmeetcaptions.test.js`](https://github.com/sanand0/tools/blob/main/gmeetcaptions/gmeetcaptions.test.js), using an anonymized fixture at [`__fixtures__/captions-anonymized.html`](https://github.com/sanand0/tools/blob/main/gmeetcaptions/__fixtures__/captions-anonymized.html).

---

**BUT #2**: Google Meet's DOM is not a public API. Class names like `.nMcdL`, `.NWpY1d`, and `.ygicle` can vanish overnight.

So the scraper first tries semantic and structural selectors:

- `[role="region"][aria-label="Captions"]` for the captions region
- `img[data-iml]` and `googleusercontent.com` avatars to identify caption items
- the first `<span>` as the speaker
- the last non-image `<div>` as the caption text

Only then does it fall back to obfuscated class names. That selector strategy is documented in the [`README`](https://github.com/sanand0/tools/blob/main/gmeetcaptions/README.md).

Boring, but also the difference between "worked once" and "might work tomorrow."

---

The weirdest was Chrome writing to a `.md.crswap` file while recording. The file appears unfinished until I click **Stop Recording**. Then Chrome finalizes it.

This is good, actually. It means the browser is safely streaming to a local file via the [File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API). But it also means: **stop the recorder before trusting the file**!

I captured these bugs and prompts in [`prompts.md`](https://github.com/sanand0/tools/blob/main/gmeetcaptions/prompts.md), because future-me will forget. Future-agent, too.

---

Why bother? Because transcripts are not the output. They are raw material.

Once a meeting is Markdown, I can ask agents to extract decisions, questions, follow-ups, contradictions, reusable prompts, and blog ideas. I can diff it. Search it. Commit it. Feed it to another workflow.

Meetings now become the "context" in context engineering!
