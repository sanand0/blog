---
title: Pipes May Be All You Need
date: "2025-07-05T11:49:24Z"
lastmod: "2025-07-01T12:06:32Z"
categories:
  - coding
wp_id: 4158
---

![Pipes May Be All You Need](/blog/assets/ChatGPT-Image-Jul-1-2025-05_34_17-PM.webp)

Switching to a Linux machine has advantages. My thinking's moving from [apps](https://en.wikipedia.org/wiki/Application_software) to [pipes](https://en.wikipedia.org/wiki/Pipeline_(Unix)).

I wanted a spaced repetition app to remind me quotes from my notes. I began by writing a prompt for Claude Code:

> Write a program that I can run like `uv run recall.py --files 10 --lines 200 --model gpt-4.1-mini [PATHS...]` that suggests points from my notes to recall. It should
>
> `--files 10`: Pick the 10 latest files from the `PATH`s (defaulting to `~/Dropbox/notes`)\
> `--lines 200`: Take the top 200 lines (which usually have the latest information)\
> `--model gpt-4.1-mini`: Pass it to this model and ask it to summarize points to recall

Then I realized that I could do this on the CLI:

```bash
find ~/Dropbox/notes -type f -printf "%T@ %p\n" \   # Print the timestamp and file path
  | sort -nr \                                      # Sort latest first
  | head -n 10 \                                    # Pick the 10 latest files
  | cut -d" " -f2- \                                # Drop the timestamp, just get paths
  | xargs -I {} head -n 200 "{}" \                  # Get the first 200 lines
  | llm -s "List 3 points to remember"              # Ask an LLM to share points to recall
```

This works well!
