---
title: How long can I make ChatGPT think?
date: "2025-06-29T04:08:32Z"
lastmod: "2025-06-29T04:08:56Z"
categories:
  - coding
  - llms
wp_id: 4150
---

![How long can I make ChatGPT think?](/blog/assets/ChatGPT-Image-Jun-29-2025-09_33_38-AM.webp)

[Jason Clarke](https://jack-clark.net/)'s [Import AI 414](https://jack-clark.net/2025/05/26/import-ai-414-superpersuasion-openai-models-avoid-shutdown-weather-prediction-and-ai/) shares a Tech Tale about a game called "Go Think":

> … we’d take turns asking questions and then we’d see how long the machine had to think for and whoever asked the question that took the longest won.

I [prompted](https://github.com/sanand0/chatgpt-to-markdown/blob/a9d97319176a28ca13d95db7015fe0976068605c/prompts/thinktime-generation.txt) [Claude Code](https://www.anthropic.com/claude-code) to write a [library](https://github.com/sanand0/chatgpt-to-markdown/blob/a9d97319176a28ca13d95db7015fe0976068605c/prompts/thinktime-integration.txt) for this. (Cost: $2.30).

(FYI, this takes 2.3 seconds in NodeJS and 4.2 seconds in Python. A clear gap for JSON parsing.)

The top 3 thinking blocks took 6m 50s, 6m 21s, and 6m 1s each, all in roughly the same conversation thread. Here were my questions:

> - Here are vehicle telematics stats for 2 months. Unzip it and take a look. Find interesting insights from this data. Look hard until you find at least 5 surprising insights from this.
> - Double check these with the data
> - Run the analyses and tell me what factors drive the maintenance schedule. Give me insights validated with tables and charts.

The next largest thinking block (5m 42s) was on what happens when [intelligence becomes cheap](https://chatgpt.com/share/684a129d-4ec0-800c-a1fa-ecb1b83fecc1):

> I would like to explore parallels to the current phenomenon where intelligence is becoming too cheap to meter. Historically, both in recent history as well as over ancient history, what technologies have made what kind of tasks so cheap that they are too cheap to meter? Give me a wide range of examples

[Completing long tasks is a measure of intelligence](https://www.lesswrong.com/posts/deesrjitvXM4xYGZd/metr-measuring-ai-ability-to-complete-long-tasks). **Working independently for long** is another. O3 is at about 6 minutes on this. While it works, I'm practicing [Bubble Shooter](https://www.msn.com/en-us/play/games/Bubble-Shooter-HD/cg-9nzvl6gzqhkj) in 6 minutes.

You can run by [exporting your ChatGPT history](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data), extracting `conversations.json` and running:

```bash
npx -p chatgpt-to-markdown thinktime conversations.json
```
