---
title: Drawing humans only CAPTCHAs
date: 2026-10-31T14:38:26+05:30
categories:
- links
description: I tested a drawing CAPTCHA where classmates guessed one-minute sketches while vision models failed. A ladder looked like a saw to AI, and simple caterpillar and medal strokes fooled it.
tags: [computer-vision, testing]
---

My [TDS](https://tds.s-anand.net/) course [asked](https://exam.sanand.workers.dev/tds-2026-09-ga3#hq-trading-humans-only) students to draw objects in one minute. The drawing is sent to their classmates as well as three vision models. They score if:

- Classmates guess it right
- AI guesses it wrong

In other words, can you, in 1 minute, draw something that fools AI but not humans?

Here are some of the best results, when I ran it against [GPT 6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [GLM 5.3 Flash](https://openrouter.ai/z-ai/glm-5.3-flash), and [Deepseek v4.1 Flash](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017), which are really cheap and good vision models.

### How to fool AI

[![Ladder](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0420.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0420)

AI was convinced that this [ladder](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0420) was a _saw_!

[![Ladybird](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0434.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0434)

Most people guessed this as [ladybird](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0434) (lady + bird) but Luna said "butterfly", Deepseek said "dragonfly", and GLM said "butterfly" but did, once, guess ladybird.

[![Donkey](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0242.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0242)

Everyone guessed this as [donkey](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0242). AI guessed sheep, cow, horse, pig, and even turkey.

[![Lamp](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0436.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0436)

Here's a good CAPTCHA idea. All the humans guessed this as [lamp](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0436). AI thought hammock, occasionally table or chair.

[![Caterpillar](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0148.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0148)

Everyone guessed this single stroke as a [caterpillar](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0148). But most AI thought it was a snail.

[![Medal](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0484.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0484)

Everyone guessed this single stroke as [medal](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0484) AI thought it was a whistle, tennis racket or shuttlecock.

[![Mango](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0481.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0481)

But the one that puzzles me the most is: why did AI struggle so much with this [mango](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0481)? Humans got it right. AI guessed pear - even banana.

---

### How to fool humans

This is the reverse category. AI guessed it right away but people couldn't.

[![Owl](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0524.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0524)

No, this does NOT look like an [owl](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0524) to me. People guessed: pigeon, penguin, flamingo, crow, eagle - but AI guessed owl _every_ time.

[![Seahorse](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0673.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0673)

This does NOT look like a [seahorse](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0673) to me and people guessed: jellyfish, whale, fish, lobster, whale. But AI guessed seahorse _every_ time.

[![Horse](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0364.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0364)

[Horses](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0364) are really tough to draw. People guessed: buffalo, buffalo, donkey, goat, cow. AI guessed horse almost perfectly.

### How to fool everyone

And then there are images that EVERYONE gets wrong.

[![Turkey](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0838.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0838)

That's supposed to be a [turkey](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0838).

[![Zebra](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0866.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0866)

This is a [zebra](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0866). Not a camel, giraffe, elephant, or even a kangaroo.

[![Guitar](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0771.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0771)

This is a [guitar](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0771). Not a middle finger.

[![Lemon](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0453.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0453)

Does a [lemon](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0453) have a stem and leaf, usually?

[![Shark](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0677.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0677)

Good attempt at [shark](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0677) that NO one guessed. Everyone said fish.

[![Buffalo](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0099.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0099)

It's REALLY hard to differentiate cow from [buffalo](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0099).

[![Jellyfish](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/gallery/0379.webp)](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0379)

And finally, I drew a [jellyfish](https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/#drawing=0379) like a helicopter when I was testing because I didn't see the word jellyfish!

---

Humans are _slightly_ better than AI at guessing humans' drawings. The advantage is ~3.5%.
Strikingly, 8 drawings were understood by _every_ human but missed by _every_ AI. Only 2 drawings were the reverse.

GLM 5.3 guesses very similar to humans (75%), while DeepSeek 4.1 Flash is next closest (73%), and GPT 6 Luna the furthest of the three (68%).

<table>
  <thead>
    <tr>
      <th scope="col" style="text-align: left;">↓ Humans / AI →</th>
      <th scope="col" style="text-align: left;">Right</th>
      <th scope="col" style="text-align: left;">Partly right</th>
      <th scope="col" style="text-align: left;">Wrong</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row" style="text-align: left;">Right</th>
      <td style="text-align: right; background-color: rgb(8, 48, 107); color: rgb(255, 255, 255);">368</td>
      <td style="text-align: right; background-color: rgb(181, 212, 233); color: rgb(0, 0, 0);">112</td>
      <td style="text-align: right; background-color: rgb(244, 249, 254); color: rgb(0, 0, 0);">8</td>
    </tr>
    <tr>
      <th scope="row" style="text-align: left;">Partly right</th>
      <td style="text-align: right; background-color: rgb(188, 215, 235); color: rgb(0, 0, 0);">104</td>
      <td style="text-align: right; background-color: rgb(98, 167, 210); color: rgb(255, 255, 255);">196</td>
      <td style="text-align: right; background-color: rgb(232, 241, 250); color: rgb(0, 0, 0);">30</td>
    </tr>
    <tr>
      <th scope="row" style="text-align: left;">Wrong</th>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">2</td>
      <td style="text-align: right; background-color: rgb(240, 246, 253); color: rgb(0, 0, 0);">15</td>
      <td style="text-align: right; background-color: rgb(231, 241, 250); color: rgb(0, 0, 0);">31</td>
    </tr>
  </tbody>
</table>

<!-- https://chatgpt.com/c/6ae41598-0df8-83ec-8451-f1f784a34dac -->
