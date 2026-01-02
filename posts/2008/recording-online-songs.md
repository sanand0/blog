---
title: Recording online songs
date: "2008-09-21T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 28
---

In the 1980s, we rarely used to buy audio cassettes. It was a lot cheaper to record songs from the radio. It's amazing that in the 2000s, this technique seems to be less used than before.

If you wanted to record a song that was streamed online, you could go through the complex procedures I'd mentioned earlier to [download online songs](/blog/downloading-online-songs/), or you could use the 1980s technologies. Get a tape recorder, connect the headphones of your PC to the tape recorder's microphone using a stereo cable, and record to your heart's content.

Except, of course, that tape recorders are rather outdated. And with the right software, your PC can act like a tape recorder. Here's how you can go about it.

1. [Download Audacity](http://audacity.sourceforge.net/download/) and install it
2. Download [Lame](http://lame.buanzo.com.ar/) and save it
3. Open Audacity and select "Wave Out" as the source
4. [Play a song online](/hindi) and click on the Record button. Press the Stop button when done
5. File - Export as MP3. (The first time, you need to tell Audacity where you've saved Lame)

That's it. You can convert anything your computer plays into an MP3 file. (The general rule in digital media is: if you can see / hear it, you can copy it.)

OK, lets' do this more slowly.

**1. [Download Audacity](http://audacity.sourceforge.net/download/) and install it.**

Audacity is a program lets you record and edit music. Just visit the link above (or search on Google for "Download Audacity") and install the program. This is what it looks like.

[![Audacity](/blog/assets/flickr-audacity_2875838821_o-jpg.webp)](/blog/assets/flickr-audacity_2875838821_o-jpg.webp)

**2. Download [Lame](http://lame.buanzo.com.ar/) and save it**

When you record something with Audacity, you'll usually want to save it as an MP3 file. Lame is another software that lets you do that. Go to the link above, download the ZIP file, and unzip it in some folder. (Remember where you unzipped it.)

**3. Open Audacity and select "Wave Out" as the source**

You can choose which source to record from in Audacity. Do you see the "Line In" in the screenshot below? That's the source from which Audacity will record sound from. Usually, your PC will have a "Microphone" socket, and may have a "Line in" socket. It may also have a built-in microphone. Depending on what sockets and capabilities your PC has, you may see different things.

[![Audacity source](/blog/assets/flickr-audacity-source_2875838825_o-jpg.webp)](/blog/assets/flickr-audacity-source_2875838825_o-jpg.webp)

One of these sources will probably be "Wave Out". That lets you record any sound played by your computer. So if you want to record a song your computer's playing, what's what you should choose.

Not all sound cards have the "Wave Out" option, though. Many laptops that I have used don't seem to have this option. If that's the case with you, there's a fairly simple solution. Just buy a stereo-to-stereo cable (shown below) and connect your headphone socket to your microphone socket.

[![Stereo to stereo cable](/blog/assets/flickr-stereo-to-stereo-cable_2875838813_o-jpg.webp)](/blog/assets/flickr-stereo-to-stereo-cable_2875838813_o-jpg.webp "Stereo to stereo cable by S Anand, on Flickr")

This transfers everything your computer plays back into the microphone, and you can select "External Mic" as your source.

Buying this stereo cable has another advantage. Rather than connect one end to your computer's headphones, you can connect it to anything: your old cassette player, your radio, a microphone, whatever. So that means you can now:

- Convert your old tapes to MP3
- Record songs on the radio as MP3
- Record songs from the TV / DVD player as MP3
- Record live conversations as MP3
- Record phone conversations as MP3
- etc.

**4. [Play a song online](/hindi) and click on the Record button. Press the Stop button when done**

That's easy. The Record button is the red circular button that's third from the left. The Stop button is the yellow square button that's second from the right.

**5. File - Export as MP3**

When you've stopped recording, you can actually do a bunch of useful things with Audacity.

The first is to **adjust the volume level**. Go to the Effect menu and select Amplify. Then you can try different amplification levels to see how it sounds.

The next is to **trim the audio**. Unless you're really fast with the keyboard, you probably have some unwanted sound recorded at the beginning or the end. You can select these pieces by dragging the mouse over the wiggly blue lines, and go to the Edit menu and pick Delete.

Lastly, you'll want to **set the sound quality**. Go to Edit - Preferences and under the File Formats tab, set the bit rate under the MP3 Export Setup section. (If you don't know what rate to put in there, 128 is a safe number. If you want better quality, increase it. If you're short of disk space or want to mail it to someone, decrease it. Based on my [experiments](/blog/mp3-bitrates-and-sound-quality/), even a good ear can't tell the difference at 128. I use 64 or 96. My ear is pretty bad.)

All of the above was optional. If you just wanted to save the file, go to the File menu and select "Export as MP3". The first time you do that, you'll be asked to mention the folder where you saved lame\_enc.dll (which is where you unzipped Lame.) Show Audacity the folder, and that's it.

---

## Comments

<!-- wp-comments-start -->

- **Vivetha** _26 Sep 2008 4:03 am_:
  Hai Anand,\
  \
  Thanks lot for your technical supports and guidlines. Still I couldn't able to understand what have to do for recording my skype conversation. Can you help on this?\
  \
  I use Acer 2413 laptop which has one headphone port and another microphone port. I have Stereo to Stereo to cable. Can you tell me what the next step to proceed for recording Skype conversation, and next for recording online songs?\
  \
  Thanks & Regards\
  Vivetha\
  Madurai
- **S Anand** _26 Sep 2008 12:51 pm_:
  @Vivetha: This link explains how to record Skype conversations:\
  http://www.voip-sol.com/15-apps-for-recording-skype-conversations/
- **Preet** _27 Sep 2008 10:12 pm_:
  Hello Anand,\
  \
  Thank you for the updates.\
  Can it download all Online songs from all sites?\
  The Lame site says as follows: "Once you have unzipped the archive, you will have a file called LameLib or libmp3lame.dylib"\
  However after downloading I am not getting the above files in the zip folder. There are 2 notepad files and one dll files in the zip folder.\
  Could you please advise me what to do next.\
  Thanks and Rgds,\
  Preet\
  Chennai
- **Preet** _28 Sep 2008 3:39 am_:
  Also Anand one more help...\
  \
  The wave out option is not appearing in the Audacity version 1.2.6 which I downloaded.\
  Thanks and Rgds,\
  \
  Preet\
  Chennai
- **S Anand** _28 Sep 2008 4:48 am_:
  @Preet: You need to copy the DLL file (lame\_enc.dll) to your C:\Windows\system32 folder. (Or any other folder would be fine, as long as you remember to tell Audacity where the file is.\
  \
  If "Wave Out" does not appear as an option, your sound card doesn't support that option. Your only option is to use the stereo cable.
- **Ashwani** _18 Nov 2008 4:54 am_:
  hi anand\
  thanx for ur support\
  i have a proble, no any option highlighted in ''SELECT COURCE'' area\
  \
  plz told me solution\
  here i see recordind & save that but without sound\
  \
  Thanx & rtegards,\
  \
  Ashwani Shukla
- **ssr** _3 Dec 2008 2:14 am_:
  how to download songs from www.devotionalsongs.com\
  It is a challenging job?
- **&gt;kk;** _9 Dec 2008 9:58 am_:
  hi anand,\
  great site and very helpful.\
  My sound card does not support "Wave Out" so i bought a stereo-to-stereo cable, exactly as the pic you've put.\
  After connecting the ends to my headphone and mic slots, i tried to record, but no positive results.\
  The options shown by audacity both before and after plugging in the cable are "Front mic, Mic Colume, CD Volume, Line Volume".\
  I've got a Logitech webcam,which is the "Front mic" i think, and it does record my voice when i record after chosing that as the option.\
  How do i go about recording playback of whatever songs i play on my PC using audacity using the cable ?\
  Any help is greatly appreciated. (....u're on vacation..)\
  keep up the good work !!\
  -kk
- **S Anand** _9 Dec 2008 8:35 pm_:
  KK, try plugging the cable into each slot (line out / mic) and try all\
  options: "Front mic", "Mic Volume", etc. I usually do this hit-and-miss, and\
  something eventually works.
- **tk** _29 Jan 2009 10:59 am_:
  Hey\
  \
  My audacity doesn't even have that drop down menu. Its just a gray box...any ideas?\
  \
  Thanks
- **S Anand** _31 Jan 2009 5:57 am_:
  In that case, the sound card probably doesn't support it. I'm afraid\
  you may have to do it the old-fashioned way: play it on one computer,\
  connect the headphone socket to another computer's mic socket, and\
  record it on the second computer.
- **swapna** _6 Mar 2009 12:32 pm_:
  Hi,
  Am Indian classical Music singer . I would like to sing and record my songs which people must be able to listen it on internet. Can you please tell me how it is possible .
  Thanks
- **[S Anand](http://www.s-anand.net/)** _6 Mar 2009 2:25 pm_:
  Swapna, just record your songs on to a tape recorder. Then connect its headphone socket to a PC's mic socket. Install Audacity and select "Microphone" or "Line in" as the source. Play the tape and press the red record button. When done, press the stop button and save the file from Audacity. You can upload the file to sites like odeo.com
- **Purushothaman** _8 Mar 2009 1:38 pm_:
  Hi,
  How can I record the conversations and online-music class in skype?
- **[S Anand](http://www.s-anand.net/)** _8 Mar 2009 4:06 pm_:
  Here are some ways of recording Skype conversations: http://www.voip-sol.com/15-apps-for-recording-skype-conversations/
  I haven't tried any of them myself. If they fail, you could always download Audacity, select "Wave Out" as your input and press the Record button during the class.
- **[S Anand](http://www.s-anand.net/)** _23 Mar 2009 7:44 am_:
  This might be because MusicIndiaOnline is down. That's where I'm getting this songs from, ultimately. It's a pity that MusicIndiaOnline is down quite frequently these days. Could you please try again when their site is up?
- **Valavan** _23 Mar 2009 12:16 am_:
  Hi Anand,
  I'm unable to download the songs of "Dance of Shiva" by Sudha Raghunathan from your website s-anand.net/carnatic. I'm using latest ver of firefox. I'm getting the error "Couldn't match M in" after saving the file name in local disk. I tried in i.e. 8 also and got the same error. Please help me in downloading the songs.......
- **[Kapil India](http://Hindiwapsite)** _13 May 2010 5:17 am_:
  Ahaan...why record that way ... simply using windows Sound Recorder and double clicking Volume Icon in taskbar with Recording Device selected as Stereo Mix will do the job and by default it can support mp3 at 56Kbps or else download Lame or other Mp3 encoders and use it in sound record...also some WinAmp Plugin will do that for you too.
  Simple
  Kapil

<!-- wp-comments-end -->
