---
title: Embeddings similarity threshold
date: "2024-02-03T03:21:02Z"
lastmod: "2024-08-27T03:12:49Z"
categories:
  - coding
  - llms
wp_id: 3508
---

![Embeddings similarity threshold](/blog/assets/image-81.webp)

`text-embedding-ada-002` used to give high cosine similarity between texts. I used to consider 85% a reasonable threshold for similarity. I almost never got a similarity less than 50%.

[`text-embedding-3-small` and `text-embedding-3-large`](https://openai.com/blog/new-embedding-models-and-api-updates) give much lower cosine similarities between texts.

For example, take these 5 words: "apple", "orange", "Facebook", "Jamaica", "Australia". Here is the similarity between every pair of words across the 3 models:

![](/blog/assets/image-79.webp)

![](/blog/assets/image-80.webp)

![](/blog/assets/image-81.webp)

For our words, new `text-embedding-3-*` models have an average similarity of ~43% while the older `text-embedding-ada-002` model had ~85%.

Today, I would use 45% as a reasonable threshold for similarity with the newer models. For example, "apple" and "orange" have a similarity of 45-47% while Jamaica and apple have a ~20% similarity.

Here's a [notebook](https://github.com/sanand0/ipython-notebooks/blob/master/embedding-similarity.ipynb) with these calculations. Hope that gives you a feel to calibrate similarity thresholds.

---

## Comments

<!-- wp-comments-start -->

- **[The LLM Psychologist - S Anand](/blog/the-llm-psychologist/)** _6 Oct 2024 11:04 am_ _(pingback)_:
  […] Over the last few months, several things changed. Most of my time is spent researching LLMs. […]

<!-- wp-comments-end -->
