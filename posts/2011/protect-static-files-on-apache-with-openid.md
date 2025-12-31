---
title: Protect static files on Apache with OpenID
date: "2011-11-18T23:11:50Z"
lastmod: "2011-11-19T13:58:36Z"
categories:
  - coding
wp_id: 2695
---

I moved from static HTML pages to web applications and back to static HTML files. There’s a lot to be said for the simplicity and portability of a bunch of files. Static site generators like [Jekyll](https://github.com/mojombo/jekyll) are increasingly popular; I’ve built a simple [publisher](https://bitbucket.org/sanand0/utils/src/tip/publish.make) that I use extensively.

Web apps give you something else, though, that are still useful on a static site. Access control. I’ve been resorting to [htpasswd](http://httpd.apache.org/docs/2.2/programs/htpasswd.html) to protect static files, and it’s far from optimal. I **don’t** want to know or manage users’ passwords. I **don’t** want them to remember a new ID. I just want to allow specific people to log in via their Google Accounts. (OpenID is too [confusing](http://www.gibdon.com/2008/06/openid-is-confusing.html), and most people [use Google anyway](http://blog.stackoverflow.com/2010/04/openid-one-year-later/).)

The easiest option would be to use Google [AppEngine](http://appengine.google.com/). But their [new pricing](http://code.google.com/appengine/docs/billing.html) worries me. Hosting on EC2 is expensive in the long run. All my hosting is now out of a shared [Hostgator](http://www.hostgator.com/) server that offers Apache and PHP.

So, obviously, I wrote a library protects static files on Apache/PHP using OpenID.

### [Download the code](https://github.com/sanand0/protectstatic)

Say you want to protect `/home/www` which is accessible at <http://example.com/>.

- Copy `.htaccess` and `_auth/` under `/home/www`.
- In .htaccess, change `RewriteBase` to `/`
- In `_auth/`, copy `config.sample.php` into `config.php`, and

- change `$AUTH_PATH` to <http://example.com/>
- add permitted email IDs to `function allow()`

Now, when you visit <http://example.com>, you’ll be taken to Google’s login page. Once you log in, if your email ID is allowed , you’ll be able to see the file.

Feel free to try, or [fork the code](https://github.com/sanand0/protectstatic).

---

## Comments

<!-- wp-comments-start -->

- **[S Anand](http://www.s-anand.net/)** _19 Nov 2011 10:31 am_:
  I could. But what I've learnt is that while the static content on this site has survived 14 years, moving from host to host, the same can't be said of ANY of the apps I've written to create the site. I've moved from shell scripts to Perl to Python to node.js... and something else will come up. I can't maintain this stuff. Fortunately, HTML will stay.
  So I'm making the content primary. I just have a bunch of static files, and that's the key. This is an OPTIONAL library that sits on the side. Without it, the worst that'll happen is that the content becomes public. But otherwise, all URLs will remain unbroken. That's a big win with this approach.
  That's also the reason I rejected AppEngine. For my volume of usage, pricing isn't a serious issue. It's simplicity.
- **[Manu](http://www.reviewgang.com)** _19 Nov 2011 5:59 am_:
  If you are willing to host it outside, then heroku allows one free instance per project.
- **[S Anand](http://www.s-anand.net/)** _2 Dec 2011 10:09 pm_:
  I too will probably stay on WordPress for a while. But recently, I've been creating quite a few microblogs for various topics, and find that the workflow of Markdown -> Dropbox -> PHP -> HTML far too compelling to ignore. It's worked quite well from an ease of publishing perspective. I'm still ironing out few edges. Will publish once I do.
- **[Thejesh GN](http://thejeshgn.com)** _25 Nov 2011 11:56 am_:
  I was planning to move to static using http://www.blogofile.com/ (python and variety of templating systems are supported). But I am still betting on wordpress for many things. One day I will probably move to static blog.
- **[Christophe-Marie Duquesne](http://chmd.fr)** _22 Dec 2013 12:53 pm_:
  Hi,
  Your post inspired me to write a lighttpd magnet script that protects content regardless of its nature (static or dynamic). I use it:
  - for protecting my (static) photo gallery and only giving access to people I select
  - for protecting my (dynamic) rss reader and only giving access to myself
  - for protecting my (dynamic) online file manager and only giving access to my girlfriend and myself.
    It is completely pluggable, and it sets the REMOTE\_USER server variable so that user-aware applications can use this mechanism to authentify you.
    https://lighttpd-external-auth.chmd.fr/

<!-- wp-comments-end -->
