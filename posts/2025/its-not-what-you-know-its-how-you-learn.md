---
title: It's not what you know. It's how you learn
date: "2025-03-27T15:06:11Z"
lastmod: "2025-03-28T02:24:56Z"
categories:
  - data
  - llms
wp_id: 3972
---

![It's not what you know. It's how you learn](/blog/assets/calvin.webp)

[Simon Willison's blog post](https://simonwillison.net/2024/Nov/11/mdn-browser-support-timelines/) mentioned [MDN's browser compatibility tables](https://github.com/mdn/browser-compat-data/) that list the earliest release date for each browser feature. I figured: let's see **which browsers release features fastest**.

I calculated average delay for each browser's feature release. For each browser, I looked at how many days after the first release it took to add a feature, averaged it, and published an [interactive, scrolly-telling data story](https://sanand0.github.io/webfeatures/).

<a href="https://sanand0.github.io/webfeatures/">![](/blog/assets/screenshot.webp)</a>

What's interesting is that I built almost all of this using LLMs in about 4 hours with

- [Cursor](https://www.cursor.com/) + [Claude 3.7 Sonnet](https://www.anthropic.com/news/claude-3-7-sonnet) for data disualization, and
- [Gemini 2.5 Experimental 03-25](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) for the story

Here's what I learned in the process.

**The real winners are off-beat stories.** Earlier, I'd spend 16-24 hours per visual. So, I'd stick to the "important" stories I wanted to tell. Now it takes four hours. That frees me to experiment and share those lesser data stories that get overlooked. **This change is incredibly powerful.**

**LLMs don't replace **all** expertise.** For example, when I saw the data, it didn't immediately tell a story. It took me some time to realize the story isn't how slow browsers are, but how browsers' speed evolved over time. For example, in Firefox's early days, it was the **only** browser actively releasing features. These days, it's one of the slowest. Figuring that out took expertise.

I spent two decades studying data visualization. So, this comes naturally to me. How does someone new build expertise?

**Expertise is a moving frontier.**

- At BCG in the early 2000s, I built interactive stories with PowerPoint. My PowerPoint skill was the critical expertise.
- At Gramener in the early 2010s, I used D3 for interactive stories. My programming skill was the critical expertise.
- Now, in the mid-twenties, LLMs write code with ease. My expertise is in choosing the right visual and shape the right narrative.

As tools change, expertise evolves. I don't know what the next frontier of expertise will be. I couldn't predict the last few. I can't predict the next.

**But LLMs can help build expertise.** In this project, I missed an opportunity to learn. I should have asked the LLM to show me a dozen options to visualize the data. For example, "Show a version geared toward an executive, a technologist, or a general audience". "Critique each." Such practice can help anyone - beginner or expert - build skill and learn. Practicing this is hard, but LLMs **do** help in this process.

But what gives me confidence is that LLMs **help me learn**. So, when the next frontier arrives, I'm less worried I'll be too old. I think we'll have tools to build expertise too.

**Update (28 Mar 2025)**: Earlier, I wrote that "LLMs don't replace expertise". I inferred that because I (an expert) could use an LLM well. [This research](https://www.oneusefulthing.org/p/the-cybernetic-teammate) with 700+ people at P&G shows that when given LLMs, outsiders perform as well as insiders. So, I corrected my statement to say, "LLMs don't replace **all** expertise."

---

## Comments

<!-- wp-comments-start -->

- **Ritwik Trivedi** _29 Mar 2025 5:29 pm_:
  This is really insightful. I especially loved the visualization and learning that it was made with the help of AI was shocking even though I have generated similar things myself. What stood out I guess was this realization that the prompts reflected expertise. You really had an intuitive idea of direction. Maybe knowledge management along with LLMs augmenting our work is the way forward.

<!-- wp-comments-end -->
