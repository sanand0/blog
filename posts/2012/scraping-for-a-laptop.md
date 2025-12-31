---
title: Scraping for a laptop
date: "2012-01-14T04:00:51Z"
lastmod: "2019-08-12T06:50:21Z"
categories:
  - how-i-do-things
wp_id: 2708
---

I've returned my [laptop](/blog/software-for-my-new-laptop-2/), and it's time to buy a new one. For the first time in my life, I'm buying a laptop for myself.

I have a fairly clear idea of what I want: a [500GB+ 7200 rpm](http://dalvenjah.foxfire.net/2010/01/5400rpm-vs-7200rpm-hard-disks-should-you-care/) hard disk with 4GB of RAM and an [Intel Core i7](http://en.wikipedia.org/wiki/Intel_Core#Core_i7_2). I thought that would make finding one of those [powerful laptops for producing music](https://musiccritic.com/equipment/studio/best-laptops-music-production/) since I record some stuff too out of hobby.

Sheer naïveté. Not a single site let me filter by hard disk rpm in India. (To be fair, I haven't found any sites outside India that did that either.)

After spending a good two hours hunting for the details and collating it, I did what I normally would: spend 30 minutes [writing a scraper](https://scraperwiki.com/scrapers/flipkart_laptops/). The scraper runs through all laptops on [Flipkart](http://www.flipkart.com/) and pulls out all of their specs. Thanks to the diligence of the good folks at Flipkart, this information is readily available on each page. The HTML is structured quite neatly too, so it was just a 30-line program to scrape it all. Full credit to [ScraperWiki](http://scraperwiki.com/) as well — I could use it on a netbook without any developer tools installed.

The scraper took 2 hours to run. Feel free to filter through the [output](https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=csv&name=flipkart_laptops&query=select+*+from+`swdata`&apikey=) (CSV) for your favourite laptop, or fork the code and pull any other data you like.

---

## Comments

<!-- wp-comments-start -->

- **ravi atluri** _14 Jan 2012 4:19 am_:
  If weight is not a limitation...i would recommend XPS15 or XPS15z
  i prefer it because of the i7 and >8GB RAM. gives me flexibility to run linux on VMs and 8 cores and 8GB RAM gives a lot of VMs :P
  if you are looking for portability. mac book pro :D it best fits for coding too
- **Subodh M** _24 Jan 2012 1:05 pm_:
  Anand, hv u explored Thinkpad T410i? I am using one with with an i5 processor with4GB RAM, 500GB HDD, @ 7200 rpm and am happy with it.
- **[S Anand](http://www.s-anand.net/)** _14 Jan 2012 10:29 am_:
  Battery life is the other consideration, and may be more important than performance. I am edging towards the Sony Vaio S VPCSA35GG. Despite the terrible name, it seems to have a decent performance battery-life trade off.
- **Indira** _14 Jan 2012 5:40 pm_:
  dell xps 14/15z comes with a good battery life. dell claims 7 hours, but i would think that would be with a slightly less than optimal settings of screen brightness, it would at least give you 4 hours, which is reasonable. Between sony and dell, my choice would be dell
- **[S Anand](http://www.s-anand.net/)** _14 Jan 2012 5:59 pm_:
  @Indira: thanks! Have added Dell XPS to my list. Also considering an Thinkpad E520 (i5, 4GB, 750GB) that seems very reasonably priced by a local vendor. I'll try and avoid Sony.
- **[Yuvi](http://yuvi.in)** _14 Jan 2012 6:47 pm_:
  SSD!
- **Somnath** _14 Jan 2012 7:31 pm_:
  If you are planning to buy from flipkart you may like to contact Ravi Vohra. He is a big shot at flipkart :D
- **[S Anand](http://www.s-anand.net/)** _16 Jan 2012 1:25 pm_:
  @pavan: agreed. I already have an external SSD though, so I just need a USB 3.0 port to take advantage of it. Can live with a more cost effective laptop :-)
- **pavan** _16 Jan 2012 6:38 am_:
  Anand, try to get a laptop with SSD, or upgrade later.
  Even the cheapest SSDs are 10 times faster than HDDs.
  Low noise and better battery life are nice to have side effects of SSD.
- **S.C** _8 Aug 2012 3:20 pm_:
  I had gone to a HP authorized service center, since browsers other than IE wouldn't work on my 3+ yr. old HP Pavilion Multimedia laptop. The person in charge of this center said that my laptop had probably been infected with a virus and advised me to install Norton AV. He also offered to 'upgrade' the OS in it from the licensed version of Windows Vista to Windows 7.
  When I started working on the laptop at home, I found messages that the OS was an unlicensed one. A few days later, I found that the laptop was not booting in the first attempt. Even when it booted, I got 'blue screen' errors before booting and horizontal and vertical lines on the screen which sometimes intersected.
  On taking the laptop back to the service center, I was told that the NVIDIA graphics card on the laptop's motherboard had malfunctioned. I want to ask users through this forum, whether this could have happened because of the extra load imposed on the 3+ yr. old graphics card by Windows 7? Since the personnel at the center now claimed that they could repair the graphics card for Rs. 1500, I gave them the laptop. But, when I collected it back after a week, I found no change in the laptop. So, I took it to the main HP service center in my city (where laptops covered by warranty are repaired).
  The personnel at this center said that they would have to replace the mother-board, since they didn't do chip level repairing. So, in order to get a graphics card repaired, I would have to shell out Rs. 22K for a new mother-board. Though I accepted this, HP hit me on the head with their next condition, when they said that they could repair the laptop, only if I surrendered the existing mother-board (in the malfunctioning laptop) to them, free of cost. This was in spite of the fact, that they had not mentioned this when taking the laptop from me for repair. Since, I couldn't have taken the earlier HP service center personnel to court for cheating me out of Rs. 1500 (in the name of repairing the graphics card), I refused and had to come back from the service center without getting the laptop repaired, in spite of pleading with HP to repair the mother-board for a month. They not only refused repeatedly, saying that this was their policy world wide and they couldn't change it just for me, but added insult to injury, by charging me Rs. 300 for inspecting the laptop.
  The reason I am mentioning this incident here, is because I feel this is malafide on the part of HP. Since I pay for a laptop when I buy it, the motherboard in it becomes my property then and there. If it malfunctions, why should I have to surrender it, to get it replaced and that also free of cost? I can choose to do whatever I want with it, which in this case, will definitely be to take HP to court for deficiency of service and causing mental agony, which wouldn't have been possible if I had surrendered the defective mother-board.
  I have heard that DELL is also taking customers for a ride in a similar way. Have any of you faced this?
- **[S Anand](http://www.s-anand.net/)** _16 Jan 2012 1:27 pm_:
  @Ravi, will reach out and take advice on how to get those discounts!
- **Deepak** _15 Jan 2012 4:17 am_:
  Aww, that is awesome. Can you include the price as well? :)
- **[Sri](http://www.ikway.blogspot.com)** _15 Jan 2012 9:26 am_:
  Try to check the prices at Dell Web Site directly and speak to the sales guy as well, they may give you a better price. Also it is better to have a look at Croma where you get a chance to touch and feel the different products and you will get an idea of price.
- **[Thejesh GN](http://thejeshgn.com)** _15 Jan 2012 1:53 pm_:
  I use Hp Probook 6460b which actually matches all your requirements. Unfortunately Flipkart has i5 one :(
- **[S Anand](http://www.s-anand.net/)** _15 Jan 2012 3:08 pm_:
  Thanks Sri, that's a great idea. Will check Croma tomorrow.
- **[S Anand](http://www.s-anand.net/)** _15 Jan 2012 3:28 pm_:
  How are HP laptops, generally? I haven't heard anything one way or the other so far...
- **ravi atluri** _15 Jan 2012 6:20 pm_:
  my dell xps15 gives me around 4.5 hours ..that's a 9 cell battery and is pretty heavy :P XPS is more of a portable desktop than a portable one ;)
  I prefer Dell, because of their better service in India.
  and if you are buying Dell...there are tricks to get discounts ;) dont order online directly :D
- **[How to Scrap Web Pages using ScraperWiki? | Python, ScraperWiki, HasGeek, Jobs | Sanspace Blog](http://blog.sanspace.in/scraperwiki/)** _28 Sep 2012 8:04 pm_ _(pingback)_:
  [...] data from web pages in a programmable way. For example, Check out Anand’s post about how he scraped for a laptop on Flipkart. That’s how I came to know about ScraperWiki and recently I wrote some quick and [...]

<!-- wp-comments-end -->
