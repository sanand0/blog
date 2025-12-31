---
title: Designing Complex Shapes in PowerPoint
date: "2021-04-18T04:26:11Z"
lastmod: "2021-04-18T04:26:14Z"
categories:
  - how-i-do-things
wp_id: 3117
---

![Designing Complex Shapes in PowerPoint](/blog/assets/image-28.webp)

I use PowerPoint instead of Adobe Illustrator or Sketch. I'm familiar with it, and it does everything I need.

One of the features I'm really excited by in PowerPoint is the ability to manipulate shapes.

![](/blog/assets/image-19.webp)

Let's say you have a rectangle and a circle. You can select both of these shapes and in the Shape Format > Merge Shapes dropdown, you can:

- merge them with a **union**
- **combine** them (like an XOR operation in Boolean algebra)
- **fragment** them, which breaks them up into pieces
- **intersect** them
- **subtract** them

This is so powerful that you can create any kind of shape. Let's take an icon from [Font Awesome](https://fontawesome.com/) at random -- say an [address card](https://fontawesome.com/icons/address-card) -- and create it.

![](/blog/assets/image-21.webp)

Here's the video of the process. I'll explain it step-by-step below.

<div class="video-embed"><iframe src="https://www.youtube.com/embed/Kwa0N5M-3ag" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

First, let's take a screenshot of this and copy it into PowerPoint.

![](/blog/assets/image-23.webp)

Now let's draw over this. So we'll start with a rounded rectangular box with the same color as the address card. We can use the [eyedropper](https://support.microsoft.com/en-us/office/use-eyedropper-to-match-colors-on-your-slide-d5e7a32a-da6c-4bed-9f1e-8797f07174e9) to pick the right color. Remove the outline. Then match the edges as closely as you can. (Add a bit of transparency so you can see through it -- that helps match edges closely.)

![](/blog/assets/image-24.webp)

Move this card boundary to a new page.

Now, on top of the original image we copy-pasted from Font Awesome, trace 3 rounded rectangles for the address lines. Trace a circle over the head. Fill them white. Remove the outline. It should look like these.

![](/blog/assets/image-28.webp)

Next, let's create the body. We'll create a rounded rectangle that matches the bottom half of the body, another that matches the top half of the body, and intersect them, like this:

![](/blog/assets/ppt-shapes-bust.gif)

Then, draw a large circle around the head and subtract it from the body, like this:

![](/blog/assets/ppt-shapes-neck.gif)

Finally, copy all these shapes over the card boundary on the next page. Select the card boundary first. Then select these copied shapes (3 address lines, head, and bust). Select Shape Format > Merge Shapes > Subtract.

![](/blog/assets/ppt-shapes-address-card.gif)

With that, we have a single shape that contains the entire address card. The white areas are transparent.

You can download the Merge-Shapes.pptx file below with each of the steps.

[Merge-Shapes](https://files.s-anand.net/images/Merge-Shapes.pptx) (Download)

Like I said, I don't bother with Adobe Illustrator or Sketch. PowerPoint does it all for me 😊.
