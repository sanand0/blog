---
title: Google Chrome screenshots
date: "2008-09-02T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 39
---

I went to the [Google Chrome](http://www.google.com/chrome) site.

[![](/blog/assets/flickr-google-chrome-1_2822929746_o-png.webp)](/blog/assets/flickr-google-chrome-1_2822929746_o-png.webp)

Clicking on the "Accept and Install" button...

[![](/blog/assets/flickr-google-chrome-2_2822094501_o-png.webp)](/blog/assets/flickr-google-chrome-2_2822094501_o-png.webp)

... automatically launched the downloader in Firefox...

[![](/blog/assets/flickr-google-chrome-3_2822930042_o-png.webp)](/blog/assets/flickr-google-chrome-3_2822930042_o-png.webp)

... and (after a fairly short while) started installing the application directly. This may be the most painless install I've done in a while.

[![](/blog/assets/flickr-google-chrome-4_2822094883_o-png.webp)](/blog/assets/flickr-google-chrome-4_2822094883_o-png.webp)

I clicked on "Customise the settings"

[![](/blog/assets/flickr-google-chrome-5_2822930598_o-png.webp)](/blog/assets/flickr-google-chrome-5_2822930598_o-png.webp)

This is what it looks like.

[![](/blog/assets/flickr-google-chrome-6_2822095325_o-png.webp)](/blog/assets/flickr-google-chrome-6_2822095325_o-png.webp)

And that's it! It installs, and launches in just a few seconds. First impressions: the startup and rendering are really fast.

[![](/blog/assets/flickr-google-chrome-7_2822095593_o-png.webp)](/blog/assets/flickr-google-chrome-7_2822095593_o-png.webp)

The address bar doubles up as a search bar. Very sensible.

[![](/blog/assets/flickr-google-chrome-8_2822931146_o-png.webp)](/blog/assets/flickr-google-chrome-8_2822931146_o-png.webp)

Several nice [features](http://tools.google.com/chrome/intl/en-GB/features.html): incognito mode, application shortcuts, and developer tools.

[![](/blog/assets/flickr-google-chrome-9_2822095935_o-png.webp)](/blog/assets/flickr-google-chrome-9_2822095935_o-png.webp)

The Javascript console has Javascript autocompletion! Watch out, Firebug.

[![](/blog/assets/flickr-google-chrome-10_2822096083_o-png.webp)](/blog/assets/flickr-google-chrome-10_2822096083_o-png.webp)

[![](/blog/assets/flickr-google-chrome-11_2822931444_o-png.webp)](/blog/assets/flickr-google-chrome-11_2822931444_o-png.webp)

[![](/blog/assets/flickr-google-chrome-12_2822096215_o-png.webp)](/blog/assets/flickr-google-chrome-12_2822096215_o-png.webp)

The "Use DNS pre-fetching" looks interesting. My browsing certainly seems faster. Might be faster than Opera, even.

[![](/blog/assets/flickr-google-chrome-13_2822096303_o-png.webp)](/blog/assets/flickr-google-chrome-13_2822096303_o-png.webp)

The "Show suggestions for navigation errors" feature.

[![](/blog/assets/flickr-google-chrome-14_2822931820_o-png.webp)](/blog/assets/flickr-google-chrome-14_2822931820_o-png.webp)

There's a task manager...

[![](/blog/assets/flickr-google-chrome-16_2822096869_o-png.webp)](/blog/assets/flickr-google-chrome-16_2822096869_o-png.webp)

... that shows how much memory each site uses.

[![](/blog/assets/flickr-google-chrome-17_2822096977_o-png.webp)](/blog/assets/flickr-google-chrome-17_2822096977_o-png.webp)

But not all is good. This jQuery animation on my site leaves trails behind.

[![](/blog/assets/flickr-google-chrome-15_2822096585_o-png.webp)](/blog/assets/flickr-google-chrome-15_2822096585_o-png.webp)

And the text box resizing is good, but feels a bit... wrong, somehow.

[![](/blog/assets/flickr-google-chrome-18_2822097085_o-png.webp)](/blog/assets/flickr-google-chrome-18_2822097085_o-png.webp)

Plus: I can re-import history, bookmarks, etc. from Firefox at any point, so I don't have to worry about using this as a secondary browser.

**Update (8am UK, 3rd Sep)**: Chrome.exe isn't installed in your "Program Files" folder. It's in your "Documents and Settings" folder, under "Local Settings\Application Data\Google\Chrome\Application". (That's on Windows XP. Not sure about Vista.)

There's a Themes folder, so I imagine more themes should be on their way.

There doesn't seem to be an about:config option. But there are a whole lot of others:

- about:cache
- about:dns
- about:histograms
- about:memory
- about:plugins
- about:stats
- about:version
- about:crash
- about:internets
- about:network
- about:blank
- about:shorthang
- about:hang
- about:objects

I'm not entirely sure if the last two work. Based on [comments at John Resig's blog](http://ejohn.org/blog/google-chrome-process-manager/). Go through the [code](http://src.chromium.org/viewvc/chrome/trunk/src/chrome/browser/) to see if you can find more.

---

## Comments

<!-- wp-comments-start -->

- **Sumit Dhar** _11 Sep 2008 1:47 am_:
  Have found an interesting use for "Incognito" mode. Both my wife and I use the same laptop to access Gmail. Not wanting to use a second browser, invariably one has to logout to allow the other to access mail.\
  \
  With Chrome's Incognito mode, it uses a different directory to store the cookies. This allows two or more people to login to their Gmail accounts in different tabs.\
  \
  Cheers,\
  D.
- **S Anand** _12 Sep 2008 1:19 am_:
  But do sessions persist? I thought that once you switch to incognito mode, your cookies would no longer be sent to the server, and that you would need to at least log in. So while one person can stay logged in, the other would still need to log in. Is that right?

<!-- wp-comments-end -->
