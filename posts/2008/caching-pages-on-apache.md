---
title: Caching pages on Apache
date: "2008-08-14T12:00:00Z"
categories:
  - coding
wp_id: 44
---

I don't use any [blogging software](http://en.wikipedia.org/wiki/Blog_hosting_service) for my site. I just hand-wired it some years ago. When doing this, one of the **biggest problems was [caching](http://en.wikipedia.org/wiki/Caching)**.

Consider each blog entry page. Each page has the same template, but different content. Both the template and content could be changed. So ideally, blog pages should be served dynamically. That is, every time someone requests the page, I should look up the content, look up the template, and put them together.

I did that, and within a few days outgrew my [hosting service](http://www.hostgator.com/)'s CPU usage limit. Running such a program for every page hit is too heavy on the CPU.

One way around this is to create the pages beforehand and serve it as regular HTML. But every time the template changes, you need to re-generate every single page. I had over 2,500 pages. That would kill the CPU usage if I changed the template often.

At that point, I did a piece of analysis. **Do I really need to regenerate all 2000 blog entries?** Wouldn't the [80-20 rule](http://en.wikipedia.org/wiki/80-20_rule) apply? The Apache log confirmed that 20% of the URLs were accounting for 76% of the hits. So I'd be wasting my time regenerating all the pages every time I changed the template.

[![Graph: 20% of URLs account for 76% of hits](/blog/assets/flickr-hits-per-page_2761682983_o-png.webp)](/blog/assets/flickr-hits-per-page_2761682983_o-png.webp "Cumulative Hits Per Page")

So based on this, I decided to dynamically cache the pages. When a page is requested for the first time, I create the page and save it in a cache. The next time, I'd just serve it from the cache. If the template changes, I just need to delete the cache. This way, I only generate pages that are requested, and they're only generated once.

OK, so that's the background. Now let me get to how I did it.

I wrote a Perl script, `blog.pl`, that would generate a page in the `html` folder whenever it is called. Next, I changed [Apache](http://httpd.apache.org/)'s [.htaccess](http://httpd.apache.org/docs/2.0/howto/htaccess.html) to run this program **only** if the page did not exist in the `html` folder.

```bash
# Redirect to cache first
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^([^/]*)\.html$       html/$1.html

# If not found, run program to create page
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^html/([^/]*)\.html$  blog.pl?t=$1
```

The first block redirects Apache to the cache. The second block checks if the file exists in the cache. If it doesn't, the Apache redirects to the program. The program creates the page in the cache and displays it. Thereafter, Apache will just serve the file from the cache.

---

This Apache trick can be used in another way. I keep files organised in different folders to simplify my work. But to visitors of this site, that organisation is irrelevant. So I effectively merge these folders into one. For example, I have a folder called [a](/a/) in which I keep my static content. I also have this piece of code:

```apacheconf
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^([^/]+)$   a/$1
```

If any file is not found in the main folder, just check in the `a/` folder. So I can access the file [/a/hindholam.midi](/blog/assets/hindholam.midi) as </hindholam.midi> as well.

This can be extended to a series of folders: either as a cascade of caches, or to merge many folders into one.

---

## Comments

<!-- wp-comments-start -->

- **Kannan Ekanath** _17 Aug 2008 7:00 am_:
  [http://random-thoughts-and-rambling.blogspot.com/]

  Hi,
  I wanted to know a comparison/contrast how setting up blog etc in your own hosted space compares with things like http://sites.google.com. I have always postponed this buying of a domain in favour of things like sites.google.com. Obviously I understand that the advantages would be you can control the LAF, the content, the organisation etc. But have you got a comparison doc or something on what precisely one would get if he hosts things in his own domain instead of a google/yahoo powered wiki style page?
- **S Anand** _17 Aug 2008 1:31 pm_:
  @Kannan: Don't have anything offhand, Kannan. But buying a domain would make sense anyway -- you could point your domain to sites.google.com transparently. If you wanted to build your own blogging system for your site, though, I'd advise against it. I did it because I started in 1999 and there weren't many blogging systems then. Today, it just doesn't make sense.
- **Nirupam** _18 Aug 2008 7:43 am_:
  Hi
  Want to create a site for myself. Should I go for own hosted space or should I start using sites like Geosites etc. I want to deploy web-based applications in my site. Can you please advise?
- **S Anand** _19 Aug 2008 11:24 am_:
  @Nirupam: If you want to deploy your own applications, you should probably create your own site. Get a free hosting service to start with. I've used 110mb.com, freestarthost.com and awardspace.com, and found them to be OK.

<!-- wp-comments-end -->
