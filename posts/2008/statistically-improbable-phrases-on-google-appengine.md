---
title: Statistically improbable phrases on Google AppEngine
date: "2008-04-08T12:00:00Z"
lastmod: "2009-03-23T15:33:29Z"
categories:
  - coding
  - tools
wp_id: 54
---

I [read](http://googleappengine.blogspot.com/2008/04/introducing-google-app-engine-our-new.html) about [Google AppEngine](http://appengine.google.com/) early this morning, and applied for an invite. Google's issuing beta invites to the first 10,000 users. I was pretty convinced I wasn't among those, but turns out I was lucky.

AppEngine lets you write web apps that Google hosts. People have been highlighting that it give you access to the [Google File System](http://en.wikipedia.org/wiki/Google_file_system) and [BigTable](http://en.wikipedia.org/wiki/Bigtable) for the first time. But to me, that isn't a big deal. (I'm not too worried about reliability, and MySQL / flat files work perfectly well for me as a data store.)

What's more interesting unlike Amazon's EC2 and S3, this is free up to a certain quota. And you get a fair bit of processing power and bandwidth for free. One of the reasons I've held back on creating some apps was simply because it would take away too much bandwidth / CPU cycles from my site. (I've [had this problem before](/Reducing_the_server_load.html).) Google [quota](http://code.google.com/appengine/articles/quotas.html) is 10 GB of bandwidth per day (which is about 30 times what my site uses). And this is on Google's [incredibly](/Why_Google_Reader.html) [fast](/GMail_is_fast.html) servers It also offers 200 million megacycles a day. That's like a dedicated 2.3 GHz processor (200 million megacycles = 200,000 GHz x 1 second ~ 2.3 GHz x 86,400 seconds/day) -- better, because this is the average capacity, not peak capacity. The only restriction that really worries me is that only 3 apps are allowed per developer.

So I decided to give a shot at publishing some code I'd kept in reserve for a long time. You may remember my [statistical analysis of Calvin & Hobbes](/Statistically_improbable_phrases.html). For this, I'd created a script in Perl that could generate Statistically Improbable Phrases (SIPs) for any text. This is based on (a somewhat limited) 23MB corpus of ebooks that I had. I'd wanted to put that up on my website, but ...

AppEngine only uses Python. So the first task was to [get Python](http://www.activestate.com/Products/activepython/), and then to [learn Python](http://www.diveintopython.org). The only saving grace was that I was just cutting-and-pasting most of the time. Google wasn't helping:

[![Google AppEngine Over Quota Error](/blog/assets/flickr-google-appengine-over-quota-error_2398327713_o-png.webp)](/blog/assets/flickr-google-appengine-over-quota-error_2398327713_o-png.webp "Google AppEngine Over Quota Error")

Anyway, the site is up. You can view it at **[sip.s-anand.net](http://sip.s-anand.net/)** for now. Just type a URL, and it'll tell you the improbable words in that site.

[Visit sip.s-anand.net](http://sip.s-anand.net/)

**Technical notes**

I realise that these are statistically improbable **words**, not **phrases**. I'll get to the phrases in a while.

The logic is simple:

- **Get the frequency of words in a corpus**. I pre-generated this file. It has over 100,000 words.
- **Get the URL as text**. Rather than muck around with Python, I decided to use the [W3 html2txt](http://cgi.w3.org/cgi-bin/html2txt) service.
- **Convert the text to words**. [Splitting text into words is tricky](/Splitting_a_sentence_into_words.html). For now, I'm simply assuming that any group of letters is a word, and anything that's not a letter is a word delimiter.
- **Find the relative frequency (improbability) of words**. This is the frequency in the URL divided by the frequency in the corpus, normalised (i.e. scale it so that the maximum value is 1.0).
- **Create a tag cloud**. I use the word frequency as the size and the improbability as the colour. You need a bit of mathematical jugglery to get the pattern right. Right now, I'm taking the 6th root of the improbability and the logarithm of the frequency to get a reasonably smooth tag cloud.

The source code is at [statistically-improbable-phrases.googlecode.com](http://statistically-improbable-phrases.googlecode.com/).

**Update**: 12-Apr-2008. I've added some interactivity. You can play with the contrast and font size, the filter out common or infrequent words.

**Update**: 22-Apr-2008. Added concordance. You can click on a word and see the context in which it appears.

---

## Comments

<!-- wp-comments-start -->

- **Sasidhar** _8 Apr 2008 12:00 pm_:
  Interesting. Great to see you've already developed an App. :) I was trying it out, and looks like something broke. Here's the error. Traceback (most recent call last): File "/base/python\_lib/versions/1/google/appengine/ext/webapp/\_\_init\_\_.py", line 486, in \_\_call\_\_ handler.post(\*groups) File "/base/data/home/apps/sip/1.35/sip.py", line 64, in post result = urlfetch.fetch("http://cgi.w3.org/cgi-bin/html2txt?noinlinerefs=on&nonums=on&url=" + urllib.quote(url)) File "/base/python\_lib/versions/1/google/appengine/api/urlfetch.py", line 95, in fetch raise DownloadError() DownloadError
- **Glenn** _8 Apr 2008 12:00 pm_:
  This is a great app and uses some techniques I wanted to learn more about. The source code seems out of date with the currently running app. Any chance you can update the source .zip file as well? Thanks in advance.
- **Brandon** _8 Jun 2011 10:40 pm_:
  The app is really, really neat. Is there any chance there will be a version that can do the same for Word files?

<!-- wp-comments-end -->
