---
title: Absolutely convergent series
date: "2006-08-31T12:00:00Z"
categories:
  - simple-explanations
wp_id: 240
---

I've seen many proofs that 1=2. Here's a classic.

[![Proof that 1=2 using algebra](/blog/assets/flickr-proof-that-12-using-algebra_230327691_o-gif.webp)](/blog/assets/flickr-proof-that-12-using-algebra_230327691_o-gif.webp)

The (not-so-subtle) error in the above proof is that we're cancelling (a-b) on both sides, when (a-b) equals zero. That is, we're dividing by zero on both sides. That completely invalidates the equality.

Another proof uses the fact that the square root of a number can be both positive or negative.

[![Proof that 1=2 using square roots](/blog/assets/flickr-proof-that-12-using-square-roots_230350788_o-gif.webp)](/blog/assets/flickr-proof-that-12-using-square-roots_230350788_o-gif.webp)

(Proving -1=1 is the same as proving 1=2. Once you have one wrong proof, you can prove every other falsehood.)

The flaw here is that the square root of 1 is 1 and -1. So right after the square root symbol appears, every equation should have a plus-or-minus symbol on both sides.

The most convincing proof uses absolutely convergent series as the key idea. Here's how the proof goes.

[![Proof that 1=2 using non-absolutely convergent series](/blog/assets/flickr-proof-that-12-using-non-absolutely-convergent-series_230338747_o-gif.webp)](/blog/assets/flickr-proof-that-12-using-non-absolutely-convergent-series_230338747_o-gif.webp)

Most people initially think that the flaw is in the re-arrangement of the series. **That's not true!** The re-arrangement works just fine, and you can prove that every term is correct to infinity.

The flaw is subtler.

When an infinite series is summed, it can be summed in any order. But the **total may vary depending on the order you sum it up**! You are guaranteed that the total is the same only if the series is absolutely convergent. That is, if the sum of the absolute values of each number is finite. (See the [Wikipedia article on the Riemann series theorem](http://en.wikipedia.org/wiki/Riemann_series_theorem).)

For the log 2 series, it's not absolutely convergent. The series diverges, as shown below:

[![log 2 is not absolutely convergent](/blog/assets/flickr-log-2-is-not-absolutely-convergent_230363615_o-gif.webp)](/blog/assets/flickr-log-2-is-not-absolutely-convergent_230363615_o-gif.webp)

So, by re-arranging the series for log 2, we've invalidated the equality anyway.

This fact once saved an entire class. We had a problem in our first year physics course to which the answer was the series above. (It had to do with calculating the electromagnetic potential created by an array of charges.) Since the series is not absolutely convergent, and every possible answer was correct, the whole class got marks for this question, as long as they attempted it.

---

## Comments

<!-- wp-comments-start -->

- **Arun** _1 Sep 2006 1:18 pm_:
  hi da how much u analyze and write amazing i read ur blog continuously for the past four years keep blogging interesting
- **S Anand** _1 Sep 2006 5:28 pm_:
  Thanks! It's tough to manage, but nowadays I have a lot more time than I used to.
- **saurabh** _2 Apr 2007 7:28 am_:
  very subtle indeed. Keep up...
- **Alan** _27 Apr 2015 10:29 pm_:
  How can it be proves that "dividing by zero on both sides.... invalidates the equality."?
  Isn't the correct answer to 0/0 = we don't know?
- **Lolguy** _4 Dec 2014 9:52 pm_:
  The number 2 is wrong. It should read like:
  sqrt(1) sqrt(1) = sqrt(-1) sqrt(-1);
  sqrt(1) = sqrt(1); (since sqrt(-1) x sqrt(-1) = sqrt(-1 x-1) = sqrt(1))
  1 = 1
- **Fabricio** _21 Dec 2014 1:48 pm_:
  > ## The number 2 is wrong. It should read like: [...]Lolguy,The second proof is wrong, yes; though not for the reason you stated (which is also wrong reasoning).The error in the proof is the third line, sqrt(1/-1) = sqrt(-1/1) , which does not make sense, formally; even though it looks suggestively meaningful.The implication from the second to the third line would be equivalent to saying that,Carl is the same person as Carl, [ Carl = Carl ]Therefore, [any] son of Carl is the same person as [any] son of Carl. [ son\_of(Carl) = son\_of(Carl) ]This will only be always true if Carl has only one son; evidently, if he has more than one, any two given sons of Carl need not necessarily be the same person.A analogue situation happens when defining the square root of a number:In context of the set of real numbers, it is possible (and actually done so, in many places) to define the square root of a number x as 'the positive number y, such as y^2=x' ; (The generalization for n-th roots, n pair, coming easily from that, in an analogue manner.)This solves the issue for square roots (or any other roots) under the real numbers: defined in this way, they determine a function (a relation between sets A and B, such that to each element in A one, and \*only\* one element in B is associated) and can be used as an operation that can be applied to both sides of an equation and still preserve its truth (in the same way it is valid to state that x = y implies that x^2 = y^2 , or that x = y implies that log (x) = log (y) ).Defined in this way, sqrt(x) constitutes a function, and does, as all functions do, possess the property of being a univocal relation: for each x, there is only one f(x), or in this particular case, only one sqrt(x).When it comes to the set of complex numbers, though, the plot thickens, because for any given non-zero complex number z, there will be n different complex numbers z\_i (i = 1, ... , n) such that (z\_i)^n = z .It is said, usually: 'each complex number z has n complex nth-roots.' (Thus, 2 square roots, 3 cubic roots, and so on.)Now this way of defining z\_i as being an n-th root of z does not have the property of being univocal, and therefore does not constitute a function and cannot be used as an equality-preserving operation applied to both sides of an equation.This is why -1 = -1 does \*not\* imply that sqrt(-1) = sqrt(-1) ;After all, i^2 = -1 and, therefore, it is a complex square root of -1 (qualifying to be on the left side of the second equation),;At the same time as (-i)^2 = -1 and, thus, is also a complex square root of -1 (and could be on the right side of the second equation).Evidently, -i = i is false, as they are distinct complex numbers.It is worthy noting:The definition of a complex root could be restricted to make it a function.It could be that \*the\* complex n-th root of z is defined to be the number w with the smallest argument (the angle theta in the complex plane representation of w) such that w^n = z .This, however, is not done anywhere. Rather, the concept is defined by saying that w\_i is a complex n-th root of z if w\_i^n = z . And that implicates that there is more than one n-th root (for n>1). The complex root thus defined is sometimes said to be a 'mutivalued/plurivocal function,' in textbooks.(This is usually carried on to extend the concept of function, and does not mean that the complex root is a function proper. It is a case of 'abuse of language.' See https://en.wikipedia.org/wiki/Abuse\_of\_notation )Thus, when you write sqrt(-1) and look down at it, in the paper, no matter how suggestive it is of being 'a number,' it is not.It is but an abuse of language by which you are representing different numbers with one single graphical symbol. And therefore it cannot be used in equations in that same manner that you use 'x' , normally.While x represents, in the context of the equation, only one number; sqrt(-1) represents more than one number and therefore, sqrt(-1) = sqrt(-1) is wrong.Abuse of notation can be used effectively to produce correct results, if communications, or reasoning, take place between two parties that are well informed and conscious of the limitations of the notationally abused language. What is gained, many times, is a more compact way of expressing ideas well known to both parties.For instance, it can be economical to write and think 1/0 = infinity, or, lim (1/x) as x->0 = infinity, even though, strictly, both of these 'equation-like' arrays of symbols have no meaning.If both parties are well trained in the definition and properties of limits, the shorthand notation can be used to perform calculations correctly, saving a great deal of paper and time needed to write formally correct statements regarding the (non-existent) limit of 1/x as x approaches 0.The danger here, is uninformed third-parties reading those and due to lack of training, drawing false conclusions.
  >
  > Even understanding it all, it is not uncommon, from time to time, for one to come back to those false implications/proofs using sqrt(-1) and scratch one's head, while going 'damn... I know this is false, but, why, again?'
  > Notational intuition is a powerful force within your mathematical brain. (And it shows in the history of mathematics, in episodes where bouts of prolific development in theory come right after some better notation gets introduced.)
  > You might wanna memorize a formalist mantra designed to safeguard you against this particular situation:
  > 'Sqrt(-1) is not a specific number. It cannot be hurled around inside equations just like x.'
  > Repeat ad nauseam until all thought is drowned. :p
  > Put this formalist mantra in your personal mantra library along with
  > 'Thou shalt not divide by zero.'
  > and also,
  > 'The square root of a^2 is modulus of a, and \*not\* just a.'
  > (which helps you avoid the common and tempting mistake of assuming that a^2 = b^2 implies that a = b )
  > Cheers,
  > Fabricio
- **Ignis** _5 Nov 2023 3:25 am_:
  X≠Y, but 0=0 so X=Y 🤪

<!-- wp-comments-end -->
