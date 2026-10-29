---
title: Code on remote machines
date: 2026-10-29T17:23:48+01:00
categories:
- llms
description: I set up my Windows laptop for remote coding with Remote Desktop, Tailscale, and file sync. While traveling, I used my phone to draft, code, research, and access work from home.
tags: [coding-agents, experiments]
---

Thornston Bell's [How I work with Agents](https://x.com/thorstenball/status/2114386050638336082) suggests actively using remote machines for coding. I'd struggled with this for many months, and finally managed to set up my Windows laptop for remote coding.

How?

1. Tell my wife to tell the maid to never switch it off. (It doesn't have battery.)
2. Tell ChatGPT to install [Remote Desktop Commander](https://chatgpt.com/settings/plugins-settings/plugin_asdk_app_6a057d268ebc81919918d37eec718425) - and schedule it to run on boot. Now agents can use it.
3. Tell ChatGPT to install [Tailscale](https://tailscale.com/) so I can SSH into it and copy files.
4. Tell ChatGPT to create a [`sync-plutonium.sh`](https://github.com/sanand0/scripts/blob/a24b328da41c23748677d3b678e7ff1e3d7b38ae/services/sync-plutonium.sh) that pushes files from my Linux system (`graphene`) to the Windows machine (`Plutonium`).

That last step was the critical enabler. This means that most of the files on my regular laptop is also on the home laptop, and it has the same context.

This is proving to be quite a big unlock!

For example, I landed in Brussels on Monday. The immigration queue for took about 2 hours and 15 minutes for me - as a non-EU citizen. I used this time to:

1. Install [Taildrive](https://tailscale.com/docs/features/taildrive) on my home laptop and [Material Files](https://play.google.com/store/apps/details) on my phone, so I can edit files in Singapore from Brussels.
2. Draft an email and blog post about [our innovation team's work last week](https://www.s-anand.net/blog/innovations-26-oct-2026/). Since all the transcripts and repos were synced, ChatGPT could find up everything, create screenshots, and explain it the way I wanted it.
3. Run an [agent swarm experiment](https://chatgpt.com/share/6ae3759b-2a0c-83ec-a189-6fa62e0ffb42) <!-- https://chatgpt.com/c/6adeee3c-c4b8-83ec-ad37-a5c4eb55e6e1 --> - to see if 4 Codex agents running GPT 6 Luna would, if allowed to do what they want, do something interesting. They didn't - they decided not to waste tokens. When pushed, [they fumbled and formed two groups and built two tools](https://github.com/sanand0/research/blob/8f2e851b06547f84f5bcc6490f2b5dfa49b9d658/agent-swarm/experiments/005-collaborate/story.md).
4. Ideate how to structure a market economy that grows in value when students do useful work - as part of my [TDS](https://tds.s-anand.net/) course. <!-- https://chatgpt.com/c/6adf07b0-b0e0-83ec-b89c-1866d601ea34 --> Since it had the code base for my entire course and evaluation, ChatGPT could give me relevant ideas.
5. Read Anthropic's [code review process](https://x.com/addyosmani/status/2114604912520921136).

On the way back, the emigration queue was only 1 hour and 30 minutes. I used this time to:

1. Make my Calvin and Hobbes browser mobile-friendly. My blog was already cloned on my home laptop.
2. Create an [annotated Asterix comic viewer](https://www.s-anand.net/blog/reading-asterix-from-brussels-to-dubai-via-singapore/). The comics were available on the home laptop. So was Python (for OCR).
3. Mine all my data and documents to understand my preferences - since almost all my docs are on the home laptop.
4. Complete email requests and tasks from several colleagues - since I'd give it access to my email via [`gws`](https://github.com/googleworkspace/cli).

Increasingly, I find myself comfortable not taking my laptop when I go out. I can talk to my phone and get stuff done - and that might be _more_ efficient than me typing it out on my laptop.

![](https://files.s-anand.net/images/2026-10-29-code-on-remote-machines.avif)
