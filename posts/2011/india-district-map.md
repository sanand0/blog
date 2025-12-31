---
title: India district map
date: "2011-07-21T16:50:33Z"
lastmod: "2011-07-21T16:53:14Z"
categories:
  - data
  - visualisation
wp_id: 2681
---

I put together a [district map of India in SVG](https://bitbucket.org/sanand0/districts/src/tip/districts.svg) this weekend.

### So what?

You can now plot data available at a district level on a map, like the temperature in India over the last century (via [IndiaWaterPortal](http://www.indiawaterportal.org/met_data/)). The rows are years (1901, 1911, … 2001) and the columns are months (Jan, Feb, … Dec). Red is hot, green is cold.

[![temperature](/blog/assets/temperature.webp "temperature")](/blog/assets/temperature.webp)

(Yeah, the west coast is a great place to live in, but I probably need to look into the rainfall.)

[districts.svg](https://bitbucket.org/sanand0/districts/src/tip/districts.svg) has has 640 districts (I’ve no idea what [the 641st](http://en.wikipedia.org/wiki/Chhatrapati_Shahuji_Maharaj_Nagar_district) looks like) and is tagged with the State and District names as titles:

```xml
<g title="Madhya Pradesh">
  <path title="Alirajpur" d="..." />
  <path title="Jhabua" d="..." />
  ...
</g>
```

### How?

I made it from the [2011 census](http://www.censusindia.gov.in/2011census/maps/maps2011.html) [map](http://www.censusindia.gov.in/2011census/maps/administrative_maps/INDIA2011.pdf) (0.4MB PDF). I opened it in [Inkscape](http://inkscape.org/), removed the labels, added a layer for the districts, and used the [paint bucket](http://wiki.inkscape.org/wiki/index.php/ReleaseNotes046#Paint_Bucket_tool) to fill each district’s area. I then saved the districts layer, cleaning it up a big. Then I labelled each district with a title. (Seemed like the easiest way to get this done.)

Thanks to [@planemad](https://twitter.com/planemad), [@gkjohn](https://twitter.com/gkjohn), [@arjunram](https://twitter.com/arjunram) for inputs. Play around. Feedback welcome.

---

## Comments

<!-- wp-comments-start -->

- **[Thejesh GN](http://thejeshgn.com)** _22 Jul 2011 9:27 am_:
  Thanks for the map. Very useful.
  Btw you can cname map your bitbucket account. Its free.
- **[S Anand](http://www.s-anand.net/)** _23 Jul 2011 9:39 am_:
  @Thej -- AHA! Didn't know about the CNAMEing bitbucket. Thanks.
- **Rishi** _23 Jul 2011 9:15 am_:
  Wonderful stuff Anand!!!
  I would say - upload this on Wikipedia - but then we would have several flamewars with our dear neighbours on the borders shown.
- **[Arulalan.T](http://tuxcoder.wordpress.com)** _29 Dec 2011 10:17 am_:
  Thanks a lot for the India District Map in pdf and svg. From this post I got few ideas to generate shape (shp) files. I edited the India map in CDAT [1] shape files by generate the lat,lon points by hand itself [2]. I want to develop the India district shape file by automatic.
  Your project and code lights in my way.
  Thanks a lot.
  [1] http://www2-pcmdi.llnl.gov/cdat
  [2] http://tuxworld.wordpress.com/2010/02/13/how-to-edit-world-map-in-cdat-documentation/
- **Dibyo** _11 Aug 2011 4:29 am_:
  Awesome - I've struggled with this for a while now.
- **Minh** _12 Dec 2012 8:11 pm_:
  Thanks a lot. Do you have the shapefiles for your svg data? I could not find the new district level (2011 census) anywhere? Can you share with me?
  Many thanks.
- **mahir** _19 Dec 2012 6:11 am_:
  Dear Anand,
  Great work. I have made a tool to translate these location names using wikipedia's toolserver. people can translate these svg maps from http://toolserver.org/~mahir/
  I have successfully translated India political map from english to tamil for tamil wikipedia.
  http://ta.wikipedia.org/wiki/படிமம்:Ta\_India\_National\_Highway\_17.png
  Please try once.
  thanks
- **Arijit Upadhyay** _26 Dec 2013 3:37 am_:
  Some district names have changed since you posted this. Do you have an update for this map. Or how to edit them. Linkscape destroys the XML tags.
- **Prakash** _18 Jan 2014 10:43 am_:
  Dear Friend would it be possible to get shp and dbf file of indian state with undivided bihar, up and mp.

<!-- wp-comments-end -->
