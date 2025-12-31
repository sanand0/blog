---
title: Random quotes generator
date: "2009-03-23T15:22:17Z"
lastmod: "2009-03-23T15:29:45Z"
categories:
  - tools
wp_id: 2350
---

The Random Quotes Generator is a simple tool that creates quotes by mixing up words on a web page. The results are often funny, but sometimes surprisingly insightful.

[![Monkey Typing Shakespeare](/blog/assets/flickr-monkey-typing-shakespeare_3379486150_o-jpg.webp)](/blog/assets/flickr-monkey-typing-shakespeare_3379486150_o-jpg.webp "Monkey Typing Shakespeare by S Anand, on Flickr")

Yes, this is the equivalent of a [million monkeys typing Shakespeare](http://en.wikipedia.org/wiki/Infinite_monkey_theorem), except that they’re using the works of Shakespeare as a starting point. And  it doesn’t have to be Shakespeare. It could be you or your friends.

**To try it out, visit [this page](/random-quotes-generator.html), select the link and “Add to Favorites” or drag it into your browser’s bookmark toolbar.**. Then go to any web page **that has a lot of text**, and click the link to generate random quotes.

Here’s an example of random text from [TechCrunch](http://www.techcrunch.com/).

> The net will find monetization models of theater and sporting events before them. Indeed, there has to be some way to create websites that do other than Advertising. The expected drop in internet advertising will rapidly lose its value and its impact, for reasons that can easily be understood.

For the technically minded, [Programming Pearls](http://www.cs.bell-labs.com/cm/cs/pearls/) has a section on [Generating Text](http://www.cs.bell-labs.com/cm/cs/pearls/sec153.html) that explains the concept. The bookmarklet uses an Order-2 word-level Markov chain. Translated into English, what that means is: I look at every pair of words in and find out what word is likely to follow that.

For example, in the [Generating Text](http://www.cs.bell-labs.com/cm/cs/pearls/sec153.html) page, the pair of words “we can” are followed by the words “extend”, “also”, “get” and “write” with equal probability. We pick one randomly (say “also”) and write “we can also”. Then we look at the word pair “can also”, see what word follows that, pick one at random, and so on.

This is Order-2 because we pick pairs of words. And it’s word-level rather than letter-level because we use words instead of letters as the basic building blocks.

When you’re trying it out, make sure that the page is large enough. If not, you may find that the page’s content is reproduced verbatim.

The bookmarklet is built on top of the excellent [Readability](http://lab.arc90.com/2009/03/readability.php) [bookmarklet](http://lab.arc90.com/experiments/readability/) by [Arc90](http://www.arc90.com/), which helps identify the main content to be randomized.
