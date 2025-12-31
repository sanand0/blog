---
title: Colour spaces
date: "2012-08-27T14:04:23Z"
categories:
  - coding
  - visualisation
wp_id: 2785
---

In reality, a colour is a combination of light waves with frequencies between 400-700THz, just like sound is a combination of sound waves with frequencies from 20-20000Hz. Just like mixing various pure notes produces a new sound, mixing various pure colours (like from a rainbow) produces new colours (like white, which isn’t on the rainbow.)

Our eyes aren’t like our ears, though. They have 3 sensors that are triggered differently by different frequencies. The sensors roughly peak around red, green and blue. Roughly.

![](http://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Cones_SMJ2_E.svg/300px-Cones_SMJ2_E.svg.png)

It turns out that it’s possible to recreate **most** (not all) colours using a combination of just red, green and blue by mimicking these three sensors to the right level. That’s why TVs and monitors have red, blue and green cells, and we represent colours using [hex triplets](http://en.wikipedia.org/wiki/Web_colors#Hex_triplet) for RRGGBB – like #00ff00 (green).

There are a number of problems with this from a computational perspective. Conceptually, we think of (R, G, B) as a 3-dimensional cube. That’d mean that 100% red is about as bright as 100% green or blue. Unfortunately, green is a lot brighter than red, which is a lot brighter than blue. Our 3 sensors are not equally sensitive.

You’d also think that a colour that’s numerically mid-way between 2 colours should **appear** to be mid-way. Far from it.

This means that if you’re picking colours using the RGB model, you’re using something very far from the intuitive human way of perceiving colours.

Which is all very nice, but I’m usually in a rush. So what do I do?

1. I go to the Microsoft Office [colour themes](http://office.microsoft.com/en-us/infopath-help/apply-a-color-scheme-HP001230316.aspx?CTT=1) and use a colour picker to pick one. (I [extracted them](https://github.com/sanand0/less/blob/master/color_themes.less) to make life easier.) These are generally good on the eye.
2. Failing that, I pick something from <http://kuler.adobe.com/>
3. Or I go to <http://colorbrewer2.org/> and pick a set of colours
4. If I absolutely have to do things programmatically, I use the [HCL](http://tristen.ca/hcl-picker/) [colour scheme](http://vis4.net/blog/posts/avoid-equidistant-hsv-colors/). The good part is it’s perceptually uniform. The bad part is: not every interpolation is a valid colour.

---

## Comments

<!-- wp-comments-start -->

- **[isomorphismes](http://isomorphismes.tumblr.com)** _13 Mar 2013 5:20 pm_:
  What colours can't be created by convex combinations of {R, G, B}? I mean within the visible spectrum.

<!-- wp-comments-end -->
