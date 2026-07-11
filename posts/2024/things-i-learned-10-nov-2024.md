---
title: Things I Learned - 10 Nov 2024
date: 2024-11-10T00:00:00+00:00
categories:
  - til
description: I explored OpenFreeMap and Zapier Actions for GPTs, then researched LLM vision use cases in energy and manufacturing. I also looked into IBM's Docling for PDF conversion and Hamel Husain's framework for building effective LLM-as-a-judge systems.
tags: [llms, ai-workflows, image-recognition, speech-to-text, ai-coding, productivity-tools, fine-tuning, open-source]
---

This week, I learned:

- [OpenFreeMap](https://openfreemap.org/) is a free embeddable OpenStreetMap tile server. You can use [MapLibre GL](https://maplibre.org/) (more features) or Leaflet (simpler) to render it. It offers styling and self-hosting.
- [Zapier Actions](https://actions.zapier.com/) are an easy way to set up custom actions like GMail / Google Calendar APIs for GPTs, since [GPTs' callback URLs keep changing](https://community.openai.com/t/gpt-oauth-callback-url-keeps-changing/493236). But they fail often, and don't work on mobile. At least for me.
- LLM Vision Use Cases in manufacturing and earth sciences (via Shivku)
  - Automated geoscience image descriptions [Ref](https://www.linkedin.com/posts/paulhcleverley_geosciences-earthscience-geology-activity-7254037937674240000-pQab/)
  - Interpret Wind Turbine photos and charts, construction monitoring, equipment maintenance & charts [Ref](https://www.linkedin.com/pulse/vision-ai-energy-use-cases-copilot-wind-siting-impact-kalyanaraman-wqe7c/)
  - Forecast weather based on cloud photos! [Ref](https://www.linkedin.com/pulse/cloud-typing-local-weather-forecasting-using-chatgpt-cam-shivkumar-1hhkc/)
  - Analyze thermal image of solar panels, electroluminescence images for warranty claims, ROI estimates from Google Sunroof rooftop images [Ref](https://www.linkedin.com/pulse/vision-ai-energy-use-cases-part-1-copilot-solar-pv-kalyanaraman-ccszc/)
  - Corrosion detection in electricity towers, turbines, storage tanks, penstock. Interpret non-destructive test images [Ref](https://www.linkedin.com/pulse/vision-ai-energy-use-cases-copilot-corrosion-shivkumar-kalyanaraman-onuic/)
- Google counts auto-completion when saying "25% of all the code is written by AI at Google". "It's a helpful productivity tool but it's not doing any engineering at all. It's probably about as good, maybe slightly worse, than Copilot." [YCombinator](https://news.ycombinator.com/item?id=42002212)
- Workflow for AI video creation: Use Meshcapade (meshcapade.com) to generate body movement of a 3D-rendered character. Pass that video to Runway's video-to-video model to generate any visual. Add music from Suno [Ref](https://www.linkedin.com/posts/peter-gostev_i-discovered-a-really-cool-new-workflow-for-activity-7260003053771141120-DJpS)
- Someone sorted the X and Y columns independently for regression. [Ref](https://stats.stackexchange.com/q/185507)
- Android keyboard learning only sends model changes back to server and not local keywords. Model changes are aggregated! [Ref](https://chatgpt.com/share/672d6d6d-46a0-800c-a130-c689f5ebc0b7)
- Here is a prompt for audio transcription using Gemini. [Ref](https://gist.github.com/rajivsinclair/8fb0371f6eda25f9e5cc515cd77abd62)
  - Transcription: Accurately transcribe the audio clip in the original language. Include all spoken words, fillers, slang, colloquialisms, and any code-switching instances. Pay attention to dialects and regional variations common among immigrant communities. Do your best to capture the speech accurately, and flag any unintelligible portions with `[inaudible]`.
  - Translation: Translate the transcription into English. Preserve the original meaning, context, idiomatic expressions, and cultural references. Ensure that nuances and subtleties are accurately conveyed.
  - Capture Vocal Nuances: Note vocal cues such as tone, pitch, pacing, emphasis, and emotional expressions that may influence the message. These cues are critical for understanding intent and potential impact.
- Here are some approaches to large-scale classification of medical codes. [ChatGPT](https://chatgpt.com/share/672dd476-7694-800c-a150-f3de912788ef)
  - Fine-Tuning LLMs on Medical Data: Enhance LLMs by training them on medical datasets, such as clinical notes and discharge summaries, to improve their understanding of medical terminology and context.
  - Multi-Agent Frameworks: Implement a multi-agent system that simulates real-world coding processes with distinct roles (e.g., patient, physician, coder, reviewer, adjuster). Each agent utilizes an LLM to perform specific functions, enhancing interpretability and reliability. [ArXiv](https://arxiv.org/abs/2406.15363)
  - Retrieve-Rank Systems: Develop a two-stage system where the LLM first retrieves potential ICD-10 codes and then ranks them based on relevance, improving precision in code assignment. [ArXiv](https://arxiv.org/abs/2407.12849)
  - Embedding-Based Approaches: Use LLMs to generate embeddings for ICD-10 codes and medical texts, facilitating the matching of texts to appropriate codes through similarity measures. [GitHub](https://github.com/kaneplusplus/icd-10-cm-embedding)
  - Hierarchical Classification: Leverage the hierarchical structure of ICD-10 codes by first classifying texts into broader categories before assigning specific codes, reducing complexity and improving accuracy. [ArXiv](https://arxiv.org/abs/2310.06552)
  - Two-Stage Verification Models: Combine LLMs with verification models, such as Long Short-Term Memory (LSTM) networks, to validate and refine the codes suggested by the LLM, balancing recall and precision. [ArXiv](https://arxiv.org/abs/2311.13735)
  - Also, a mixture of models approach might work. Feed any existing NLP model / rules as a second opinion.
- GraphRAG is better if data is naturally graph-structured. Else, it's slow and fills up the context window with even vaguely related stuff. Vigneshbabu, AMAT.
- ChatGPT for Windows desktop supports real-time voice and a global shortcut (Alt Space).
- [uithub](https://uithub.com) converts GitHub repos to Markdown. Just replace "g" in "github.com/..." with "u". [Example](https://uithub.com/gramener/asyncllm)
- WebContainers are a thing and Bolt.new uses them!
- [Docling](https://github.com/DS4SD/docling) by IBM converts PDF, DOCX, etc. to Markdown. Like [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/) but better.
- Check out [Loom](https://www.loom.com/) and [Cleanshot](https://cleanshot.com/) are the recommended tools for screen recording and screenshotting. But Loom is paid and Cleanshot is Mac only.
- The Rubik's cube has a Hamiltonian cycle through every one of its 43 quintillion states. [Ref](https://bruce.cubing.net/ham333/rubikhamiltonexplanation.html)
- [OmniParser](https://microsoft.github.io/OmniParser/) is great at parsing screenshots and identifying bounding boxes.
- [Recraft.ai](https://www.recraft.ai/) is currently SOTA in text to image. It's fairly impressive and could be a good alternative to Figma.
- [Zed.dev](https://zed.dev/) is an AI code editor by the creators of Atom. It's written in Rust and is blazing fast. It has native AI integration.
- Artificial Analysis has a bunch of new leaderboards and arenas.
  - Open AI TTS leads the [TTS Leaderboard](https://artificialanalysis.ai/text-to-speech/arena?tab=Leaderboard). ElevenLabs is a bit behind.
  - Recraft V3 > Flux 1.1 leads [Text to Image Leaderboard](https://artificialanalysis.ai/text-to-image/arena?tab=Leaderboard)
- [Hertz-Dev](https://github.com/Standard-Intelligence/hertz-dev) is an open source realtime voice chat model. But it doesn't fit in Google Colab T4's RAM
- Chain of Thought reduces performance where thinking makes humans worse. [Ref](https://arxiv.org/abs/2410.21333). Specifically:
  - Artificial grammar learning
  - Facial recognition
  - Classifying data that has exceptions
- [Creating a LLM-as-a-Judge That Drives Business Results](https://hamel.dev/blog/posts/llm-judge/) by Hamel Husain.
  - Get THE domain expert (or approver) as the tester.
  - Create a dataset that is DIVERSE.
  - Covers EACH combination of:
    - Features
    - Scenarios: e.g. multiple matches, no match, ambiguous request, invalid/incomplete input, unsupported feature, system error
    - Persona: e.g. new user, expert user, non-native speaker, busy professional, technophobe, elderly user
  - Generate data using existing data + synthetic data for each SPECIFIC combination of the above
  - Evaluate based only on PASS/FAIL with a CRITIQUE detailed enough for a new employee. Include:
    - Nuances: Something a failed response did well or a passed response didn't quite do well
    - Improvements: Suggest how model can improve
  - Build an SPA to make it easy for the domain expert to review
- LLMs can be made to unlearn (copyright material) better by identifying components related to the knowledge to unlearn and applying a larger learning rate to these while leaving other parts unchanged. As opposed to low learning rates for all components. [Ref](https://arxiv.org/abs/2410.16454)
