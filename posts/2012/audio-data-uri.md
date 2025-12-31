---
title: Audio data URI
date: "2012-07-17T11:41:29Z"
categories:
  - coding
wp_id: 2773
---

Turns out that you can use [data URIs](http://en.wikipedia.org/wiki/Data_URI_scheme) in the `<audio>` tag.

Just upload an MP3 file to <http://dataurl.net/#dataurlmaker> and you’ll get a long string starting with `data:audio/mp3;base64...`

Insert this into your HTML:

```html
<audio controls src=”data:audio/mp3;base64...”>
```

That’s it – the entire MP3 file is embedded into your HTML page without requiring additional downloads.

This takes a bit more bandwidth than the MP3, and won’t work on Internet Explorer. But for modern browsers, and small audio files, it reduces the overall load time – sort of like [CSS sprites](http://css-tricks.com/css-sprites/).

So, on my bus ride today, I built a little HTML5 musical keyboard that generates data URIs on the fly. Click to play.

[![keyboard](/blog/assets/keyboard.webp "keyboard")](http://s-anand.net/musical-keyboard.html)

---

## Comments

<!-- wp-comments-start -->

- **Fabio Mazarotto** _9 May 2013 8:07 pm_:
  Can you confirm that it no longer works in Safari >= 6.0?

<!-- wp-comments-end -->
