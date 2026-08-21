---
title: Writing articles from my blog posts
date: '2026-02-16T18:03:12+08:00'
categories:
- llms
description: I used Gemini to research Built In, find a topic in my blog archive, and assemble an article from my words. After two poor drafts, a fresh chat produced a mostly authentic edit.
tags: [content-repurposing, llms, writing-style, gemini]
---

You can use AI to submit not just [talk proposals](/blog/submitting-an-ai-ded-vizchitra-proposal/) but entire articles from your past work.

[Ranjeeta](https://www.linkedin.com/in/ranjeetaborah) said [Built In](https://builtin.com/) wants an article and had written one on my behalf.

If someone's going to write for me, I'd rather pick an AI! So here's what I did:

![](https://files.s-anand.net/images/2026-02-16-writing-articles-from-my-blog-posts.avif)

### Research the audience

So I asked [Gemini](https://gemini.google.com/share/709961aadd75) to research and suggest topics:

<!-- https://gemini.google.com/app/344c4ed087238f36 -->

> I received a request to write an article for Built In (https://builtin.com/), an online community and publication for startups and tech companies.
>
> Research this publication. How large is it? How respected is it? Give me an intuition comparing with other publications.
>
> Also help me with the type of content to write. What do its readers read? What's popular? Among the most popular articles, what're typical article lengths? What is the most appreciated style of writing? Are these heavily linked, lightly linked, or not at all? Are they illustrated - and if so, how, e.g. images, charts, animations, videos, etc. and in any case, is this appreciated or frowned upon? What's the review process like?
>
> Knowing me, what are examples of topics you'd suggest I write about that will be well received and popular with this audience?

It said basically told me:

- Built In is basically "HBR for coders" - huge reach (3M+), totally legit, and targets mid-to-senior tech pros who want the real scoop, not just fluff.
- They want "in the trenches" war stories and "how-to" career/tech guides (1k-1.5k words). Less "breaking news," more "here's how I actually built this."
- Keep it conversational and punchy (no jargon); no selling, but linking your blog/open-source stuff is cool.
- Pitch "I replaced my workflow with AI" (hot topic), "Chat is the new Dashboard" (your wheelhouse), or "Prototyping your Career" (agile life advice). The AI angle works.

### Suggest topics from existing content

This is the cool part. I told it:

> I'd like to re-purpose one or some of my blog posts. Here are my LLM-related blog posts in 2025-26. I'd like you to recommend the top 3 articles I could write. Each article could cover 1 or more posts about a single topic. Think about what will be most impactful for this audience as well as unique, i.e. a lot less covered elsewhere.

... and then passed it _all_ of my 2025-2026 [blog posts](https://github.com/sanand0/blog/tree/main/posts) related to LLMs using:

```bash
ug -l ' - llms' \                 # Find all LLM-related posts
  | ug '2025|2026' \              # From 2025-206
  | uvx files-to-prompt --cxml \  # Convert to XML for better LLM ingestion
  | xclip -selection clipboard    # Copy to clipboard and paste into Gemini
```

Gemini _churned_ and suggested three topics.

- **Vibe Coding**: It's not magic, it's a gamble-awesome for rapid prototypes but risky for production.
- **RIP Data Engineering:** Stop wasting 15 years fixing fragile web scrapers-just tell the AI.
- **The AI Mirror:** Flip the script and use AI to roast _you_-feed it your meeting transcripts.

### Find best content for topic

> I like #3 - AI Mirror: Using LLMs to Decode Your Leadership Style.
>
> Look at my blog posts and see which ones are most apt for this topic. Then synthesize from these, writing as much as possible with the same words I used in my blog posts, and combine them into an article for Built In.
>
> Plan first. Think hard about the approach, then execute carefully.

It wrote a nice, long **rubbish** article that had little of my style. But, why be rude?

> Nice structure. But rewrite it using exactly my words in every place unless unavoidable.

It wrote another nice, long, **rubbish** article with little of my style. I don't give third chances.

> List all the files you used as reference. Then list other files that would align with this topic. In other words, I would like all the file names directly or indirectly related to this topic that can serve as source material for this.

... and it gave me the most relevant articles.

- [`2025/the-surprising-power-of-llms-jack-of-all-trades.md`](/blog/the-surprising-power-of-llms-jack-of-all-trades/)
- [`2025/how-to-double-check-personality-flaws-with-ai.md`](/blog/how-to-double-check-personality-flaws-with-ai/)
- [`2025/llms-as-idea-connection-machines.md`](/blog/llms-as-idea-connection-machines/)
- [`2025/measuring-talking-time-with-llms.md`](/blog/measuring-talking-time-with-llms/)
- [`2025/llm-psychology-podcast.md`](/blog/llm-psychology-podcast/)
- [`2025/wait-thats-my-mic-lessons-from-an-ai-co-host.md`](/blog/wait-thats-my-mic-lessons-from-an-ai-co-host/)
- [`2025/extracting-ai-advice.md`](/blog/extracting-ai-advice/)
- [`2025/top-8-ways-i-use-chatgpt-in-2025.md`](/blog/top-8-ways-i-use-chatgpt-in-2025/)
- [`2026/breaking-rules-in-the-age-of-ai.md`](/blog/breaking-rules-in-the-age-of-ai/)
- [`2025/turning-generic-gifts-into-joy-with-ai.md`](/blog/turning-generic-gifts-into-joy-with-ai/)

### Generate the article using my words

<!-- https://gemini.google.com/app/7cf151511ad8f917 -->

I started a [new chat](https://gemini.google.com/share/56efa70f7d3f) to avoid confusion and told it to:

> Write an article for Built In. Read the section below for context on Built In's audience, style, and content preferences. Then read my blog posts further down. Based on that, write an article titled: "AI Mirror: Using LLMs to Decode Yourself".
>
> This should be a synthesis of my words, i.e. always use my blog post content, except for transitions, etc. Select content and include images, data visualizations, links, etc. aligned with Built In's style.

Then I fed it all the context about Built In as well as the relevant blog posts.

[The result](https://gemini.google.com/share/56efa70f7d3f) was pretty good. It was mostly in my voice - literally copy-pasted from my articles. I just made some edits where it had used its own words.

<!-- Edited article: https://docs.google.com/document/d/1HSBePk8fMl01V3Qoiym4AYEH81ZqQXlC3-gyr336e1M -->

---

The best part is that when AI is assembling your own words, it's acting more like an editor, not an author. That probably isn't slop, right?
