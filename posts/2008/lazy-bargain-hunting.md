---
title: Lazy bargain hunting
date: "2008-01-04T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 61
---

I'm thinking of buying a [digital keyboard](http://images.google.com/images?q=digital+keyboard) with [touch sensitive keys and MIDI support](http://www.catherineduc.com/linkkeyboards.htm). (The one other thing that I thought off -- a [pitch bend](http://commons.wikimedia.org/wiki/Image:Pitch_Bend_Up.jpg) -- puts the keyboards out of my budget.)

I'd like a good deal. (Who doesn't?) But I don't like to spend time searching for one. (Who does?)

So here's the plan.

Firstly, I'll **restrict my search to [Amazon.co.uk](http://www.amazon.co.uk/)**. For electronics items, I haven't found anyone consistently cheaper. [Tesco](http://direct.tesco.com/) has some pretty low prices, but not the range. [eBuyer](http://www.ebuyer.com/) is pretty good, but not often enough. [Google Products](http://www.google.co.uk/products) is the only other one that gets me consistent lower prices, but I've had my credit card identity stolen once before while shopping online, so I'd rather not pick any random seller listed on Google.

**Amazon has a [secret discount](http://www.enjoydeals.com/amazon_uk.php)**. You can search for [electronics](http://www.amazon.co.uk/gp/search/?node=560798) items with [30% off or more](http://www.amazon.co.uk/gp/search/?node=560798&pct-off=30-&sort=salesrank). And then you can narrow it down to [Sound & Vision > Musical Instruments > MIDI Keyboards](http://www.amazon.co.uk/s/ref=sr_nr_n_4?ie=UTF8&rs=10305241&sort=salesrank&rh=n%3A560798%2Cp%5F8%3A30-%2Cn%3A560858%2Cn%3A10305241%2Cn%3A310201011). Further cap a [100 - 200 GBP](http://www.amazon.co.uk/s/ref=sr_nr_p_36_2?ie=UTF8&rs=310201011&sort=salesrank&rh=n%3A560798%2Cp%5F8%3A30-%2Cn%3A560858%2Cn%3A10305241%2Cn%3A310201011%2Cp%5F36%3A10000-20000) restriction. That leaves us with one product:

[![MIDI keyboard on Amazon](/blog/assets/flickr-midi-keyboard-on-amazon_2166283290_o-png.webp)](/blog/assets/flickr-midi-keyboard-on-amazon_2166283290_o-png.webp "MIDI keyboard on Amazon")

While that matches my criteria, I'm in no hurry and can wait for more offers to come up. But I don't want to keep checking this page every day. So, [**RSS to the rescue**](/Advanced_Google_Reader.html). You probably think I can't get enough of RSS feeds. And you'd be right. The thing is, as an attention mechanism, it is incredibly powerful, and I never cease to be amazed that the things it lets me do.

Using my [XPath checker](https://addons.mozilla.org/en-US/firefox/addon/1095) and a bit of trial and error, I figured all product links link to "amazon.co.uk/dp/..." with a `<span>` inside. So this XPath gets all the links:

```xpath
//a[contains(@href,'/dp/')][span]
```

And I made an RSS feed out of that using my [XPath server](/Scraping_RSS_feeds_using_XPath.html) and [subscribed to it on Google Reader](http://www.google.com/reader/shared/user/16836184467750910501/label/blog:%20keyboard%20rss%20feed).

Combining a bunch of such searches, I have a shopping folder on Google Reader has all the items I'm searching for. Now **that's** lazy bargain hunting.

---

Which is all very fine. But given that I'm buying a car in a hurry right now, and I'm not doing any bargain hunting, it's a classic case of being penny-wise and pound-foolish. Sigh...

---

## Comments

<!-- wp-comments-start -->

- **Oracle** _4 Jan 2008 12:00 pm_:
  Alternate way is to set-up a google alert for the specific item in the chosen sites. Do you see any disadvantages with that?
- **Rajesh** _11 Nov 2008 7:58 am_:
  Never had someone's personal website kept me so drawn in. You are smart and very articulate (u probably know this already) and it shows in each intersting and very often informative article you write. you can even try writing columns in magazines, websites or papers. i've learnt a lot from your site already and haven't finished reading them all. i also see you play the keyboard and maybe interested in midis. i've sequenced some midis. u can can find them at

  http://rajesh.annamalaisamy.googlepages.com/rajeshmidis

  if u're interested. The best tamil song midis in my opinion are done by kishmu. His midi works can be found at

  www.geocities.com/kishmu/

  Eagerly anticipating your next article.

  Regards

  Rajesh

<!-- wp-comments-end -->
