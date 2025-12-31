---
title: Automated image enhancement
date: "2010-11-22T12:10:38Z"
categories:
  - coding
  - how-i-do-things
wp_id: 2557
---

There are some standard enhancements that I apply to my photos consistently: auto-levels, increase saturation, increase sharpness, etc. I’d also read that [Flickr](http://www.petapixel.com/2009/05/19/sharpening-your-photos-like-flickr/) [sharpens](http://colorspretty.blogspot.com/2007/01/flickrs-dirty-little-secre_117020899505299548.html) uploads (at least, the resized ones) so that they look better.

So last week, I took 100 of my photos and created 4 versions of each image:

1. The base image itself ([example](http://www.s-anand.net/phototest/048-base.jpg))
2. A sharpened version ([example](http://www.s-anand.net/phototest/048-sharpen.jpg)). I used a sharpening factor of 200%
3. A saturated version ([example](http://www.s-anand.net/phototest/048-saturate.jpg)). I used a saturation factor of 125%
4. An auto-levelled version ([example](http://www.s-anand.net/phototest/048-autocontrast.jpg))

I created a [test](http://www.s-anand.net/phototest/) asking people to compare these. The differences between these are not always noticeable when placed side-by-side, so the test flashed two images at the same place.

After about 800 ratings, here are the results. (Or, [see the raw data](https://spreadsheets.google.com/ccc?key=0Av599tR_jVYgdEtmeWNMYUNFamNWZ05oaEQ5NXd6b1E&hl=en_GB).)

**Sharpening clearly helps**. 86% of the sharpened images were marked as better than the base images. Only 2 images ([base](http://www.s-anand.net/phototest/000-base.jpg)/[sharp](http://www.s-anand.net/phototest/000-sharpen.jpg), [base](http://www.s-anand.net/phototest/012-base.jpg)/[sharp](http://www.s-anand.net/phototest/012-sharpen.jpg)) received a consistent feedback that the sharpened images were worse. (I have my doubts about those two as well.) On the whole, it seems fairly clear that sharpening helps.

**Saturation and levels were roughly equal, and somewhat unclear**. 69% of the saturated images and 68% of auto-levelled images were marked as better than the base images. And almost an equal number of images (52%) showed saturation as being better than the auto-levelled version. For a majority of images (60%), there’s a divided opinion on whether saturation was better than levelling or the other way around.

On the whole, sharpening is a clear win. When in doubt, sharpen images.

For saturation and levelling, there certainly appears to be potential. 2 in 3 images are improved by either of these techniques. But it isn’t entirely obvious which (or both) to apply.

Is there someone out there with some image processing experience to shed light on this?

---

## Comments

<!-- wp-comments-start -->

- **[Jason](http://www.flickr.com/photos/yorkjason/)** _14 Feb 2011 11:27 am_:
  Depending on your settings in Photoshop (i assume that's what you're using since you refer to it as "levels"), when you adjust levels to increase contrast (when either the left or right sliders are moved toward each other), the saturation is also increased. You can click "preserve tones" or something like that, to help keep the saturation unchanged but I don't due to some reason I can't recall right now.
  Anyway, so when you hit Auto-Levels, it moves the sliders closer toward each other (since they start out farthest away from each other). This increases the contrast and ALSO increases the saturation. You'll also notice this effect with the dodge/burn brushes: the saturation is also effected in the applied area. Now, your test results seem similar between the 'levels' group and the 'saturation' group because both groups are seeing photos with saturation increases.
  Note that the converse is not true: changes made only to saturation do not yield a change in contrast. The fact that hues will now stand out more from each other sorta gives the affect of "contrast" in a sense though, even if it isn't reflected accurately in the histogram.
  I would still expect people to prefer the photos with Auto-Levels applied, since those photos will have greater detail and less of a hazy look in the mid-ranges, but whatever. People are hard to predict. I prefer the auto-leveled photos over the saturated photos. In fact, I almost always adjust levels, and when I do, I often decrease saturation a tiny bit depending on the subject.
- **S Ganesh** _6 Mar 2011 3:44 am_:
  Sharpening is always better because it is non-destructive in nature and does not add any new details unlike the the saturation and levels.
  In a way it is illusory but it works. It basically works on the edges and emphasize them. Internally, it can be assumed as a 2 step process, the first step is to blur the image slightly and the second step is to compare the original with blur version one pixel at a time & emphasize them. If original pixel is brighter than the blurred version, then lighten; if original is darker than the blur version, then darken. The objective is to increase the contrast between each pixel and its neighbours...
  Sharpening works well on images that has slight blur originally, inherently due to the way in which pictures are taken... casually on the move, non-sturdy hands etc... Hence, it appears to work on most of the pictures
  Advanced photo editing tools provide feature called Unsharp Masking, where it is possible to control the 'radius' - amount of blur and 'Threshold' - difference in value between original and blur when it exceeds certain value sharpening is applied...

<!-- wp-comments-end -->
