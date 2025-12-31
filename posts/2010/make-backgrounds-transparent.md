---
title: Make backgrounds transparent
date: "2010-04-28T06:57:37Z"
categories:
  - coding
  - how-i-do-things
wp_id: 2510
---

This is the simplest way that I’ve found to make the background colour of an image transparent.

1. [Download GIMP](http://portableapps.com/apps/graphics_pictures/gimp_portable)
2. Open your image. I’ll pick this one:\
   [![](/blog/assets/killme1.webp)](/blog/assets/killme1.webp)
3. Optional: Select Image – Mode – RGB if it’s not RGB.
4. Select Colors – Colors to Alpha…\
   [![](/blog/assets/killme2.webp)](/blog/assets/killme2.webp)
5. Click on the white button next to “From” and select the eye-dropper.[![](/blog/assets/killme3.webp)](/blog/assets/killme3.webp)
6. Pick the green colour on the image, and click OK\
   [![](/blog/assets/killme4.webp)](/blog/assets/killme4.webp)

The anti-aliasing is preserved as well.

---

## Comments

<!-- wp-comments-start -->

- **Vinu** _28 Apr 2010 11:21 pm_:
  There is a tool in MS Office products (Word, Excel, PowerPoint) to set the transparent color as well, assuming of course that you plan to embed the image in a document...
- **[S Anand](http://www.s-anand.net/)** _29 Apr 2010 7:19 am_:
  Need to use the image in web pages, mostly. Would this MS Office tool still work?
- **[S Anand](http://www.s-anand.net/)** _29 Apr 2010 7:20 am_:
  True, Ravi. I need to automate this task, though. Tried ImageMagick at first, but gave up after a while.
- **Vinu** _30 Apr 2010 5:51 pm_:
  Good question. If you use a drag and drop, WYSIWYG web page editor, then perhaps it will translate. I tested it between Powerpoint & Word and it worked.
  Here's the location of the control on PowerPoint 2007: on the Picture Tools /Format ribbon> Recolor (in the Adjust group, first from the left) drop down to "Set Transparent Color'.
  Keyboard accelerator = Alt + J P E S.
- **[Atluri](http://www.raviatluri.in)** _28 Apr 2010 3:59 pm_:
  This works well only for text and images with strong contrast against their background
  text as an image is outdated ;)
  and for images i would use blend->merge->eraser for edges!
- **[Vipul](http://bit.ly/vipulrawal)** _13 May 2010 5:31 am_:
  Remove background option in MS-PowerPoint 2010 works even better. In love with that feature. :)

<!-- wp-comments-end -->
