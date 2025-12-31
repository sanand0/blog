---
title: Ubuntu 8.10 on a Dell Latitude D420
date: "2009-01-15T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 17
---

Here's the fastest way I've found to install Ubuntu on a USB flash drive, for my Dell Latitude D420. ([Pendrivelinux.com](http://www.pendrivelinux.com) is a great resource for this sort of thing.)

**Ingredients**

1. One large USB flash drive [like this one](http://www.amazon.co.uk/exec/obidos/ASIN/B001E97G6C). Not less than 4GB. I'd suggest 8GB or more
2. One CD (not a DVD)
3. [Ubuntu 8.10 desktop](http://releases.ubuntu.com/releases/8.10/ubuntu-8.10-desktop-i386.iso) CD ISO
4. [IMGBurn](http://www.imgburn.com/) or any other CD burning software
5. Direct Internet via LAN cable (without proxy, without wireless)

**[Installation](http://www.pendrivelinux.com/ubuntu-810-install-using-the-built-in-usb-installer/)**

1. Burn the Ubuntu ISO file on the CD
2. Press F12 when the laptop boots up, and select CD/DVD Drive as the boot device
3. On the Ubuntu splash screen, select "Try Ubuntu without making any change to your computer" and wait
4. Insert the flash drive
5. Go to System > Administration > Create a USB startup disk and follow instructions there
6. Once done, remove the CD and reboot using the USB flash drive (pressing F12 during the boot sequence)

**To enable wireless**, which won't work by default

1. Connect to the Internet using a LAN cable
2. Go to System > Administration > Hardware devices
3. Select the Broadcom LAN driver, and activate it

That's it. It's been a fairly painless installation.

I do have one big crib. I planned to use Hibernation (or suspend-to-disk on Ubuntu) to switch between Windows and Ubuntu. But there are a couple of problems:

- Hibernate doesn't work on Ubuntu. I need to reboot Ubuntu every time, and that takes 3 minutes
- When Windows is hibernating, Ubuntu can't access any files on the hard disk

This means switching between Ubuntu and Windows is roughly a 6 minute shutdown-one-OS-reboot-the-other process rather than the 1-minute hibernate-one-OS-resume-the-other that I had had hoped for.

Another minor problem I have is that our Exchange server doesn't seem to have an IMAP interface, at least that I know of. So I can't check mail. But like I said, it's minor. I just forward mails from my BlackBerry to GMail.

---

## Comments

<!-- wp-comments-start -->

- **deeaycee** _19 Jan 2009 10:50 am_:
  Your post is how I got my wireless working. Thank you.\
  I'm also using a Dell D420. I have 8.10 on a 8g Attache flash drive. I ran into a problem while updating. I'm stuck at kernel 2.6.27-7 and it should be updating to 2.6.27-11. The error it gives has something to do with running from a live-cd. After some research, I found that there is a bug that prevents solid updates from the live-cd. The work-around is to actually do a real install to the flash drive from the live-cd. This presents another problem/bug. The only way to see the flash drive during the install is to disconnect the hd, so the install prg doesn't see it. It was suggested to physically disconnect the hd, but I wonder if it could be done temporarily through the bios. I'll try this later today. I haven't even thought about the hibernation/suspend issues yet. Good luck!
- **[ActionParsnip](http://www.bmezine.com)** _30 May 2010 10:22 pm_:
  orks 100% OOTB with Ubuntu Lucid.

<!-- wp-comments-end -->
