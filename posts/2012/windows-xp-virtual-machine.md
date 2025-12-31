---
title: Windows XP virtual machine
date: "2012-09-16T09:05:50Z"
lastmod: "2012-09-18T04:07:07Z"
categories:
  - coding
wp_id: 2799
---

Here’s the easiest way to set up a Windows XP virtual machine that I could find.

(This is useful if you want to try out programs without installing it on your main machine; test your code on a new machine; or test your website on IE6 / IE7 / IE8.)

1. Go to the [Virtual PC download site](http://www.microsoft.com/windows/virtual-pc/download.aspx). (I tried [VirtualBox](https://www.virtualbox.org/) and [VMWare Player](http://www.vmware.com/products/player/). Virtual PC is better if you’re running Windows on Windows.)\
   [![image](/blog/assets/image1.webp "image")](/blog/assets/image1.webp)\
   **If you have Windows 7 Starter or Home**, select "Don’t need XP Mode and want VPC only? Download Windows Virtual PC without Windows XP Mode."\
   **If you have Windows Vista or Windows 7**, select “Looking for Virtual PC 2007?”
2. Download it. (You may have to jump through a few hoops like activation.)
3. Download [Windows XP](http://www.microsoft.com/en-us/download/details.aspx?id=11575) and run it to extract the files. (It’s a 400MB download.)
4. Open the “Windows XP.vmc” file – just double-clicking ought to work. At this point, you have a working Windows XP version. (The Administrator password is “Password1”.)
5. Under Tools – Settings – Networking – Adapter 1, select “Shared Networking (NAT)”\
   [![image](/blog/assets/image2.webp "image")](/blog/assets/image2.webp)

That’s pretty much it. You’ve got a Windows XP machine running inside your other Windows machine.

**Update (18 Sep 2012)**: I noticed something weird. The memory usage of VMWindow and vpc.exe is **tiny**!

[![image](/blog/assets/image3.webp "image")](/blog/assets/image3.webp)

Between the two processes, they take up less than 30MB of memory. This is despite the Windows XP Task Manager inside the virtual machine showing me 170MB of usage. I’ve no clue what’s happening, but am beginning to enjoy virtualisation. I’ll start up a few more machines, and perhaps install a database cluster across them.

---

## Comments

<!-- wp-comments-start -->

- **Vivek T** _16 Sep 2012 6:53 pm_:
  I agree that Virtual PC is the easiest to use. However, Microsoft has stopped all development on it for about 2 years now. We use Virtualbox since it's open-source and provides access to virtually all USB devices connected to the host and also provides 2D & 3D graphics acceleration.
- **Fuu** _9 May 2013 11:42 pm_:
  how do you download windows xp.vmc file?

<!-- wp-comments-end -->
