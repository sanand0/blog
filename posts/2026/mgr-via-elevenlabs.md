---
title: MGR via ElevenLabs
date: 2026-03-29T22:31:33+08:00
categories:
  - llms
description: A short film clip can be reverse-engineered into transcription, translation, and voice recreation workflows, showing how accessible historical or cinematic voice cloning has become.
keywords: [ElevenLabs, voice cloning, Tamil, film audio, transcription, AI media]
---

I was watching [Vaa Vaathiyar](https://en.wikipedia.org/wiki/Vaa_Vaathiyaar) which has a short clip of [MGR](https://en.wikipedia.org/wiki/M._G._Ramachandran) speaking. It's either AI-generated or mimic-ed and it wasn't bad.

<audio controls src="https://files.s-anand.net/images/2026-03-29-mgr-in-film.opus"></audio>

I used `ffmpeg` to record the audio from the film, transcribed it via [Gemini 3 Pro on AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview) with the prompt:

> Transcribe this into Tamil

... which gave me:

> ராமு...
> என்ன செய்திருக்கிறாய் நீ...
> வாத்தியார் கேட்கிறேன் சொல்
> நிமிர்ந்து பார்க்க கூட தைரியம் இல்லையா...
> ஓடாதே... நில்...

Translation:

> Ramu...
> What have you done...
> Vaathiyar (MGR) is asking, tell me
> Don't you have the courage to stand up and look at me...
> Don't run... stop...

(GitHub Copilot's auto-complete translated the above for me as I typed - flawlessly. It's getting better by the day!)

Then, I used [yt-dlp](https://github.com/yt-dlp/yt-dlp) to download the audio from this [MGR Short Clip](https://www.youtube.com/shorts/1jQqKds2z7g).

<iframe width="560" height="315" src="https://www.youtube.com/embed/1jQqKds2z7g?si=8GUnT7IvcsQZpwDb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Here's the sample:

<audio controls src="https://files.s-anand.net/images/2026-03-29-mgr-sample.opus"></audio>

I fed this into ElevenLabs' [Instant Voice Clone](https://elevenlabs.io/app/voice-library) that needs just 10 seconds of audio and created an "MGR" voice.

Here's the same dialogue in the cloned voice:

<audio controls src="https://files.s-anand.net/images/2026-03-29-mgr-generated.opus"></audio>

Personally, I think the ElevenLabs version is _slightly_ better. Of course, given the pace of AI improvement, this might just be the impact of a new model release.

---

**2 Apr 2026**: Here's the non-cloned generation from [Sarvam's text to speech](https://dashboard.sarvam.ai/text-to-speech) with Bulbul v3 standard quality. It feels pretty weak.

<audio controls src="https://files.s-anand.net/images/2026-03-29-mgr-sarvam.opus"></audio>

[Gemini 2.5 Pro Preview TTS](https://aistudio.google.com/u/2/generate-speech?model=gemini-2.5-pro-preview-tts) gave me this, which feels _much_ better.

<audio controls src="https://files.s-anand.net/images/2026-03-29-mgr-gemini.opus"></audio>
