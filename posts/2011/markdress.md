---
title: Markdress
date: "2011-12-03T18:05:26Z"
categories:
  - coding
  - tools
wp_id: 2704
---

This year, I’ve converted the bulk of my content into [Markdown](http://daringfireball.net/projects/markdown/) – a simple way of formatting text files in a way that can be rendered into HTML.

Not out of choice, really. It was the only solution if I wanted to:

- Edit files on my iPad / iPhone (I’ve started doing that a lot more recently)
- Allow the contents to be viewable as HTML as well as text, **and**
- Allow non techies to edit the file

As a bonus, it’s already the format [Github](https://github.com/) and [Bitbucket](https://bitbucket.org/) use for markup.

If you toss [Dropbox](http://www.dropbox.com/) into the mix, there’s a powerful solution there. You can share files via Dropbox as Markdown, and publish them as web pages. There are already a number of solutions that let you do this. [DropPages.com](http://droppages.com/) and [Pancake.io](http://pancake.io/) let you share Dropbox files as web pages. [Calepin.co](http://calepin.co/) lets you blog using Dropbox.

My needs were a bit simpler, however. I sometimes publish Markdown files on Dropbox that I want to see in a formatted way – without having to create an account. Just to test things, or share temporarily.

Enter [Markdress.org](http://markdress.org/). My project for this morning.

Just add any URL after markdress.org to render it as Markdown. For example, to render the file at <http://goo.gl/zTG1q>, visit <http://markdress.org/goo.gl/zTG1q>.

To test it out, create any text file in your Dropbox public folder, get the public link and append it to <http://markdress.org/> without the http:// prefix.

---

## Comments

<!-- wp-comments-start -->

- **Gee** _14 Jan 2012 12:38 am_:
  Great news. And all the best in your new ventures. Meanwhile, I made a simple bookmarklet for you: https://gist.github.com/1609547
- **[Thejesh GN](http://thejeshgn.com)** _5 Dec 2011 6:47 am_:
  Check this
  http://markdoc.org
  I have been using it locally for sometime. Its cool.
- **[S Anand](http://www.s-anand.net/)** _4 Dec 2011 12:18 pm_:
  James, your suggestion on following URLs is spot-on! I'll put this in (one of these days, when I get back to this...)
- **[S Anand](http://www.s-anand.net/)** _6 Dec 2011 10:10 pm_:
  You need to have an empty line before a list. For example:
  # Test
  This is a list:
  \* one
  \* two
  \* three
- **[Michael Lajlev](http://osweb.dk)** _5 Dec 2011 2:12 pm_:
  I seem to struggle getting list items to work http://markdress.org/dl.dropbox.com/u/623576/test.md
  Any idea?
- **Gee** _12 Jan 2012 9:14 pm_:
  Markdress is great. I have it running on my server. I would like to render files in a directory adjacent to, or inside the app folder, instead of entering a URL path each time. I would like to enter just `filename.txt` and it would default back to (effectively) `/markdress/filename.txt`
  I looked over index.php and tried a few things but I can't get relative files to render. Is this an enhancement you've considered? Thanks for the great tool.
- **[S Anand](http://www.s-anand.net/)** _13 Jan 2012 12:51 am_:
  I personally use this sort of a variant, but havent gotten around to making the same changes on markdress. I will do that over the next few days, once I settle down.
- **[The Bootcamp Blog Begins | JFDI–Innov8 2012 Bootcamp](http://bootcamp.jfdi.asia/2011/12/03/the-bootcamp-blog-begins/)** _3 Dec 2011 8:16 pm_ _(pingback)_:
  [...] kind of people who can whip up something like Markdress in a [...]
- **[James Manning](http://blog.sublogic.com/)** _4 Dec 2011 9:08 am_:
  Awesome! Nicely done!
  Not sure if it's by design or not, but FWIW the example given seems to show that relative url's aren't handled correctly - the bottom of this page:
  http://daringfireball.net/projects/markdown/index.text
  has this relative url:
  [tfmenu]: /graphics/markdown/mt\_textformat\_menu.png
  which gets faithfully rendered into:
  That fails, of course, with the attempted get operation returning:
  http://markdress.org/graphics/markdown/mt\_textformat\_menu.png
  Could not fetch http://graphics/markdown/mt\_textformat\_menu.png
  FWIW, inserting a base tag in the head seems to work fine, like:
  However, it would have to be the 'real' url in the base - IOW, this doesn't work:
  On a related note, IMHO it seems like markdress should handle redirects and 'pass through' as a redirect to the markdress version.
  IOW, looking at this example request from the post:
  http://markdress.org/goo.gl/zTG1q
  When markdress requested the page and got back a redirect, instead of following it, it should have instead passed back a redirect to:
  http://markdress.org/daringfireball.net/projects/markdown/index.text
  IMHO, that's a better user experience as it's more clear what's getting served up (and it would reflect in the title as well). If/when caching was added (assuming it's not there now), then you'd want to have the canonical url for targets anyway. :)
  That behavior isn't required to fix the relative-url issue, but since you'll have to know what requests redirect to (the call may be implicitly following it now, so you don't currently know?), then you'll have the necessary info to do this piece as well. :)
  Thanks again for marking markdress! It's definitely going to be incredibly useful!
- **[Jeff Byrnes](http://jeffbyrn.es/)** _6 Dec 2012 3:14 pm_:
  Markdress appears to have expired, any chance of its return?
- **[S Anand](http://www.s-anand.net/)** _7 Dec 2012 3:53 am_:
  I didn't think anyone was using it -- so I just let the domain expire.
  Alternatives are at https://github.com/sanand0/markdress#alternatives. You could also host the code yourself.

<!-- wp-comments-end -->
