---
title: Using browser history as memory
date: 2026-02-18T10:02:56+08:00
categories:
  - how-i-do-things
  - llms
---

I have a bad memory. (I need to write about that. I k eep forgetting to.)

It's worsening. Yesterday, I misplaced my debit card for the first time. Or maybe the second...? Which reminds me, I just forgot a call I have now! (Panic.)

(15 min later.) So, anyway, therefore, I log stuff meticulously. Like what I did each day, what I ate, what I weigh, what pained me, etc. But the best logging is automated. My phone logs where I am. My bank logs what I spend. My calendar logs who I meet.

The main gap now is when I'm at home, not spending money or meeting people. Just... browsing. And browser history is a _great_ way to "remember" this.

![](https://files.s-anand.net/images/2026-02-18-using-browser-history-as-memory.avif)

I figure out what I did this weekend, I ran:

```bash
datasette ~/.config/microsoft-edge/Default/History --nolock
```

... and then this query:

```sql
SELECT
datetime(visit_time / 1000000 - 11644473600, 'unixepoch', 'localtime') AS visit_date,
  urls.title,
  urls.url
FROM visits
JOIN urls ON visits.url = urls.id
WHERE visit_date >= '2026-02-14 00:00:00'
  AND visit_date < '2026-02-16 00:00:00'
ORDER BY visit_time ASC;
```

<!-- https://gemini.google.com/app/6c832c9c0127526e -->

I pasted the CSV output into Gemini along with this prompt:

> Here is my browsing history this Sunday. Summarize what I did, grouping into logical groups like:
>
> 10:00 - 12:30: What I did in 1-2 sentences
> 12:30 - 13:00: Next activity
> ...
>
> Ask me questions for whatever's unclear.

Here's what it said {with my comments}:

- **10:00 – 12:00: VizChitra Planning & AI Research**. You started with administrative tasks (AWS, Google AI Studio keys) before diving into **VizChitra 2026** proposals. You researched AI attribution bias and data storytelling, then used Claude and Gemini to brainstorm ideas, eventually drafting your blog post: "[Submitting an AI-Ded VizChitra Proposal](/blog/submitting-an-ai-ded-vizchitra-proposal/)."
- **12:00 – 14:15: Blogging & Philosophy** You continued refining your blog post and engaged in deep discussions with Claude about "[developing taste and judgment in the AI age](/blog/how-to-develop-taste/)." You also briefly checked LinkedIn {"anyone liked my post yet?"} and explored some Dutch legal terms ("Stijlrichtlijn") {work-related}.
- **14:15 – 16:30: Academic Research & Entertainment**. You read heavy research papers on the economic and aesthetic impacts of AI (Microsoft's Future of Work, Peyman Shahidi) {to [develop taste](/blog/how-to-develop-taste/)}. You then prototyped an "Ask AI" tool using Codex before switching gears {here's the [Ask AI tool](https://tools.s-anand.net/askai/)} to watch the Telugu comedy movie _[Khatarnak](https://youtu.be/nf0A84cmQA0)_ on YouTube {Telugu films are best for vibe coding}.
- **16:30 – 17:45: Local Development & Coding** You spent this block coding on localhost (port 8000), testing your "Ask AI" tool and a "JSON to CSV" converter. You also managed GitHub pull requests for your [tools](https://github.com/sanand0/tools/) repository.
- **17:45 – 19:00: Deep Dive into Learning Theory**. You went down a rabbit hole on pedagogy and mastery, reading about the "psychology of interest," "tacit knowledge" (Commoncog), "cognitive apprenticeship," and Austin Kleon’s "Scenius" {to [develop taste](/blog/how-to-develop-taste/)}. You also looked up directions to the Isha Yoga Center in Singapore {my wife asked}.
- **19:00 – 20:30: Course Admin & Networking**. You switched context to your **[Tools in Data Science (TDS)](https://tds.s-anand.net/)** course, troubleshooting a "[GA1 Question 9](https://exam.sanand.workers.dev/tds-2026-01-ga1#hq-python-refactor-server)" submission issue for students. You checked LinkedIn profiles ({names redacted}) and watched a few more comedy clips (_[Baladoor](https://youtu.be/Lhnl6rBzw6A)_, _[Julai](https://youtu.be/B4O_eHOWqo)_) to relax.
- **20:30 – 22:00: TDS Live Session**. You prepared for and joined a Google Meet (likely the TDS Live Session), reviewing papers on "automation bias" beforehand. Afterward, you managed the meeting recordings and looked into configuring custom commit messages for GitHub Copilot.
- **22:00 – 23:00: Cloudflare & Wrap-up**. You ended the day deploying updates on Cloudflare Workers, handling more student emails regarding the GA1 deadline, and doing some light image editing on Squoosh.

This is a _fantastic_ way to jog my memory about what I did - and is obviously spot on. The questions it asked were also insightful:

1. The search for "Stijlrichtlijn Verdict to Video" (Dutch guidelines) seemed distinct from your other work—was this for a specific project? **ANS** A specific work project.
2. Did you end up watching the full _Khatarnak_ movie, or was it background noise while you prototyped? **ANS** Background noise while vibe0coding.
3. The very last search was for "cnc machine"—are you looking to buy one? **ANS** [Prof Shantanu Chaudhury](https://scholar.google.com/citations?user=V6NJi4kAAAAJ), a few days ago, likened vibe coding practices to "something like you're creating a CNC machine for coding. You're just giving the specification, programming it, and it's generating the code." Which felt _very_ apt, but I haven't used a CNC machine (or have I?) and asked Google what it was.

---

So there it is. Export your browser history and as an LLM to summarize your day. Great way to jog your memory - and waste an hour.

---

**11 Mar 2026**. This continues to be a useful memory hack. In the last 4 weeks, I've used this at least 4 times to find out what I was doing the previous day or previous few days.
