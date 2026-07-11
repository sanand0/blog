---
title: Things I Learned - 16 Feb 2025
date: 2025-02-16T00:00:00+00:00
categories:
  - til
description: I explored Connected Papers for research and summarized a StackOverflow talk on AI's impact on developer productivity. I also switched to fish shell, configured the Ruff VS Code extension, and discovered the CDPATH variable and Flipper Zero.
tags: [developer-productivity, developer-tools, developer-workflow, research-workflows, ai-coding, vs-code, hardware]
---

This week, I learned:

- [Connected Papers](https://www.connectedpapers.com/) shows papers similar to each other based on co-citation and bibliographic coupling for ~50,000 papers.
- Notes from a fireside chat with [Prashanth Chandrasekar](https://www.linkedin.com/in/pchandrasekar/), CEO, StackOverflow, and the StackOverflow team
  - There's a signal that software demand is growing in 2024. Many more students took the StackOverflow survey in 2024. So more students (or other professionals) are shifting into / starting to learn software development.
  - The [AI Index](https://aiindex.stanford.edu/report/) is a good resource for AI trends.
  - Experts are better able to use AI for writing code. Less experienced developers are more likely to use AI for code reviews, project planning, etc.
  - There's a 5% _decline_ in favorability for AI tools compared to 2023, maybe due to disappointing results.
  - Pilot groups working on AI are 25-30% more productive. They're the most enthusiastic. For the rest of the company, it drops off to 5-10%
    - #LEARNING Benefit comes from NEW people becoming programmers, not existing ones getting more effective?
  - StackOverflow wants to be where the developer is.
    - The programmer workflow was: Google -> StackOverflow -> GitHub.
    - Now it's changing to ChatGPT / Cursor -> GitHub.
    - StackOverflow has a partnership with OpenAI and working on a plugin. Same with Google's Duet AI, GitHub Copilot, many others. They'll link to StackOverflow.
  - StackOverflow is driving integration actively through an enterprise Overflow API
  - Q: What tech have you seen blaze through the ranks?
    - Prashanth: Abstraction wins. Stuff that abstracts away things well and more wins. This includes Gen AI.
    - [Erin Yepis](https://stackoverflow.blog/author/eyepis/): Rust (from 3% to 12%). AWS has steady growth.
    - Erin Yapis: I have a time series spreadsheet that I'll publish.
  - Q: What technologies are unusually tightly coupled?
    - Prashanth: AWS & Google Cloud are tightly coupled.
  - Q: We have an engagement problem. Might be India-specific. What are low-effort high-return mechanisms to increase engagement.
    - [Eric Woodring](https://www.linkedin.com/in/eric-woodring-1823bb84/): Rather than a static web page, integrate it using the API. #TODO
    - [Ben Marconi](https://www.linkedin.com/in/benjaminmarconi/): Use LLMs to write post mortems and push to StackOverflow. #TODO
    - Eric Woodring: "Hydrating" the community helps.
      - We take repeat questions on Teams / Slack and seed them using LLMs.
      - We integrate with the API to auto-add Q&A.
      - Transform documentation into Q&A. Potentially **UPDATE** existing Q&A if it's wrong.
  - Q: What unexpected lessons about developer behavior have you learned while running StackOverflow?
    - Prashanth: We didn't expect developers moving away from Google. Now it moved to the IDE.
  - Q: What are you learning about developer learning behavior?
    - Ben Marconi: Generating LLM-based onboarding documents.
    - Using StackOverflow for Teams to identify who the experts are to contact for specific topics.
  - Q: Are you thinking about leveraging Stack Overflow's knowledge base for personalized or interactive learning experiences? How?
    - Prashanth: Traditionally, people use StackOveflow for productivity, learning, and flexibility (i.e. to ask/answer questions asynchronously without breaking their flow). So yeah, learning is important for us. (Duh!)
  - Q: Could Stack Overflow’s interactions help evaluate the accuracy and relevance of LLM-generated code? Or provide potential metrics on quality?
    - Prashanth: LLM accuracy improves by ~30%. Upvotes / downvotes are reinforcement learning (RL) in steroids, so that helps.
  - Q: What are your thoughts on reliance on LLMs potentially deskill-ing developers?
    - Prashanth: A real issue for _junior_ developers, not for senior ones.
    - They'll _come across_ as knowledgeable.
    - Make internal evaluations and interviews more rigorous.
  - Anand's requests for action:
    - Could I get a copy of Erin's spreadsheet? Vivek Narayanan will follow-up.
    - Could you help me learn more about hydration? Nick Madison will set up a meeting with customer success group.
- I switched to [fish shell](https://fishshell.com/) mainly because:
  - Autocomplete and tab completion works perfectly, out-of-box.
  - Syntax highlighting is beautiful
  - Great multi-line editing
- To format with [VS Code Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff), you need to point the `ruff.interpreter` setting to a Python interpreter. You can't run the ruff server without Python, even though ruff itself doesn't need Python.
- `cd` checks all paths specified in [`CDPATH`](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/cd.html) for the directory name and changes to the first match. That's pretty convenient!
- [Flipper Zero](https://flipperzero.one/) is now on my list of "To Buy" tools. It has a variety of hardware devices including NFC, RFID, Bluetooth, Infrared, etc. and is great to reverse engineer or hack devices.
