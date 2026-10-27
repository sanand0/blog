---
title: Innovations 26 Oct 2026
date: 2026-10-27T07:02:14+01:00
categories:
- llms
description: 'I share new Innovation team demos: live meeting translation, remote hand-tracked 3D sculpting, audio search beyond transcripts, and AI agents reproducing scientific results and surfacing operational exceptions.'
tags: [llms, ai-agents, audio-search]
---

The Innovation team has built a few more demos since the last update. Three interesting learnings:

1. We can speak in one language and be heard in another, *live*, in a normal Google Meet call.
2. A person in another city can use their hands and a phone to sculpt a 3D object on your laptop.
3. AI can search what was *heard*, not just said, and can check scientific claims by actually reproducing them.

### New capabilities

**[Translate a live meeting into almost any language](https://github.com/hrmiitm/live-translator/releases)** (Hritik). At Friday's VIA talk, I spoke and the audience heard Filipino, Hindi, Tamil and Telugu with a short delay. Hritik built a desktop app that creates a virtual microphone and speaker for Meet. It translates both ways: what others hear from you, and what you hear from them. It took him a day or two to vibe code, and comes as a Windows, Mac or Linux app. I estimated about **0.6 US cents a minute** in my trial.

- **Uses:** Global customer service, multilingual client discovery, remote consulting and workshops.
- **Ideas:** One attendee immediately thought of discovery with a Spanish-speaking client. Could service teams work across language boundaries? Could every listener choose their own language? There is some voice delay, and virtual audio devices still need setup on each computer.

[![Gemini Audio desktop app: translate my voice and translate what I hear, shown as an offline UI preview](https://files.s-anand.net/blog/2026-10-26-innovations/live-translator.avif)](https://github.com/hrmiitm/live-translator/releases)

**[Sculpt a 3D pot with your hands, from anywhere](https://spatial-studio-webcam.dearmacaw4.chatgpt.site/pottery)** (Sujal). Sujal used his laptop camera to track his hands and shape a pot, then Jivraj used his phone from Hyderabad to manipulate the same 3D object remotely. The result can be exported as a 3D model or JSON. We saw it work live, with some lag.

- **Uses:** Product design, education, remote training, rehabilitation and industrial operations.
- **Ideas:** If gestures can control a model remotely, can an expert teach somebody to sculpt, assemble machinery or lift equipment safely without being there? Can the same phone sensors guide a real machine? Sujal also built [3D maths and geometry controls](https://spatial-studio-webcam.dearmacaw4.chatgpt.site/maths). The example below was sculpted in the web page with its mouse fallback; the live hand-tracking demo was at VIA.

[![A 3D pot sculpted in Sujal's browser interface, with a shape profile and phone-control option](https://files.s-anand.net/blog/2026-10-26-innovations/remote-pottery.avif)](https://spatial-studio-webcam.dearmacaw4.chatgpt.site/pottery)

**[Search audio for things nobody said](https://atharva-729.github.io/sound-search-demo/)** (Atharva). An embedding model searches over 7,000 clips for sounds like whispering, laughter, an angry tone or a jazz instrument, without a transcript. Click "Whispering": all ten displayed matches have whisper labels. Atharva compared CLAP with EmbeddingGemma 2; neither model is best for every sound.

- **Uses:** Call centres, meeting recordings, media archives and music libraries.
- **Ideas:** Find meetings where people laughed or argued, or customer calls where the tone changed, even if the transcript looks innocuous. The hosted page has working sample searches; free-text searches and playback require its local server.

[![Audio embeddings showing matches for whispering among thousands of recordings](https://files.s-anand.net/blog/2026-10-26-innovations/audio-search.avif)](https://atharva-729.github.io/sound-search-demo/)

### Checking what the results say

**[Can AI independently reproduce a scientific paper?](https://jivraj-18.github.io/agentic-reproduction/)** (Jivraj). The agents get a paper's Methods and publicly deposited data, but not the original code or results. They write code to rebuild a table, and a fixed script checks every number. On six papers from Elsevier, Springer Nature and Wiley, **Sonnet 5.5 reproduced 77% of 495 numbers within 2%**, versus **71% for Opus 5.5**, at about **$1.11 versus $2.56**.

- **Uses:** Scientific publishers, research-integrity teams and editors.
- **Ideas:** What if a paper came with a reproducibility report that pinpoints which methodological choices were missing? Six selected papers and mostly one attempt each are only a pilot, but the individual failures are interesting.

[![A comparison of Opus and Sonnet recreating six papers' numerical results](https://files.s-anand.net/blog/2026-10-26-innovations/paper-reproduction.avif)](https://jivraj-18.github.io/agentic-reproduction/)

**[How often does Veeva change a release-risk rating?](https://eshwarpotturi.github.io/release-second-opinion/)** (Eswar). Across 11 Veeva Vault releases with comparable old and new ratings, **91 of 2,547 features (3.6%)** were re-rated. Just **1.9%** changed whether a feature needed testing.

- **Uses:** Pharma software validation, regulated technology and QA.
- **Ideas:** Track what vendors initially say and what they later correct. Could validation teams automatically catch changes that actually affect testing?

[![Veeva feature risk changes, with revised features highlighted](https://files.s-anand.net/blog/2026-10-26-innovations/veeva-release-risks.avif)](https://eshwarpotturi.github.io/release-second-opinion/)

### Let agents handle the routine cases

**[Show a shipping manager only what needs a decision](https://eshwarpotturi.github.io/low-water-clock/)** (Eswar). The system combines Rhine water levels with dated carrier notices, converts notices to versioned rules, and checks shipments. On the selected day, **26 shipments need a human**, while **27 are handled without a screen**. The water levels and carrier notices are real; the 420 shipments are invented.

- **Uses:** Logistics, shipping, supply chains and exception management.
- **Ideas:** Perhaps a good operations dashboard should hide everything that is going right. Surface exceptions with the evidence, the rule version and the decision history. Try "Replay the season".

[![Rhine shipping exception console showing only shipments requiring a person](https://files.s-anand.net/blog/2026-10-26-innovations/rhine-exceptions.avif)](https://eshwarpotturi.github.io/low-water-clock/)

### And more

- **[A pharma tablet-plant twin](https://eshwarpotturi.github.io/pharma-plant-twin/)** (Eswar). The factory demo from last week now follows a tablet batch through production, showing where an agent can act and where QC approval is mandatory. A synthetic, guided demo.
- **[Send messages between devices using sound](https://jivraj-18.github.io/virtual-air/sound-lab/)** (Jivraj). Laptop and phone communicating through speakers and microphones, without a network. Interesting for offline environments; still an experiment.
- **[An AI meeting stand-in](https://eshwarpotturi.github.io/meeting-standin/)** (Eswar). An explicitly labelled AI can answer some questions from your notes and show slides. Prototype, not an unattended meeting assistant.
- **[Eight AI delegates negotiate a budget](https://eshwarpotturi.github.io/the-summit/)** (Eswar). Their private instructions and secret votes make a fun workshop discussion about what to delegate to agents.

If you get any ideas from these or want us to try something for a client, please let me know.
