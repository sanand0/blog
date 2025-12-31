---
title: Visualising the Wilson score for ratings
date: "2010-11-24T10:48:13Z"
categories:
  - visualisation
wp_id: 2559
---

[Reddit](http://www.reddit.com/)’s [new comment sorting system](http://blog.reddit.com/2009/10/reddits-new-comment-sorting-system.html) (charmingly explained by [Randall Munroe](http://www.xkcd.com/)) uses what’s called a [Wilson score confidence interval](http://www.evanmiller.org/how-not-to-sort-by-average-rating.html).

I’ll wait here while you read those articles. If you ever want to implement user-ratings, you need to read them.

The summary is: don’t use average rating. Use something else, which in this case, is the Wilson score, which says that if you got 3 negative ratings and no positive ratings, your average rating shouldn’t be zero. Rather, you can be 95% sure that it’ll end up at 0.47 or above, given a chance, so rate it as 0.47.

I understand this stuff better visually, so I tried to see what the rating would be for various positive and negative scores. Here’s the plot.

![3D animation of Wilson score for ratings](https://files.s-anand.net/images/2010-11-24-3d-wilson.webp)

The axes on the floor show the number of positive and negative ratings (you can figure out which is which), and the height of the surface is the average rating it should get.

You can see that if there are only positive ratings, the average rating is 100% (because there’s a 95% chance it’ll end up at 100% or above). If there are only negative ratings, the rating falls of sharply. In the early stages, a few positive ratings can correct that very quickly, but over time, the correction’s a lot weaker.

You can move your mouse over the visualisation to control the angle. (For those reading this this via the RSS feed, you may need to visit [my blog](http://www.s-anand.net/).) Try it out: I understood the behaviour a lot better this way.

---

## Comments

<!-- wp-comments-start -->

- **[Safe Hammad](http://safehammad.com)** _8 Dec 2010 5:49 pm_:
  Very interesting! Great visualisation.
  Although using the Wilson score confidence interval is "more correct" than simpler alternatives, I can't help feel that web sites need absolute transparency as much as correctness when it comes to how their rating system works. I wonder what would happen if Amazon or Urban Dictionary had to point visitors to Wilson's formula to help them understand how their ratings system worked! There may be a case for the trade-off between simplicity and correctness.
  Thankfully many sites, including both Amazon and Urban Dictionary, also publish the raw data i.e. a breakdown of ratings allowing visitors to draw their own conclusions ... should they choose to do so.
- **[Dan Murray](http://www.thedatarevolution.com)** _22 Dec 2010 6:22 pm_:
  I don't like the 3D representation. It obscures the meaning.

<!-- wp-comments-end -->
