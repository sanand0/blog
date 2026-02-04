---
title: Gemini 3 Flash OCRs Dilbert accurately
date: 2026-02-02T18:53:15+08:00
categories:
  - llms
---

[Scott Adams](https://en.wikipedia.org/wiki/Scott_Adams), the author of [Dilbert](https://en.wikipedia.org/wiki/Dilbert), passed away last month. While his work will live on, I was curious about the best way to build a Dilbert search engine.

The first step is to extract the text. [Pavan](https://github.com/pavankumart18) tested over half a dozen LLMs on ~30 Dilbert strips to see which one transcribed them best.

[Here are the results](https://pavankumart18.github.io/comic-transcriptions/).

**Summary**: [Gemini 3 Flash](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-flash) does the best, and would cost ~$20 to process the entire Dilbert archive. But if you want a local solution, [Qwen 3 VL 32b](https://ollama.com/library/qwen3-vl:32b) is the best.

<table>
  <thead>
    <tr>
      <th scope="col" style="text-align: right;">Model</th>
      <th scope="col" style="text-align: right;">Score (%)</th>
      <th scope="col" style="text-align: right;">Text (40)</th>
      <th scope="col" style="text-align: right;">Spkr (25)</th>
      <th scope="col" style="text-align: right;">Caps (15)</th>
      <th scope="col" style="text-align: right;">Panel (10)</th>
      <th scope="col" style="text-align: right;">Halluc (10)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left;">gemini-3-flash-preview</td>
      <td style="text-align: right; background-color: rgb(0, 104, 55); color: rgb(255, 255, 255);">99.3%</td>
      <td style="text-align: right; background-color: rgb(0, 104, 55); color: rgb(255, 255, 255);">39.9</td>
      <td style="text-align: right; background-color: rgb(0, 104, 55); color: rgb(255, 255, 255);">24.4</td>
      <td style="text-align: right; background-color: rgb(0, 104, 55); color: rgb(255, 255, 255);">15.0</td>
      <td style="text-align: right; background-color: rgb(0, 104, 55); color: rgb(255, 255, 255);">10.0</td>
      <td style="text-align: right; background-color: rgb(0, 104, 55); color: rgb(255, 255, 255);">10.0</td>
    </tr>
    <tr>
      <td style="text-align: left;">qwen3-vl-32b-instruct</td>
      <td style="text-align: right; background-color: rgb(42, 156, 82); color: rgb(255, 255, 255);">96.0%</td>
      <td style="text-align: right; background-color: rgb(7, 117, 62); color: rgb(255, 255, 255);">39.8</td>
      <td style="text-align: right; background-color: rgb(132, 202, 103); color: rgb(255, 255, 255);">21.6</td>
      <td style="text-align: right; background-color: rgb(0, 104, 55); color: rgb(255, 255, 255);">15.0</td>
      <td style="text-align: right; background-color: rgb(18, 134, 70); color: rgb(255, 255, 255);">9.9</td>
      <td style="text-align: right; background-color: rgb(29, 145, 76); color: rgb(255, 255, 255);">9.7</td>
    </tr>
    <tr>
      <td style="text-align: left;">llama-4-maverick</td>
      <td style="text-align: right; background-color: rgb(247, 248, 173); color: rgb(0, 0, 0);">85.1%</td>
      <td style="text-align: right; background-color: rgb(205, 234, 133); color: rgb(0, 0, 0);">38.5</td>
      <td style="text-align: right; background-color: rgb(251, 162, 93); color: rgb(255, 255, 255);">16.3</td>
      <td style="text-align: right; background-color: rgb(48, 160, 84); color: rgb(255, 255, 255);">13.2</td>
      <td style="text-align: right; background-color: rgb(254, 234, 158); color: rgb(0, 0, 0);">9.1</td>
      <td style="text-align: right; background-color: rgb(254, 236, 160); color: rgb(0, 0, 0);">8.1</td>
    </tr>
    <tr>
      <td style="text-align: left;">llama-4-scout</td>
      <td style="text-align: right; background-color: rgb(252, 244, 170); color: rgb(0, 0, 0);">84.1%</td>
      <td style="text-align: right; background-color: rgb(129, 201, 102); color: rgb(255, 255, 255);">39.0</td>
      <td style="text-align: right; background-color: rgb(251, 167, 96); color: rgb(255, 255, 255);">16.4</td>
      <td style="text-align: right; background-color: rgb(80, 178, 93); color: rgb(255, 255, 255);">12.5</td>
      <td style="text-align: right; background-color: rgb(238, 102, 64); color: rgb(255, 255, 255);">8.7</td>
      <td style="text-align: right; background-color: rgb(249, 150, 87); color: rgb(255, 255, 255);">7.5</td>
    </tr>
    <tr>
      <td style="text-align: left;">gemma-3-27b-it</td>
      <td style="text-align: right; background-color: rgb(254, 211, 130); color: rgb(0, 0, 0);">81.3%</td>
      <td style="text-align: right; background-color: rgb(254, 233, 156); color: rgb(0, 0, 0);">37.8</td>
      <td style="text-align: right; background-color: rgb(165, 0, 38); color: rgb(255, 255, 255);">13.1</td>
      <td style="text-align: right; background-color: rgb(11, 124, 65); color: rgb(255, 255, 255);">14.4</td>
      <td style="text-align: right; background-color: rgb(165, 0, 38); color: rgb(255, 255, 255);">8.4</td>
      <td style="text-align: right; background-color: rgb(251, 168, 97); color: rgb(255, 255, 255);">7.6</td>
    </tr>
    <tr>
      <td style="text-align: left;">nemotron-nano-12b-v2-vl-free</td>
      <td style="text-align: right; background-color: rgb(254, 211, 130); color: rgb(0, 0, 0);">81.3%</td>
      <td style="text-align: right; background-color: rgb(192, 228, 124); color: rgb(0, 0, 0);">38.6</td>
      <td style="text-align: right; background-color: rgb(165, 0, 38); color: rgb(255, 255, 255);">13.1</td>
      <td style="text-align: right; background-color: rgb(11, 124, 65); color: rgb(255, 255, 255);">14.4</td>
      <td style="text-align: right; background-color: rgb(195, 31, 40); color: rgb(255, 255, 255);">8.5</td>
      <td style="text-align: right; background-color: rgb(165, 0, 38); color: rgb(255, 255, 255);">6.6</td>
    </tr>
    <tr>
      <td style="text-align: left;">molmo-2-8b-free</td>
      <td style="text-align: right; background-color: rgb(165, 0, 38); color: rgb(255, 255, 255);">70.4%</td>
      <td style="text-align: right; background-color: rgb(165, 0, 38); color: rgb(255, 255, 255);">36.2</td>
      <td style="text-align: right; background-color: rgb(251, 167, 96); color: rgb(255, 255, 255);">16.4</td>
      <td style="text-align: right; background-color: rgb(165, 0, 38); color: rgb(255, 255, 255);">0.5</td>
      <td style="text-align: right; background-color: rgb(248, 141, 82); color: rgb(255, 255, 255);">8.8</td>
      <td style="text-align: right; background-color: rgb(241, 248, 170); color: rgb(0, 0, 0);">8.4</td>
    </tr>
  </tbody>
</table>

That accuracy of 99.3% is impressive. Here's the biggest error it made:

![](https://web.archive.org/web/20230301061931im_/https://assets.amuniversal.com/d999ece0979e012f2fe400163e41dd5b)

1. Dogbert: CHAPTER IV. "TIME MANAGEMENT"
2. Dogbert: "ALWAYS POSTPONE MEETINGS WITH TIME-WASTING MORONS."\
   Dilbert: "HOW DO YOU DO THAT?"
3. Dogbert: CAN I GET BACK TO YOU ON THAT?

Can you spot the error? The model attributed the text to Dogbert instead of the computer. (But you _could_ argue that Dogbert is the one typing it...)

---

Here's another error:

![](https://web.archive.org/web/20230228074232im_/https://assets.amuniversal.com/7cf00b10979d012f2fe400163e41dd5b)

1. Dilbert: I'VE DECIDED WE SHOULD OPERATE ALONG MORE CLASSIC LINES, LIKE DR. FRANKENSTEIN'S LAB.
2. Dogbert: YOU KNOW WHAT THAT MAKES YOU?
3. Dogbert: I'VE GOT A HUNCH...
4. Dilbert: LET'S PRACTICE...
5. Dilbert: DOGBERT, FETCH ME A BRAIN!\
   Dogbert: LIKE YOUR PRESENT MODEL, OR ONE THAT WORKS?

Can you spot the error? In Panel 2, it's Dilbert speaking, not Dogbert.

---

In fact, the only transcription errors Gemini 3 Flash made was writing "McDONALD'S" instead of "MCDONALD'S" ([see panel 2](https://web.archive.org/web/20230228083128im_/https://assets.amuniversal.com/3eb64cb0979e012f2fe400163e41dd5b)), and not hyphenating a line-break in "PRESEN-TATION" ([see panel 4](https://web.archive.org/web/20230228231330im_/https://assets.amuniversal.com/03d47960979f012f2fe400163e41dd5b)).

Qwen 3 VL 32b made almost as few errors. The bigger gap is in speaker detection, where the models fall off steeply.

---

This incredibly low cost + high accuracy enables a _number_ of new things. For example:

- **Infrastructure Serial Tracking:** Extract serial numbers and maintenance dates from photos of utility meters, fire hydrants, streetlights, etc. to build a live digital twin of city assets.
- **Small-Business Permit Audits:** Process photos of street-facing shop permits to flag expired licenses.
- **Evidence Label Transcription:** Annotate small-text labels on physical exhibits in legal archives, e.g. "Exhibit A" becomes "Exhibit A: Photo of the crime scene taken on 03/15/2020 at 14:32 by Officer J. Smith."

---

I spent [7 years typing out every one of the ~3,000 Calvin & Hobbes strips by hand](https://www.s-anand.net/blog/the-calvin-and-hobbes-search-takedown/). For these ~12,000 Dilbert strips, it might take a few hours and a few dollars for the same.
