---
title: My food preferences
date: 2026-04-24T14:09:36-04:00
categories:
  - llms
  - how-i-do-things
description: Using ChatGPT to conduct a targeted interview and analyze a daily food log generates a concise, AI-readable specification of dining preferences to improve automated restaurant recommendations.
keywords: [ai restaurant recommendations, chatgpt prompt, food preference profile, personal context specification, food log analysis]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7453512626417975296/
---

I use ChatGPT to recommend which restaurant I should eat at and what food I should eat. So often that I decided to share a profile of my eating preferences.

![](https://files.s-anand.net/images/2025-04-24-my-food-preferences-2.avif) <!-- https://chatgpt.com/c/69ebb649-60d8-839c-8c04-9438af5f9c66 -->

But rather than think about it and type it myself, I asked it to

> Efficiently interview me to identify my food preferences. Document it for AI agents to help me pick restaurants. Plan like an expert.

(Knowing ChatGPT, I also had add "efficiently" - otherwise it would give me a huge list of questions! Which it did that anyway...)

That makes it easy. Now, I just have to answer questions about my preferences, e.g. my budget range, restaurant styles, cuisines etc.

I also gave it a dump of my daily food log. (This year I've been logging all the food that I eat - for no reason actually - along with which of those I liked and disliked.) This proved to be a good idea, because it picked up something I didn't realize:

> You are unusually tolerant of repeating humble comfort foods at home, ...

Very true. I ate curd rice day and night for 22 years at every meal. I eat [Kaya Peanut Toast](https://app.yakun.com/kaya-peanut-toast.html) every day at Ya Kun Kaya Toast. (They make it the instant they see me standing at the back of the line, and miss me when I travel.)

So, here's my tweaked version of [ChatGPT's recommended food spec](https://chatgpt.com/share/69ebb1d6-a528-839e-a410-4141b84a15a9) on how agents should pick for me:

```markdown
Eggetarian. No meat or seafood; eggs & milk are OK.
Prioritize novel cuisines & known exceptional dishes.
Prefer casual, functional, non-fine dining. SGD $5-20 feels fine.
Any cuisine works: Indian, Italian, Mediterranean, Middle Eastern, ...
Creamy > crunchy > gooey > chewy > airy.
Spicy is good. Heavy, raw, or loud are bad.
Desserts are great! Too sweet is bad.
E.g. creative fusion, chaat, inventive small plates, nutty flavors, hot cookies, textured desserts.
Prefer 10 min travel, 5 min wait. For exceptional food in a new city, an hour is OK.
```

PS: This is styled _quite_ differently from how ChatGPT writes, but the content was correct.

<!--
https://chatgpt.com/c/69e90e35-f72c-839d-a67e-df335251d420
https://claude.ai/chat/108b839f-7217-49b0-ad0e-a12e68cf0efe
-->
