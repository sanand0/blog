---
title: My learnings as week notes
date: "2024-12-25T14:27:11Z"
lastmod: "2024-12-25T14:27:13Z"
categories:
  - how-i-do-things
wp_id: 3777
---

![My learnings as week notes](/blog/assets/things-i-learned.webp)

One of my [goals for 2024](/blog/my-year-in-2023/) is to "Compound long-term goals, daily." Learning is one of those.

Some people publish their learnings as weekly notes, like [Simon Willison](https://simonwillison.net/tags/weeknotes/), [Thejesh GN](https://thejeshgn.com/category/weekly-notes/), [Anil Radhakrishna](https://mvark.blogspot.com/), and [Julia Evans](https://jvns.ca/til/). I follow their notes.

I started doing the same, quietly, to see if I could sustain it. It's been a year and it **has sustained**.

I'm finally publishing them. [My week notes are at **til.s-anand.net**](https://til.s-anand.net/). Here's the [source code](https://github.com/sanand0/til).

### Capturing learnings must be frictionless

I learn things when I'm reading, listening to podcasts, listening to people, or thinking. In every case I'm close to my phone or laptop.

If my laptop is open, I add my notes to a few (long) Markdown files like [this `til.md`](https://github.com/sanand0/til/blob/main/til.md).

If my phone is easier to access, I type or dictate my notes into [Microsoft To Do](https://to-do.office.com/tasks/), which is currently my most convenient note-taking app. It syncs with my laptop. I transfer it (via OCR on [Microsoft Power Toys](https://learn.microsoft.com/en-us/windows/powertoys/text-extractor)) into the Markdown file.

The Markdown files are synced across my devices using [Dropbox](https://www.dropbox.com/), which I find the most convenient and fast way to sync.

The notes have a **simple** format. Here's something I quickly wrote down in Microsoft To Do while speaking with [a senior](https://www.linkedin.com/in/krangana/) at a restaurant:

```markdown
Government websites like the official press releases cannot be crawled from outside India. Hence the need for server farms in India!
```

Then I copied that over to the Markdown file as a list item along with the date (which Microsoft To Do captures), like this:

```markdown
- 15 Dec 2024. Government websites like the official press releases cannot be crawled from outside India. Hence the need for server farms in India!
```

That's it. Quick and simple. The most important thing is to capture learnings **easily**. Even the slightest friction hurts this goal.

### Publishing learnings

I run this [Deno script](https://github.com/sanand0/til/blob/main/convert.js) which parses the Markdown files, groups them by week, and generates a set of static HTML pages. These are published on [GitHub Pages](https://pages.github.com/), which is currently my favorite way to publish static files.

It generates an [RSS feed](https://til.s-anand.net/feed.xml) as well. I've started reading more content using RSS feeds via [Feedly](https://feedly.com/), including my own notes. I find browsing through them a useful refresher.

This format is different from my [blog](/blog/). In the 1990s and early 2000s, I published individual links as posts. Then I moved to long form posts. This consolidates multiple links into a single weekly post. But rather than publish via WordPress (which is what my blog is currently based on), I prefer a Markdown-based static site. So it's separate for the moment.

I intend to continue with these notes (and the format) for the foreseeable future.

---

## Comments

<!-- wp-comments-start -->

- **[My Year in 2024 - S Anand](/blog/my-year-in-2024/)** _30 Dec 2024 10:01 pm_ _(pingback)_:
  […] Learning. I took weekly notes of things I learned. […]

<!-- wp-comments-end -->
