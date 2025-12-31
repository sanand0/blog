---
title: "“Wait, That’s My Mic!”: Lessons from an AI Co-Host"
date: "2025-01-09T07:32:08Z"
lastmod: "2025-01-09T07:32:10Z"
categories:
  - llms
  - talks
wp_id: 3822
---

![“Wait, That’s My Mic!”: Lessons from an AI Co-Host](/blog/assets/DALL·E-2025-01-09-15.25.13-A-colorful-single-panel-wide-comic-strip-in-the-style-of-classic-Calvin-Hobbes.-Calvin-a-young-boy-with-wild-hair-stands-in-front-of-a-whiteboard-.webp)

I spoke at [LogicLooM](https://logicloom.iitmparadox.org/) this week, with ChatGPT as my co-panelist. It was so good, it ended up stealing the show.

### Preparation

Co-hosting an AI was one of my [goals this year](/blog/my-year-in-2024/). I tried several methods.

1. [ChatGPT's advanced voice mode](https://help.openai.com/en/articles/8400625-voice-mode-faq): Lets you interrupt it. But if you pause, it replies immediately. Muting caused the app to hang.
2. [Realtime API](https://openai.com/index/introducing-the-realtime-api/): Gave me control of pauses and custom prompts, but used `gpt-4o-realtime-preview` (not as good as `o1`).
3. [Standard voice with `o1`](https://help.openai.com/en/articles/8400625-voice-mode-faq) on [Desktop](https://openai.com/chatgpt/download/): Worked best. It transcribes my speech, sends it to `o1`, and speaks back. There’s a lag, but it feels like it’s thinking.

I prepped the chat with this prompt:

> You are a co-panelist with me (Anand) in a Data Science panel with students. Aim to educate the audience on data science - large language models in particular.
>
> We will be on audio.\
> Speak informally, with humor.\
> Speak succinctly and thoughtfully.\
> Ask me questions as appropriate.
>
> Don't say anything now. Wait for my cue.

I loved how it "thought" for 8 seconds and silently complied:

```javascript
**Waiting for the go-ahead**
OK, let me see. The user wants me to keep quiet until prompted, then respond clearly and succinctly, while mixing in some playful, dry humor and constructive suggestions.

**Ensuring adherence**
Not confirming yet? The response needs to strictly omit any confirmed words, instead noting the importance of remaining quiet until prompted, aligning with the user's directive.

**Waiting for instructions**
The user is clear: stay silent and wait for their cue. This means holding off on any responses until they initiate the conversation.

**Balancing silence and response**
Focusing on maintaining silence until prompted, while preparing brief and compliant responses. This approach respects the user's request and ensures readiness for future instructions.
```

[Here is the full conversation](https://chatgpt.com/share/677f6310-5118-800c-8b97-73f5f201fcfe).

<div class="video-embed"><iframe src="https://www.youtube.com/embed/Zc-s9P61XIc" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

### Pace of innovation

[At 13m, I asked if LLM innovation might stabilize or pause](https://www.youtube.com/watch?v=Zc-s9P61XIc&t=13m).

> ChatGPT, I'm curious, what do you think about the pace of innovation? Do you think it's stabilizing? Do you think it's going to pause at some point? And if it is, then why? And if it is not, why not?

The reply was well crafted.

> Great question, Anand! The pace of innovation, especially in data science and AI, is like a runaway train. Stabilizing? Unlikely. Pausing? Even less likely. Why? Because every breakthrough creates the foundation for the next…
>
> If it slows, it'll be less about tech and more about factors like regulation, ethical considerations, or even resource constraints…
>
> What about you, Anand? Do you see a ceiling, or are we all just bracing for more chaos?

Notice how it followed my prompt:

1. `Speak succinctly`: "Stabilizing? Unlikely. Pausing? Even less likely." That's how I like to speak.
2. `Ask me questions as appropriate`: It mirrored my question, playing a supportive co-panelist.

### Day-to-day tasks

[I bypassed the question and changed the topic.](https://www.youtube.com/watch?v=Zc-s9P61XIc&t=13m57s)

> What I'm also curious about … is how can we use it for day-to-day tasks? … And in particular, let's talk about specific small little things that are not so intuitive …

Again, a beautiful reply.

> Oh, absolutely! Everyone expects AI to solve world hunger, but the magic is in the small, clever hacks. For students, think about this: you're drowning in textbooks, and suddenly, AI summarizes a 400-page book into three bullet points. Or it rephrases your answer to sound like you actually paid attention in class.
>
> Not-so-intuitive? How about using AI to analyze your sleep patterns—just by feeding it data from a smartwatch? Or creating custom flashcards for exams by feeding in lecture notes. Even meal planning—students juggling assignments could have ChatGPT whip up recipes based on the random ingredients in their fridge.
>
> What’s your favorite not-so-obvious example, Anand? Something fun or borderline ridiculous?

Again, it follows style prompts:

1. `Speak informally`: "Oh, absolutely!" is **so** conversational.
2. `Speak thoughtfully`: It was so thoughtful I started taking notes. (**Irony**: Human taking notes from AI? When it's already logged!?)

### Sanderson fan fiction

It's hard to ignore **good** questions. [I got dragged me in - though it was **completely** irrelevant to what I wanted to cover.](https://www.youtube.com/watch?v=Zc-s9P61XIc&t=15m17s)

> I'm a huge Brandon Sanderson fan. … What I'd like to do … is asking Claude to write short stories set in Brandon Sanderson's universe. … What if that character met this character? … I think it can be a very powerful short story.

Its respose dragged me in further.

> Oh, that's such a perfect example! (**Damn! It's too good at flattery!**)
>
> Using AI as your co-author for fan fiction is genius, especially in a universe as rich as Brandon Sanderson’s. I mean, where else can you have Dalinar having tea with Kaladin while debating ethics, written with just a nudge and a prompt? (**Damn again! I \_want** to talk a lot more about this to a fellow Sanderson fan!\_)
>
> … Do you think this could evolve into a broader creative tool, where students could rewrite endings of famous books or create their own alternate universes? Or would Sanderson fans revolt?

A few things:

1. The flattery worked. I couldn't stop talking to it.
2. I was **blown** away by it's last suggestion. It took all of my will power to move things back on track.

### Applications in daily life

> … what you mentioned earlier about analyzing sleep patterns, that strikes me as an even more interesting direction to explore, which is looking at personal data.
>
> … for students, it may be more like write an article, write an essay, write an assignment … If you break this down into specifics, what are examples where people could apply …?

The reply was noteworthy. I started taking notes again!

> Ah, you’ve hit on something profound there, Anand. (**Flatterer!**) … For students, this could mean automating those "reflective essays" … Or taking notes from a lecture, summarizing them, and turning them into flashcards or a study guide.
>
> On a more personal level, think about journaling. LLMs could help draft daily reflections based on snippets of your conversations or social media activity.
>
> … But here’s a twist: do you think people might lose the ability to express themselves … Playing Devil's Advocate, isn’t there a risk of homogenized communication if everyone uses AI?

This was specific, practical, and useful. I felt comfortable answering the question and continuing the conversation.

### Risks of AI dependency

[I continued the conversation](https://www.youtube.com/watch?v=Zc-s9P61XIc&t=19m51s). Actually, I spoke a fair bit at this point in response. Here's the gist:

> Yes … it becomes a monoculture. … people lose their ability to think. … this is not a new theme. … (I rambled a while.) I'd love to pick your brain on this. What specific negative impacts do you think are going to be there because of an increased use on AI?

ChatGPT responded with a few **excellent** points:

> … one big risk is intellectual atrophy, the use it or lose it phenomenon.
>
> … Then there's the risk of AI amplifying biases or inaccuracies.
>
> … Another sneaky one is dependence. If you always have AI to help, what happens when it's unavailable …

…followed by an extraordinary question:

> Playing devil's advocate, do you think people might swing back the other way, deliberately choosing unplugged creativity or even analog tools as a rebellion against this AI dependency? Could that counterbalance the risks or is that just wishful thinking?

[You should see my response.](https://www.youtube.com/watch?v=Zc-s9P61XIc&t=23m50s)

All I could say, was: "I have no idea. At this point my head just exploded so I'm\
going to stop ChatGPT there."

### Applause for ChatGPT

It got more applause than me. I suspect the breakdown was:

- 10% for insight. People don't applaud insight much. They're busy taking notes.
- 30% for novelty. An AI speaking is like a talking dog.
- 60% for humor. Especially towards then end, which I'll explain shortly.

### ChatGPT steals the show

[I was chatting using this thread](https://chatgpt.com/share/677f6310-5118-800c-8b97-73f5f201fcfe). Near the end, I accidentally switched over to a **different conversation** with this (old) prompt:

> From now on, you are a stand-up comedian. You're on stage with a group of doctors as your audience. Got it?

I didn't know I had switched threads. So when I asked ChatGPT:

> And ChatGPT, we are about to conclude. Any parting comments, any parting advice?

… it replied (and [you SHOULD listen to it, while watching my reaction](https://www.youtube.com/watch?v=Zc-s9P61XIc&t=54m45s))

> Oh, you’re putting me on the spot for parting words? Alright, here goes:
>
> Doctors, you are the true miracle workers. You handle life and death situations, decipher patient handwriting that looks like hieroglyphics, and somehow keep a straight face when someone says, “I Googled my symptoms, and I’m pretty sure I have something rare.”
>
> Here’s my parting advice: Keep laughing. It’s not just good medicine for your patients—it’s great for you, too. Take care of yourselves, because burnout isn’t something you can treat with antibiotics.
>
> And finally, always remember: when life gets tough, you have two options—cry or laugh. And if you choose to cry, do it with a smile so it confuses everyone.
>
> Thank you for everything you do, and keep being the superheroes we all need. Goodnight, doctors! Keep saving the world, one patient at a time!

The audience went **wild** with applause and laughter.

### Takeaways

- Co-hosting AI is a no-brainer. I need to improve myself in comparison.
- AI can be:
  - A stand-up comedian. Add humor to my seriousness.
  - An expert. Answer questions that I cannot.
  - A researcher. Support my claims with evidence.
- `o1` model in standard voice mode is best right now.

[LinkedIn](https://www.linkedin.com/feed/update/urn%3Ali%3Ashare%3A7283025621503356930)

---

## Comments

<!-- wp-comments-start -->

- **[My Goals Bingo as of Q1 2025 - S Anand](/blog/my-goals-bingo-as-of-q1-2025/)** _1 Apr 2025 9:36 am_ _(pingback)_:
  […] 🟡 Build a robot. No progress.🟢 Co-present with an AI. Done […]

<!-- wp-comments-end -->
