---
title: "Vibe-Scraping: Write outcomes, not scrapers"
date: "2025-09-30T13:18:20Z"
lastmod: "2025-09-30T13:19:33Z"
categories:
  - coding
  - llms
wp_id: 4220
---

![Vibe-Scraping: Write outcomes, not scrapers](/blog/assets/image-12.webp)

There hasn't been a box-office explosion like Dangal in the history of Bollywood. CPI inflation-adjusted to 2024, it is the only film in the ₹3,000 Cr club.

3 Idiots (2009) is the first member of the ₹1,000 Cr club (2024-inflation-adjusted). The hot streak was 2013-2017: **each** year, a film crossed that bar: Dhoom 3, PK, Bajrangi Bhaijaan, Dangal, Secret Superstar.

Since then, we **never** saw such a release except in 2023 (Jawan, Pathan).

But this story isn't about the box-office drought. It's about **vibe-scraping**.

---

To scrape the 1k Cr club data, here's what my process would be in:

- 2008-2015. Requests + BeautifulSoup in Python. Takes ~1 day.
- 2015-2024. Puppeteer. Still takes ~1 day.
- 2025-Today. AI writes code. ~2 hours/site. **4x faster**.
- Today-???. Coding agents **scrape directly**. ~30 min/site. **16 times faster**.

I passed Codex CLI (roughly) this prompt:

> Write scrape.py to scrape the highest-grossing films from Wikipedia's list of Hindi films: 1994 to 2024.\
> Read pages as required. Save results as CSV.

Here's what it did.

- Read the Wikipedia lists starting [1994](https://en.wikipedia.org/wiki/List_of_Hindi_films_of_1994)
- Failed on missing BeautifulSoup dependency. I allowed install.
- Discovered that tables below "grossing" or "box office" headings are relevant.
- Noticed "Rank" became “No” in the column header since 2016 and adapted.
- Fixed all errors and generated a clean CSV.

That's… **incredible**!

The code was a by-product. The prompt and evals matter. When sites change, agents can fix the code. Or better agents will rewrite it.

I guess I'll call this **vibe-scraping**.

I also asked Claude Code vibe-code a data story. Here are the links:

- [Visualization](https://sanand0.github.io/datastories/bollywood-top-grossing/)
- [Code](https://github.com/sanand0/datastories/blob/6f6ef4b92adccdb519a8de717ac330268ab4e341/bollywood-top-grossing/)
- [Scraper chat](https://github.com/sanand0/datastories/blob/6f6ef4b92adccdb519a8de717ac330268ab4e341/bollywood-top-grossing/prompts/scraper.md)
- [Dataviz chat](https://github.com/sanand0/datastories/blob/6f6ef4b92adccdb519a8de717ac330268ab4e341/bollywood-top-grossing/prompts/dataviz.md)

---

This afternoon, in front of a client, I spoke with Codex:

> Write a scrape.py that searches Dutch fashion merchant websites and lists what delivery carriers they use.

~10 minutes later, we had a table. The client spotted one error that I couldn't have. Expert review still matters. But what's redundant is my 20-year scraping experience!

If agents can scrape on the fly, what **new** questions do we ask?

[LinkedIn](https://www.linkedin.com/posts/sanand0_there-hasnt-been-a-box-office-explosion-activity-7378964378899054593-X4mP)
