---
title: Gemini CLI harness is not good enough
date: 2026-03-08T15:09:25+08:00
categories:
  - llms
---

I've long felt that while the Gemini 3 Pro model is fairly good, the Gemini CLI harness isn't. I saw an example of this today.

**Me**: Tell me the GitHub IDs of all students in this directory.

**Gemini CLI**:

```
SearchText 'github' within ./
Found 100 matches (limited)
Sending this message (14606686 tokens) might exceed the remaining context window limit (1037604 tokens).
```

**Me**: Only send the (small) required snippets of data. Write code as required.

**Gemini CLI**:

```
SearchText 'github' within ./
Found 100 matches (limited)
Sending this message (14606686 tokens) might exceed the remaining context window limit (1037604 tokens).
```

![](https://files.s-anand.net/images/2026-03-08-gemini-cli-harness.avif)

Come ON! It's **March 2026**. We can't pretend it's October 2025 any more.

---

PS: I partly take back what I said. Codex had trouble, too. This problem may be harder than I thought. Still, Gemini CLI should not have gotten stuck where it did.
