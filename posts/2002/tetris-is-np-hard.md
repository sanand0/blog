---
title: Tetris is NP-Hard
date: "2002-10-26T12:00:00Z"
categories:
  - links
wp_id: 1071
---

[Tetris is NP-Hard](http://slashdot.org/article.pl?sid=02/10/24/2251234&mode=thread&tid=127). Let me explain, in English, what that means.

**The toughness of problems is how much time it takes to solve them.**

Adding two 3-digit number takes less time than adding two 30-digit numbers, and hence is easier. Similarly, figuring out if a 3-digit number is prime or not is easier than a 30-digit number.

**Some problems grow tough very quickly.**

Adding two 30-digit numbers is 10-times slower than adding two 3-digit numbers. But checking if a 30-digit number is prime is **several trillions** of times slower than checking a 3-digit number. That is because, to check if a number is prime, you need to repeatedly divide it by numbers smaller than it. For a 3-digit number, you need to divide by around 1,000 numbers. For a 30 digit number, it's several trillions.

**Problems that grow tough at a constant rate are 'P'.**

What this means is: if you keep on doubling the number of digits, the problem repeatedly becomes twice as tough (or 3 times as tough, or whatever -- some constant rate). Adding of numbers is an example. ('P' stands for polynomial time.)

**Problems that grow tough at a constant rate **if you already know how to solve them** are 'NP'.**

For instance, to check if a 30-digit number is a prime, you needn't check with **all numbers** below the number. You just need to check with **all primes** below the number. That takes about 10-times as much time as for a 3-digit number. Hence, if you knew which primes were below the number, it would be 'P'.

**'P' is a subset of 'NP'.**

The real question is, are there any problems that are 'NP' and not 'P'. That is, are there problems for which you **really** need to know how to solve the problem to be able to solve them in polynomial time? Or is it that we've just not been smart enough to come up with solutions that are fast enough? We don't know. The first step is to make a list of [NP problems that are not obviously in 'P'](http://www.nada.kth.se/~viggo/problemlist/compendium.html). Then, we try converting these problems into each other in polynomial time.

**NP problems that can be converted into each other in polynomial time are 'NP-hard'.**

So, if you solve any one of these 'NP-hard' problems in polynomial time, you can solve all NP-hard problems in polynomial time. Figuring out the right moves in Tetris is one such problem.
