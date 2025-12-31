---
title: Javascript error logging
date: "2007-12-25T12:00:00Z"
lastmod: "2022-01-22T06:40:34Z"
categories:
  - coding
wp_id: 69
---

> If something goes wrong with my site, I like to know of it. My top three problems are:
>
> 1. [The site is down](/Monitoring_site_downtime.html)
> 2. [A page is missing](/Handling_missing_pages.html)
> 3. [Javascript isn't working](#start3)
>
> This is the last of 3 articles on these topics.

**I am a bad programmer**
I am not a professional developer. In fact, I'm not a developer at all. I'm a management consultant. (Usually, it's myself I'm trying to convince.)
Since no one pays me for what little code I write, no one shouts at me for getting it wrong. So I have a happy and sloppy coding style. I write what I feel like, and publish it. I don't test it. Worse, sometimes, I don't even run it once. I've sent little scripts off to people which wouldn't even compile. I make changes to this site at midnight, upload it, and go off to sleep without checking if the change has crashed the site or not.
**But no one tells me so**
At work, that's usually OK. On the few occasions where I've written Perl scripts or VB Macros that don't work, people call me back within a few hours, very worried that THEY'd done something wrong. (Sometimes, I don't contradict them.) It can be quite a stressful experience but good thing you can [**learn more here**](https://www.exhalewell.com/cbd-flower/) on how to cope up with it.
On my site, I don't always get that kind of feedback. People just click the back button and go elsewhere.
Recently, I've been doing more Javascript work on my site than writing stuff. Usually, the code works for me. (I write it for myself in the first place.) But I end up optimising for Firefox rather than IE, and for the plugins I have, etc. When I try the same app a few months later on [my media PC](/Making_a_Media_PC.html), it doesn't work, and shockingly enough, no one's bothered telling me about it all these months. They'd just click, nothing happens, they'd vanish.
**But their browsers can tell me**
The good part about writing code in Javascript is that I can catch exceptions. Any Javascript error can be trapped. So since the end of last year, I've started wrapping almost every Javascript function I write in a `try {} catch() {}` block. In the `catch` block, I send a log message reporting the error.
The code looks something like this:

```javascript
function log(e, msg) {
  for (var i in e) msg += i + "=" + e[i] + "\n";
  (new Image()).src = "log.pl?m=" + encodeURIComponent(msg);
}

function abc() {
  try {
    // ... function code
  } catch (e) {
    log(e, "abc");
  }
}
```

Any time there's an error in `function abc`, the `log` function is called. It sends the function name (`"abc"`) and the error details (the contents of the error event) to `log.pl`, which stores the error, along with details like the URL, browser, time and IP address. This way, I know exactly where what error occurs.
This is a fantastic for a three reasons.

- **It tells me **when** I've goofed up**. This is instantaneous feedback. I don't have to wait for a human. If you run my program on your machine, and it fails, **I get to know immediately.** (Well, as soon as I read the error log, at least.)
- **It tells me **where** I've goofed up**. The URL and the function name clearly indicate the point of failure.
- **It tells me **why** I've goofed up**. Almost. Using the browser name and the error message, I can invariably pinpoint the reason for the error. Then it's just a matter of taking the time to fix it.

I'd think this sort of error reporting should be the norm for any software. At least for a web app, given how easy it is to implement.

---

## Comments

<!-- wp-comments-start -->

- **CodeKitten** _25 Dec 2007 12:00 pm_:
  You should bind an onerror-triggered method to call your log method aswell :)
- **Danko Stojanovic** _10 May 2010 8:12 am_:
  I feel your pain. I also moved away from programming to management. I have to live with customers saying "It doesn't work" and programmers "It works just fine when I test it".
  I so wish to know what is going on my client's computer.
  Thanks for this article. It helped me decide to pursue this further
- ## **[Allan Ebdrup](http://muscula.com)** _13 Nov 2011 7:23 am_:The onerror event is a great way to start logging JavaScript errors, more people should use it. JavaScript errors can be just as bad as a webserver that is down, you really need to log those errors so you can do something about them.onerror, is quirky. It does not fire on iPad, iPhone, Safari and some other browseres. To catch those errors you have to insert try-catch'es arount your event handlers, xhr-requests and some other places. This will also let you get more detail about the errror (call stack in some browsers).But onerror is still much better than nothing.
  We've solved a lot of these issues, with a solution that you install just like Google Analytics. Currently we are in a testing phase, private beta (free). To get an invite you can got to http://muscula.com and sign up.
- **Kiawaki** _8 Jul 2011 5:45 am_:
  A question from somebody who is even less of a pro web developer: how exactly do you use this code? Do you put it before or after the script or both? Thanks!
- **[Offbeatmammal](http://jserrlog.appspot.com)** _23 Sep 2011 12:48 am_:
  if you want a no-brain, minimal effort then have a look at jsErrLog ... a simple utility that does this and logs it to a remote AppEngine service (all for free, in an open source project) - check out http://jsErrLog.appspot.com which links to the GitHub repository as well

<!-- wp-comments-end -->
