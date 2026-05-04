---
title: NPTEL Applied Vibe Coding Workshop
date: 2026-01-11T22:53:28+08:00
categories:
  - llms
  - coding
  - education
description: I summarize my NPTEL workshop on vibe coding, sharing over thirty lessons on building apps via natural language. I cover practical prompt frameworks, iterative workflows, and security frameworks like Simon Willison's 'lethal trifecta' for AI development.
keywords: [vibe coding, prompt engineering, llms, lethal trifecta, nptel, software development]
---

For those who missed my [Applied Vibe Coding Workshop](https://elearn.nptel.ac.in/shop/iit-workshops/ongoing/computer-science/applied-vibe-coding-workshop/) at NPTEL, here's the video:

<div class="video-embed"><iframe src="https://www.youtube.com/embed/m9mIe4baN-k" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

You can also:

- [Read this summary of the talk](https://sanand0.github.io/talks/2026-01-11-nptel-vibe-coding-workshop/)
- [Read the transcript](https://github.com/sanand0/talks/blob/main/2026-01-11-nptel-vibe-coding-workshop/transcript.md)

![Sketchnote of the talk](https://raw.githubusercontent.com/sanand0/talks/refs/heads/main/2026-01-11-nptel-vibe-coding-workshop/sketchnote.avif)

Or, here are the three dozen lessons from the workshop:

- Definition: Vibe coding is building apps by talking to a computer instead of typing thousands of lines of code.
- Foundational Mindset Lessons
  1. **"In a workshop, you do the work"** - Learning happens through doing, not watching.
  2. **"If I say something and AI says something, trust it, don't trust me"** - For factual information, defer to AI over human intuition.
  3. **"Don't ever be stuck anywhere because you have something that can give you the answer to almost any question"** - AI eliminates traditional blockers.
  4. **"Imagination becomes the bottleneck"** - Execution is cheap; knowing _what_ to build is the constraint.
  5. **"Doing becomes less important than knowing what to do"** - Strategic thinking outweighs tactical execution.
  6. **"You don't have to settle for one option. You can have 20 options"** - AI makes parallel exploration cheap.
- Practical Vibe Coding Lessons
  1. **Success metric**: "Aim for 10 applications in a 1-2 hour workshop" - Volume and iteration over perfection.
  2. **The subscription vs. platform distinction**: "Your subscriptions provide the brains to write code, but don't give you tools to host and turn it into a live working app instantly."
  3. **Add documentation for users**: First-time users need visual guides or onboarding flows.
  4. **Error fixing success rate**: "About one in three times" fixing errors works. "If it doesn't work twice, start again-sometimes the same prompt in a different tab works."
  5. **Planning mode before complex builds**: "Do some research. Find out what kind of application along this theme can be really useful and why. Give me three or four options."
  6. **Ask "Do I need an app, or can the chatbot do it?"** - Sometimes direct AI conversation beats building an app.
  7. **Local HTML files work**: "Just give me a single HTML file... opening it in my browser should work" - No deployment infrastructure needed.
  8. **"The skill we are learning is how to learn"** - Specific tool knowledge is temporary; meta-learning is permanent.
- Vibe Analysis Lessons
  1. **"The most interesting data sets are our own data"** - Personal data beats sample datasets.
  2. **Accessible personal datasets**:
     - WhatsApp chat exports
     - Netflix viewing history (Account > Viewing Activity > Download All)
     - Local file inventory (`ls -R` or equivalent)
     - Bank/credit card statements
     - Screen time data (screenshot > AI digitization)
  3. **ChatGPT's hidden built-in tools**: FFmpeg (audio/video), ImageMagick (images), Poppler (PDFs)
  4. **"Code as art form"** - Algorithmic art (Mandelbrot, fractals, Conway's Game of Life) can be AI-generated and run automatically.
  5. **"Data stories vs dashboards"**: "A dashboard is basically when we don't know what we want." Direct questions get better answers than open-ended visualization.
- Prompting Wisdom
  1. **Analysis prompt framework**: "Analyze data like an investigative journalist" - find surprising insights that make people say "Wait, really?"
  2. **Cross-check prompt**: "Check with real world. Check if you've made a mistake. Check for bias. Check for common mistakes humans make."
  3. **Visualization prompt**: "Write as a narrative-driven data story. Write like Malcolm Gladwell. Draw like the New York Times data visualization team."
  4. **"20 years of experience"** - Effective prompts require domain expertise condensed into instructions.
- Security & Governance
  1. **Simon Willison's "Lethal Trifecta"**: Private data + External communication + Untrusted content = Security risk. **Pick any two, never all three.**
  2. **"What constitutes untrusted content is very broad"** - Downloaded PDFs, copy-pasted content, even AI-generated text may contain hidden instructions.
  3. **Same governance as human code**: "If you know what a lead developer would do to check junior developer code, do that."
  4. **Treat AI like an intern**: "The way I treat AI is exactly the way I treat an intern or junior developer."
- Business & Career Implications
  1. **"Social skills have a higher uplift on salary than math or engineering skills"** - Research finding from mid-80s/90s onward.
  2. **Differentiation challenge**: "If you can vibe code, anyone can vibe code. The differentiation will come from the stuff you are NOT vibe coding."
  3. **"The highest ROI investment I've made in life is paying $20 for ChatGPT or Claude"** - Worth more than 30 Netflix subscriptions in utility.
- Where Vibe Coding Fails
  1. **Failure axes**: "Large" and "not easy for software to do" - Complexity increases failure rates.
  2. **Local LLMs (Ollama, etc.)**: "Possible but not as fast or capable. Useful offline, but doesn't match online experience yet."
- Final Takeaways
  1. **"Practice vibe coding every day for one month"** - Habit formation requires forced daily practice.
  2. **"Learn to give up"** - When something fails repeatedly, start fresh rather than debugging endlessly.
  3. **"Share what you vibe coded"** - Teaching others cements your own learning. "We learn best when we teach."
  4. **Tool knowledge is temporary**: "This field moves so fast, by the time somebody comes up with a MOOC, it's outdated."
