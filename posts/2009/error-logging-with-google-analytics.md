---
title: Error logging with Google Analytics
date: "2009-05-23T19:29:01Z"
categories:
  - coding
wp_id: 2378
---

A quick note: I blogged earlier about [Javascript error logging](/blog/javascript-error-logging/), saying that you can wrap every function in your code (automatically) in a `try{} catch{}` block, and log the error message in the `catch{}` block.

I used to write the error message to a Perl script. But now I use [Google’s event tracking](http://code.google.com/apis/analytics/docs/tracking/eventTrackerGuide.html).

```javascript
var s = [];
for (var i in err) s.push(i + "=" + err[i]);
s = s.join(" ").substr(0, 500);
pageTracker._trackEvent("Error", function_name, s);
```

The good part is that it makes error monitoring a whole lot easier. Within a day of implementing this, I managed to get a couple of errors fixed that had been pending for months.

---

## Comments

<!-- wp-comments-start -->

- **[Thejesh GN](http://thejeshgn.com)** _29 May 2009 7:40 am_:
  That is a good tip. I can use the present infrastructure for error logging..

<!-- wp-comments-end -->
