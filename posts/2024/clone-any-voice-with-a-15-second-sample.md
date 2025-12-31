---
title: Clone any voice with a 15-second sample
date: "2024-10-24T01:36:21Z"
lastmod: "2024-10-24T01:36:58Z"
categories:
  - coding
  - llms
wp_id: 3667
---

![Clone any voice with a 15-second sample](/blog/assets/calvin-voice-cloning.webp)

<p>It's surprisingly easy to clone a voice using <a href="https://github.com/SWivid/F5-TTS">F5-TTS</a>: "A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching".</p>
<p>Here's a clip of me, saying:</p>
<blockquote class="wp-block-quote">
<p>I think Taylor Swift is the best singer. I've attended every one of her concerts and in fact, I've even proposed to her once. Don't tell anyone.</p>
</blockquote>
<p>(Which is ironic since I didn't know who she was until this year and I still haven't seen or heard her.)</p>
<figure class="wp-block-audio"><audio controls="" src="/blog/assets/anand-proposes-to-taylor-swift.opus"></audio></figure>
<p>You'll notice that my voice is a bit monotic. That's because I trained it on a segment of my talk that's monotonic.</p>
<figure class="wp-block-audio"><audio controls="" src="/blog/assets/anand.opus"></audio></figure>
<p><a href="https://colab.research.google.com/drive/1YEMIdby-Nr--ox2-Wl5Racb5f0ncpqRu?usp=sharing"><strong>Here's the code</strong></a>. You can run this on Google Colab for free.</p>
<p>A few things to keep in mind when preparing the audio.</p>
<ol class="wp-block-list">
<li>Keep the input to just under 15 seconds. That's the optimal length</li>
<li>For expressive output, use an input with a broad range of voice emotions</li>
<li>When using unusual words (e.g. LLM), including the word in your sample helps</li>
<li>Transcribe <code>input.txt</code> <em>manually</em> to get it right, though <a href="https://huggingface.co/openai/whisper-large-v3">Whisper</a> is fine to clone in bulk. (But then, who are you and <em>what</em> are you doing?)</li>
<li>Sometimes, each chunk of audio generated has a second of audio from the original interspersed. I don't know why. Maybe a second of silence at the end helps</li>
<li>Keep punctuation simple in the generated text. For example, avoid hyphens like "This is obvious - don't try it." Use "This is obvious, don't try it." instead.</li>
</ol>
<p>This has a number of uses I can think of (er... ChatGPT can think of), but the ones I find most interesting are:</p>
<ol class="wp-block-list">
<li><strong>Author-narrated audio books</strong>. I'm sure this is coming soon, if it's not already there.</li>
<li><strong>Personalized IVR</strong>. Why should <em>my</em> IVR speak in some <em>other</em> robot's voice? Let's use mine. (This has some prank potential.)</li>
<li><strong>Annotated presentations</strong>. I'm too lazy to speak. Typing is easier. This lets me create, for example, slide decks with my voice, but with <em>editing made super-easy</em>. I just change the text and the audio changes.</li>
</ol>
