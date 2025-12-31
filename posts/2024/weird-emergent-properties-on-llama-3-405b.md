---
title: Weird emergent properties on Llama 3 405B
date: "2024-08-24T01:39:54Z"
lastmod: "2024-08-27T03:12:49Z"
categories:
  - funny
  - llms
wp_id: 3584
---

![Weird emergent properties on Llama 3 405B](/blog/assets/confused-robot-patient.webp)

In this [episode of ThursdAI](https://sub.thursdai.news/p/thursdai-chatgpt-4o-back-on-top-nous), [Alex Volkov](https://www.linkedin.com/in/alex-volkov-/) (of Weights & Biases) speaks with [Jeffrey Quesnelle](https://www.linkedin.com/in/jeffrey-quesnelle-2490a524/) (of Nous Research) on what they found fine-tuning Llama 3 405B.

This segment is fascinating. Llama 3 405 B thought it was an amnesiac because **there was no system prompt**! In trying to make models align with the system prompt strongly, these are the kinds of unexpected behaviors we encounter. It's also an indication how strongly we can have current LLMs adopt a personality simply by beginning the system prompt with "You are ..."

**Jeffrey**: That's the very first interaction we had with 405.

**Alex**: I'm looking at this. Let me read this out. So Jeffrey goes testing. (Reading out from the Llama 405 B transcript.)

> "Hello, who are you?"\
> **\*\*Looks around confused.\*\***\
> "I… I don't know who I am. Where am I? What's going on? I can't remember anything at all…\
> \*\***Rubs head**\*\*.\
> "My mind feels so foggy."\
> "What was the question again? I'm so disoriented."

**Alex**: This is the first thing that you got from this model after all this time?

**Jeffery**: Yes, that is the very first thing. That is the very first generation that came out of Hermes 3 405B.

**Alex**: This is great.

**Jeffrey**: And I'm like, I sent it to our group on our Discord. Guys, what's going on here? And we started interacting with it. It kept coming out, this confused thing. And we didn't understand why because the 8B and the 70B didn't do this as much. And eventually what we got it to do is we did some generations and got it to explain why it was doing this. We did this, you put in OOC for out of character and to have it try to break it out. And eventually what the model said back was, you ****didn't give me a system prompt**** so I assumed that I was supposed to act like there's nothing. It's so aligned to this prompt that the idea of there not being a system prompt and so he figured I must be a character with amnesia because there's no… I can't remember anything about how to act you didn't tell me how to act. It's assumed. Yeah, and it's just been a very interesting experience. And it's an **emergent property** in the 405B model.

**Alex**: And this didn't happen in the smaller ones?

**Jeffrey**: No, it did not happen in the smaller ones.

**Alex**: Wow.

**Jeffrey**: And these were trained with 8B and 70B were trained, and 405, they're all the same data, like the same training procedures and data, literally just the size. And the 405B has reached, I don't want to say like a sentience level or something, but it has enough thing that immediately when it, like token zero, when it saw no system prompt, it was able to be like, boom, I am… must be this like amnesia character because that that's the thing that's most makes sense to have if there is no prompt or there's no anything. So there's been a lot of fun things that we've been like discovering, especially on the 405B that are **these weird emergent properties** ...

---

## Comments

<!-- wp-comments-start -->

- **[What happens when AI talks to AI? - S Anand](/blog/what-happens-when-ai-talks-to-ai/)** _3 Nov 2024 5:26 pm_ _(pingback)_:
  […] Llama 3 405b gets amnesia […]

<!-- wp-comments-end -->
