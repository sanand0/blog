---
title: How IMF mis-forecasts GDP growth
date: 2026-06-22T10:41:30+08:00
categories:
  - data
  - visualization
  - llms
description: I used LLMs to audit IMF GDP forecasts, revealing a systematic optimistic bias for future growth. You can use AI to fact-check institutional datasets, identify specific country-level errors, and generate interactive visualizations to expose hidden patterns.
keywords: [imf, gdp growth, forecast accuracy, data visualization, llms, world economic outlook]
---

The IMF forecasts GDP growth every year. Their forecasts for the current year are slightly low. Their forecasts for the next year are slightly high. After that, it remains high.

![](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/screenshot.avif)

Some forecasts, like
[China](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/#country=China),
[Singapore](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/#country=Singapore),
[UAE](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/#country=United+Arab+Emirates),
[Equatorial Guinea](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/#country=Equatorial+Guinea)
are consistently low.

Other forecasts, like
[Japan](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/#country=Japan),
[Congo](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/#country=Congo%2C+Democratic+Republic+of+the),
[Mexico](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/#country=Mexico),
[Pakistan](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/#country=Pakistan)
are consistently high.

---

The interesting meta-pattern is how this sort of past-forecast analysis can be done for any topic. This emerged from an [Ethan Mollick post](https://bsky.app/profile/emollick.bsky.social/post/3moraa7zius2c) and then I asked:

- **Me**: Ethan Mollick had GPT-5.5 Pro update his grad school paper. Cool! What can I do like this?
- **[Claude](https://claude.ai/share/a79319c0-96a1-4e18-a2ed-c0911e232875)**: Analyze your past work - like your blog posts.
  1. Fact-check it
  2. Find wrong sources
  3. Critique it
  4. Find contradictions
  5. Find buried ledes / unbuilt sequels
  6. Find what aged badly. What's the pattern?
- **Me**: Um, what about others' work?
- **[Claude](https://claude.ai/share/a79319c0-96a1-4e18-a2ed-c0911e232875)**: Sure!
  1. Check IMF GDP forecast accuracy
  2. Check target market size forecasts
  3. Check company / asset price forecasts
  4. Find which books are based on studies no longer true
  5. Find sources of popular stats that are wrong
  6. Find what numbers people quietly revised
- **Me**: Where can I find IMF GDP forecasts?
- **[ChatGPT](https://chatgpt.com/share/6a389d6e-4180-83e8-a759-95734a64b000)**: On the [IMF Data WEO site](https://data.imf.org/en/datasets/IMF.RES%3AWEO)
- **Me**: Check IMF GDP forecast accuracy.
- **[ChatGPT](https://chatgpt.com/share/6a389d6e-4180-83e8-a759-95734a64b000)**: The IMF has a modest optimistic bias for future-year GDP-growth forecasts, but not for same-year nowcasts.
- **Me**: Translate that to English.
- **[ChatGPT](https://chatgpt.com/share/6a389d6e-4180-83e8-a759-95734a64b000)**: For the current year, IMF typically underestimates. Next year onwards, they typically overestimate.
- **Me**: Why? How?
- **[ChatGPT](https://chatgpt.com/share/6a38a70d-4f34-83ee-b193-0b3dd2351422)**: IMF has systematic biases.
  - Advanced economies are easier to forecast and slightly less biased
  - Some countries (China, UAE, ...) are largely under-forecasted. Others (DR Congo, Haiti, ...) are consistently over-forecasted.
  - They underpredicts extremes in both directions.
  - When their forecast is very high, it is more likely to be too high.
  - Corrections are timid. They don't close old error gap until very late.
- **Me**: Draw this as a dot chart.
- **[ChatGPT](https://chatgpt.com/share/6a389d6e-4180-83e8-a759-95734a64b000)**: OK
- **Me**: Spread out the dots.
- **[ChatGPT](https://chatgpt.com/share/6a389d6e-4180-83e8-a759-95734a64b000)**: OK
- **Me**: Let me filter by country.
- **[ChatGPT](https://chatgpt.com/share/6a389d6e-4180-83e8-a759-95734a64b000)**: OK
- **Me**: Let me permalink to the selection.
- **[ChatGPT](https://chatgpt.com/share/6a389d6e-4180-83e8-a759-95734a64b000)**: OK
- **Me**: Split this into a HTML and JSON file.
- **[ChatGPT](https://chatgpt.com/share/6a389d6e-4180-83e8-a759-95734a64b000)**: OK

... and [here is the data visualization](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/).

<!--
Ideation: https://claude.ai/chat/0943a775-b971-41f5-b578-3bf9319642a6
Data visualization: https://chatgpt.com/c/6a3863f4-6798-83ee-ae5c-6d17ee525ce6
Data analysis: https://chatgpt.com/c/6a387079-6dc0-83ee-ac9e-df650426ddd1
-->
