---
title: Auto reloading pages
date: "2012-09-30T10:33:15Z"
categories:
  - coding
wp_id: 2804
---

After watching [Bret Victor](http://worrydream.com/)’s [Inventing on Principle](http://www.youtube.com/watch?v=PUv66718DII), I just **had** to figure out a way of getting live reloading to work. I know about [LiveReload](http://livereload.com/), of course, and everything I’ve heard about it is good. But their Windows version is in alpha, and I’m not about to experiment just yet.

This little script does it for me instead:

```javascript
(function(interval, location) {
  var lastdate = "";
  function updateIfChanged() {
    var req = new XMLHttpRequest();
    req.open("HEAD", location.href, false);
    req.send(null);
    var date = req.getResponseHeader("Last-Modified");
    if (!lastdate) {
      lastdate = date;
    } else if (lastdate != date) {
      location.reload();
    }
  }
  setInterval(updateIfChanged, interval);
})(300, window.location);
```

It checks the current page every 300 milliseconds and reloads it if the Last-Modified header is changed. I usually include it as a minified script:

```html
<script>(function(d,c){var b="";setInterval(function(){var a=new
XMLHttpRequest;a.open("HEAD",c.href,false);a.send(null);
a=a.getResponseHeader("Last-Modified");if(b)b!=a&&
c.reload();else b=a},d)})(300,window.location)</script>
```

There are no dependencies on any library, like jQuery. However, it requires that the file be on a web server. (It’s easy to fix that, but since I always run a local webserver, I’ll let you solve that problem yourself.)
