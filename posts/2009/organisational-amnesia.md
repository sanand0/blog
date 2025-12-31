---
title: Organisational amnesia
date: "2009-05-19T20:23:36Z"
lastmod: "2009-05-19T20:24:55Z"
categories:
  - business-realities
wp_id: 2374
---

It’s amazing how much of a dependency there is on individuals writing IT systems. Reminds me of that [Dilbert strip](http://dilbert-search.appspot.com/dilbert/19940610):

[![19940610](/blog/assets/flickr-19940610_3545523502_o-gif.webp)](/blog/assets/flickr-19940610_3545523502_o-gif.webp "Dilbert: 1994-06-10")

A few weeks ago, I was trying to figure out in what happens when there are multiple promotions. (Our client is a retailer.) I mean, if there’s a phone that costs £100 and there are 2 promotions: 10% off on phones and £10 off on phones. Do you apply the 10% off first and pay £80 or the £10 off and pay £81?

Funnily enough, the organisational answer is, “I don’t know.” The person who determined the logic is no longer with the firm. The person who wrote the code was a contractor and moved on to another project. The vendor hadn’t gotten around to documenting the code. Sure, the code’s **there**, and you just had to read it to figure out what it does. But no human knew what it was supposed to do.

Last week, there was a decision to rewrite some code that was 10 years old. A colleague who wasn’t quite involved in this work said, “I’m going to have to set aside 2-3 weeks for this. I wrote this stuff when I was a developer. The docs have vanished. The business owners have vanished. I’m the only one who has any clue on what it’s supposed to do.”

This week, we were trying to figure out how their store locator system works. After fiddling around with [Fiddler](http://www.fiddler2.com/), and seeing that it used Microsoft Virtual Earth, I was able to figure out that it identified stores near a location using a simple JSON API. But can we get the documentation around that? Nope. Tough luck. Nobody knows how it works any longer.

Personally, I don’t think this is unusual. We forget. Companies forget. But it’s usually good if what we forget is derivable. That’s how I got through my high-school physics exams: not by remembering stuff, but by being able to derive the stuff from a few principles.

Organisations can do the same. But to be able to do that, you need to have commonly understood principles. As Fred Brooks put it in **The Mythical Man Month**,

> I contend that conceptual integrity is the most important consideration in system design. It is better to have a system omit certain anomalous features and improvements, but to reflect one set of design ideas, than to have one that contains many good but independent and uncoordinated ideas.

One of the biggest enemies of conceptual integrity is growth. Too many people too soon, and the important decisions are taken by people who’ve never had a long chat about things. There’s another reason not to grow too fast.

---

## Comments

<!-- wp-comments-start -->

- **Kalpesh** _20 May 2009 2:27 am_:
  I guess, it should help having a debug log of things as the code is executed & the decision made in the code based on the data available.
  e.g. the code will put the log (conditionally)
  gave 10% discount, thus derived value of 90 (100 - 10)
  reducing $10 of the calculated value above = 80 (90 - 10)
  Basically, having a log of the sequence of steps, the state on which the code relies, input any function takes and output thereafter (but in a user understandable manner or in business language).
  One step closer to this could be writing code in a language that is relevant to business
  I feel we still write our code in terms of technology (arrays, exceptions, serializations etc).
  I don't mean that we should not worry about those things. But, those things should be covered under a layer which makes easy for business people OR a new comer to come back to the code and read it like a specification.
- **[Nagarjun](http://nagarjunv.blogspot.com)** _13 Dec 2009 10:50 am_:
  We faced same situation while trying to find out how the comission is calculated. In the end it so happened that the commision was being calculated based on data that was 5 years old. Nobody had realised that the new data was not comin into the system :)

<!-- wp-comments-end -->
