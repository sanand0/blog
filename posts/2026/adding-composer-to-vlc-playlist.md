---
title: Adding Composer to VLC Playlist
date: 2026-10-03T16:37:14+08:00
categories:
- coding
- llms
---

[VLC 3.0](https://images.videolan.org/vlc/releases/3.0.24.html), there's a Playlist view that can show the title, album, etc.

![](https://files.s-anand.net/images/2026-10-03-vlc-3-playlist.avif)

But the [Composer](https://docs.mp3tag.de/mapping/#composer) field is [not supported](https://github.com/videolan/vlc/blob/6de05adcbaf2e8b85fe86aad4169393098628119/modules/gui/qt/components/playlist/sorting.h#L33-L45). That's a big deal for me. I track composers for ~1,200 Tamil, Hindi, and Telugu songs in that field. I _really_ need to see and sort and filter by composer.

("Really need" like I "really need a cheesecake", not like "really need a charger".)

Software's so easy to change, so [I asked ChatGPT](https://chatgpt.com/share/6ac0c700-971c-83ec-8a4e-7d19a9bd170a):

<!-- Build VLC Album Artist Support: https://chatgpt.com/c/6ac08dda-38fc-83ec-950e-f514ddb20e8a (2026-10-03T16:35:55+08:00) -->

> Fork and clone `sanand0/vlc`, check out `3.0.24` and add **Album Artist** as an optional playlist column. Keep it minimal.

After fixing one error, this worked, except that I didn't know the [Album Artist](https://docs.mp3tag.de/mapping/#musicbrainz_albumartistid) is different from [Composer](https://docs.mp3tag.de/mapping/#composer). So:

> Which of the songs have an album artist? Many have a composer.
> Is it possible to display the composer in VLC?

It told me to add Composer. I told it to add Composer instead of Album Artist, and had a few iterations:

> How can I run a binary directly in my Ubuntu host instead of via Docker?

> Is there a clean, portable way of installing what's required?

> Give me the (minimal) commands I should run to install.

> How should I commit these?

That gave me [two commits](https://github.com/videolan/vlc/compare/3.0.24...sanand0:vlc:vlc-3.0.24-composer) and a working VLC with the Composer field!

![](https://files.s-anand.net/images/2026-10-03-vlc-3-composer.avif)

---

This is the version I'm using now.

The ability to tweak a daily-use software with 15 minutes of supervision in a language I don't know feels really powerful!
