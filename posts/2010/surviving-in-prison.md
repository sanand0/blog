---
title: Surviving in prison
date: "2010-11-12T16:25:37Z"
categories:
  - business-realities
  - how-i-do-things
wp_id: 2555
---

As promised, here are some tips from the trenches on surviving in prison. (For those who don’t follow my blog, [prison is where your Internet access is restricted](/blog/you-are-in-prison/).)

There are two things you need to know better: software and people. I’ll try and cover the software in this post, and the more important topic in the next.

**Portable apps**

You’re often not in control of your laptops / PCs. You don’t have administrator access. You can’t install software. The solution is to install [Portable Apps](http://www.portableapps.com/). Most popular applications have been converted into Portable Apps that you can install on to a USB stick. Just plug them into any machine and use them. I use Firefox and Skype quite extensively this way, but increasingly, I have a preference for Portable Apps for just about everything. It makes my bloated Start Menu a lot more manageable. Some of the other portable apps I have are: Audacity, Camstudio, GIMP, Inkscape and Notepad++.

**Admin access**

The other possibility is that you try and gain admin access. I did this once at a client site (a large bank). We didn’t have admin access. I wasn’t particularly thrilled. So I borrowed a floppy, installed an [offline password recovery tool](http://www.pogostick.net/~pnh/ntpasswd/), rebooted, and got the admin password within a few minutes. This is with the full knowledge of the (somewhat worried) client. This is where the people part comes in, and I’ll talk about that later.

**Proxies**

But before you do any of these, you need to be able to download the files, most of which are executables. Those are probably blocked. Heck, the sites from which you can download these files are probably blocked in the first place.

Sometimes, internal proxies help. Proxies for different geographies may have different degrees of freedom. When I was at IBM, the Internet was accessible from most US proxies, just not from the Indian proxy. So it may just be a matter of finding the right internal proxy.

Or you can search for [external public proxies](http://www.google.com/search?q=free+public+proxy). Sadly, many of these are blocked. Another option is for you to set up your own proxy. You can install [mirrorrr](http://code.google.com/p/mirrorrr/) on [AppEngine](http://appengine.google.com/) for free, for example.

The most effective option, of course, is to use [SSH tunnels](/blog/ssh-tunneling-through-web-filters/). I’ve covered this is some detail earlier.

**Google**

Google has a wide range of tools that can help access blocked sites. If the site you’re accessing provides public RSS feeds, use [Google Reader](http://reader.google.com/) to access these. Public feeds for Twitter, for example, are available as RSS feeds.

Google’s cache is another way of getting the same information. Search for the URL, click on the “Cache” link to read the text even if it’s blocked.

To find more such help, [Google for it](http://www.google.com/search?q=access+blocked+sites)!

**Peopleware**

… but all of this is, honestly, just a small part of it. The key, really, is to understand the people restricting your access. I’ll talk about this next.

---

## Comments

<!-- wp-comments-start -->

- **[Raghu](http://raghustwocents.blogspot.com)** _12 Nov 2010 7:53 pm_:
  Hello Anand,
  First off, superb blog. I've been reading your stuff for the past year or so and I really enjoy your content. I am able to relate to the most part about this post, previous prison posts etc., as I was in a similar situation some time ago. And, as my friend once said, being engineers, we will devote all time to try and work around potential temporary barriers - thus defeating the purpose of proxies and web filters in the first place.
  When you talk about booting via a floppy, you'd first need BIOS access to modify the boot order. That is usually blocked with a password -is there a workaround that?
- **Deepak** _13 Nov 2010 3:06 am_:
  Portable apps - USB is disabled!
  Admin access - I have it. Doesn't help much though! (This and the previous one seem to be mutually exclusive. USB is disabled by policy)
  Proxies - Not very helpful. Too many hoops to jump through!
  SSH Tunnels - This is the only one that has a way of working reliably. Is there a free reliable provider?
  Google - Reader works. But a lot of images are cropped off because of the same issues above. Somehow, even Google's cache seems to be falling under the parent url's restrictions.
- **[Fibinse](http://weedjoint.wordpress.com)** _9 Mar 2011 6:53 am_:
  I honestly thought that you were gonna write about prison! :)

<!-- wp-comments-end -->
