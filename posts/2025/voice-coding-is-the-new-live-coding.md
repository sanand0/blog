---
title: Voice coding is the new live coding
date: "2025-09-21T11:18:17Z"
lastmod: "2025-09-21T11:20:30Z"
categories:
  - coding
  - llms
wp_id: 4194
---

![Voice coding is the new live coding](/blog/assets/ChatGPT-Image-Sep-21-2025-04_46_27-PM.webp)

In Feb 2025 at PyConf Hyderabad, I tried a new slide format: [command-line slideshows in `bash`](/blog/command-line-slideshows-in-bash/).

I've used this format in more talks since then:

- [LLMs in the CLI](https://github.com/sanand0/talks0/blob/main/2025-06-pycon-sg/llm-cli.md), PyCon Singapore, Jun 2025
- [Agents in the CLI](https://github.com/sanand0/talks/blob/main/2025-07-24-pugs-agent-loop/README.md), Singapore Python User Group, Jul 2025
- [DuckDB is the new Pandas](https://github.com/sanand0/talks/blob/main/2025-09-13-duckdb-is-the-new-pandas/README.md), PyCon India, Sep 2025

It's my favorite format. I can demo code without breaking the presentation flow.\
It also draws interest. My setup was the [top question in my PyCon talk](https://github.com/sanand0/talks/blob/main/2025-09-13-duckdb-is-the-new-pandas/README.md#qa).

In Sep 2025, at PyCon India, I extended the setup for voice typing. [`talkcode.sh`](https://github.com/sanand0/scripts/blob/54560718bf2f4148d9005d74ab1543de52cff6d9/talkcode.sh) is a Bash pipeline that:

- uses [`ffmpeg`](https://ffmpeg.org/) to record mic into as 16 kHz mono, voice-optimized `.opus`
- sends audio to Gemini via [`llm`](https://llm.datasette.io/) for transcription
- uses [`awk`](https://en.wikipedia.org/wiki/AWK) to extract the code fence
- uses [`xclip`](https://github.com/astrand/xclip) to copy the code to the clipboard
- uses [`xdotool`](https://github.com/jordansissel/xdotool) to paste it back to the original window

````bash
# Mic only, 16 kHz mono, voice filtering, fast Opus
ffmpeg -hide_banner -v error \
  -f pulse -i default \
  -ac 1 -ar 16000 \
  -af "highpass=f=100,lowpass=f=6000" \
  -c:a libopus -b:a 16k -vbr on \
  -compression_level 2 -application voip -frame_duration 60 \
  -y "$AUDIO"

# Transcribe, extract the code fence and copy to clipboard
llm -m gemini-2.5-flash -a "$AUDIO" -s "$SYSTEM_TEXT" \
  | tee /dev/tty \
  | awk 'BEGIN{f=0} /```/{f=!f; next} f{buf=buf$0"\n"} END{print buf}' \
  | xclip -selection clipboard

# Bring last window to foreground and paste from clipboard
if [ -n "${ACTIVE_WIN:-}" ]; then
  xdotool windowactivate --sync "$ACTIVE_WIN"
  sleep 0.08
  xdotool key --clearmodifiers ctrl+shift+v
fi
````

During the workshop, I said, "Which (judicial) bench has the longest pending cases," and it generated a DuckDB query that, single-shot, ran correctly on the [Indian High Court judgements](https://github.com/vanga/indian-high-court-judgments) dataset.

---

But LLMs are slow and break the flow. Here's how I keep the room engaged:

1. **Dictate, don't type.** Speaking is faster **and** more engaging. That's why I built this workflow.
2. **Avoid Alt-Tab.** Bring the LLM **into** your app. Window-switching and copy-paste break focus for you **and** the audience.
3. **Always stream output.** Narrate as it loads. `| tee /dev/tty` streams while piping.
4. **Answer questions while you wait.** Keep a [Slido](https://www.slido.com/) Q&A open and address the top ones while waiting for the LLM.

[LinkedIn](https://www.linkedin.com/posts/sanand0_%F0%9D%97%A9%F0%9D%97%BC%F0%9D%97%B6%F0%9D%97%B0%F0%9D%97%B2-%F0%9D%97%B0%F0%9D%97%BC%F0%9D%97%B1%F0%9D%97%B6%F0%9D%97%BB%F0%9D%97%B4-%F0%9D%97%B6%F0%9D%98%80-%F0%9D%98%81%F0%9D%97%B5%F0%9D%97%B2-%F0%9D%97%BB%F0%9D%97%B2%F0%9D%98%84-activity-7376824026595278848-PxgV)
