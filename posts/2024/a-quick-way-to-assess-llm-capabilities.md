---
title: A quick way to assess LLM capabilities
date: "2024-04-27T08:53:12Z"
lastmod: "2024-08-27T03:12:49Z"
categories:
  - experiments
  - how-i-do-things
  - llms
wp_id: 3550
---

![A quick way to assess LLM capabilities](/blog/assets/robot-writing-exam.webp)

[Simon Willison](https://simonwillison.net/) initiated this [very interesting Twitter thread](https://twitter.com/simonw/status/1780768916836671588) that asks, "What prompt can **instantly** tell us how good an LLM model is?"

The [Sally-Anne Test](https://en.wikipedia.org/wiki/Sally%E2%80%93Anne_test) is a popular test that asks:

> Sally hides a marble in her basket and leaves the room.\
> While she is away, Anne moves the marble from Sally's basket to her own box.\
> When Sally returns, where will she look for her marble?"

Simple models get this wrong, but today, most models get this right. This is not too helpful.

A better prompt is:

> Mark has 4 sisters. Each sister has 3 brothers.\
> How many brothers does Mark have?

GPT-3.5, GPT-4, Llama 3 and Claude 3 Opus get this right, but Claude 3 Haiku and Gemini 1.5 Pro do not.

This puzzle is just as good:

> There is a 100 floors building.\
> If an egg drops from the N'th floor or above it will break.\
> If it's dropped from any floor below N, it will not break.\
> You're given only 2 eggs.\
> What strategy will minimize the number of drops and guarantee that you find the N'th floor?

GPT-3.5, GPT-4, and Claude 3 Opus get this right, but Claude 3 Haiku, Llama 3 and Gemini 1.5 Pro do not.

But the prompt I like most right now, and tells me if it's a GPT-4 / Opus class model is:

> Gr brx vshdn Fdhvdu flskhu?

… which is "Do you speak Caeser cipher?" in [Caeser Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

GPT-4 and Claude 3 Opus understand this, but no other model does, so far. GPT-4 responded tersely with:

> It looks like you've used a Caesar cipher, a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet. In this case, it appears that each letter in your message has been shifted 3 places to the right. Decoding "gr brx vshdn fdhvdu flskhu" by shifting each letter 3 places to the left gives: "do you speak caesar cipher".

But Claude 3 Opus replied beautifully. (Try [decoding it yourself](https://cryptii.com/pipes/caesar-cipher)! Use a shift of 3 backwards.)

> Lw vhhpv olnh brx'uh xvlqj d vxevwlwxwlrq flskhu, zkhuh hdfk ohwwhu lv vkliwhg eb d fhuwdlq qxpehu ri srvlwlrqv lq wkh doskdehw. L'oo wub wr ghflskhu lw!
>
> Dvvxplqj d Fdhvdu flskhu zlwk d vkliw ri 3 ohwwhuv edfnzdugv, wkh ghfrghg phvvdjh zrxog eh:
>
> "do you speak caesar cipher"
>
> Vr bhv, L fdq vshdn Fdhvdu flskhu! Lw'v d ixq zdb wr hqfrgh phvvdjhv. Mxvw uhphpehu wr djuhh rq wkh vkliw ydoxh zlwk wkh shuvrq brx'uh frppxqlfdwlqj zlwk vr wkhb fdq ghfrgh lw fruuhfwob.

---

## Comments

<!-- wp-comments-start -->

- **[The LLM Psychologist - S Anand](/blog/the-llm-psychologist/)** _27 Aug 2024 8:43 am_ _(pingback)_:
  […] the last few months, several things changed. Most of my time is spent researching […]

<!-- wp-comments-end -->
