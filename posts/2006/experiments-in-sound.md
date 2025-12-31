---
title: Experiments in sound
date: "2006-09-12T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 224
---

Wikipedia says the human [voice frequency](http://en.wikipedia.org/wiki/Voice_frequency) for speech is between 85 to 155 Hz for men, and 165 to 255 Hz for women. That set me thinking.

1. What is the limit to our hearing?
2. How do sounds differ?
3. How can we synthesise speech?

**What are the limits to our hearing?**

Kids can hear frequencies from 20 Hz to 20 kHz, while adults hear only up to 12-14 kHz ([Frequency Range of Human Hearing](http://hypertextbook.com/facts/2003/ChrisDAmbrose.shtml)).

To check the lower frequency limit, I created an MP3 with [sounds from 1 Hz to 100 Hz](/blog/assets/lower.mp3) at 1 second intervals. Just play the sound, and see when you **start** hearing something. (Of course, whether you can hear something also depends on the volume of your speaker, the ambient noise, etc.) I could hear nothing for the first 40 seconds: so I can't hear frequencies lower than 40 Hz.

**PS: Don't be worried if you don't hear anything for a while. You're not supposed to!** Keep the volume at full level, though.

To check the upper frequency limit, I created this MP3 with [sounds from 1 kHz to 20 kHz](/blog/assets/upper.mp3) in 1 second intervals. Just play the sound, and see when you **stop** hearing anything. I couldn't hear anything beyond 14 seconds: so I can't hear frequencies beyond 14 kHz.

**How do sounds differ?**

I took this [audio file of someone reciting vowels](/blog/assets/vowels.mp3) and plotted a spectrogram (below). A [spectrogram](http://www.google.com/search?q=define%3Aspectrogram) plots time on the X axis and frequency on the Y-axis.

[![Vowels spectrogram](/blog/assets/flickr-vowels-spectrogram_241586415_o-jpg.webp)](/blog/assets/flickr-vowels-spectrogram_241586415_o-jpg.webp)

Some observations:

- All the vowels have evenly spaced bars. (In this case, they're all multiples of something around 120 Hz.)
- 'u' has the lowest frequency mix. 'a' spans from low to high. 'i' has a bit of low and a bit of high, nothing in the middle. 'ai' and 'au' look like 'a' followed by 'i' and 'u' respectively.

**How can we synthesise speech?**

I don't know. There are lots of speech synthesizers. They sound robotic. I'm trying to see if knowing what sounds look like improves things. I'll let you know if I do well.

---

## Comments

<!-- wp-comments-start -->

- **Dhar** _13 Sep 2006 5:09 am_:
  How did you go about synthesizing the MP3s with increasing frequencies? Did you use some software for that? Similarly what software did you use to plot the spectrogram?
- **S Anand** _13 Sep 2006 6:10 am_:
  I wrote a [perl script to generate the frequencies](http://www.s-anand.net/a/sound), and [Spectrogram v.0.8](http://www.hitsquad.com/smm/programs/SPECTROGRAM/) to create the spectrograms.
- **Sumit Dhar** _16 Sep 2006 9:23 am_:
  Dude, just downloaded the files. Is the sound stereophonic or monoaural? If it is mono, do you think creating an MP3 with stereophonic sound will make a difference? Cheers, D.
- **Sumit Dhar** _16 Sep 2006 9:25 am_:
  Loved the experiment. Lower: 42 Hz, Higher: 15 KHz
- **S Anand** _16 Sep 2006 9:38 am_:
  It's mono. I doubt if stereo would make a difference. I'd be playing the same frequency on both speakers, which is what a mono MP3 does anyway.
- **Dhar** _17 Sep 2006 2:05 am_:
  The reason I asked about whether the sound is Mono or Stereo is because of my experience during eye tests. Some letters that were not visible when viewed with just **one** eye, were clearly readable when using both eyes. Was wondering if the same **may** be applicable in this case?
- **S Anand** _17 Sep 2006 7:36 am_:
  Ah, I see what you mean. Since both speakers would be playing the sound, hopefully this should not be a factor.

<!-- wp-comments-end -->
