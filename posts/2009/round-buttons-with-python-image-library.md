---
title: Round buttons with Python Image Library
date: "2009-06-11T10:41:27Z"
lastmod: "2009-06-29T04:30:10Z"
categories:
  - coding
wp_id: 2382
---

After much hunting, I finally settled on [Hedger Wang’s simple round CSS links](http://www.hedgerwow.com/360/dhtml/css-round-button/demo.php) as the most acceptable cross-browser round button implementation. The minified CSS is about 2.5KB, and the syntax is very simple. To make an input button into a round button, just wrap it within a `<span class="button">`:

```html
<span class="button"><input type="submit"></span>
```

… and it’s just as easy to convert a link into a rounded button:

```html
<a class="button" href=”/”><span>Home</span></a>
```

It works by using a transparent PNG / GIF that looks like this:

![](http://www.hedgerwow.com/360/dhtml/css-round-button/btn0.png)

The first button is the default button. The second appears on hover. The bottom two are for disabled buttons.

**Can we easily create buttons in different colours?**

That’s what this post is about: creating that image with round buttons and gradients.

When I tried creating these rounded buttons myself (and trying to do it in an automated was as usual), I saw 3 possible approaches:

1. **Create it using** [**PowerPoint via Python**](/blog/automating-powerpoint-with-python) **and export as a PNG.**
   So we make a curved box, put in the appropriate gradients and borders, and export it as a PNG. But the problem is **I couldn’t figure out how to get transparent PNGs**.
2. **Create it in** [**GIMP**](http://www.gimp.org/) **using** [**script-fu plugin**](http://www.gimp.org/docs/scheme_plugin/script-fu-gimp.html) **.**
   The problem is, **I don’t know scheme or GIMP’s API**. So I gave up on this as well.
3. **Create it using** [**Python Image Library**](http://www.pythonware.com/library/pil/) **.**
   This was inspired by Nadia’s [PIL Tutorial: How to Create a Button Generator](http://nadiana.com/pil-tutorial-how-create-button-generator). Let me explain how this works.

The first step is to create a ‘button-mask.png’ like this one:

![](/blog/assets/flickr-mask_3615809813_o-png.webp)

1. Create a transparent 300 x 120 image in GIMP
2. Selecting a box from (0,0) to (300,30)
3. Shrink it by 2 pixels
4. Convert it to a rounded rectangle with a radius of 80%
5. Fill this in white
6. Copy it to 60 pixels below

Now, we need code to create a gradient:

```python
start, end = (192, 192, 224), (255, 255, 255)
grad = Image.new("RGBA", (300, 120))
draw = ImageDraw.Draw(grad)
for y in range(0, 30):
    draw.line(((0, y), (300, y)), fill=rgb(start, end, y / 30.0))
    draw.line(((0, y + 60), (300, y + 60)), fill=rgb(start, end, 1.0 - y / 30.0))
```

Now that the gradient is created, convert that into a round button by loading button-mask.png’s alpha layer onto the gradient:

```python
mask = Image.open("button-mask.png").convert("RGBA").split()[3]
border = Image.open("button-border.png").convert("RGBA")
grad.putalpha(mask)
grad.save("button.png")
```

There it is: a simple round button generator. You can see a sample of these buttons at my [Dilbert search](http://dilbert-search.appspot.com/) site.

---

## Comments

<!-- wp-comments-start -->

- **helpful** _27 Jun 2009 8:01 pm_:
  The best way to do this is to use python's cairo support to fully draw the button and apply the gradient and add text.
- **[S Anand](http://www.s-anand.net/)** _29 Jun 2009 5:08 am_:
  Thanks -- Cairo seems a lot more powerful than PIL. Will give it a shot.

<!-- wp-comments-end -->
