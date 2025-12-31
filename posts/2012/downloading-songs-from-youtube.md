---
title: Downloading songs from YouTube
date: "2012-03-15T13:11:36Z"
lastmod: "2012-07-31T02:02:22Z"
categories:
  - how-i-do-things
wp_id: 2745
---

Five years ago, I built a [song search engine](http://www.s-anand.net/hindi) – mainly because I needed to listen to songs. Three years ago, I stopped updating it – mainly because I stopped listening to songs actively, and have been busy since. For those of you who have been using my site for music: my apologies.
These days, I don’t really find the need to download music. [YouTube](http://www.youtube.com/) has most of the songs I need. Bandwidth is pretty good too [even when on the move](https://twitter.com/#!/sanand0/status/166886668958318592).
But when I do need to download music, this is my new workflow.

1. Find the song on [YouTube](http://www.youtube.com/). (Misspellings are still an issue, but you’ll usually find what you need)
2. Download the video. [Keepvid](http://keepvid.com/) is the simple option. [youtube-dl](http://rg3.github.com/youtube-dl/)is the geek’s option (for multiple downloads)
3. Use [VLC](http://www.videolan.org/vlc/) – the swiss-army knife of media – to convert the video into an MP3.

That last step requires a bit of explaining. It’s very simple once you know how, but it took me a few months to get it right. So here goes.
**Select the Convert / Save option in the Media menu.**
[![audio-conversion-1](/blog/assets/audio-conversion-1.webp "audio-conversion-1")](/blog/assets/audio-conversion-1.webp)
**Click on Add to open file you want to convert.** You can pick a track from an disk as well if you want to rip an audio CD or a DVD.
[![audio-conversion-2](/blog/assets/audio-conversion-2.webp "audio-conversion-2")](/blog/assets/audio-conversion-2.webp)
**Choose the file.**
[![audio-conversion-3](/blog/assets/audio-conversion-3.webp "audio-conversion-3")](/blog/assets/audio-conversion-3.webp)
**Click on Convert / Save.**
[![audio-conversion-4](/blog/assets/audio-conversion-4.webp "audio-conversion-4")](/blog/assets/audio-conversion-4.webp)
**Type the destination filename.** Make sure you type the full file name, and not just the name of the folder.
[![audio-conversion-5](/blog/assets/audio-conversion-5.webp "audio-conversion-5")](/blog/assets/audio-conversion-5.webp)
**Select the output format you want under Settings – Profile.** You can tweak the bitrate with the settings button, but I usually don’t bother.
[![audio-conversion-6](/blog/assets/audio-conversion-6.webp "audio-conversion-6")](/blog/assets/audio-conversion-6.webp)
**When you click on the Start button, the file will be converted** or the CD will be ripped. You’ll see the position marker move fairly fast.
[![audio-conversion-7](/blog/assets/audio-conversion-7.webp "audio-conversion-7")](/blog/assets/audio-conversion-7.webp)

The only problem I have with this method is that I can’t seem to do batch conversions easily enough with the GUI. Does anyone have any other workflow they like?
**Update (31 Jul 2012)**: Aditya Sengupta suggests the following: (should've guessed VLC would have something up its sleeve)

```
vlc -I dummy $FILENAME --no-sout-video --sout "#transcode{acodec=mp3,5Dab=<wbr>AUDIO_BITRATE,channels=2}:std{<wbr>access=file,mux=raw,dst=$NAME.<wbr>mp3}" vlc://quit
```

---

## Comments

<!-- wp-comments-start -->

- **408wij** _15 Mar 2012 1:48 pm_:
  Coincidentally, I just ripped a bunch of MP3s from AVIs last night. I used a Windows program called Format Factory. It supports batch conversion. Some AVIs failed on first past, so I reset their status in the queue and reran.
- **vB** _16 Mar 2012 5:31 am_:
  Hey
  Try using freemake. The best as per me. You paste youtube URL and select the format you want to save on your machine and it does the rest.
  btw - found your website pretty neat, do not remember what was i looking for when i discovered it couple of days back, but now have put it on my reader.
- **[Ramanujam](http://ramanuj.me)** _24 Mar 2012 1:18 pm_:
  Alternatively, you can skip all the steps and use one of the numerous sites that will directly give you the mp3.
  Here is one that works pretty well.
  http://www.youtube-mp3.org/
- **[Pravin](http://www.geekshike.co.cc/)** _16 Mar 2012 5:50 pm_:
  I've been using this nifty little freeware for a long time and i would suggest it to you if you are interested in an all-in-one video downloading and format conversion. The feature set is really impressive for a freeware. It has also got support for GPU acceleration which might prove use full for those who want to work while conversion is on.
  http://bit.ly/aayV0
- **Pravin** _25 Mar 2012 12:48 pm_:
  @Sanketh
  normally flv's have ~32kbps audio bit rate
  if you could go for 480p mode you will get ~128kbps(Audio CD Quality) audio bit rate
- **[Pankaj](http://pankajnath.in)** _10 Apr 2012 8:57 pm_:
  Seems you take a lot pain in getting few MP3s. :P
  Try freemake software (freeware) or even simpler this one http://www.youtube-mp3.org/
- **Sanketh** _20 Mar 2012 3:49 pm_:
  Roughly what bitrate are the youtube flv encoded at?
- **Ganesh Kondal** _4 Apr 2012 4:54 pm_:
  youtube-dl works like a charm. Thanks dude. Using it in Ubuntu 11
- **Chaitanya** _20 Mar 2012 9:01 am_:
  Hey Anand
  This blog post has been very useful. I just used Freemake and it's cool and easy.
  Also, converting few videos using VLC Player. Does it take as much time as the length of the video? Or conversion is slow because I am doing it on my pretty old spec'ed laptop.
- **Sendhil** _17 Mar 2012 6:18 pm_:
  I heard of this one-step workflow from my colleague:
  http://www.singyoutube.com/
- **Deepak** _17 Mar 2012 7:11 am_:
  I have used Listen to Youtube (http://www.listentoyoutube.com/). Works very well, especially for my son and his nursery rhymes and we dont want to see the computer screen for a long time.
- **[Ganesh](http://fillambazi.com)** _29 Mar 2012 10:50 am_:
  If listening to mp3 is what you want then there are several free mp3 search sites. I use www.mp3skull.com You get a lot of options with various bit rates, and can listen to the song before downloading it.
- **Vishal Dalmia** _24 May 2012 6:46 am_:
  http://musicable.com/ is a simple site that does the download easily with no downloads or installation required.
- **Vijay Gnanaraj** _30 Sep 2012 12:29 am_:
  The next best option wud be IDM, internetdownloadmanager, which can download any video (almost from any website) playing on ur screen
- **[Streaming audio to iOS via VLC | s-anand.net](http://www.s-anand.net/blog/streaming-audio-to-ios-via-vlc/)** _13 Oct 2012 4:51 pm_ _(pingback)_:
  [...] listen to it on your iPhone / iPad – converting your PC into a radio station. As with most things VLC related, it’s tough to figure out but obvious in [...]

<!-- wp-comments-end -->
