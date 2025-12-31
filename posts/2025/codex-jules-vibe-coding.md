---
date: "2025-06-22T09:52:29Z"
categories:
  - linkedin
---

I use Codex and Jules to code while I walk. I've merged several PRs without careful review. This added technical debt.

This weekend, I spent four hours fixing the AI generated tests and code.

---

**What mistakes did it make?**

**Inconsistency**. It flips between `execCommand("copy`") and `clipboard.writeText`(). It wavers on timeouts (50 ms vs 100 ms). It doesn't always run/fix test cases.

**Missed edge cases**. I switched <`div`> to <`form`>. My earlier code didn't have a `type="button`", so clicks reloaded the page. It missed that. It also left scripts as plain <`script`> instead of <`script type="module`"> which was required.

**Limited experimentation**. My failed with a HTTP 404 because the `common`/ directory wasn't served. I added `console.log`s to find this. Also, `happy-dom` won't handle multiple `export`s instead of a single `export` { ... }. I wrote code to verify this. Coding agents didn't run such experiments.

---

**What can we do about it?**

**Detailed coding rules**. E.g. _always_ run test cases and fix until they pass. Only use ESM. Always import from CDN via JSDelivr. That sort of thing.

100% **test coverage**. Ideally 100% of code and all usage scenarios.

**Log everything**. My tests got a HTTP 404 because I was not serving the `common`/ directory. LLMs couldn't figure this out because it was not logged. Logging everything helps humans _and_ LLMs debug.

**Wait**. LLMs and coding agents keep improving. A few months down the line, they'll run more experiments themselves.

---

**Was AI coding worth the effort**? Here, yes. The tools _worked_. Codex saved me 90% effort. My code quality obsession reduced savings to ~70%. Still huge.

![](https://files.s-anand.net/images/2025-06-22-codex-jules-vibe-coding-linkedin.jpg)

[LinkedIn](https://www.linkedin.com/feed/update/urn%3Ali%3Ashare%3A7342489647257632769)
