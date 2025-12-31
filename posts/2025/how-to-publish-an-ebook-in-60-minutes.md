---
title: How to publish an eBook in 60 minutes
date: "2025-03-31T12:47:13Z"
lastmod: "2025-04-03T07:48:34Z"
categories:
  - how-i-do-things
  - llms
wp_id: 4000
---

![How to publish an eBook in 60 minutes](https://files.s-anand.net/images/2025-03-31-an-lbs-exchange-program-ebook-cover.webp)

I [published an eBook on Amazon](https://www.amazon.in/dp/B0F3D55R2Z/). It takes an hour **if you have the content ready**.

**STEP 1** (10 min): [Set up a Kindle Direct Publishing account](https://account.kdp.amazon.com/) with your address, bank details, and tax info.

**STEP 2** (15 min): [Export](https://wordpress.com/support/export/) my [London 2000](/blog/category/london-2000/) blog archive and [convert to Markdown](https://github.com/lonekorean/wordpress-export-to-markdown).

**STEP 3** (10 min): Reformat the Markdown by writing a script in [Cursor](https://cursor.com/). Here's the prompt:

> Write a Python script that reads `*.md` including the YAML frontmatter, adds the YAML `title` as H1, `date` (yyyy-mm-dd) like **Sun, 01 Jan 2000** in a new para after the frontmatter and before the content.

**STEP 4** (15 min): Convert it to an ePub using [pandoc](https://pandoc.org/).

```bash
pandoc *.md -o book.epub --toc \
  --metadata title="An LBS Exchange Program" \
  --metadata author="Anand S" \
  --metadata language=en \
  --metadata date="31 Mar 2025"
```

**STEP 5** (10 min): Generated a cover page with [ChatGPT](https://chatgpt.com/) (5 min) and compressed it into JPEG via [Squoosh](https://squoosh.app/).

> Draw a comic-style book cover page that covers the experiences of an Indian exchange student (picture attached) from IIM Bangalore at London Business School and exploring London. The book title is "An LBS Exchange Program".

**STEP 6** (10 min): [Publish the book on KDP](https://kdp.amazon.com/). It's priced at $0.99 / ₹49 because Kindle doesn't allow free downloads.

That's it. Here's the book: <https://www.amazon.in/dp/B0F3D55R2Z/>

The three things that made publishing in 1 hour possible are:

1. Amazon's publishing process is **simple**.
2. Open-source tooling ([WordPress](https://wordpress.org/), [Markdown](https://en.wikipedia.org/wiki/Markdown), [ePub](https://en.wikipedia.org/wiki/EPUB), [pandoc](https://pandoc.org/)) has built a big part of the infrastructure.
3. LLMs make the rest ([figuring out the steps](https://chatgpt.com/share/67ea8da7-7f90-800c-a89c-6f087e893749), generating the cover) very easy.

(An eBook takes 72 hours of review before going live on the Kindle store.)

[LinkedIn](https://www.linkedin.com/feed/update/urn%3Ali%3Ashare%3A7314884520820854784)
