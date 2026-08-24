---
title: Local agents are good but slow
date: 2026-08-21T12:40:28+08:00
categories:
- llms
description: I tested local agents with Ollama and Pi on an 8 GB GPU. They were slow but useful in emergencies, while ChatGPT found the right blog post through smarter searches and self-correction.
tags: [ai-agents, ai-coding-agents, llms]
---

Last year, I shared how local LLMs [are](https://www.s-anand.net/blog/llm-gpu-or-api-the-cost-will-surprise-you/) [expensive](https://www.s-anand.net/how-to-use-llms-better/). There are only 3 reasons to use them over an inference API:

1. **You have no choice**, e.g. Government, pharma, finance, or other sensitive data.
2. **You have free GPUs**, e.g. your laptop, local data center with sunk cost, free cloud credits, etc. This doesn't scale.
3. **You want to learn**.

This year, I finally started using them for a combination of #1 (on flights) and #2 (my 8 GB NVIDIA RTX 2000).

It began with simple queries on [Edge Gallery on my mobile](https://www.s-anand.net/blog/ai-on-flights/) - like "Is this vegetarian?", "What do you call those caption boxes in comics?", etc.

I recently read how easily you can run [Pi with Ollama](https://docs.ollama.com/integrations/pi) and that `ornith:9b` and `gemma4:e4b-it-qat` are [good models for my system](https://chatgpt.com/share/6a870334-8e50-83e8-a5f9-8cc13940993f) <!-- https://chatgpt.com/c/6a802a27-5cf4-83e8-b999-f483c97263db --> so I can just run:

```bash
ollama launch pi --model gemma4:e4b-it-qat
```

... to get a reasonable coding model locally.

I tried it for a few non-technical things first. For example:

1. That morning, I asked my talkative train neighbor, "Are you an extrovert?" He said "No, I'm an introvert." On the flight, [Gemma4 explained the contradiction well](https://www.s-anand.net/blog/extrovert-or-introvert/)
2. I tried reducing my battery usage on the flight by asking it what different processes were. It didn't solve the problem but gave me some ideas.

But that's not to say it's great. For example, when I asked it:

> Can you find a blog post where I spoke about an incident at BCG in the early 2000s (I may have written about it later) where I asked them, "you keep saying we should do more of this and more of that, what should we do less of"? I think there is an entire blog post about that.

Here's the approach it took (comments are mine): <!-- AgentsView http://localhost:8080/sessions/pi%3A01a0228b-9a9d-7fc7-851f-57f7d35029c9 -->

```bash
# List my blog posts - which showed this: https://github.com/sanand0/blog/tree/main/posts
ls ~/code/blog/posts/

# Search for "BCG" - which returned 63 results, NONE of which were the post I needed!
grep -r -i "BCG" ~/code/blog/posts/

# Read the most likely first candidate
cat ~/code/blog/posts/2000/another-day-at-lbs.md

# ...and the next
cat ~/code/blog/posts/2000/boston-consulting-group-interview.md

# .. and the next
path: ~/code/blog/posts/2012/the-next-chapter-of-my-life.md

# Back-track and search for doing more or less in 2000-2003 - again, no results
grep -r -iE "d o more|d o less|sh ould" ~/code/blog/posts/200[0-3]/

# Try across all years - this gives 2718 results
grep -r -iE "more|less" ~/code/blog/posts/
```

... and it's been **_**20 minutes**_** so far - but it probably would have gotten to the answer if it hadn't crashed for some reason.

![](https://files.s-anand.net/images/2026-08-21-local-agents-are-good-but-slow.avif)

On the other hand, GPT-5.6 Sol (on ChatGPT) did the following (comments are mine): <!-- https://chatgpt.com/c/6a87d41f-7fb8-83e8-ace3-e7f692fbc76b -->

```bash
# Write a couple of multi-line scripts to search for "do more", "do less", etc. AS WELL AS for "BCG" and "Boston Consulting" and "consult"
set -euo pipefail
BLOG="$HOME/code/blog/posts"
test -d "$BLOG"
echo '--- phrase matches ---'
rg -n -i --glob '*.md' --glob '*.html' --glob '*.txt' \
  -e 'do more' -e 'do less' -e 'less of' -e 'more of this' -e 'what should we do less' \
  "$BLOG" | head -120 || true

echo '--- BCG/context matches ---'
rg -n -i --glob '*.md' --glob '*.html' --glob '*.txt' \
  -e '\bBCG\b' -e 'Boston Consulting' -e 'consult' \
  "$BLOG" | head -120 || true

# That failed. It provided the wrong home directory: /home/oai/share
#   - It got confused with its own container.
# But it corrected itself and tried again. That got ~220 GOOD matches.

# Now, it does 3 things:
# 1. Read the most promising post (which is the correct one): https://www.s-anand.net/blog/less-is-more/
# 2. ALSO search in the file for related terms like Infosys, manager, office, consultant, years ago, etc.
# 3. A BRILLIANT step - search for other phrases, like "do less... do more" or "what... do less", etc.
#    Just in case it missed something!
set -euo pipefail
F="$HOME/code/blog/posts/2008/less-is-more.md"
echo '--- less-is-more.md ---'
nl -ba "$F" | sed -n '1,125p'

echo '--- nearby explicit provenance clues ---'
rg -n -i -C 3 'BCG|Infosys|manager|office|consultant|years ago|back then|firm' "$F" || true

echo '--- exact/near quote elsewhere ---'
rg -n -i --glob '*.md' -C 2 \
  -e 'you can.t do more of something unless you do less' \
  -e 'what.*do less' \
  -e 'do less.*do more' \
  "$HOME/code/blog/posts" | head -120 || true
```

That's it. That's all it needed to find the post.

What impressed me about _both_ agents is that:

1. They used **smart synonyms** just from my query - they _know_ how people typically mis-spell.
2. They **corrected themselves** as they went along. For example:
    - Pi found no results between 2000-2003, and extended to all my blog posts.
    - ChatGPT got the home directory wrong, but corrected itself.
3. They **revised strategies** as they learnt. For example:
   - Pi realized I might not have mentioned "BCG" in my post.
   - ChatGPT realized I might have _multiple_ blog posts about this.
   - Both updated search terms to use based on the results. For example, ChatGPT learnt I was at Infosys from the search results and _added_ that as a search term!

So, I've reached a mental tipping point. **Local agents are good enough in an emergency**. They're slow, but they can get my work done if needed.
