---
title: Things I Learned - 18 Jan 2026
date: 2026-01-18T00:00:00+00:00
categories:
  - til
description: I cleaned dead Python code using Vulture, explored GoatCounter for private analytics, and reviewed psychology books on performance and trauma. I also simplified Indian tax residency rules and switched to AVIF for better image compression.
tags: [avif, python]
---

This week, I learned:

- [Vulture](https://pypi.org/project/vulture) is a neat library that funds unused Python code. `uvx vulture script.py` works fairly well, out-of-box. This helps when cleaning up AI-edited scripts that often have left-over code or imports.
- One of the lightest alternatives to Google Analytics is [GoatCounter](https://goatcounter.com/). If you just want page views, referrers, browsers, OSes, countries, and devices, it's great. It's privacy-friendly (no cookies), open source, easy to self-host, free for small sites, and the data is exportable.
- The number of countries that allow visa-free entries to Indian passports is gently growing in Asia (Kazakhstan, Thailand, Sri Lanka, Malaysia, Iran, and Philippines).
- Lessons from performance books. [Claude](https://claude.ai/public/artifacts/cd4074fd-f227-4b77-8366-cdc1c2a6199b) [#](https://claude.ai/chat/ee0c099e-ed4c-46d1-9dcd-111010334375) [#](https://gemini.google.com/u/2/app/f6756cca3a258d92)
  - Summary: In early days, explore, sample. Then narrow based on interest & fit. Practice hard and persist.
  - ⭐⭐⭐⭐ Range (David Epstein): In changing environments (rules shift, feedback is noisy/late), sample broadly, i.e. generalize. [Specialization vs generalization](https://chatgpt.com/share/68902bbf-bf58-800c-b6b5-9ae787fa9c26)
    - Nobel laureates have more hobbies. Olympic athletes have less. Shift nurses have same hobbies as non-shift workers. [Hobbies help expertise in some areas](https://chatgpt.com/share/6894691e-f530-800c-b594-824814559dd2)
    - Rewarding ONLY what succeeds locks behavior, halts exploration. Vary / delay incentives. Reward AFTER figuring out what works. [Reinforcement and rewards](https://chatgpt.com/share/68946330-d714-800c-b845-ca86df7729b6)
    - Maybe "orderly" people specialize and creative people generalize? So pick what aligns with personality?
  - ⭐⭐⭐ Peak (Anders Ericsson & Robert Pool): Compounded practice at the edge of competence, with good immediate feedback, helps 14-26%.
    - But talent (genetics, upbringing, brainpower) differentiates more the expert level.
    - Slow, effortful practice (spaced recall, interleaving topics, self-testing) builds lasting knowledge - but looks inefficient and doesn't help with exams. [Learning and long-term retention](https://chatgpt.com/share/689180c7-03a0-800c-a5d4-5a455429e97f)
    - "Easy" 10K hours don't help.
  - ⭐⭐ Grit (Angela Duckworth): predicts roughly the same as conscientiousness (18%). It predicts success in stable paths moderately (but brainpower, etc. matter too).
    - But premature grit hurts. Quit if it helps.
    - But environment can defeat grit.
- Lessons from attention economy books. [Claude](https://claude.ai/public/artifacts/ce1ce275-1d79-443b-bfd6-9a6f2a3ddfbe) [#](https://claude.ai/chat/1fdda7c7-9d70-47d9-9a4c-7e54c16091da) [#](https://gemini.google.com/u/2/app/6cbffbe94a9a4e2c)
  - The attention economy is real. It is _designed_ to capture our mind, and it is winning.
  - Distractions hurt _MUCH_ more than we think. Batching, focus time helps.
  - Privilege helps. The rich have more control over these than the poor do.
  - ⭐⭐⭐⭐ Deep Work (Cal Newport, 2016) and ⭐⭐⭐ Digital Minimalism (Cal Newport, 2019): control the tools. **Focus time, digital detox, embrace boredom**. This helps - when you can afford to.
  - ⭐⭐⭐ Indistractable (Nir Eyal): control yourself. The problem is internal (also true), so **build habits**, since willpower depletes (hm... not really).
  - ⭐⭐⭐ How to Do Nothing (Jenny Odell, 2019): reject. **Embrace boredom** as resistance. This helps - when you can afford to.
  - ⭐⭐ Stolen Focus (Johann Hari, 2022): regulate & rebel. The problem is systemic and external (also true). **Reclaim your interface**.
  - BTW: Goldfish have _excellent_ attention spans and memory :-)
- Lessons from trauma books. [Claude](https://claude.ai/public/artifacts/b3e2120b-d65f-4beb-94d0-7e8a710bafb9) [#](https://claude.ai/chat/d33b75b9-a4ed-4972-8f31-c1e34b00b194) [#](https://gemini.google.com/u/2/app/ca92bd9b7c2c2549)
  - ⭐⭐⭐ The Body Keeps the Score (Bessel van der Kolk, 2014): trauma recall shuts down the speech area. Eye movement desensitization (EMDR) helps. So does CBT, despite what the book says. But does yoga (only a little) or neurofeedback (too little data)?
  - ⭐⭐⭐ What Happened to You? (Bruce Perry & Oprah Winfrey, 2021): calming people down before talking. Strong connections help more than a therapist.
  - ⭐⭐ The Myth of Normal (Gabor Maté, 2022): trauma causes cancer (no), autoimmunity (partly), ALS (?), etc.
  - ⭐ It Didn’t Start with You (Mark Wolynn, 2016): maybe anxiety is epigenetic and heriditary? Unproven. [Family Constellation Therapy](https://en.wikipedia.org/wiki/Family_Constellations) is wrong
  - ⭐⭐ My Grandmother’s Hands (Resmaa Menakem, 2017): maybe racism is a somatic (body) response to generational (epigenetic) trauma? Too little data
  - ⭐⭐ No Bad Parts (Richard Schwartz): maybe we're not one person but a collection of parts, and interviewing family systems (IFS) helps? Unclear
  - ⭐⭐⭐ Maybe You Should Talk to Someone (Lori Gottlieb): our memory is unreliable and therapy is messy. Connection & compassion help
  - Most of these are based on the contested Polyvagal Theory: the nervous system scans for danger before the mind can process it. But the specific claims of the theory are wrong and it makes no other falsifiable claims.
    - The nervous system has hierarchical responses to threat. 🟢 Not unique to PVT
    - Social connection regulates physiology. 🟢 Not unique to PVT
    - Unconscious threat detection (neuroception). 🟡 Weak evidence
    - Mamellian brain (ventral vagal system) is uniquely mammalian. 🔴 Lungfish have it
    - Reptilian brain (dorsal vagal) "shutdown" causes dissociation. 🔴 No evidence
    - RSA directly measures vagal tone. 🔴 Contested
    - Reptiles are "asocial". 🔴 Wrong
  - Trauma causes _body_ changes too. It's not just the mind.
  - Childhood trauma persists.
  - Relationships (connection & compassion) help more than therapy
- What constitutes tax residency in India? For an Indian citizen, as I understand it (after 2 hours of research):
  - If you were in India >= 182 days: Resident\*
  - Else, if you left India _this year_ for employment: NRI.
  - Else, if you are an Indian Citizen living abroad (visiting or not):
    - If Indian Income <= ₹15 Lakhs: NRI.
    - Else if you were in India >= 120 days AND >= 365 days in the last 4 years: RNOR.
    - Else if you are not liable to tax in any other country: RNOR.
  - Else, if you left India for non-employment (students, tourism) and were in India >= 60 days AND >= 365 days in the last 4 years: Resident\*
  - Else: NRI.
  - If you ended up as a Resident\*
    - If you were NRI in 9 of the last 10 years OR in India <= 729 days in the last 7 years: RNOR
    - Else: ROR (Resident & Ordinarily Resident).
  - For all practical purposes, RNOR is like an NRI. You pay tax only on Indian income, not global income. It's like a transition status for returning NRIs.
- [AVIF compresses better than WebP](https://www.ctrl.blog/entry/webp-avif-comparison.html) and [may be the "next big thing"](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types#avif_image). I will be switching for all future images. [Squoosh](https://squoosh.app/) remains my choice of compressor and Ezgif's [AVIF maker](https://ezgif.com/avif-maker) and [GIF to AVIF](https://ezgif.com/gif-to-avif) are handy.
