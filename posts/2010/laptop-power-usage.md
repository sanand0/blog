---
title: Laptop power usage
date: "2010-02-07T18:09:29Z"
lastmod: "2010-02-07T18:13:11Z"
categories:
  - how-i-do-things
wp_id: 2459
---

<p>I just got a <a href="http://en.wikipedia.org/wiki/Wattmeter#Digital">digital wattmeter</a>. Had no idea about these until <a href="http://en.wikipedia.org/wiki/Google_PowerMeter">Google PowerMeter</a>, but now, they’re all the rage. Mine’s a pretty <a href="http://www.maplin.co.uk/Module.aspx?ModuleNo=286534">simple model</a> and all&nbsp; I plan to do with it is play around with a few household gadgets.</p> <p><a href="/blog/assets/n67hhsmall.webp"><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="n67hh-small" border="0" alt="n67hh-small" src="/blog/assets/n67hhsmall.webp" width="240" height="166"></a> </p> <p>My first target, obviously, was my <a href="http://www.dell.com/us/en/enterprise/notebooks/laptop_latitude_e5400/pd.aspx?refid=laptop_latitude_e5400">Dell Latitude E5400</a>. The statistics are interesting:</p> <table class="lines" cellspacing="0" cellpadding="2"> <tbody> <tr> <th valign="top" width="63">Power</th> <th valign="top" width="537">… when…</th></tr> <tr> <td valign="top" width="63">0.3W</td> <td valign="top" width="537">Laptop is switched off. The adapter must be consuming the power</td></tr> <tr> <td valign="top" width="63">1.3W</td> <td valign="top" width="537">Laptop is on standby.</td></tr> <tr> <td valign="top" width="63">12W</td> <td valign="top" width="537">The lid is closed, and no applications are running.</td></tr> <tr> <td valign="top" width="63">18.5W</td> <td valign="top" width="537">The laptop is on, the lid is open, and no applications are running</td></tr> <tr> <td valign="top" width="63">25W</td> <td valign="top" width="537">The laptop is writing to the hard disk</td></tr> <tr> <td valign="top" width="63">34W</td> <td valign="top" width="537">One CPU is fully utilised</td></tr> <tr> <td valign="top" width="63">41W</td> <td valign="top" width="537">Both CPUs are fully utilised</td></tr></tbody></table> <p>Looks like the display and hard disk each consume about 6.5 watts each, while the CPU consumes a whopping 15 + 7 = 22 watts.</p> <p>One interesting observation is that the colour of the display doesn’t make much of a difference. From my CRT monitor days, I’d remembered that a black screen consumes less power, and is less likely to wear the screen off. So my desktop background has always been black, and most of <a href="/hindi">my applications use a black theme</a>. But it turns out that on LCDs, it makes absolutely no difference. A full white screen uses the same power as a full black screen. So I’ve really been wasting my time the last 9 years. (There <em>is</em> a good reason to have a black screen, sometimes – it’s much easier on the eyes when reading without lights.)</p> <p>Another lesson was that turning off the wireless had no effect whatsoever. (It worked quite well for my <a href="/blog/my-new-blackberry-bold-9700/">Blackberry</a>, though. Increased the battery life quite a bit. I thought the same might apply for laptops, but looks like it doesn’t.)</p> <p>I’ll do an audit of some of my home appliances and post it out here. Wonder if there’s a repository of power usage for appliances…</p>

---

## Comments

<!-- wp-comments-start -->

- **[Dibyo](http://dibyo.blogspot.com)** _8 Feb 2010 3:15 am_:
  I have always run a laptop battery longer by putting the wireless off, the difference is immediate, so this is NEWS TO ME!
  This is how I figured it - point at battery icon (e.g. 50 mins left) - switch off wireless - point a min later (1 hour left). What was I doing wrong?
- **[JB](http://viewsofjb.wordpress.com)** _8 Feb 2010 5:25 am_:
  Informative. I should buy one as well as show this to my roomies, who leave their personal laptops lid-opened throughout the day and night while sleeping or away to office.
  Thanks.
- **Nikhith** _8 Feb 2010 5:44 am_:
  I have one doubt about the way u conducted these tests and deduced the results Mr. Anand. I'm sure u could use the power meter only to check the power usage when u connected the charger. But the power strain on the charger due to white background and wireless on, is much less significant as compared to the power strain on the batteries alone. So i guess there will considerable increase in the battery backup due to black background and wireless off. I'm just hypothesizing this, and this must answer u r question too Dibyo
- **[S Anand](http://www.s-anand.net/)** _10 Feb 2010 5:06 pm_:
  @Dibyo: just to be sure, I tried it again. Definitely no change in power consumption when the wireless is turned off. Not sure if the problem is with how Windows calculates the power consumption, or whether your laptop's wireless is different somehow...
- **[S Anand](http://www.s-anand.net/)** _10 Feb 2010 5:09 pm_:
  @Nikhith: If that were the case, changing the display's brightness shouldn't have affected much either. But for every notch that I darkened the display, the power consumption fell visibly by about 0.5W. So I suspect the actual usage of the laptop is directly transmitted to the mains, and the battery doesn't really do much of a buffering. (At least when it's charged, I guess. Mine was fully charged.)
  This means that the the wireless power consumption really is insignificant compared to CPU usage, brightness, or hard disk usage.
- **Amit** _22 Mar 2010 3:32 pm_:
  thanks Anand for sharing the experiment result.
  As per my understanding, with wireless switch on battery consumption is higher.
  many times my laptop's battery has dried very fast because by mistake I have left the wireless switch on.
  you can also validate this by just leaving machine for sometime on battery power with/without wireless switch on ( dont use the ac power).
- **Rajesh** _25 Mar 2010 11:13 am_:
  Where can I get this gadget in India?
- **[S Anand](http://www.s-anand.net/)** _25 Mar 2010 4:18 pm_:
  You know, I've been hunting all over Bangalore and Chennai for it. Yet to find one!
- **[Raj](http://tech-spirit.blogspot.com)** _24 Feb 2011 7:10 am_:
  Wonderful information. No one has given this much clarity on this topic. Keep going.
  Thanks
  R@J.

<!-- wp-comments-end -->
