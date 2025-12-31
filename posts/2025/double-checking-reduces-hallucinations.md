---
date: "2025-05-10T09:35:14Z"
categories:
  - linkedin
---

How can we rely on unreliable LLMs?" people ask me.

Double-checking with another LLM," is my top response. That's what we do with unreliable humans, anyway.

LLMs feel magical until they start confidently hallucinating. When I asked 11 cheap LLMs to classify customer service messages into billing, refunds, order changes, etc. they got it wrong ~14%. Not worse than a human, but in scale-sensitive settings, that's not good enough.

But different LLMs make **DIFFERENT** mistakes. When double-checking with two LLMs, they were **both** wrong only 4% of the time. With 4 LLMs, it was only 1%.

Double-checking costs almost nothing. When LLMs disagree, a human can check it. Also, multiple LLMs rarely agree on the **same** wrong answer.

So, instead of 100% automation at 85% quality, double-check with multiple LLMs. You can get 80% automation with 99% quality.

- Full analysis: https://sanand0.github.io/llmevals/double-checking/
- Code and data: https://github.com/sanand0/llmevals/tree/main/double-checking

![](https://github.com/sanand0/llmevals/raw/main/double-checking/improvement.webp)

[LinkedIn](https://www.linkedin.com/feed/update/urn%3Ali%3Ashare%3A7326902628490059776)
