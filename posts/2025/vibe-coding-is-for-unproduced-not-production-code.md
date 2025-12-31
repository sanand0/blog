---
title: Vibe-coding is for unproduced, not production, code
date: "2025-08-02T06:26:18Z"
lastmod: "2025-08-02T06:32:33Z"
categories:
  - coding
  - llms
wp_id: 4161
---

![Vibe-coding is for unproduced, not production, code](/blog/assets/Gemini_Generated_Image_klq1ckklq1ckklq1-1.webp)

Yesterday, I helped two people vibe-code solutions. Both were non-expert IT pros who can code but aren't fluent.

Person Alpha and I were on a call in the morning. Alpha needed to OCR PDF pages. I bragged, "Ten minutes. Let’s do it now!" But I was on a train with only my phone, so Alpha had to code. Vibe-coding was the only option.

- **Me**: Go to any chat engine and pick Claude Sonnet 4 as your model.
- **Alpha**: We have an internal chatbot that has Claude Sonnet 4.
- **Me**: Type, "Write a Python program to accept a PDF filename and page number and extract it into output.pdf".
- **Alpha**: Done. I'm not used to the CLI but can run it in PyCharm.
- **Me**: OK. Run it, but first, modify by saying, "Shorten code. Drop error handling."
- **Alpha**: Done. (Runs the code, and it works!)
- **Me**: Great. Let's do the next part. Paste the sample code for OCR from our team into the chatbot.
- **Alpha**: But our chatbot is limited to ~15K characters.
- **Me**: OK. Go to Claude.ai and paste the code.
- **Alpha**: Um… is that allowed? (Alpha's colleague pitched in, saying "If it weren't, it'll be blocked. Also, the code isn't sensitive, only data, so go ahead.")
- **Me**: Use this prompt: "Write a Python program to send output.pdf to an LLM for OCR. Use this code as reference." Then "Shorten code. Drop error handling."
- **Alpha**: (Runs the code, and it works!)

All this happened during my commute plus a haloumi-cheese-wrap purchase. A very satisfying experience!

That evening, Person Gamma and I were on a call. Gamma had a client meeting and needed an LLM image editing tool tailored. I tried the same approach.

- **Me**: Create a GitHub account, first.
- **Gamma**: I think I already have one. Let me log in.
- **Me**: I've given you maintainer access to the repo. You'll get an email. Accept it. Then upload the images you want edited.
- **Gamma**: Done (with me guiding on what to click)
- **Me**: Now log into <https://jules.google.com/>
- **Gamma**: Done
- **Me**: In Jules, select the repo and tell it what change you want.
- **Gamma**: OK. "Use the JPG images uploaded as the samples".
- (Jules churns out it's thinking)
- "Oh, wow! This is amazing! It's actually thinking about the approach."
- (Jules is done in about 2 min)
- "My god! This is going to make things so much easier!"
- **Me**: Now publish the branch, create a pull request on GitHub, and merge.
- **Gamma**: Done (with guidance).
- **Me**: Now try something yourself.
- **Gamma**: OK. "Change the prompts to something more relevant that improves the brand image." (merges the code, and it works!)

Yet another very satisfying experience. Gamma went on to make another change in my absence. Exactly the point: enable them to work without me.

---

**But isn't [vibe code legacy code](https://blog.val.town/vibe-code)**? Reducing quality, increasing technical debt?

Yes. Vibe-coding ships debt. But not all code is production code. Vibe coding can accelerate throw-away prototypes.

More importantly, **so many** ideas sit idle because devs lack time and non-devs lack skills. Vibe coding shrinks that effort. **That** is what vibe-coding is **really** for.

Think Excel. Most Excel sheets are messy apps, yet Excel's made more people productive than any language. In [No Silver Bullet](https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet.html), Fred Brooks said:

> I believe the single most powerful software-productivity strategy for many organizations today is to equip the computer-naive intellectual workers who are on the firing line with personal computers and good generalized writing, drawing, file, and spreadsheet programs and then to turn them loose. The same strategy, carried out with generalized mathematical and statistical packages and some simple programming capabilities, will also work for hundreds of laboratory scientists.

This is what vibe-coding enables. And more.
