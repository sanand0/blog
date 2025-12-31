---
title: Mistakes AI Coding Agents Make
date: "2025-06-22T09:21:05Z"
lastmod: "2025-06-22T09:21:07Z"
categories:
  - coding
  - llms
wp_id: 4147
---

![Mistakes AI Coding Agents Make](/blog/assets/image-9.webp)

I use [Codex](https://chatgpt.com/codex) to write tools while I walk. Here are merged PRs:

- [Add editable system prompt](https://github.com/sanand0/tools/pull/27)
- [Standardize toast notifications](https://github.com/sanand0/tools/pull/23)
- [Persist form fields](https://github.com/sanand0/tools/pull/25)
- [Fix SVG handling in page2md](https://github.com/sanand0/tools/pull/22)
- [Add Google Tasks exporter](https://github.com/sanand0/tools/pull/19)
- [Add Markdown table to CSV tool](https://github.com/sanand0/tools/pull/20)
- [Replace simple alerts with toasts](https://github.com/sanand0/tools/pull/24)
- [Add CSV joiner tool](https://github.com/sanand0/tools/pull/21)
- [Add SpeakMD tool](https://github.com/sanand0/tools/pull/12)

This added technical debt. I spent four hours fixing the AI generated tests and code.

### What mistakes did it make?

1. **Inconsistency**. It flips between `execCommand("copy")` and `clipboard.writeText()`. It wavers on timeouts (50 ms vs 100 ms). It doesn't always run/fix test cases.
2. **Missed edge cases**. I [switched](https://github.com/sanand0/tools/pull/25) `<div>` to `<form>`. My earlier code didn't have a `type="button"`, so clicks reloaded the page. It missed that. It also left scripts as plain `<script>` instead of `<script type="module">` which was required.
3. **Limited experimentation**. My failed with a HTTP 404 because the `common/` directory wasn't served. I added `console.log`s to find this. Also, [happy-dom](https://www.npmjs.com/package/happy-dom) won't handle multiple `export`s instead of a single `export { ... }`. I wrote code to verify this. Coding agents didn't run such experiments.

### What can we do about it?

Three things could have helped me:

1. **Detailed coding rules**. E.g. **always** run test cases and fix until they pass. Only use ESM. Always import from CDN via JSDelivr. That sort of thing.
2. **100% test coverage**. Ideally 100% of code and all usage scenarios.
3. **Log everything**. My tests got a HTTP 404 because I was not serving the `common/` directory. LLMs couldn't figure this out because it was not logged. Logging everything helps humans **and** LLMs debug.
4. **Wait**. LLMs and coding agents keep improving. A few months down the line, they'll run more experiments themselves.

**Was AI coding worth the effort?** Here, yes. The tools **worked**. Codex saved me 90% effort. My code quality obsession reduced savings to ~70%. Still huge.
