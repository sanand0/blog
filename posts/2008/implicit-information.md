---
title: Implicit information
date: "2008-01-03T12:00:00Z"
categories:
  - interviews
wp_id: 62
---

From what I've seen, puzzles and exam questions share two un-real-worldly characteristics. Firstly, **you are guaranteed that a solution exists**. Secondly, you are given that all the **information provided to you is relevant**. (Well, not always. Some case studies I've seen have had their share of contrived irrelevance. But that's often what it is, I think. People fill in the relevant stuff, and then try and distract by adding irrelevant material in the hope of making it more real-world-like. But that's just a guess).

These are very powerful constraints. I know of nothing that has given me as much confidence in solving puzzles as the assurance that a solution exists (and that someone thinks me capable of getting it).

But it's more than just a confidence builder. The guarantee that a solution (and invariably it's a unique) is a very powerful one. An extreme case is an objective type question, which explicitly provides three guarantees:

1. There is a solution
2. There is only ONE solution
3. It is among the choices listed below

(Some papers try and take away the first guarantee by having an `(E) None of the above` category. But that's still leaving behind the other two more powerful guarantees.)

Marking answers randomly, or marking (A) for every question would still get you 25% in an exam with 4 choices. (Marking (C) would prove just as good, [unless you had a kind professor like this](http://www.rayfowler.org/2007/06/14/the-answer-is-not-always-c/).) That's better than any real-world scenario I've seen. (Real-world strategies aren't much better, though.)

Using guarantee 2, you [can eliminate choices](/blog/solving-multiple-choice-questions/) easily. If (A) and (B) do not satisfy some property of the solution, they CANNOT be the answer. There's only one solution, and these are not it.

Using guarantee 3, you can pick the last remaining choice wihout having to check it. The solution is definitely among the choices listed. So **you don't need to solve an objective type question**. You just need to pick the right answer -- which is completely different.

The principle applies even outside of objective type questions, especially in mathematically-oriented problems, or puzzles. And you can solve it by trial and error. For example, try this one from [Martin Gardner](http://en.wikipedia.org/wiki/Martin_gardner)'s [Mathematical Magic Show](http://books.google.com/books?id=DvBQAAAACAAJ):

> Two brothers own n sheep, each of which is sold for n dollars. Thus they have n2 dollars in all. This is in the form of 10 dollar notes and 1 dollar coins, the number of 1 dollar coins being less than 10 dollars. The elder brother divides the money as follows: he takes a note for himself, gives one to his younger brother, takes a note for himself and so on. At the end, the younger brother complains that the elder took the first note as well as the last. So the elder gives the younger all the one dollar coins. The younger brother complains that he still has more. So the elder brother writes the younger a cheque to equalize their share. What was the cheque for?

Now, this is a weird problem. Think about it. You're told almost NOTHING. And you have to guess what the amount is. (Note: you don't have to guess what 'n' is. That's impossible.)

Here's how I solved the problem. I said, let me find **even one case** where the elder brother gets the first and last note. Let's see what the answer is. Whatever the answer is for that case, it **has** to be the answer for all other cases -- because otherwise, the problem does not have a unique solution.

So I tried n=1. n=2. n=3. For n=4, the amount is 16. That's 1 $10 note and 6 $1 coins. The elder brother would get the first and the last $10 note. The younger would get $6. So the elder would have $4 more than the younger, and would write out a cheque for $2. (It's amazing how many people get as far as the $4, but forget to divide by two.)

You can try if for any other value that has an odd number of $10 notes. It has to be for n ending with 4 or 6. That means n2 ends in 6, and the cheque has to be for $2.

Notice that you didn't need number theory to get the answer. The assurance that there is a unique answer is enough.

---

There's another kind of implicit information usually available: the amount of information there is. For example, take the following question:

> Which city has a higher population: San Antonio or San Diego?

Children in the US apparantly had difficulty answering it. Children in Germany had less trouble. The reason? The German kids had heard of San Diego, but not San Antonio. They figured the one they'd heard of was more likely bigger. [Knowing less may be better](/blog/knowing-less-is-better/).

It's the same principle you use to check spellings. Run a Google search on two spellings. The one that returns a higher number of results is the correct spelling. (Of course, Google has a spelling correction mechanism that works well, but I use it for Tamil words. I can never tell if I should use ர or ற.)

Of course, the fundamental assumption here is: MORE INFORMATION = MORE CORRECT, which is not always the case. But the point I'm driving to is this:

> **You're always given additional information**. Even if you're not given any information, that's informative.

---

## Comments

<!-- wp-comments-start -->

- **Sathyaraj** _3 Jan 2008 12:00 pm_:
  this article was "fucking" good..i was reading a book called fooled by randomness and i just could relate to the way you and the author went about writing this.. can you write more about monte carlo simulation too?? and how it is used in finance...
- **Vasanth** _3 Jan 2008 12:00 pm_:
  Very interesting post! New insight for me into puzzles. I had always realized, but never analyzed, that I never give up when it comes to puzzles and brain teasers. On the contrary I give up relatively easily with some technical or work related problem the minute it appears probable that a (reasonable) solution does not exist.
- **S Anand** _3 Jan 2008 12:00 pm_:
  @Sathyaraj: Thanks! The sequel to "Fooled by Randomness" is pretty good to: "The Black Swan". @Vasanth: Another big problem, if you ask me, is that the problem is unbounded. In puzzles, you have a test case to determine whether you've solved it or not. In life, you aren't often sure.
- **Jayanth Sankar** _3 Jan 2008 12:00 pm_:
  Hey I like your posts. Pretty good. The question about the money between the two brothers.. I have a doubt here.. you had mentioned number of 1 dollar notes should be less than 10 dollar notes, so then 16 wont work right ? 1 - $ 10 and 6 - $1... what am I missing ?

<!-- wp-comments-end -->
