---
title: Normalising non-normal distributions is bad
date: "2006-07-19T12:00:00Z"
lastmod: "2019-12-01T14:27:00Z"
categories:
  - business-realities
wp_id: 271
---

I was working with the treasury of a bank. They were trying to estimate how much money could flow out of their savings account in a day, worst case.

I took their total savings account balance at the end of each day and found the standard deviation. I took thrice the standard deviation, and said, "You can be 99.7% sure that your daily loss won't be more than 1.5% of the balance."

That would be right if it were a normal distribution. But it's not.

Banks have millions of savings accounts, each of which is like a random variable. But unless they're independent, and they have finite standard deviations, the central limit theorem won't work.

Firstly, **savings account transactions are not independent**. If there's a run on the bank, they'd all pull out their money. Whenever a company declares dividend, a large number of savings account are credited. Salary accounts are credited at the end of the month. As a rule of thumb, you could say that if one savings account goes up, the others are likely to as well.

Secondly, **savings account transactions are not normally distributed**. If you take a single savings account, you won't find a bunch of debits and credits. Every month, you'll find one large credit for the salary, one mid-sized debit for monthly expenses, and several small debits for individual transactions (bills, ATM, etc.) Once in several years, you'll find a gigantic debit (purchase of car or house, wedding, etc.) or a gigantic credit (retirement / pension fund, sale of property, etc.)

As a result, the **savings account is likely to fluctuate a LOT more than if it were a normal distribution**.

If I had just looked at the data, I'd have found several occurrences of fluctuations greater than 1.5%. The normal distribution predicts that there should be fewer than 0.3% of such cases. That's about 1 per year. I'd have visually been able to spot nearly one a month. I'd also have been able to spot the huge 4% swings that do happen once in a few years.

People wiser than me have made the same mistake. I was interning at Lehman Brothers when they were planning to launch a new electronic bond-trading product. My task was to trace the bond price movement.

The data we had was bad. Many bonds jumped as much as 40% in a single day, due to data errors. The bulk of my task was to clean out these errors.

After cleaning up, there was still two jumps that couldn't be explained. I went to my boss, who recognised them at sight. One was a sudden drop in price of all Government bonds in December 1998. The other was a 32% drop in price of Hikari Tsushin -- a mobile phone retailer -- on the day they went bankrupt.

We concluded that the daily price drop wouldn't be more than 9%, to a 95% confidence level. If that was right, a 32% drop in one day would happen once in a **million years**. Yet, we had Hikari Tsushin just the previous year.

We didn't bother about it. In fact, we didn't even think about it. If we'd checked, we'd have found that the daily price drop was closer to 12% or something, to a 95% confidence level.

Summary: **Force-fit a normal distribution on non-normal data can understate the worst-case scenario**. Often you're better off just inferring confidence levels from the raw data than from a fitted distribution.

Sourced statistic from: [www.forex.academy](https://www.forex.academy)

---

## Comments

<!-- wp-comments-start -->

- **Sriram** _24 Jul 2006 7:53 am_:
  what you are talking about are outliers which would be there in even the most normal of the normal distributions. One always has to take them out. This is not an "un-normal" phenomenon.
- **S Anand** _24 Jul 2006 11:20 am_:
  No, I'm not. The normal distribution asserts that the probability distribution falls of exponentially. These transactions are power-law distributed. The distribution falls off as a power law. Specifically, this means that the normal distribution has a finite standard deviation. Power law distributions have an infinite standard deviation. You can check this from the wikipedia articles on power law distributions.
- **RaviM** _3 Aug 2006 7:09 am_:
  When I was doing Risk Management for a mutual fund, we were facing the same problems. So we used to take two approaches to calculate VaR for various products- Assuming Normal distribution of stock price changes(the problem here is that you are not sure what is the current Std dev of any Stock... which can change drastically on a single day in case of events. I still remember Mastek which dropped 50% on a single day). We also used to take historical data to figure out what are the past occurances when such events has happened. but here the disadvantage is that we assume that stock price movements are historically dependent, which is also not correct
- **Naresh** _21 Sep 2010 8:45 pm_:
  Complex problems have simple, easy to understand wrong answers.
  The world does not run on a normal distribution. If we could predict the future behaviour (even heavily populated datasets) using a normal distribution, the world would be a different place, wouldn't it?
  The answer to this problem is to use a time weighted average of data with the latest data having the highest weight, or using the exponentially weighted moving average formula developed by Riskmetrics. Use a lambda of .94 for daily observations. You can alternatively use an empirical lambda. Use it to predict earthquakes (?), junior miners, venture investments, come what may. And then you will find that too is inadequate as a risk tool.
- **[The Curse of the Bell Curve &#8211; Part 2 | Jigsaw Academy | Training for careers in Analytics](http://analyticstraining.com/2013/the-curse-of-the-bell-curve-part-2/)** _16 Jan 2013 8:55 am_ _(pingback)_:
  [...] in Checking/Saving account – This is an interesting article written by a friend during his consulting days. He illustrates how we tend to blindly apply the [...]

<!-- wp-comments-end -->
