---
title: Innovations 2 Nov 2026
date: 2026-11-03T14:26:39+05:30
categories:
- llms
description: 'I share Innovation team demos: gesture-controlled 3D molecules, videos with evidence-backed critiques, audio search beyond transcripts, cheap machine-fault detection, and governed AI agents.'
tags: [experiments, llms, ai-agents, audio-search]
---

The Innovation team has been experimenting with 3D interaction, audio, video and AI agents. Three things struck me:

1. We can manipulate a 3D molecule with our hands, or try different furniture in a virtual room, using a browser.
2. Sound search can find things a transcript never records. And a small specialist model can diagnose a machine at a tiny fraction of an audio LLM's cost.
3. AI can help us improve videos and business decisions when its suggestions are checked against evidence, not just written convincingly.

### New ways to interact and create

**[Hold a 3D molecule in your hands](https://spatial-mirror.pages.dev/atp)** (Sujal). At our Innovation Team meeting, I used hand gestures in front of my camera to manipulate a colourful 3D ATP synthase molecule: pluck, slice, scale, rebuild and explore its parts. The browser recognizes the gestures; a paired phone can also control the scene. It is related to Sujal's [remote 3D pottery](https://spatial-studio-webcam.dearmacaw4.chatgpt.site/pottery) experiment.

- **Uses:** Science education, pharma/medtech training, virtual exhibits, remote product demonstrations.
- **Ideas:** Could a biology teacher pull apart a molecule while explaining it? Could a field engineer demonstrate how to assemble a part without shipping the equipment? The gestures take practice, and this is a visual learning interface, not a validated physical simulation.

[![Hands-on manipulation of a 3D ATP synthase molecule during the Innovation Team meeting](https://files.s-anand.net/blog/2026-11-02-innovations/atp-gesture.avif)](https://spatial-mirror.pages.dev/atp)

**[Rearrange a room, not just render it](https://roomshift-studio.pages.dev/)** (Sujal). Roomshift lets you move furniture through a 3D room, swap pieces, compare layouts and walk inside. You can bring your own 3D model; the important difference from image generation is that the objects remain editable.

- **Uses:** Real estate, furniture retail, interior design, offices and facilities.
- **Ideas:** Could customers try a product in their own space before buying? Could we test hotel or hospital layouts with staff? Measurements are estimates until checked.

[![Roomshift's editable 3D room and layout options](https://files.s-anand.net/blog/2026-11-02-innovations/roomshift.avif)](https://roomshift-studio.pages.dev/)

**[Find where a video might lose viewers](https://sujalpradhan.github.io/content-dna-analyzer/)** (Sujal). Choose a demo video, click **Analyze**, and inspect a timeline showing cuts, speech, silence, visual formats and potential problems. In the Uber Eats Super Bowl ad, it suggests introducing the brand sooner and flags a static four-second stretch around **1:22**. Every suggestion links to measured evidence, rather than being a free-form AI opinion.

- **Uses:** Marketing, video production, learning-content teams and media publishers.
- **Ideas:** What if every training video or campaign got an automatic editorial first pass? The tool flags *possible* attention problems; it does not measure actual audience retention or predict views.

[![Content DNA's video timeline: cuts, speech, flagged moments and evidence-backed recommendations](https://files.s-anand.net/blog/2026-11-02-innovations/content-dna-timeline.avif)](https://sujalpradhan.github.io/content-dna-analyzer/)

### Search and understand sound, not just speech

**[Find sounds that transcripts cannot search](https://atharva-729.github.io/sound-search-demo/)** (Atharva). Search **7,221 clips** for laughter, whispers, musical styles and conversations without using transcripts. In the live demo, CLAP found **8 of the top 10** human-labelled laughing clips. Atharva found **CLAP stronger for recognizable sound events** like coughing, sneezing and laughter, while **Gemma is stronger for conversational scenes** like friends joking about football. The demo can use both.

- **Uses:** Broadcast and podcast archives, contact-centre QA, accessibility, video tagging.
- **Ideas:** Search an archive for applause, sirens, background music or a change in tone. Could we enrich transcripts with a second index of *everything audible that isn't said*? The hosted demo has preset searches; arbitrary new queries need its local backend.

[![CLAP retrieves laughter and related audio without transcripts](https://files.s-anand.net/blog/2026-11-02-innovations/sound-search.avif)](https://atharva-729.github.io/sound-search-demo/)

**[Diagnose a compressor from one second of sound](https://jivraj-18.github.io/machine-sound-diagnosis/)** (Jivraj). On recordings of one compressor in eight states, a specialist industrial-audio model, **FISHER**, identified the correct fault **97.4%** of the time after seeing five examples of each state. Simple signal processing reached **96%**; Gemini 3.1 Pro with *no* examples scored **16.3%**. Estimated analysis cost: **$0.10–$0.27 per compressor per month** for the cheaper approaches, versus **$254** for the zero-shot LLM.

- **Uses:** Manufacturing, predictive maintenance, industrial monitoring.
- **Ideas:** Before deploying an expensive general model, try a microphone and a few labelled fault recordings. These results are from one machine in one lab; transfer to a second machine remains untested.

[![Accuracy versus cost of specialist industrial audio models and a zero-shot LLM](https://files.s-anand.net/blog/2026-11-02-innovations/compressor-diagnosis.avif)](https://jivraj-18.github.io/machine-sound-diagnosis/)

**[Can a phone hear your password?](https://eshwarpotturi.github.io/keystroke-replication/)** (Eswar). After training on the sounds of 25 presses per key, a small model identified **93%** of unseen mixed keypresses from a nearby phone microphone. The page lets you listen to a word and see what the model inferred.

- **Uses:** Security awareness, endpoint and microphone risk assessments.
- **Ideas:** What can an innocent microphone reveal? It is *device-specific*: tested on different devices, accuracy fell close to chance.

[![A password typed on a keyboard compared with keys reconstructed from sound](https://files.s-anand.net/blog/2026-11-02-innovations/keystroke-listener.avif)](https://eshwarpotturi.github.io/keystroke-replication/)

**[Can we detect a cloned voice?](https://eshwarpotturi.github.io/fakevoice/)** (Eswar). A WavLM detector classified **94%** of 604 held-out real/fake clips correctly, including simulated phone audio. But it caught only **one of three** newer voice clones when passed through a simulated phone line.

- **Uses:** Banking fraud, contact centres and identity checks.
- **Ideas:** A suspicious voice score could trigger callback verification, not automatic rejection. The newer-clone trial is tiny, and false alarms become costly when most callers are genuine.

### The system around the model matters

**[Search 10,469 financial filings: simple versus agentic](https://hrmiitm.github.io/rag-on-large-data/)** (Hritik). On 50 questions with the same Gemini 3.8 Flash model, agentic search achieved **81% answer correctness** against **54.9% for BM25**. But it cost about **3.2× more**, took **178 seconds rather than 23**, and had slightly lower faithfulness (**87.6% versus 92.1%**).

- **Uses:** Asset managers, investment research, enterprise knowledge search.
- **Ideas:** Don't choose a RAG architecture from a single accuracy score. Compare *correctness, citations, latency and cost* on the client's questions.

[![Financial document search: answer correctness, faithfulness, latency and cost](https://files.s-anand.net/blog/2026-11-02-innovations/financial-rag.avif)](https://hrmiitm.github.io/rag-on-large-data/)

**[Agents that cannot give themselves permission](https://eshwarpotturi.github.io/AIA-Gov/)** (Eswar). In a simulated bank, eight agents investigate a trader's $2 million discrepancy. Every request goes through a code-enforced gate checking both agent permissions and the human's entitlement. An auditor probes the rules; governance proposes changes; Compliance approves them.

- **Uses:** Banking, healthcare, agent security and compliance.
- **Ideas:** Let AI discover and propose fixes, but keep authorization and enforcement outside the model. The replay is synthetic, not a production security certification.

### One experiment for education

**[Can an AI be wrong in exactly the way a student is?](https://atharva-729.github.io/llm-distractors/)** (Atharva). Across almost **68,000** questions to nine models, prompting a model to hold a specific maths misconception can make it choose the corresponding wrong answer. Reasoning often helps it make the *intended* mistake.

- **Uses:** Assessment publishers and adaptive-learning platforms.
- **Ideas:** Let simulated students test multiple-choice options for misconceptions they do or don't catch, before giving them to real students. Their behaviour still needs checking against actual student choices.

Also worth exploring: [Reproducible LLM-answer replay](https://eshwarpotturi.github.io/llm-seed/) (Eswar)—it saves and replays the first answer, rather than controlling model randomness—and [news grouped by headlines, patterns and underlying forces](https://atharva-729.github.io/news-digest-123/) (Atharva), which could be adapted into a client-specific industry briefing.

These are experiments. If one sparks an idea or connects to a client problem, please let me know.
