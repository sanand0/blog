---
title: Software for my new laptop
date: "2006-09-26T12:00:00Z"
lastmod: "2021-12-07T08:28:06Z"
categories:
  - top-10-lists
wp_id: 199
---

And so, thanks to Infosys Consulting being spun off as a separate legal entity in the UK, I got my new laptop. (Because our old laptops were legally the assets of Infosys Technologies Ltd, and not Infosys Consulting Inc. Weirder things have happened, but who's complaining?)

My old [Toshiba Portege A200](http://www.google.com/search?q=Toshiba+Portege+A200) has been replaced by a [Dell Latitude D420](http://www.google.com/search?q=dell+latitude+D420) (which I was dreaming for, after having just read [Jeff's post on big laptops](http://www.codinghorror.com/blog/archives/000685.html)).

[![Dell Latitude D420](/blog/assets/flickr-dell-latitude-d420_252330198_o-png.webp)](/blog/assets/flickr-dell-latitude-d420_252330198_o-png.webp)

Firstly, it's **light**. I thought my Toshiba was light compared to the Dell monsters others had, but this weighs 1.4 kgs! Secondly, it's **thin**. It's thinner than some of the paper notebooks I used to carry. It's hard to imagine where we will be in 5-7 years time if innovations keep rolling in at this rate.

There were only two (minor) problems I saw with it. It didn't have an S-Video port -- so I can't watch movies on TV. And it had a fairly small (12") screen. Being a wide screen, I get a lot less height than I used to. I'm still having some trouble getting used to that, especially when browsing tall pages but it's a good laptop for playing games such as [올인구조대](https://floorballontario.com).

My weekend was like a kid in a candy store. Here's what I did.

**Uninstalled useless software**: The laptop came with [Roxio Easy CD Creator 5 Basic](http://www.roxio.com/) and [PowerDVD 5.1](http://www.cyberlink.com/multi/products/main_1_ENU.html). I got rid of them.

**Copied all my files**: I had about 25GB of data (15GB of music, 5 GB of books, 2 GB of video, 3GB of work). This was a bit tricky: some of my data was in [SVN](http://subversion.tigris.org/) repositories, and I had to [migrate them](http://dotnot.org/blog/archives/2005/01/13/move-a-subversion-repository-from-one-machine-to-another/).

**Configured the new system** by literally running through each entry in the control panel, and ensuring that it's the same as my old machine. Most of my changes are spartan (aimed at less eye-candy, usually). For example,

- **Display**: I switch to Windows Classic and a black background. I used to do this because it takes less memory, but with 1GB of RAM, that's no longer a consideration. I just got used to this. I also turn off all special effects, and remove everything except the Recycle Bin from my desktop. But the really useful thing is to [turn on ClearType](/blog/assets/flickr-display-settings_252330202_o-png.webp).
- **Taskbar and Start Menu**: I switch to the Classic Start Menu, and turn off everything. Here's what mine looks like now.[![Start Menu settings](/blog/assets/flickr-start-menu-settings_252330205_o-png.webp)](/blog/assets/flickr-start-menu-settings_252330205_o-png.webp)
- **Toolbars**: I like my toolbars to fit on one line. So I do some heavy customisation with the [Internet Explorer toolbar](/blog/assets/flickr-ie-toolbar-settings_252330204_o-png.webp) to shrink it to a line. Similarly on the [desktop toolbars](/blog/assets/flickr-desktop-toolbar-settings_252330208_o-png.webp).

**Installed software**. This is the fun part. I've made a number of changes to [my software inventory](/blog/software-inventory/).

- [ActivePerl](http://www.activestate.com/activeperl/): Perl is the only language I still know.
- [ActivePython](http://www.activestate.com/activepython/): I'm learning Python. I'm not impressed, but the [Python Image Library](http://www.pythonware.com/products/pil/) makes [jigsaw quizzes](/blog/movie-jigsaw-quiz-1/) easier than in Perl.
- [Apache HTTP server](http://httpd.apache.org/): To test this web page locally.
- [Audacity](http://audacity.sourceforge.net/): To record and convert sounds. I've ditched [Goldwave](http://www.goldwave.com/).
- [Camstudio](http://www.google.com/search?q=camstudio): To capture screen sessions.
- [Crimson Editor](http://www.crimsoneditor.com/): I'm still trying to [pick a good text editor](http://wikipedia/wiki/Comparison_of_text_editors). (I need block operations, filtering, regular expressions and syntax highlighting. No editor seems to offer all of these. Filtering is especially rare.)
- [Cygwin](http://www.cygwin.com/): Just for the basic tools (head, tail, less). [UnixUtils](http://unxutils.sourceforge.net/) would do just fine, actually.
- [DX-Ball 2](http://www.ldagames.com/dxball2/): The only game I play other than Solitaire, Minesweeper and Age of Kings.
- [Google Desktop](http://desktop.google.com/): I can't live without it any more.
- [Google Earth](http://earth.google.com/): I find [Google Maps](http://maps.google.com/) faster and better (because of the street maps).
- [Google Toolbar for IE](http://toolbar.google.com/): It practically replaces my address bar.
- [ImgBurn](http://www.imgburn.com/): I'm trying it instead of Nero. Except for multi-session support, it's great.
- [Microsoft Reader](http://www.microsoft.com/reader/default.mspx): I have a lot of books in the .LIT format
- [Mozilla Firefox](http://www.mozilla.com/firefox/): Mainly for its extensions ([Google Suggest](http://www.google.com/tools/firefox/suggest/), [NextPlease](https://addons.mozilla.org/firefox/390/), [Tab Mix Plus](https://addons.mozilla.org/firefox/1122/), [Google Bookmarks Button](https://addons.mozilla.org/firefox/2453/), [Extended Statusbar](https://addons.mozilla.org/firefox/1433/), [IE Tab](https://addons.mozilla.org/firefox/1419/), [Live HTTP Headers](http://livehttpheaders.mozdev.org/), [Web Developer](https://addons.mozilla.org/firefox/60/))
- [Paint.NET](http://www.getpaint.net/): Quicker than Photoshop. Mostly I just crop images.
- [Picasa](http://picasa.google.com): Adequate for viewing photos.
- [Powertoys for Windows - TweakUI](http://www.microsoft.com/windowsxp/downloads/powertoys/xppowertoys.mspx): To make Windows even more spartan.
- [Restoration](http://www.aumha.org/a/recover.php): Can restore permanently deleted files.
- [Subversion](http://subversion.tigris.org/): I like the version numbers (1, 2, 3, ...) better than CVS' (1.1, 1.1.1, 1.1.1.1, ...).
- [VirtualDub](http://www.virtualdub.org/): Mainly to convert videos from my digicam to DivX.
- [VLC player](http://www.videolan.org/vlc/): When all else fails, I turn to VLC.
- [WinAmp](http://www.winamp.com/): with [Media Library import/export](http://forums.winamp.com/showthread.php?s=&threadid=155680#b4s) and [Pepper](http://www.winamp.com/plugins/details.php?id=91119)
- [WinRAR](http://www.rarlab.com/): For the occasional .rar download

And finally, after reinstalling my SVN repository and copying my WinAmp playlists, Firefox bookmarks, etc, my new laptop feels as good as old.

---

## Comments

<!-- wp-comments-start -->

- **Somnath** _27 Sep 2006 4:03 am_:
  How do you have admin rights our laptop? Most companies IT security policy means no admin rights on your machines (laptops or desktops).
- **S Anand** _27 Sep 2006 7:08 am_:
  Oh yes, thankfully! I can install pretty much anything, and the only issue is that these won't be "supported" by our IT team. (But in reality, they're actually thrilled to support these, when called :-)
- **Somnath** _3 Oct 2006 3:30 am_:
  One definitely good reason to work for Infy Consulting then ;-)
- **Michelle** _5 Dec 2006 12:38 pm_:
  Please tell me there is literature of non-fiction in 1977. Except for MOVIES!
- **Anand** _8 Jan 2007 6:59 pm_:
  Do you plan to embrace Windows Vista when it is released later this month ? Also I recommend the Firefox extension Colorful Tabs. It is pretty
- **S Anand** _15 Jan 2007 8:16 pm_:
  Guess I don't have a choice about Vista. If Infosys upgrades, I upgrade.
- **Anonymous** _3 Apr 2007 3:58 pm_:
  I have also reently swicthed to D420. I can't get it to record on audacity (or anything else). Previous Dell laptop was fine. Any suggestions
- **S Anand** _3 Apr 2007 4:19 pm_:
  I'm able to record using the Microphone on Audacity. But on my Toshiba, I was able to record what I was playing on the speaker as well, and that's not possible on D420, thanks to the sound card. Also, the hard disk is incredibly slow.
- **Rockey Nebhwani** _11 Jan 2010 4:02 pm_:
  I would like to see the revised list of softwares on your laptop :-)
- **[Software for my new laptop 2 | s-anand.net](http://www.s-anand.net/blog/software-for-my-new-laptop-2/)** _27 Sep 2011 7:15 pm_ _(pingback)_:
  [...] for my new laptop 2 September 27th, 2011 Top 10 lists S Anand Time for a new laptop, and to replace software. Here’s my new [...]
- **[Software I currently use | s-anand.net](http://www.s-anand.net/blog/software-i-currently-use/)** _9 May 2014 6:23 pm_ _(pingback)_:
  […] Every few years, I review the software I use. Here are some of my earlier lists. […]

<!-- wp-comments-end -->
