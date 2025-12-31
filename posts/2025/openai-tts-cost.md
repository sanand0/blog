---
title: OpenAI TTS cost
date: "2025-11-02T05:12:32Z"
lastmod: "2025-11-02T05:12:34Z"
categories:
  - experiments
  - llms
wp_id: 4245
---

![OpenAI TTS cost](/blog/assets/doodle.webp)

<p>The OpenAI <a href="https://platform.openai.com/docs/guides/text-to-speech">text-to-speech</a> cost documentation is confusing.</p>
<p>As of 2 Nov 2025:</p>
<ul class="wp-block-list">
<li><a href="https://platform.openai.com/docs/models/gpt-4o-mini-tts">GPT-4o mini TTS</a> costs $0.60 / MTok input and $12.00 / MTok audio output according to the <a href="https://platform.openai.com/docs/models/gpt-4o-mini-tts">model page</a> and the <a href="https://platform.openai.com/docs/pricing">pricing page</a>. They also estimate this to be ~1.5c per minute - both for input and output. It supports up to 2,000 tokens input.</li>
<li><a href="https://platform.openai.com/docs/models/tts-1">TTS-1</a> costs $15 / MTok speech generated according to the <a href="https://platform.openai.com/docs/models/tts-1">model page</a> but the <a href="https://platform.openai.com/docs/pricing">pricing page</a> says it's $15 / MChars. No estimate per minute is provided. Is supports up to 4,096 characters input.</li>
<li><a href="https://platform.openai.com/docs/models/tts-1-hd">TTS-1 HD</a> is twice as expensive as TTS-1</li>
</ul>
<p>I wanted to find the approximate total cost for a typical text input measured per character and token.</p>
<p>I converted this <a href="podcast.txt">podcast</a> with 4,096 ASCII characters and 877 tokens on <a href="https://github.com/openai/tiktoken">o200k_base</a> using:</p>
<p>I ran:</p>

```bash
curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg text "$(cat podcast.txt)" '{
    model: "tts-1",
    voice: "coral",
    input: $text
  }')" \
  --output tts-1.mp3
```

<p>This took 46 seconds to generate and produced a 5.1 MB MP3 file (256 seconds)</p>
<p>To measure the cost, I ran:</p>

```bash
curl "https://api.openai.com/v1/organization/costs?start_time=$(date -d '1 day ago' +%s)&project_ids=$PROJECT_ID&group_by=line_item" \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"
```

<p>This cost: <strong>USD 0.061425</strong>. Then I ran:</p>

```bash
curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg text "$(cat podcast.txt)" '{
    model: "gpt-4o-mini-tts",
    voice: "coral",
    input: $text
  }')" \
  --output gpt-4o-mini-tts.mp3
```

<p>This took 44 seconds to generate and produced a 4.3 MB MP3 file (268 seconds).</p>
<p>When I ran the admin API call again, the costs did not reflect for 5 minutes. So I ran it the GPT-4o mini TTS call again with the same input. This took 44 seconds to generate a 4.3 MB MP3 file. When I ran the admin API call again, the total cost for <strong>the 2 requests</strong> was: <strong>USD 0.12942</strong> audio output and USD 0.0010524 input.</p>
<p>I also checked for TTS-1 HD. Here are the costs in USD:</p>
<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th>Model</th><th class="has-text-align-right" data-align="right">$ / MTok</th><th class="has-text-align-right" data-align="right">$ / MChars</th><th class="has-text-align-right" data-align="right">$ / hour</th><th class="has-text-align-right" data-align="right">Time (s)</th><th class="has-text-align-right" data-align="right">Audio (s)</th><th class="has-text-align-right" data-align="right">Cost $</th></tr></thead><tbody><tr><td>GPT-4o mini TTS</td><td class="has-text-align-right" data-align="right">74.4</td><td class="has-text-align-right" data-align="right">15.9</td><td class="has-text-align-right" data-align="right">0.876</td><td class="has-text-align-right" data-align="right">46</td><td class="has-text-align-right" data-align="right">268</td><td class="has-text-align-right" data-align="right">0.0652</td></tr><tr><td>TTS-1</td><td class="has-text-align-right" data-align="right">70.0</td><td class="has-text-align-right" data-align="right">15.0</td><td class="has-text-align-right" data-align="right">0.864</td><td class="has-text-align-right" data-align="right">44</td><td class="has-text-align-right" data-align="right">256</td><td class="has-text-align-right" data-align="right">0.0614</td></tr><tr><td>TTS-1 HD</td><td class="has-text-align-right" data-align="right">140.0</td><td class="has-text-align-right" data-align="right">30.0</td><td class="has-text-align-right" data-align="right">1.728</td><td class="has-text-align-right" data-align="right">62</td><td class="has-text-align-right" data-align="right">257</td><td class="has-text-align-right" data-align="right">0.1228</td></tr></tbody></table></figure>
<p>The GPT-4o mini TTS audio output cost was USD 0.06471 for the input of 877 tokens, i.e. $73.8 / MTok. Since the actual cost is $12 / MTok, this is a 6.15x multiplier. I guess <strong>1 input text token produces ~6 output audio tokens</strong>.</p>
<p>In terms of quality:</p>
<ul class="wp-block-list">
<li>GPT-4o mini TTS: Very slightly robotic. Looser interpretation of text (e.g. says "October" when I write "Oct").</li>
<li>TTS-1: Natural. Strict interpretation of text.</li>
<li>TTS-1 HD: Very slightly more natural. Strict interpretation of text.</li>
</ul>
<p><strong>I will likely use TTS-1 for now</strong> given the cost difference is small and the quality is good enough.</p>
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<p>Incidentally, the <a href="https://platform.openai.com/docs/api-reference/usage/audio_speeches">usage API</a> did not show an GPT 4o mini TTS line items even after 20 minutes.</p>

```bash
curl "https://api.openai.com/v1/organization/usage/audio_speeches?start_time=$(date -d '1 day ago' +%s)&project_ids=$PROJECT_ID&group_by=model" \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"
```
