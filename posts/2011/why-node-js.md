---
title: Why node.js
date: "2011-03-11T19:57:12Z"
lastmod: "2011-03-11T20:41:59Z"
categories:
  - coding
wp_id: 2613
---

I’ve moved from [Python](http://www.python.org/) to Javascript on the server side – specifically, [Tornado](http://www.tornadoweb.org/) to [Node.js](http://nodejs.org/).

Three years ago, I [moved](/blog/statistically-improbable-phrases-on-google-appengine) from Perl to Python because I got free hosting at [AppEngine](http://appengine.google.com/). Python’s a cleaner language, but that was not enough to make me move. Free hosting was.

Initially, my apps were on AppEngine, but that wouldn’t work for [corporate apps](/blog/open-source-in-corporates), so I tried [Django](http://www.djangoproject.com/). IMHO, Django’s too bulky, has too much “magic”, and templates are restrictive. Then I tried [Tornado](http://www.tornadoweb.org/): small; independent modules; easy to learn. I used it for almost 2 years.

The unexpected bonus with Tornado was it’s event-based model: it wouldn’t wait for file or HTTP requests to be complete before serving the next request. I ended up getting a fair bit of performance from a single server.

Trouble is, Python’s a rare skill. I tried selling Python in corporates a couple of times, and barring [RBS](http://www.rbs.co.uk/) (which used it before I came in, and made it really easy for me to build an [IRR calculator](/blog/calculating-irr)), I’ve failed every time. Apart from general fear, uncertainty and doubt, getting people is tougher.

Javascript’s a good choice. It has many of Python’s benefits. It’s easy to recruit people. Corporates aren’t terrified of it. [Rhino](http://www.mozilla.org/rhino/) was good enough a server. All it lacked was the “cool” factor, which [node.js](http://nodejs.org/) has now brought it. And besides,

- It’s fast. About 20 times faster than Rhino, by my crude benchmarks.
- It’s stable. (Well, at least, it feels stable. Rock solid stable. Sort of like [nginx](http://nginx.org/).)
- It’s asynchronous. So I don’t miss Tornado
- It has a pretty good set of [libraries](https://github.com/ry/node/wiki/modules), thanks to everyone jumping on to it
- I can write code that works on the client and server – e.g. form validation

Bye, Python.

---

## Comments

<!-- wp-comments-start -->

- **Philmod** _22 Mar 2011 12:09 pm_:
  Which library do you use for both server and client form validation?
- **[S Anand](http://www.s-anand.net/)** _24 Mar 2011 3:28 pm_:
  I don't have any at the moment, Phillippe -- I'm writing my own at the moment. Do you know of any good ones?
- **[Aravinda](http://aravindavk.in)** _12 Mar 2011 8:36 pm_:
  I started experimenting with nodejs and CouchDb couple of months ago. It is really awesome.
  A few good points to note about Node Js http://ncannasse.fr/blog/is\_nodejs\_wrong
- **[Shankar V](http://www.infosys.com)** _17 Mar 2011 11:44 am_:
  Oh Anand - Python I thought is such a wonderful language. That it is a rare skill should not be a reason to turn away from it. On the contrary, maybe it is good that the language is not getting dumbed down ;)
  Have you read this? - http://www.paulgraham.com/pypar.html
- **[Sathya](http://nullpointers.wordpress.com)** _17 Mar 2011 2:23 pm_:
  Javascript, as Doug Crockford said, is a misunderstood language. I was under the impression that enterprises are quite wary about server side javascript. I am quite surprised to learn that companies are more open to Javascript than Python (given that Google embraces Python). Also, in India, developers look at javascript more as a UI-bells-and-whistles stuff and it is quite difficult to hire a Quality serverside js developer. Anyway ... for rapid prototyping isn't Python good enough ? You are anyway used to the quirks of Django etc for 3 yrs. Am sure node.js would be having some baggage elsewhere. Or is it the case that change is the only constant ?
- **[Safe Hammad](http://safehammad.com)** _15 Mar 2011 7:36 am_:
  Very interesting post. I'd be keen to learn which stack of libraries and frameworks you end up using on top of node.js and your experiences with them. Also, what are your experiences so far of using node.js in a production setting and how do they compare with, for example, deploying Python code in Tornado?
- **[S Anand](http://www.s-anand.net/)** _4 Jun 2011 4:11 am_:
  Yes, I did play with it. It's amazing. I'm waiting for a few more months, allowing it to get more popular, and once someone else on my team suggests it independently, we'll jump into it!
- **Luis** _3 Jun 2011 3:30 pm_:
  If you like the benefits of JavaScript and node.js but you still miss python's syntax and productivity, you may want to play with Coffeescript. Check it out, it's addictive...

<!-- wp-comments-end -->
