---
title: Not all distributions are normal
date: "2006-07-19T12:00:00Z"
categories:
  - business-realities
wp_id: 269
---

14 years ago, I was introduced to the process of normalising grades. Professors "fit" students' marks into a [normal distribution](http://en.wikipedia.org/wiki/Normal_distribution) and assign grades based on that. (I still don't know how they do it).

Since then, I've encountered normalising a lot. My performance at work is normalised. I normalise my song ratings and movie ratings. I've normalised all kinds of things at work: lead-time of delivery of fans, movements in savings account balances, calls to a call centre, demand for a resource... you name it.

(What I mean by normalising is, I find the mean and standard deviation, and assume that it's a normal distribution with that mean and standard deviation. For things under my control, like movie ratings, I revise the ratings to fit a normal distribution.)

In fact, I normalise everything I encounter by default.

A few years ago, I started feeling uncomfortable about this. I've now figured out why **normalising is bad -- at least when done blindly like I do**.

First, let's explore why normalising is good. **Normalising eliminates biases.** If the Prof in Section A grades higher than the Prof in Section B, normalising takes care of it. If a Prof is extremist (more A's as well as F's), normalising takes care of it. If a Prof is skewed (lots below average, few extremely high above average), normalising takes care of it.

Eliminating biases makes sense if Section A is fundamentally like Section B. It's not better, nor more extremist, nor more skewed. If the sections are large enough and picked randomly, this assumption is correct. If Section A represents the smarter half, or people born in the second half of the year, or people from the Western states, or any other non-random selection, this need not be correct.

> An aside: You may wonder why people born in the second half of the year is non-random. If school admissions start in September, and admissions start when you're 3 years old, kids born in September will be nearly 4 years old when they join. Kids born in August will be between just over 3 years. That one-year difference, to a three-year old, is HUGE. For example, you will find a [birth date bias in football](http://www.11v11.co.uk/news/archives/152-Birth-Date-Bias-in-Football-An-AFS-Special-Survey.html), with most premiership players being born in the months of September - November.

Normalising goes a step further than eliminating bias, however. **Normalising forces a **normal** distribution**. This would be right if the underlying data is normally distributed. But if not, we may be making a mistake by force-fitting.

The [Central Limit Theorem](http://www.statisticalengineering.com/central_limit_theorem.htm) says that if you add up random variables, you get a normal distribution. **Provided it's a large sample, variables are independent, and each has a finite standard deviation**.

This means that **many things you get by adding random variables are normally distributed**. For example:

- Number of heads when you toss a coin (add up each coin toss)
- Average age of an army platoon (add up each soldier's age)
- Terminus-to-terminus time for a bus (add up the time between each stop)
- Price movement of an stock exchange index (add up each stock's price movement)

But a lot of **real-life data is NOT normally distributed**. The usual reasons are:

1. It's not the sum of random variables
2. It doesn't satisfy the central limit theorem (independence, large sample, finite standard deviations)

Here are some non-normal distributions that are NOT the sum of random variables:

- **Soldier's age within an army platoon**. What random variables could you add up? You'll probably find a lot of people at age 18, because that's the minimum age. A little fewer at age 19 -- last year's recruits. Far less at age 20 -- 2 years minimum service accomplished. Certainly not a normal distribution.
- **Price movement of a single stock**. What random variables could you add up? You'll find that there are far larger price movements than a normal distribution predicts.

Here are some non-normal distributions that don't satisfy the central limit theorem. (These are, in fact, things I said were normally distributed earlier. You see? It's easy to think things are normal, but in reality they're not.)

- **The terminus-to-terminus time for a bus**. The number of bus stops is quite small. More importantly, the time between stops isn't independent. If there's a traffic jam, an entire section of the route will take more time. If there's a delay between point 2 to 3, it's likely that there'll be a delay between points 1-2 and 3-4 as well.
- **The price movement of a stock exchange index**. The price movement of stocks follows a power-law distribution, which does not have finite standard deviations. Also, the price movements are not independent.
- See more [non-normal distributions](http://www.qualityamerica.com/knowledgecente/articles/PYZDEKnonnormal.html).

Summary: **Don't assume that anything you see is a normal distribution**. It usually isn't.

I'll shortly talk about what happens when you assume something's a normal distribution, when it really is not.

---

## Comments

<!-- wp-comments-start -->

- **[Wil](http://demesos.blogspot.com/)** _18 Nov 2010 9:14 pm_:
  Great article - you brought it to the point!

<!-- wp-comments-end -->
