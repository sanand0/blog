---
title: Verifying Textbook Facts
date: '2026-01-23T13:36:50+05:30'
categories:
- education
- llms
description: 'I found a practical use for LLMs: fact-checking textbooks page by page. A scan of 56 NCERT pages flagged 45 claims, including the questionable claim that only useless objects were discarded.'
tags: [fact-checking, llms, education]
---

Using LLMs to find errors is fairly hallucination-proof.

If they mess up, it's just wasted effort. If they don't, they've uncovered a major problem!

[Varun](https://github.com/PythonicVarun) fact-checked [Themes in Indian History](https://ncert.nic.in/textbook.php?lehs1=0-4), the official NCERT Class 12 textbook.

Page-by-page, he asked Gemini to:

1. **Extract each claim**. E.g. "Clay was locally available to the Harappans" on page 12.
2. **Search online for the claim**. E.g. [ASI site description](https://asi.nic.in/harappa/) and by [Encyclopedia Britannica](https://www.britannica.com/place/India/The-Indus-civilization).
3. **Fact-check each claim**. E.g. "Clay was locally available to the Harappans" is confirmed by both sources.

[Here is his analysis](https://pythonicvarun.github.io/textbook-analysis/) and [verifier code](https://github.com/PythonicVarun/textbook-analysis/blob/master/src/verifier.py).

Before hitting rate limits, he scanned 56 pages and fact checked 45 claims from a dozen pages ([detailed report](https://pythonicvarun.github.io/textbook-analysis/report/)). Even among this small sample, there was an interesting error on Page 22:

> Only broken or useless objects would have been thrown away.

![](https://files.s-anand.net/images/2026-01-23-verifying-textbook-facts.webp)

In reality, [migrants abandon useful objects](https://crowcanyon.org/ResearchReports/WoodsCanyon/Text/wcpw_abandonment.php) and [ritual deposits](https://www.mdpi.com/2673-9461/5/1/3) give us intact, useful objects.

So, is this an error in the textbook worth correcting? Maybe. Worth exploring.

BTW, the original analysis hallucinated sources: "Discard and Reuse in the Ancient Near East" and "Recycling in the Bronze Age" from Cambridge. But for fact-checking, this doesn't matter. The point is to flag questionable claims for [further review](https://chatgpt.com/share/6973498f-f784-8003-aa41-9090807c3c88).

There are others:

- Did R.E.M. Wheeler take over as Director-General of the Archeological Survey of India in 1944 (according to the book) or in 1940 (according to other sources)? Worth checking the ASI records?
- [Ashoka's army was] 600,000 foot-soldiers, 30,000 cavalry and 9,000 elephants? The book says "some historians consider these accounts to be exaggerated" but the consensus is that these are almost certainly exaggerated. Worth rewording?

If LLMs find half a dozen questionable claims from a dozen pages, fact-checking textbooks seems an effective use for LLMs.

Especially when 25 million students read them every year.

---

I have personally suffered from errors in history textbooks.

I wrote my class 9 history exam in 1989-90. The Hindu published a series titled "This Day That Age" with news from 50 years ago. That morning's was that [Germany invaded Poland with Russian aid](https://en.wikipedia.org/wiki/Soviet_invasion_of_Poland). I proudly wrote this in my exam and lost a mark, since the history textbook clearly mentioned that Russia opposed Germany.

(That I feel indignant 36 years later tells you how sorry my life is.)
