---
title: Directional feedback for AI
date: '2026-03-09T16:54:11+08:00'
categories:
- llms
- education
description: AI helps build skills best when it gives directional critique on your work instead of simply doing the task for you.
keywords: [skill building, AI critique, feedback loops, learning design, deliberate practice, education]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7436927563740082176/
---

![](https://files.s-anand.net/images/2026-03-09-directional-feedback-for-ai.avif)

People worry that AI atrophies skills. Also that junior jobs, hence learning opportunities, are shrinking.

Can AI fill the gap, i.e. help build skills?

One approach is: Do it without AI. Then have AI critique it and learn from it.

(Several variations work, e.g. have the AI do it independently and compare. Have multiple AIs do it and compare. Have AI do it and _you_ critique - but this is hard.)

I've been preaching this for a while but didn't practice consciously until today. Here's the rough prompt I used:

```markdown
I created a data story (see index.html) and reviewed it using the "Revise data story" prompt in prompts.md.

How can I improve my reviews?

Use principles of psychology, design, visual communication, storytelling, data visualization, and more. Think about what feedback and expert would have given.

- What patterns would an expert in this field check / recognize that beginners would miss?
- What questions would an expert ask that a beginner would not know to?
- What problems / failures would an expert anticipate that beginners may not be aware of?
- How would an expert analyze this? At each step, what they are looking for and why?

Then craft a prompt to revise the data story. Compare that with my prompt.

How is it similar or different? What can you teach me based on this comparison on how I can improve giving feedback and suggest improvements to coding agents for data stories?

Document this in SELF-IMPROVEMENT.md, with examples and suggestions.
```

This started telling me how I could have given it ultra-specific feedback. So, I pivoted:

```markdown
If I'm a non-expert and my aim is to provide feedback to AI coding agents that will enable the coding agent to act like an expert and use its judgement, I wouldn't be giving specific feedback - I would be driving it directionally based on my taste and judgement. From THAT perspective, suggest how I should think differently about sharing feedback - what I did well and what could improve. Append this to SELF-IMPROVEMENT.md.
```

This was gold.

> There's a different approach: **directional feedback**. Describe the *experience gap*: how the document _should_ feel versus how it _currently_ feels -- and trust the agent's expertise. Bring taste, intent, and audience knowledge. The agent brings expertise.
>
> This is not a lesser form of feedback. It's a different division of labor. And when done well, it produces better results than imprecise expert feedback, because the agent can optimize holistically rather than executing a checklist.

It suggested best practices:

1. **Who is the audience?** Like you said: "help a layman who does not understand security understand the impact of the findings"
2. **What should they _experience_?** Not "it's missing X," but "something feels thin here" or "I don't feel the urgency yet".
3. **How should it _taste_?** e.g. "Highlight elements (sparingly, wisely) in bold" -- your use of "sparingly, wisely" is excellent.
4. **How to test?** E.g. "a reader who just reads the bold text should understand the entire story".
5. **Trust the agent.** E.g. Tell the agent to "use your judgement", "act as the expert", explicitly inviting the agent to go beyond your instructions.

And now, I've learnt a little more about giving feedback as a non-expert.
