---
date: "2025-07-01T04:07:38Z"
categories:
  - linkedin
---

I catch up on long WhatsApp group discussions as podcasts.

The quick way is to scroll on WhatsApp Web, select all, paste into NotebookLM, and create the podcast.

Mine is a bit more complicated. Here's an example:

- Use a bookmarklet to scrape the messages https://tools.s-anand.net/whatsappscraper/
- Generate a 2-person script https://github.com/sanand0/generative-ai-group/blob/main/config.toml
- Have `gpt-4o-mini-tts` convert each line using a different voice https://www.openai.fm/
- Combine using `ffmpeg` https://ffmpeg.org/
- Publish on GitHub Releases https://github.com/sanand0/generative-ai-group/releases/tag/main

I run this every week. So far, it's proved quite enlightening.

- Podcast: https://github.com/sanand0/generative-ai-group/releases/download/main/podcast.xml
- Code: https://github.com/sanand0/generative-ai-group

![](https://files.s-anand.net/images/2025-07-01-generative-ai-whatsapp-group-podcast-linkedin.jpg)

[LinkedIn](https://www.linkedin.com/feed/update/urn%3Ali%3Ashare%3A7345664356799401986)
