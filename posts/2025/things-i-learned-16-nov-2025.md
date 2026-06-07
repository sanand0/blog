---
title: Things I Learned - 16 Nov 2025
date: 2025-11-16T00:00:00+00:00
categories:
  - til
description: I find faster Ubuntu mirrors, learn FLIP animation techniques, and analyze the Microsoft-OpenAI deal. Most excitingly, I calculate the low cost of using AI as a personal coach to analyze 180 of my recorded calls.
keywords: [flip animation, gemini 2.5 flash, claude code, olmoearth, microsoft-openai deal, codemods, deepseek-v3.2-exp, vaultgemma]
---

This week, I learned:

- Windows 11 got some _very_ practical updates. Notepad now supports Markdown preview natively. MS Paint has an opacity filter. Microsoft Copilot can share screens and speak/listen.
- Things I learn when Ubuntu drivers crashed on my laptop:
  - The [SG.GS Ubuntu ISO mirror](http://mirror.sg.gs/ubuntu-releases/24.04.3/ubuntu-24.04.3-desktop-amd64.iso) is a _lot_ faster than the [official Ubuntu ISO download](https://releases.ubuntu.com/24.04.3/ubuntu-24.04.3-desktop-amd64.iso) (5 min vs 12 hours).
  - [Rufus](https://rufus.ie/en/) and [balenaEtcher](https://www.balena.io/etcher/) are the de facto tools for bootable USB drives from ISO.
- Gemini 2.5 Flash Image is not great at generating text. But a clever a workaround is to provide the rendered text as an image input! Also, Gemini 2.5 Flash Image seems to ignore commands that try style transfer (e.g. "turn me into Studio Ghibli"). [GemImg](https://github.com/minimaxir/gemimg)
- [FLIP animation](https://css-tricks.com/animating-layouts-with-the-flip-technique/) is an efficient animation technique.
  - Capture the First position
  - Apply the Last position (changing position, size, rotation, etc.)
  - Invert, i.e. apply just the `transform` that'll move it back to the First position
  - Plan the animation. This _only_ needs to change transform, hence no DOM reflow.
- Asking coding agents to create a [codemod](https://github.com/rajasegar/awesome-codemods) for large-scale refactoring works well [Peter Steinberger](https://x.com/steipete/status/1987771067998339352)
- When to quit vs persist. [#](https://claude.ai/chat/8e9252da-6186-4876-be2e-d81c27a2cc7d) [#](https://chatgpt.com/c/6911a446-6018-8320-aed7-808be506d4e6)
  1. Do stats/signals support positive outcome? QUIT if not.
  2. Crossed any limits you set for yourself? QUIT if so. (Run pre-mortems to find these stats/signals and limits.)
  3. Is the decision hard to reverse AND uncertainty high? QUIT if so. Else you can experiment cheaply. (Create reversibility.)
  4. Are youI continuing because of past effort or pride? QUIT if so. (Set review cadence.)
  5. Is there a better alternative? SWITCH if so. (Get outside help.)
- Once a model generates an output, an agentic look tends not to change the fundamental approach and just tweaks it. So, if a solution is directionally wrong, restarting works better than iterating. [Agentic Pelican on a Bicycle](https://www.robert-glaser.de/agentic-pelican-on-a-bicycle/)
- [Reading between the lines on the Microsoft OpenAI deal](https://claude.ai/share/4168c00c-49f3-4007-a26a-5699bf581648):
  - Microsoft values OpenAI's growth (financial return) than control
  - Neither trusts the other enough to decide what's AGI
  - Microsoft gets some wins: models until 2032 (even post AGI) as well as research IP. Both parties expect AGI between 2027-2030.
  - OpenAI keeps all consumer hardware - so is betting hard on hardware. It's more Apple than Microsoft territory
  - Divorce preparation: Microsoft can pursue AGI with other partners. OpenAI can purchase compute from anyone and release open weights models. Infra has more value than model dev!
- [OlmoEarth](https://allenai.org/olmoearth) is a set of image models trained on labelled geospatial data. That's useful for deforestation and land cover monitoring, wildfire detection, urban growth monitoring, crop mapping, etc. The models are open weights and can be fine-tuned.
- Claude Code's [output styles](https://code.claude.com/docs/en/output-styles) are a way of using Claude Code for anything (e.g. writing, analysis, research, personal advice, etc.), not just coding. Create a `~/.claude/output-style/your-style-name.md` and run `/output-style your-style-name` to replace the system prompt will be replaced. You can also use the `--system-prompt` and `--append-system-prompt` flags with the CLI.
- Following [Ethan Mollick's lead](https://x.com/emollick/status/1987355374928769395?s=20) I asked: _I can travel back in time to any time before 1500 in India and change only one thing. What is the single thing you would change? Nothing obvious._.
  - [ChatGPT](https://chatgpt.com/share/6912a989-c858-800c-9039-a38b3f5b090e): **Create a single, simple, phonetic script** for all public life in India around 1100 CE.
  - [Claude](https://claude.ai/share/11be725d-cca3-4108-bafd-58eb3ce0510e): **institutionalize systematic historical recordkeeping**, introduce limited liability commercial entities, and mandate systematic translation of Sanskrit technical texts into all major regional languages.
  - How about now? ChatGPT suggests: **make all public rules and records computable by law**. Claude suggests: **make all state-level entitlements and civil documentation fully portable** across India.
- For the first time in history, Russian troops surrendered to a wheeled drone that carried 138 pounds of explosives - [Washington Post](https://www.washingtonpost.com/world/2025/10/20/ukraine-russia-battlefield-land-drones).
  Given the cost and accessibility of drones, I guess drone terrorist attacks will soon emerge.
- HTML + JS apps will last longer than server-side apps and it makes sense to write more of those. For essential back-end services, keep them generic. Specific services layers I see are:
  - Auth (e.g. Google Auth, Auth0, Supabase, ...)
  - Storage (e.g. Supabase, Firebase)
  - LLMs (e.g. OpenAI, Claude, OpenRouter)
  - Communications (e.g. EmailJS)
  - ... #TODO Extend with LLMs
- https://gistpreview.github.io/ is an unofficial GIST preview tool. It accepts a `?GIST_ID` and displays the gist as a standalone HTML page. [Simon Willison](https://simonwillison.net/2025/Oct/23/claude-code-for-web-video/)
- [XSLT is deprecated in Chrome](https://developer.chrome.com/docs/web-platform/deprecating-xslt). So the [`<script>` tag in XML](https://jakearchibald.com/2025/making-xml-human-readable-without-xslt/) will become the new way of rendering RSS/Atom. This is one of the rare "break-the-web" changes from browsers. [Simon Willison](https://simonwillison.net/2025/Nov/5/removing-xslt/)
- "India has _absurdly_ low internal migration - around 9% annual migration rate versus 25-30% in China or the US. Not because people don't want to move, but because the cost of moving is artificially massive. You lose your ration card, state entitlements, kids' school continuity, voting rights, ..." [#](https://claude.ai/chat/b7f7ceb9-67fe-4b42-af53-69bb9bbf1fae)
- Rolf Dobelli's [The Not To-Do List](https://www.goodreads.com/book/show/222216333-the-not-to-do-list) is a good application of inversion. Also, the chapter titles themselves explain most of the message, which is very helpful. Just thinking about any of these can be a useful path to improvement.
  1. Let things fall apart
  2. Feed your weaker self
  3. Be unreliable
  4. Be an asshole
  5. Have high expectations
  6. Drift through the day
  7. Mess up your marriage
  8. Be a quitter
  9. Be hypocritical
  10. Cling to your bad habits
  11. Set the wrong goals
  12. Drink yourself miserable
  13. Get involved in other people’s drama
  14. Only learn from your own experience
  15. Be hyperactive on social media
  16. Indulge in road rage
  17. Surround yourself with negative people
  18. Micromanage your neighbours
  19. Say yes to drugs
  20. Get stuck in your career
  21. Never be playful
  22. Feel guilty
  23. Practise ingratitude
  24. Trust your banker
  25. Be paranoid
  26. Make other people feel unimportant
  27. Live in the past
  28. Listen to your inner voice
  29. Expect rationality
  30. Get nihilistic
  31. Catastrophize
  32. Consider money unimportant
  33. Cultivate a victim mentality
  34. Become a lapdog
  35. Get rich quick, get smart quick
  36. Ruminate
  37. Trade your reputation for money
  38. Never suffer
  39. Let your emotions define you
  40. Try to end it all
  41. Marry the wrong person – and stay with them
  42. Celebrate your resentment
  43. Join a cult
  44. Try to change people
  45. Say everything you think
  46. Spin multiple plates
  47. Do only shallow work
  48. Invite bad people into your life
  49. Go where the competition is strong
  50. Say yes to everything
  51. Crowd your life with gadgets
  52. Fall into the content trap
- [DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) has linear inference time, i.e. longer inputs don't take longer time. It picks the top 2K most relevant tokenss from the input instead. This can make model inference cheaper and faster.
- California's Bill [AB 316](https://legiscan.com/CA/text/AB316/id/3223647) makes the people who build autonomous systems liable for their actions. That's quite a step.
- Udio and Universal are launching a platform to [generate music in the style of famous artistes](https://www.udio.com/blog/a-new-era). An interesting new way to monetize. Fingerprinting music is a hot area.
- [VaultGemma](https://services.google.com/fh/files/blogs/vaultgemma_tech_report.pdf) shows a fine-tuning approach that eliminates personal info that appears only once from memorization. It works by adding noise to weights and capping weights updates so that no one example has undue influence. Model quality is mostly the same.
- Amazon is giving drivers smart glasses to scan packages, get directions, capture proof of delivery and detect hazards. Cool! [TechCrunch](https://techcrunch.com/2025/10/22/amazon-unveils-ai-smart-glasses-for-its-delivery-drivers/)
- ⭐ Over 3 months, I've recorded ~180 calls. Processing each costs ~1.25 cents (GPT-5) and 1 year's conversations cost ~$9. That's _incredible_ value for money if I hired GPT-5 / Codex as a data-driven personal coach to guide me on:
  - What are my blindspots? That is, feedback people share with me that I ignore?
  - What are the clusters of persona that I interact with and which of these have a positive and negative influence on me?
  - Where am I am being unreliable? Where am I being an asshole?
  - Where are my expectations high? Where are they low? Where would the opposite have helped?
  - Where do I quit early? Where do I persist? Where would the opposite have helped?
  - What good habits should I continue? What bad habits should I stop?
  - What are the strongest opportunities to thank or praise that I missed? Is there a pattern? What triggers could I use to build this habit?
  - Where have I tried to change people? Where have people tried to change me?
  - Where have I spotted wrong questions? That is, rather than answering the question, I spotted the more apt question and answered that instead?
  - ... and a hundred other questions that I wouldn't even know to ask.
- Sub-agents can run parallel / independent tasks while keeping the context window small. (But the advantage over `xargs` seems marginal.) [Simon Willison](https://simonwillison.net/2025/Oct/11/sub-agents/)
  - Document, lint, type-check, add test cases (or other similar tasks) for all folders in a monorepo.
  - Research and create a report for each topic in \*/RESEARCH.md.
  - Synthesize learnings from each conversation in transripts/\*.md.
- "If you're signed into sensitive accounts like your bank or your email provider in your browser, simply summarizing a Reddit post could result in an attacker being able to steal money or your private data." [Brave](https://brave.com/blog/unseeable-prompt-injections/)
- OpenAI Atlas has a "Watch Mode" that will stop working if you move away from that tab. Useful to keep an eye on sensitive sites. [Simon Willison](https://simonwillison.net/2025/Oct/22/openai-ciso-on-atlas/)
- "... image editing platforms seem like they’ll eat and subsume Photoshop... modern image editors – especially Nano Banana from Google Gemini – ... they’re extremely effective and, increasingly, instructable" - [Import AI](https://jack-clark.net/2025/10/27/import-ai-433-ai-auditors-robot-dreams-and-software-for-helping-an-ai-run-a-lab/).
  Facebook now suggests edits to photos - [TechCruch](https://techcrunch.com/2025/10/17/facebooks-ai-can-now-suggest-edits-to-the-photos-still-on-your-phone/).
- [WebPerl](https://webperl.zero-g.net/) runs Perl in the browser via WebAssembly. [Simon Willison](https://simonwillison.net/2025/Oct/22/sloccount-in-webassembly/)
