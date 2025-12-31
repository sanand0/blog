---
title: Codecasting
date: "2011-11-16T20:05:52Z"
lastmod: "2022-01-21T06:49:08Z"
categories:
  - coding
wp_id: 2691
---

The best way to explain code to a group of people is by walking through it. If they’re far away in space or time, then a video is the next best thing. You can recommend them to try out the best [**coding apps**](https://skillspot.co/learning-to-code-on-your-phone-the-best-coding-apps-of-2021/) as well.
The trouble with videos, though, is that they’re big. I can’t host them on my server – I’d need YouTube. Editing them is tough. You can’t copy & paste code from videos. And so on.
One interesting alternative is to use presentations with audio. [Slideshare](http://slideshare.net/), for instance, lets you share slides and sync it with audio. That **almost** works. But it’s still not good enough. I’d like code to be stored as code.
What I really need is codecasting: a YouTube or Slideshare for code. The closest I’ve seen until day-before was [etherpad](http://etherpad.org/) or [ttyrec](http://en.wikipedia.org/wiki/Ttyrec) – but neither support audio.
Enter [Popcorn](http://popcornjs.org/). It’s a Javascript library from Mozilla that, among other things, can fire events when an audio/video element reaches a particular point.

### [Watch a demo of how I used it for codecasting](http://www.s-anand.net/outlook-mapi.html)

A look at the code will show you that I’m using two libraries: [SyntaxHighlighter](http://alexgorbatchev.com/SyntaxHighlighter/) to highlight the code, and [Popcorn](http://popcornjs.org/). The meat of the code I’ve written is in this subtitle function.

```javascript
function subtitle(media_node, pre_node, events) {
  var pop = Popcorn(media_node);
  for (var i=0, l=events.length; i<l; i++)="" {="" for="" (var="" j="0," line_selector="[]," line_no;="" line_no="events[i][1][j];" j++)="" line_selector.push(pre_node="" +="" '="" .number'="" line_no)="" }="" var="" start="events[i][0]" ,="" end="i<l-1" ?="" events[i+1][0]="" :="" events[i][0]+999;="" (function(start,="" end,="" selector)="" pop.code({start:="" start,="" end:end,="" onstart:="" function(o)="" $(selector).addclass('highlighted');="" },="" onend:="" $(selector).removeclass('highlighted');="" })="" })(start,="" line_selector.join(','));="" }<="" pre="">
```

When called like this:

```javascript
subtitle("#audio", "pre", [
  [1, [1, 2, 3]],
  [5, [4, 5, 6]],
  [9, [7, 8]],
]);
```

... it takes the #audio element, when it plays to 1 second, highlights lines 1,2,3; at 5 seconds, highlights lines 4,5,6; and so on.
Another thing that helped was that my iPad has a much better mic than my laptop, and [ClearRecord](http://itunes.apple.com/us/app/clearrecord-premium-noise/id395704227?mt=8) is a really simple way to create recordings with minimal noise. [Note to self: sampling at 16KHz and saving as a VBR MP3 (45-85kbps) seems the best trade-off.]
With these tools, my time to prepare a tutorial went down from 4 hours to half an hour!

```javascript
</l;>
```

---

## Comments

<!-- wp-comments-start -->

- **[S Anand](http://www.s-anand.net/)** _17 Nov 2011 7:58 am_:
  Want to try building one? :-)
- **Tanu** _17 Nov 2011 2:52 pm_:
  Good one..
  Want to experiment one..
- **vivek** _20 Nov 2011 2:46 pm_:
  Excellent! Will start using this right away! Thanks Anand.
- **[Veera](http://veerasundar.com/blog)** _17 Nov 2011 6:30 am_:
  Great idea for an web app/platform!

<!-- wp-comments-end -->
