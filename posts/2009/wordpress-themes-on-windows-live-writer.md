---
title: WordPress themes on Live Writer
date: "2009-03-08T01:27:20Z"
lastmod: "2021-12-08T18:47:24Z"
categories:
  - coding
wp_id: 2305
---

One of the reasons I moved to WordPress was the ability to write posts offline, for which I use [Windows Live Writer](http://download.live.com/writer) most of the time. The beauty of this is that I can preview the post **exactly** as it will appear on my site. Nothing else that I know is as [WYSIWYG](http://en.wikipedia.org/wiki/WYSIWYG), and it’s very useful to be able to type knowing exactly where each word will be.

The only hitch is: if you write your own [WordPress theme](http://wordpress.org/extend/themes/), Live Writer probably won’t be able to detect your theme — unless you’re an expert theme writer.

I hunted on Google to see how to get my theme to work with Live Writer. I didn’t find any tutorials. So after a bit of hit-and-miss, I’m sharing a quick primer of what worked for me. If you don't want to go through the hassle, you can always call on professionals who are adept at services like [professional custom website design](https://www.littlebluedeerdesign.com/).

Open any post on your blog (using your new theme) and save that as `view.html` in your theme folder. Now replace the page’s title with {post-title} and the page’s content with {post-body}. For example:

```html
<h1>{post-title}</h1>

{post-body}
```

This is the file Live Writer will be [using as its theme](http://msdn.microsoft.com/en-us/library/bb463261.aspx). This page will be displayed exactly as it is by Live Writer, with {post-title} and {post-body} replaced with what you type. You can put in anything you want in this page — but at least make sure you include your CSS files.

To let Live Writer know that `view.html` is what it should display, copy WordPress’ `/wp-includes/wlw-manifest.xml` to your theme folder and add the following lines just before `</manifest>`.

```xml
WebLayout
```

[Live Writer searches for wlmanifest.xml](http://msdn.microsoft.com/en-us/library/bb463263.aspx) in the `<link rel="wlmanifest">` tag of your home page. Since WordPress already links to its default `wlwmanifest.xml`, we need remove that link and add our own. So add the following code to your `functions.php`:

```php
function my_wlwmanifest_link() { echo
  '';
}
remove_action('wp_head', 'wlwmanifest_link');
add_action('wp_head', 'my_wlwmanifest_link');
```

That’s it. Now if you add your blog to Live Writer, it will automatically detect the theme.

---

## Comments

<!-- wp-comments-start -->

- **[Windows Live Writer 向 DEDECMS 发文章 | 快乐生活，快乐工作](http://yuntian.name/?p=228)** _30 Apr 2009 8:39 am_ _(pingback)_:
  [...] WordPress themes on Live Writer [...]
- **[San Diego Web Design](http://www.websitesare.us)** _22 Jun 2009 9:04 pm_:
  Note to my first post as it doesn't show correctly:
  What I did is I ended up adding the part between the tags to the regular wlwmanifest.xlm file.
- **[vivek](http://goodinformation)** _15 Jun 2009 6:23 am_:
  Hi,
  Thanks great information
- **[San Diego Web Design](http://www.websitesare.us)** _22 Jun 2009 9:02 pm_:
  Thank you, thank you, thank you! I was trying for hours to fix this before I found your post! Actually, the way you described it didn't exactly work for me (I guess I did something wrong with the paths), but I ended up just adding the
  WebLayout
  with the absolute path to the regular wlwmanifest.xlm inside the includes folder and now it works!
  Thanks again, your post was the only one describing this problem and helping me fix it!
- **shawn** _29 Jan 2010 7:37 pm_:
  I was having this issue today and came across this page. I came up with a very simple fix that requires no coding.
  When setting up your blog in WLW, go to your admin settings in the wordpress dashboard and temporarily set your "Reading" settings to "Front page displays -> Your latest posts ". WLW will successfully download the theme, then set your Front page displays back to your custom setting.
- **[zimmi](http://www.zimmi.cz)** _27 Jan 2010 7:53 pm_:
  What if it still doesn't work? Anything else I can try?
- **S** _15 Jul 2010 5:45 pm_:
  Thank you so much!!!!!!!!!! this worked.
- **[girls information](http://www.girls-information.com)** _27 Sep 2010 7:19 am_:
  this worked for me tanks for sharing
- **[Graphene, Child Themes, and Live Writer - Eyes2Design](http://www.eyes2design.com/flogging-and-blogging/graphene-child-themes-and-live-writer)** _28 Jul 2012 4:57 am_ _(pingback)_:
  [...] came across this page by www.s-anand.net which helped me a lot in understanding how Live Writer and WordPress get along together. So follow [...]

<!-- wp-comments-end -->
