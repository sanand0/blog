---
title: Streaming audio to iOS via VLC
date: "2012-10-13T15:50:59Z"
categories:
  - how-i-do-things
wp_id: 2830
---

You can play a song on your PC and listen to it on your iPhone / iPad – converting your PC into a radio station. As with most things [VLC related](/blog/downloading-songs-from-youtube/), it’s tough to figure out but obvious in retrospect.

The first thing to do is set up the MIME type for the streaming. This is a [bug that has been fixed](http://trac.videolan.org/vlc/ticket/7208), but might not have made it into your version of VLC.

Go to Tools – Preferences.

[![vlc-pref-1](/blog/assets/vlc-pref-1.webp "vlc-pref-1")](/blog/assets/vlc-pref-1.webp)

Click on “All” to see all the settings.

[![vlc-pref-2](/blog/assets/vlc-pref-2.webp "vlc-pref-2")](/blog/assets/vlc-pref-2.webp)

Under Stream output – Access output – HTTP, set Mime to `audio/x-mpeg`.

[![vlc-pref-3](/blog/assets/vlc-pref-3.webp "vlc-pref-3")](/blog/assets/vlc-pref-3.webp)

At this point, you should restart VLC.

As I mentioned earlier, you might not need to do this if you have new enough a version of VLC that auto-detects the content’s MIME type.

Re-open VLC, and go to the Media – Stream menu.

[![vlc-stream-1](/blog/assets/vlc-stream-1.webp "vlc-stream-1")](/blog/assets/vlc-stream-1.webp)

Click Add and choose the file you want to stream. Then click on Stream.

[![vlc-stream-2](/blog/assets/vlc-stream-2.webp "vlc-stream-2")](/blog/assets/vlc-stream-2.webp)

Click Next.

[![vlc-stream-3](/blog/assets/vlc-stream-3.webp "vlc-stream-3")](/blog/assets/vlc-stream-3.webp)

Select HTTP and click Add.

[![vlc-stream-4](/blog/assets/vlc-stream-4.webp "vlc-stream-4")](/blog/assets/vlc-stream-4.webp)

Select Audio – MP3 and click on Stream.

[![vlc-stream-5](/blog/assets/vlc-stream-5.webp "vlc-stream-5")](/blog/assets/vlc-stream-5.webp)

At this point, the audio is being streamed at port 8080 of your machine. You can change the port and path in the menu above. (To find your local IP address, open the Command Prompt and type ipconfig.)

Open Safari on your iPhone or iPad, and visit <http://your-ip-address:8080/>

[![vlc-ipad-streaming](/blog/assets/vlc-ipad-streaming.webp "vlc-ipad-streaming")](/blog/assets/vlc-ipad-streaming.webp)

I haven’t figured out the right codec and MIME type to do this for videos yet, but hopefully will figure it out soon.

---

## Comments

<!-- wp-comments-start -->

- **Shibu** _19 Sep 2014 10:12 am_:
  You should try out any of the light weight DLNA servers....

<!-- wp-comments-end -->
