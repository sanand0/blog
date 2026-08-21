---
title: Submitting an AI-ded VizChitra Proposal
date: '2026-02-15T10:49:04+08:00'
categories:
- how-i-do-things
- visualisation
- llms
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7428649582768693248/
description: I used Gemini to turn VizChitra's submission HTML into structured data, then had Gemini, Claude, and ChatGPT develop and rank topics before editing Claude's draft for a new proposal.
tags: [generative-ai, prompt-engineering, data-visualization, ai-agents]
---

![](https://files.s-anand.net/images/2026-02-15-submitting-an-ai-ded-vizchitra-proposal.avif)

**10:20 am**. After submitting my [VizChitra 2026](https://vizchitra.com/2026) [talk proposal](/blog/can-ai-discover-new-data-visualizations/), did a quick analysis of the [submissions](https://vizchitra.com/2026/submissions).

1. Copy the HTML from the [submissions page](https://vizchitra.com/2026/submissions) and paste into Gemini.
2. [Ask it](https://gemini.google.com/share/ce2853c02d63): "Given this HTML, share a JS snippet I can copy and paste into DevTools that will return an array of objects containing all the useful information about each submission."
3. Paste the JS snippet into DevTools and get the structured result.

Here's the breakdown of submissions (excluding exchibitions):

<!--

|           | Community | Craft | Work | Tools |
| --------- | --------: | ----: | ---: | ----: |
| Talks     |        10 |     9 |    8 |     3 |
| Workshop  |         4 |     2 |    1 |     3 |
| Dialogues |         1 |     0 |    1 |     1 |

-->

<table>
  <thead>
    <tr>
      <th scope="col" style="text-align: left;"></th>
      <th scope="col" style="text-align: left;"></th>
      <th scope="col" style="text-align: left;">Community</th>
      <th scope="col" style="text-align: left;">Craft</th>
      <th scope="col" style="text-align: left;">Work</th>
      <th scope="col" style="text-align: left;">Tools</th>
      <th scope="col" style="text-align: left;"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left;"></td>
      <td style="text-align: left;">Talks</td>
      <td style="text-align: right; background-color: rgb(0, 104, 55); color: rgb(255, 255, 255);">10</td>
      <td style="text-align: right; background-color: rgb(34, 150, 79); color: rgb(255, 255, 255);">9</td>
      <td style="text-align: right; background-color: rgb(100, 188, 97); color: rgb(255, 255, 255);">8</td>
      <td style="text-align: right; background-color: rgb(252, 172, 99); color: rgb(0, 0, 0);">3</td>
      <td style="text-align: left;"></td>
    </tr>
    <tr>
      <td style="text-align: left;"></td>
      <td style="text-align: left;">Workshop</td>
      <td style="text-align: right; background-color: rgb(254, 221, 141); color: rgb(0, 0, 0);">4</td>
      <td style="text-align: right; background-color: rgb(241, 110, 67); color: rgb(255, 255, 255);">2</td>
      <td style="text-align: right; background-color: rgb(212, 50, 44); color: rgb(255, 255, 255);">1</td>
      <td style="text-align: right; background-color: rgb(252, 172, 99); color: rgb(0, 0, 0);">3</td>
      <td style="text-align: left;"></td>
    </tr>
    <tr>
      <td style="text-align: left;"></td>
      <td style="text-align: left;">Dialogues</td>
      <td style="text-align: right; background-color: rgb(212, 50, 44); color: rgb(255, 255, 255);">1</td>
      <td style="text-align: right; background-color: rgb(165, 0, 38); color: rgb(255, 255, 255);">0</td>
      <td style="text-align: right; background-color: rgb(212, 50, 44); color: rgb(255, 255, 255);">1</td>
      <td style="text-align: right; background-color: rgb(212, 50, 44); color: rgb(255, 255, 255);">1</td>
      <td style="text-align: left;"></td>
    </tr>
  </tbody>
</table>

There's only one whitespace: a Dialogue for "Visualizations as Craft".

---

**10:40 am**. Obviously, I have to submit my next proposal. Partly out of fear that my other proposal will be rejected in a the crowded "Visualizations as Craft" category, and partly to see if I can write a cool blog post about "How I used AI to maximize submission acceptance".

So, I tasked [Gemini 3 Pro](https://gemini.google.com/share/046be4e91f1f), [Claude Opus 4.6 - Extended Thinking](https://claude.ai/share/04b6d5c0-2d23-4ede-ae60-7b49cf213508), and [ChatGPT 5.2 Extended Thinking - Web Search](https://chatgpt.com/share/69913840-1ce0-8003-a6e5-3c302f39ee41):

<!--
https://gemini.google.com/app/909c8c360214a631
https://claude.ai/chat/74c695ae-11da-413f-9489-b908efdb0bdb
https://chatgpt.com/c/69913513-1ab0-83a6-ab7f-8fbc6bb15dfa
-->

> I want to submit a VizChitra 2026 proposal for a Dialogue in the "Visualizations as Craft".
>
> Here are the CFP details and other dialogue proposals for your reference
>
> Research online for about the latest trends in AI in the craft of visualization and propose 10 topics for a Dialogue in the "Visualizations as Craft" category. Finally rank order these topics along with reason why this would be most useful for the community.

Then, rather than read it, I asked each other:

> Here are the suggestions from other AI agents. Think about their opinion, factor in points that are better than what you suggested, drop what's not as good, and recommend the top 3 topics. Also mention who had the best topics among you and the other two AI agents and why.

ChatGPT and Gemini said Claude had the best ideas. Claude said Gemini.

"The Curator's Dilemma" bubbled up as the top idea. Then I asked each:

> Which agent's writing style (you vs the other two) would be best to frame a winning proposal for "The Curator's Dilemma"?

Gemini and ChatGPT voted for themselves. Claude said none of these - write your own. The

- **Claude:** Structured, thorough, and thoughtful with a poetic sensibility, but can come across as impersonal or overly soft — more like a well-organized conference paper than a passionate human voice.
- **Gemini:** Punchy, direct, and provocatively sharp with a pragmatic edge, but can lean too declarative and confident, leaving little room for open-ended exploration.
- **ChatGPT:** Highly analytical and structured with reviewer-friendly specificity, but tends toward a generic, corporate tone that lacks warmth, humor, and creative soul.

Anyway, I picked Claude and told it:

> OK, write the proposal in for it, for now in your voice, and then I'll rewrite it in my voice.

---

**11:10 am**. I converted the text to ASCII to prevent obvious AI detection like em-dashes, and started editing it the way I'd write it (the content was _really_ good, actually, so editing was easy)

**11:30 am**. Finished editing. I was pleasantly surprised to find my co-founder Ganes Kesari's [Sloan Review article on "The Enduring Power of Data Storytelling in the Generative AI Era"](https://sloanreview.mit.edu/article/the-enduring-power-of-data-storytelling-in-the-generative-ai-era/) as a reference. I might even have added a sentence or two to it. Small world!

It was also impressive how little I had to edit. It think it's because:

- This is a really good topic that resonates with me. I really have this problem and want to learn about it.
- It clearly knew how to run a workshop better than I did. E.g. I would have picked 20 visualizations for the participants to review. But it knew we'd run out of time.
- It writes really well. More verbose than me, but I found it hard to edit out the emotional punch I got from the phrases.

---

Anyway, the proposal will be on the [submissions page](https://vizchitra.com/2026/submissions) soon. It takes a little over an hour to come up with a _good_ proposal if you know the topic well.

So: **experts in any field** - you have less excuses not to submit more proposals. (Deep research prompt: As an expert in [TOPIC], suggest where I could submit proposals for talks.)
