---
title: Downloading online songs
date: "2008-09-17T12:00:00Z"
categories:
  - coding
wp_id: 30
---

You know those songs on [Raaga](http://www.raaga.com/), [MusicIndiaOnline](http://www.musicindiaonline.com/), etc? The ones you can listen to but can't download?

Well, you can download them.

It's **always** been possible to download these files. After all, that's how you get to listen to them in the first place. What stopped you is [security by obscurity](http://www.google.com/search?q=security+by+obscurity). You didn't know the location where the song was stored, but if you did, you could download them.

So how do you figure out the URL to download the file from?

Let's take a look at [MusicIndiaOnline](http://www.musicindiaonline.com/) first. When you click on a song, it pops up in a new window. You can't figure out the address of that window because the address bar is hidden, but you can get it by hovering over the link before clicking, or by right-clicking and copying the link location. It's always something like this:

<http://www.musicindiaonline.com/p/x/FAfgqz0HzS.As1NMvHdW/>

It always has the same structure: **http://www.musicindiaonline.com/p/x/****something****/.** Let's call that the **something** the song's key.

Now, what this page does is play a .SMIL file. An SMIL file is a text file that has a list of songs to play. This file is always stored at

<http://www.musicindiaonline.com/g/r/FAfgqz0HzS.As1NMvHdW/play2.smil>

(Notice that the key remains the same.) If you type this into your browser, you'll get a text file that you can open in Notepad. You'll find that it has a bunch of lines, two of which are interesting. There's one that reads:

<meta name="base" content="http://205.134.247.2/QdZmq-LL/">

The content="..." part gives you the first part of the song's address. Then there's a line that reads:

<audio src="ra/film/..."/>

The src="..." part gives you the rest of the address. Putting the two together, you have the full URL at which to download the song.

Except, they're a bit smart about it. These songs are meant to be played on RealPlayer, and not downloaded. So if you try to access the page using your browser, you get a 404 Page not found error. But if you typed the same page into RealPlayer, you can hear the song play.

To actually download the song, you need to fool the site into thinking that your browser is RealPlayer. So first, you need to get a good browser like [Firefox](http://www.mozilla.com/). Then download the [User Agent Switcher](https://addons.mozilla.org/en-US/firefox/addon/59) add-on. Change your user agent to "RMA/1.0 (compatible; RealMedia)" and try the same song: you should be able to download it.

Let me summarise:

1. Right-click on the song you want to play, and copy the URL
2. Extract the key. In the URL <http://www.musicindiaonline.com/p/x/FAfgqz0HzS.As1NMvHdW/> the key is FAfgqz0HzS.As1NMvHdW
3. Open http://www.musicindiaonline.com/g/r/<your\_key>/play2.smil in your browser. Open it with Notepad
4. Switch the user agent on your browser to "RMA/1.0 (compatible; RealMedia)"
5. Put the content="..." and audio src="..." pieces together to form the URL
6. Type the URL and save the file

I've automated this in my music search engine. So if you go to the [Hindi](/hindi), [Tamil](/tamil) or any other online music page and click on the blue ball next to the song, you'll see a menu with a download option. The download opens a Java program that does these steps for you and saves the song in your PC.

So now, you're probably thinking:

1. How did he figure this out?
2. What about other sites?
3. How does that Java program work?
4. How do I listen to these on my iPod?

**How did I figure this out?**

[Fiddler](http://www.fiddlertool.com/).

I believe a good measure of a tool's power is it's ability to be the one-word answer to a relatively broad question. For example, "Where can I find more about something?" "Google it." "How do I improve my pictures?" "Photoshop it".

Fiddler's like that. "How do I find out what I'm downloading?" "Use Fiddler".

It's a proxy you can install on your machine. It automatically configures your browsers when you run it. Thereafter, it tells you about all the HTTP requests that are being sent by your machine. So if you patiently walk through the logs, you'll find all the URLs that MusicIndiaOnline or any other site uses, as well as the other headers (like User-Agent) that are needed to make it work.

**What about other sites?**

I'll list a couple here.

[Smashits](http://ww.smashits.com/):

1. Right-click on the song you want to play, and copy the URL
2. View the source and hunt for the URL fragment "player/ra/ondemand/launch\_player.cfm?something".  The key is is something.
3. Open http://ww.smashits.com/player/ra/ondemand/playlist.asp?6;giftsToIndia1.rm;1,something in your browser, using Notepad
4. Switch the user agent on your browser to "RMA/1.0 (compatible; RealMedia)"
5. Type in what's inside the src="..." in your browser and save the file

[Oosai](http://www.oosai.com/):

1. Right-click on the song you want to play, and copy the URL
2. View the source and hunt for the URL fragment onclick="setUsrlist(something)".  The key is is something.
3. Open http://www.oosai.com/oosai\_plyr/playlist.cfm?sng\_id=something in your browser, using Notepad
4. Switch the user agent on your browser to "RMA/1.0 (compatible; RealMedia)"
5. Type in the URL that you see in Notepad and save the file.

Try figuring out the others yourself.

**How does the Java program work?**

It does most of these steps automatically. The applet itself is fairly straightforward, and you can view it [here](/MDownload.java). It takes two parameters: db, which indicates the server from which to download (M for MusicIndiaOnline, S for Smashits, etc.) and num, which is the key.

But in order for an applet to be able to download files from any site, and to be able to save this on your PC, it needs to be a [signed applet](http://java.sun.com/developer/onlineTraining/Programming/JDCBook/signed.html). Since Sun offers a tool to sign JAR files, this wasn't much of an issue.

There is one pending problem with Windows Vista, however. [Signed applets can't save files anywhere on Vista](http://blogs.dekoh.com/dev/2007/11/01/signed-java-applets-broken-on-vista/). They are saved in a special folder. This is [being fixed](http://bugs.sun.com/view_bug.do?bug_id=6548078), but until then, if you use Internet Explorer on Vista, you probably will be unable to find your saved files.

**How do I listen to these on my iPod?**

The saved files are in RealMedia format. Your best bet is to convert them to MP3 files using [MediaCoder](http://mediacoder.sourceforge.net/). Then transfer them using iTunes.

---

## Comments

<!-- wp-comments-start -->

- **Murali** _18 Sep 2008 6:42 am_:
  I have to admit that, I tried and figured out the URL obfuscation. However the\
  user agent add-on switch was the missing bit.\
  \
  The quality of these songs are not good enough to download. Anyways, I'm happy someone hacked the fake security built on these sites :)\
  \
  Did you try it on Raaga and Musicmazza?
- **S Anand** _18 Sep 2008 10:23 am_:
  @Murali: I've tried it on Raaga (it's a bit subtler to crack, given that it uses cookies), but haven't visited Musicmazza so far.
- **Vaidya** _18 Sep 2008 1:02 pm_:
  Anand, this is a great piece of info for music download enthusiasts. However, i think you should put in a word of not supporting such downloads and this is only provided for the sake of learning technology..and the user would do so at his own risk..\
  \
  Your blog is a publicly accessible site and being in UK you may fall under strict purview of anti-piracy rules
- **S Anand** _18 Sep 2008 4:05 pm_:
  @Vaidya: Actually, these songs fall under the purview of the Indian Performing Rights Society (IPRS). You're right in that I may be liable for contributory infringement, but if so, it would be under the jurisdiction of Indian law, not the UK. And I'm not sure if the laws around contributory infringement is well established in India.\
  \
  It's one of those sad things, Vaidya. Something that's this easy to do shouldn't have to be illegal. And yet...
- **aish** _29 Sep 2008 10:54 am_:
  hi anand! been entertaining myself reading through this pot-pourri site of urs amidst surgery & drugs. its fun! esp the calvin series & ur interview series :) cant undertsand most of the tech stuff though, this entry on downloading music included! (i simply go to the other websites with downloadable links :p). hope london's as fun as ever!
- **Pradeep** _7 Oct 2008 3:26 am_:
  Hey, As you have so much experience with the music sites, can u prepare an auto tagging program which can fill missing tags in the songs, i.e. Music: Composer: Artist: Year etc...
- **S Anand** _7 Oct 2008 3:32 am_:
  Oh, I want to Pradeep, believe me! I've been working on that for a while...\
  it might take me a few months to get there, but it's definitely right on top\
  of my priority list.
- **AS151008** _15 Oct 2008 9:48 am_:
  how can i download songs from this site? (www.bongotrax.com)
- **S Anand** _15 Oct 2008 11:38 am_:
  Please visit http://www.s-anand.net/hindi and search for the song you want.\
  Right click on the song and select Download.\
  For other languages, use http://www.s-anand.net/tamil or\
  http://www.s-anand.net/telugu etc.\
  \
  Regards,\
  Anand
- **Satheesh** _16 Oct 2008 8:09 am_:
  But I tried in Raga.com. When copying the link location I am getting the link of page itself. Also I am not getting the ".SMIL" link..... pls help
- **Vanitha** _22 Oct 2008 6:01 am_:
  Hi Anand,\
  \
  Great work! Hats off to you.\
  I have just had a glimpse of ur site. I haven't explored it. But its awesome.\
  \
  Thanks & Regards,\
  Vanitha
- **Selvakumar** _22 Oct 2008 6:24 am_:
  Amazing and so much to learn from your site. I dont think not so many gentlemen like you share their knowledge like you do.\
  Thanks & continue your good work.
- **S Anand** _23 Oct 2008 3:42 am_:
  Thanks a lot, Vanitha.\
  Regards,\
  Anand
- **S Anand** _23 Oct 2008 3:42 am_:
  Thanks a lot, Selvakumar.\
  Regards,\
  Anand
- **Satheesh** _23 Oct 2008 3:58 am_:
  Sir,\
  Whether it's possible in raaga.com.......i tried but I cannot follow ur way...........can u plz explain it using raaga.com as an example......plz
- **satheesh** _23 Oct 2008 11:43 pm_:
  Sir,\
  u r great and u r right. Its worked out with musiconlineindia.com. Thank u very much. But I got the song in .rm format. Can we convert this to .mp3 ?
- **S Anand** _24 Oct 2008 2:20 am_:
  Satheesh, you can download MediaCoder from\
  http://mediacoder.sourceforge.net/ and convert to MP3.\
  Regards,\
  Anand
- **Satheesh** _25 Oct 2008 3:44 am_:
  Sir,\
  Thank u sir, thank u very much........You have done a great help to me............I got many songs and I converted it to mp3 with mediacoder...................It is a great help that u have done to me. I thank u very much.\
  Satheesh. S
- **Junk User** _26 Oct 2008 10:08 pm_:
  Can you figure out a way to find the source of songs at tinysong.com?\
  \
  Their songs are in real high quality.
- **Junk User** _26 Oct 2008 10:10 pm_:
  Why wouldn't you just play the song in MIO and use Audacity if you are anyway converting RM to Mp3 using some program?
- **Murali** _26 Oct 2008 11:59 pm_:
  Thank u so much for your information sir.\
  Really i appreciate your great work.\
  KEEP ROCKING.
- **S Anand** _28 Oct 2008 1:57 am_:
  Thanks a lot, Murali.
- **Prathibha** _29 Oct 2008 4:14 pm_:
  Great!! It works. I tried it to download kannada songs from Kannadaaudio.com. And the song quality is also great. Thats a great work. Thanks Anand.\
  \
  Prathibha
- **Sujay** _30 Oct 2008 6:52 am_:
  Hi Anand,\
  it great that you have found something which is useful. But unfortunately I tried your way on www.oosai.com when I types the http://www.oosai.com/oosai\_plyr/playlist.cfm?sng\_id=2498 no notpad was opening up. So i could not go further. Would you please advice?\
  cheers\
  Sujay
- **Kalpesh** _30 Oct 2008 1:39 pm_:
  Hi Anand,\
  \
  I am a new user to itunes and iPhone.\
  \
  How does 1 arrange music?\
  I have some mp3 files. Do I copy it all to "audio" and then tag all of it individually?\
  \
  Where do I put my podcasts?\
  \
  Is there any website which facilitates hindi mp3 with tags filled in without ambiguity and it has its album art?\
  \
  I know that itunes might have all of this.\
  But who wants to pay 40 bucks for 1 song? ;)\
  \
  When you reply to this comment, please email it to me (I read your blog under bloglines).\
  \
  Thanks for all your efforts.
- **S Anand** _3 Nov 2008 6:23 am_:
  Sujay, that's because Oosai is even simpler than the other sites. The URL\
  http://www.oosai.com/oosai\_plyr/play.cfm?sng\_id=2498 is a direct link to the\
  song itself. You will need to download the song using a user agent of "RMA/1.0\
  (compatible; RealMedia)".
- **Alan** _15 Nov 2008 11:28 pm_:
  say i have a link like this: http://www.angelfire.com/freak3/devin/09\_Tha\_Mot\_Lan\_Dau.wma\
  \
  i'm not sure what happened, but before, whenever i put in a url like that in my web browser, window would pop up asking me if i wanted to save it or open it. but now it saves the file straight into my temp internet files folder and pops up in windows media player so i dont have the option of downloading the song. how can i download it now?
- **S Anand** _16 Nov 2008 4:40 am_:
  @Alan: The easiest way may be to mail yourself the links on your Yahoo or\
  Gmail account. This will convert the URLs into links. You can right-click on\
  the link and select "Save link as" and place it where you wish.
- **Rahul** _26 Nov 2008 9:31 am_:
  Hi Anand,\
  \
  I have downloaded many songs from you blog. Thanks a lot. But I have some songs which I didnot find in the blog and found in Musicindiaonline. I read the article as to how we can download the songs. But I am not able to change the user agent to RMA compatible in mozilla. can you please guide me.\
  \
  I would be very happy if you mail me the steps.\
  \
  Thanks,\
  \
  Rahul
- **Rahul** _29 Nov 2008 5:06 am_:
  Hi Anand,\
  \
  I finally figured out how to change the user agent and downloaded the songs. I am very happy. Thanks for the help.\
  \
  Regards,\
  \
  Rahul
- **bnanjunda** _20 Dec 2008 6:16 am_:
  dear anand sir i requesting\
  \
  sir this is ram I have downloaded many songs from you blog. Thanks a lot & hats off to u . But I have some songs which I didnot find in the blog and found in Musicindiaonline. I read the article as to how we can download the songs sir plz help me how i can get my faverates songs from raga.com & Musicindiaonline plz helpme .. guide me\
  \
  \
  sir i m waiting for u r reply
- **Bharat** _29 Jan 2009 9:24 am_:
  Hi Anand\
  This is an excellent tip to download from musicindi and thank you very much for sharing with all .I manage to open link into mt notepad ,and understood upto content ,however i am having trouble reg src= , i am not sure exaclty what is src= , to copy ,so can you please help me giving example of a link ,i will be very thankful .Thanks again for your contribution Anand .\
  \
  Regards,\
  Bharat
- **S Anand** _29 Jan 2009 9:37 am_:
  Bharath, I'm afraid that doing this would require some working\
  knowledge of programming. You may be better of downloading from my\
  online music sites like http://www.s-anand.net/hindimp3 or by\
  recording songs as they're playing, as described in\
  http://www.s-anand.net/Recording\_online\_songs.html
- **BHARAT** _12 Feb 2009 10:49 am_:
  Hi Anand Finally i am now able to download without any problem from notepad .Also to share with you , i use firefox add-ons download helper which can download any song you play from smashit.com and save file as .mp3.\
  Can you please help me ,how to download from hummaa.com\
  \
  Thanks\
  \
  Bharat
- **S Anand** _13 Feb 2009 5:06 pm_:
  Good to hear that, Bharat. I'm afraid I know nothing of hummaa.com, though.\
  Not sure if I can be of any help.
- **Arti** _2 Apr 2009 1:15 am_:
  Hi Anand,
  Thanks for the wonderful post. I was wondering if you know any application which converts mp3 to rm.
  Thanks
  Arti
- **[S Anand](http://www.s-anand.net/)** _2 Apr 2009 8:32 pm_:
  Try Googling for RealProducer, Arti. That might help convert MP3 to RM
- **Rahul** _4 Aug 2009 1:29 pm_:
  Hi Anand,
  I am not able download the songs of "Bhoothnath" from your blog. Can you help me?
  Thanks in advance.
- **VS** _7 Dec 2009 8:50 am_:
  I am afraid that this kind of trick may not work when the obscured mp3/video/resource is streamed rather than being sent (or stored) as a file from the server. These days this trend is on high. Store your stuff in databases (rather than in file systems), locate and stream it on demand.
  Vikas
- **[Kapil India](http://fun2mobo.servehttp.com)** _13 May 2010 5:22 am_:
  Hi there,
  Simple Alternatives...
  Some time back for english song...I used the wii player skin of Radioblogclub.com online for English Song searching and playing right there no plugin required.
  Also there is a nice search engine for all types of songs bomb-mp3.com with built-in Player support.
  Ensure you have good version updated of Flash 9 or 10 otherwise some songs may be chip-munks.
  For Hindi Songs....I have managed to download all or complete list of songs they have on their site.For More info you can write to me on mysite.
  What if you have all the songs, instead of your choosen songs, just go through complete list and search and play...as your own playlist...links to all mp3 files.
  Simply Simple,
  Kapil [NA Infosy'ite]
- **Rahul** _10 Jul 2010 9:54 am_:
  Hi Anand,
  I am not able to download old movie songs of any language from your music sites. Please help.
  Rahul

<!-- wp-comments-end -->
