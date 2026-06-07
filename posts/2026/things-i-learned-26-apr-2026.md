---
title: Things I Learned - 26 Apr 2026
date: 2026-04-26T00:00:00+00:00
categories:
  - til
description: I tested Cloudflare Browser Run and GPT 5.5, added gpt-image-2 to my art gallery, and learned Pandoc tricks for Word comments. I also found a workaround for nested git repositories and explored MCP server auth complexities.
keywords: [mdq, cloudflare browser run, gpt 5.5, gpt-image-2, pandoc, mcp server, git, claude code]
---

This week, I learned:

- `mdq` is pretty useful to extract Markdown sections. For example `cat *.md | mdq '# Title'` extracts all sections where the header contains 'Title' (case-insensitive).
- [CloudFlare Browser Run](https://developers.cloudflare.com/browser-run/) is, roughly, a browser as a service. [Pricing](https://developers.cloudflare.com/browser-run/pricing/): 10 hours free per month, then 9c per hour. I had Codex run a small [research](https://github.com/sanand0/research/tree/main/cloudflare-browser-run) to explore it, and it seems simple to set it up and use it.
- [GPT 5.5](https://openai.com/index/introducing-gpt-5-5/) seems to be especially better than GPT 5.4 and running for long, with tool calls, without losing focus. That's something OpenAI models are good at anyway, so this takes it a step further. [ChatGPT](https://chatgpt.com/share/69eaccb0-b9e0-8399-be3f-6bd73906d0ec)
- I added [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) to my [LLM Art Style gallery](https://sanand0.github.io/llmartstyle/). It is notably better with text accuracy. For example, on [Rock - Paper - Scissors - Lizard - Spock](https://sanand0.github.io/llmartstyle/?category=text) it consistently lists all 10 rules, which Nano Banana 2 does not.
- World leaders do keep us entertained. <!-- https://gemini.google.com/app/240186d320b283d8 -->
  - Saparmurat Niyazov (Turkmenistan) renamed the months of the year and days of the week after himself and his mother. He built a towering, gold-plated statue of himself in the capital that rotated so it would always face the sun. He also banned lip-syncing at concerts, outlawed gold teeth, and banished dogs from the capital because he found their smell unappealing.
  - Idi Amin (Uganda) declared himself the "Uncrowned King of Scotland" and sent baffling, unsolicited telegrams to world leaders - advising Richard Nixon to recover from Watergate, or offering food aid to a struggling Britain.
  - François "Papa Doc" Duvalier (Haiti) reportedly ordered all black dogs in Haiti to be put to death and claimed his personal Vodou curse was responsible for the assassination of John F. Kennedy.
  - Francisco Macías Nguema (Equatorial Guinea) banned the word "intellectual", banned the use of lubricants in the power plant (claiming his magic would keep it running, which promptly broke the generators), and stored the nation's remaining foreign currency under his bed.
  - Kim Jong-il (North Korea) claimed he invented the hamburger (calling it "double bread with meat") and shot 11 holes-in-one his first time playing golf.
  - Donald Trump (United States) used late-night tweets to announce major policy shifts and fire his own cabinet members. He altered an official government hurricane map with a Sharpie to match a previous erroneous statement, and publicly mused during a press briefing about the injection of household disinfectants as a medical treatment.
- Git repositories inside git repositories (without using sub-modules) don't seem to work well. I need this because I have mono-repos for research and I want to use git in a sub-folder to iterate, then commit just the final version to the parent folder. Looks like I need to remove the child `.git/` (e.g. rename to `.git.bak/`, which I've added to my `~/.config/git/ignore`) for this to work. [Gemini](https://gemini.google.com/share/1a89ad8cf6da)
- To run a script in the background (without logs) and detach / disown it, use `nohup your-script >/dev/null 2>&1 & disown`
- Running `/insights` on Claude Code helped me add these two instructions to my [code skill](https://github.com/sanand0/scripts/blob/main/agents/code/SKILL.md):
  - Test web pages with screenshots (for layout, overlaps, contrast) AND CDP (for interactions, navigation) before finalizing
  - Prefer icon libraries over unicode/emoji icons.
- Sending an entire PDF/PPTX to Gemini costs ~40% of sending PDF/PPTX + images. The quality is fine for small files, but for large files adding images reduces error rate from ~5% to 0.5%.
- Pandoc Markdown to Word DOCX supports sidebar comments. You can use this Markdown: Here is `[comment in sidebar]{.comment-start id="c1" author="Anand" date="2026-01-01T12:00:00Z"}commented text[]{.comment-end id="c1"} inline.` [Gemini](https://gemini.google.com/share/430e7556ad69). In fact, Pandoc supports lots of other things, like: <!-- https://gemini.google.com/app/0fe9e7b12650f7f2 -->
  - Custom styles via block `::: {custom-style="Custom Style Name"}`
  - Track changes via `[inserted text]{.insertion author="Name" date="2026-04-20T12:00:00Z"}` and `[deleted text]{.deletion author="Name"}`
  - Page breaks via `\newpage` (a LaTeX command that Pandoc supports in Markdown)
  - CSS styles via `![Alt Text](image.png){width="5.5in" height="3in"}`
- [Offpunk](https://offpunk.net/) is a CLI offline-first browser. Interesting idea, but installation is a problem.
  After `sudo apt uninstall offpunk` running `offpunk` failed with `ImportError: lxml.html.clean module is now a separate project lxml_html_clean.`
  After a `git clone` it reported `HTML document detected. Please install python-bs4 and python-readability`.
  These are easy to fix, but I wasn't inclined.
- Creating an authenticated [MCP Server for ChatGPT](https://developers.openai.com/api/docs/mcp) is complex. It requires OpenID Connect (for which library support is weak and requires a provider like Auth0), dynamic client registration (which is hard to implement though Auth0 supports it), and after half a day of experiments, I still couldn't connect. An easier option is to run temporary tunnels with `cloudflared` or `ngrok` or `localtunnel`.
