---
title: Automating PowerPoint with Python
date: "2009-04-02T20:22:36Z"
lastmod: "2022-02-02T07:44:12Z"
categories:
  - coding
  - tools
wp_id: 2369
---

![Automating PowerPoint with Python](/blog/assets/automating-powerpoint-with-python.webp)

Writing a program to draw or change slides is sometimes easier than doing it manually. To change all fonts on a presentation to Arial, for example, you’d write this Visual Basic macro:

```vb
Sub Arial()
    For Each Slide In ActivePresentation.Slides
        For Each Shape In Slide.Shapes
            Shape.TextFrame.TextRange.Font.Name = "Arial"
        Next
    Next
End Sub
```

If you didn’t like Visual Basic, though, you **could** write the same thing in Python:

```python
import win32com.client, sys

Application = win32com.client.Dispatch("PowerPoint.Application")
Application.Visible = True
Presentation = Application.Presentations.Open(sys.argv[1])
for Slide in Presentation.Slides:
    for Shape in Slide.Shapes:
        Shape.TextFrame.TextRange.Font.Name = "Arial"
Presentation.Save()
Application.Quit()
```

Save this as `arial.py` and type `“arial.py some.ppt”` to convert `some.ppt` into Arial.

<a href="/blog/assets/flickr-powerpoint-in-python_3404204235_o-png.webp">![Screenshot of Python controlling PowerPoint](/blog/assets/flickr-powerpoint-in-python_3404204235_o-png.webp)</a>

Let’s break that down a bit. `import win32com.client` lets you interact with Windows using [COM](http://en.wikipedia.org/wiki/Component_Object_Model). You need [ActivePython](http://www.activestate.com/activepython/) to do this. Now you can launch PowerPoint with

```python
Application = win32com.client.Dispatch("PowerPoint.Application")
```

The Application object you get here is the same Application object you’d use in Visual Basic. That’s pretty powerful. What that means is, to a good extent, you can copy and paste Visual Basic code into Python and expect it to work with minor tweaks for language syntax, just please make sure to learn [how to update python](https://blog.couchbase.com/tips-and-tricks-for-upgrading-from-python-2-to-python-3/) before doing anything else.

So let’s try to do something with this. First, let’s open PowerPoint and add a blank slide.

```python
# Open PowerPoint
Application = win32com.client.Dispatch("PowerPoint.Application")
# Create new presentation
Presentation = Application.Presentations.Add()
# Add a blank slide
Slide = Presentation.Slides.Add(1, 12)
```

That 12 is the code for a blank slide. In Visual Basic, you’d instead say:

```python
Slide = Presentation.Slides.Add(1, ppLayoutBlank)
```

To do this in Python, run `Python/Lib/site-packages/win32com/client/makepy.py` and pick “Microsoft Office 12.0 Object Library” and “Microsoft PowerPoint 12.0 Object Library”. (If you have a version of Office other than 12.0, pick your version.)

This creates two Python files. I rename these files as `MSO.py` and `MSPPT.py` and do this:

```python
import MSO, MSPPT

g = globals()
for c in dir(MSO.constants):
    g[c] = getattr(MSO.constants, c)
for c in dir(MSPPT.constants):
    g[c] = getattr(MSPPT.constants, c)
```

This makes constants like `ppLayoutBlank`, `msoShapeRectangle`, etc. available. So now I can create a blank slide and add a rectangle Python just like in Visual Basic:

```python
Slide = Presentation.Slides.Add(1, ppLayoutBlank)
Slide.Shapes.AddShape(msoShapeRectangle, 100, 100, 200, 200)
```

Incidentally, the dimensions are in points (1/72"). Since the default presentation is 10" x 7.5" the size of each page is 720 x 540.

Let’s do something that you’d have trouble doing manually in PowerPoint: a [Treemap](http://www.cs.umd.edu/hcil/treemap-history/). [The Guardian’s](http://www.guardian.co.uk/) [data store](http://www.guardian.co.uk/data-store) kindly makes available the [top 50 banks by assets](http://spreadsheets.google.com/pub?key=phNtm3LmDZEOoyu8eDzdSXw) that we’ll use for this example. Our target output is a simple Treemap visualisation.

<a href="/blog/assets/flickr-treemap_3407796884_o-jpg.webp">![Treemap](/blog/assets/flickr-treemap_3407796884_o-jpg.webp)</a>

We’ll start by creating a blank slide. The code is as before.

```python
import win32com.client, MSO, MSPPT

g = globals()
for c in dir(MSO.constants):
    g[c] = getattr(MSO.constants, c)
for c in dir(MSPPT.constants):
    g[c] = getattr(MSPPT.constants, c)

Application = win32com.client.Dispatch("PowerPoint.Application")
Application.Visible = True
Presentation = Application.Presentations.Add()
Slide = Presentation.Slides.Add(1, ppLayoutBlank)
```

Now let's import data from The Guardian. The spreadsheet is available at [http://spreadsheets.google.com/pub?key=phNtm3LmDZEOoyu8eDzdSXw](http://spreadsheets.google.com/pub?key=phNtm3LmDZEOoyu8eDzdSXw "http://spreadsheets.google.com/pub?key=phNtm3LmDZEOoyu8eDzdSXw") and we can get just the banks and assets as a CSV file by adding `&output=csv&range=B2:C51` (via [OUseful.Info](http://ouseful.wordpress.com/2009/03/10/using-many-eyes-wikified-to-visualise-guardian-data-store-data-on-google-docs/)).

```python
import urllib2, csv

url = "http://spreadsheets.google.com/pub?key=phNtm3LmDZEOoyu8eDzdSXw&output=csv&range=B2:C51"
# Open the URL using a CSV reader
reader = csv.reader(urllib2.urlopen(url))
# Convert the CSV into a list of (asset-size, bank-name) tuples
data = list((int(s.replace(",", "")), b.decode("utf8")) for b, s in reader)
```

I created a simple Treemap class based on the [squarified algorithm](http://www.win.tue.nl/~vanwijk/stm.pdf) — you can play with the [source code](http://www.s-anand.net/treemap.zip). This Treemap class can be fed the data in the format we have, and a draw function. The draw function takes (x, y, width, height, data\_item) as parameters, where data\_item is a row in the data list that we pass to it.

```python
def draw(x, y, w, h, n):
    # Draw the box
    shape = Slide.Shapes.AddShape(msoShapeRectangle, x, y, w, h)
    # Add text: bank name (asset size in millions)
    shape.TextFrame.TextRange.Text = n[1] + " (" + str(int(n[0] / 1000 + 500)) + "M)"
    # Reduce left and right margins
    shape.TextFrame.MarginLeft = shape.TextFrame.MarginRight = 0
    # Use 12pt font
    shape.TextFrame.TextRange.Font.Size = 12


from Treemap import Treemap

# 720pt x 540pt is the size of the slide.
Treemap(720, 540, data, draw)
```

Try running the [source code](http://www.s-anand.net/treemap.zip). You should have a single slide in PowerPoint like this.

<a href="/blog/assets/flickr-treemap-plain_3407796888_o-jpg.webp">![Plain Treemap](/blog/assets/flickr-treemap-plain_3407796888_o-jpg.webp)</a>

The beauty of using PowerPoint as the output format is that converting this into a cushioned Treemap with gradients like below (or changing colours, for that matter), is a simple interactive process.

<a href="/blog/assets/flickr-treemap-powerpoint_3407820202_o-png.webp">![Treemap in PowerPoint](/blog/assets/flickr-treemap-powerpoint_3407820202_o-png.webp)</a>

---

## Comments

<!-- wp-comments-start -->

- **[Catalin](http://python-catalin.blogspot.com/)** _5 Apr 2009 8:01 am_:
  Very interesting article. I think python may be the best solution on programming .
  Do you worked with python and openoffice ?
- **[Michele](http://mb.netsons.org)** _5 Apr 2009 10:35 am_:
  Very very interesting. The treemap integration is absolutely phenomenal.
- **[Greg Wilson](http://www.third-bit.com)** _3 Apr 2009 9:46 pm_:
  Thanks very much for posting this --- much appreciated. One question: how do you find documentation on the PowerPoint API? Is it just the same as the VB (with appropriate substitutions)? Or...?
- **[S Anand](http://www.s-anand.net/)** _5 Apr 2009 4:15 pm_:
  Never worked with OpenOffice, I'm afraid. If I don't use Microsoft Office, my next preference would be Google's online offerings, I guess. But either way, Python's an elegant choice.
- **[S Anand](http://www.s-anand.net/)** _4 Apr 2009 6:59 am_:
  It's the same as with VB. I just press Shift-F1 on VB in PowerPoint and search for the keywords. Usually, it's quite intuitive.
- **[crankycoder.com &raquo; Links for May 7th](http://crankycoder.com/2009/05/07/links-for-may-7th/)** _7 May 2009 5:06 pm_ _(pingback)_:
  [...] Automating PowerPoint with Python - [...]
- **[Raj](http://www.powerpoint.in)** _24 May 2009 7:03 pm_:
  Its all Intresting Anand
- **[Round buttons with Python Image Library | s-anand.net](http://www.s-anand.net/blog/round-buttons-with-python-image-library/)** _11 Jun 2009 10:41 am_ _(pingback)_:
  [...] it using PowerPoint via Python and export as a PNG.So we make a curved box, put in the appropriate gradients and borders, and [...]
- **[Python and Powerpoint &laquo; Financial Python](http://financialpython.wordpress.com/2009/08/08/python-and-powerpoint/)** _8 Aug 2009 8:48 pm_ _(pingback)_:
  [...] I’d almost forgotten since I’ve been using a Mac for a while. Anyway, I ran across this short tutorial on using COM and Python to automate the creation of powerpoint slides. I used COM with excel a [...]
- **Stef** _17 Jul 2010 7:41 pm_:
  Hi,
  I have created a program based on the example you showed on this page (creation of ppt slides with txt and images based on info in a CSV file)
  It works fine on my PC but when I compile it with py2exe, the prog works on my computer but not on another. Any idea of what I should do so that someone who didn't install ActivePython can use the prog?
  Stef
- **Layne Seely** _2 Feb 2011 5:13 pm_:
  I can follow the examples above to open a presentation, however, can you open the presentation to a particular slide?
- **tom tan** _21 May 2012 1:35 pm_:
  Great writing. Helps me to get the hang of office automation with python in general. Thanks.
- **Lolla** _2 Dec 2013 12:22 pm_:
  How to make this work with arabic text?
- **Chad Kijewski** _25 Jun 2013 10:40 pm_:
  Beautiful, thank you for the quick but effective tutorial. I never thought that I'd ever be as excited about PowerPoint as I am, but as usual Python can make anything fun.
- **[Roger](http://www.twrilla.org)** _7 Aug 2013 3:02 pm_:
  Just a heads up, you can add notes via the following command:
  notes\_range = slide.NotesPage.Shapes(2)
  notes\_range.TextFrame.TextRange.Text = snote
  And to use a solid color for a background:
  def RGB(r,g,b):
  return r\*256\*\*2 + g\*256 + b
  slide\_master.Background.Fill.ForeColor.RGB = RGB(256,256,256)
- **blerb** _23 Apr 2014 9:12 pm_:
  My wife needs a way to easily export all comments (comments, not notes) from a powerpoint, which is not a native feature. I was looking at python-pptx module but it only supports 2.6, 2.7. I don't want to downgrade from 3.
  Does win32com have a python3 version and could it be used for this?
- **Zach** _20 Aug 2015 4:59 pm_:
  I am very much a beginner with coding in general but am trying to follow along here and am confused on what I am sure is a very basic issue, so bear with me.
  At the point where you say, "To do this in Python, run Python/Lib/site-packages/win32com/client/makepy.py and pick “Microsoft Office 12.0 Object Library” and “Microsoft PowerPoint 12.0 Object Library”. (If you have a version of Office other than 12.0, pick your version.)" I am unable to run this as there is no win32com directory. I am able to import and utilize the win32com.client library just fine (It pulls up PowerPoint and creates slides) but getting the whole MSO and MSPPT part setup is confusing me. Any help or advice is appreciated, thanks!
- **Vasanth** _21 Jul 2016 10:09 am_:
  Hi Anand,
  I am unable to import MSO & MSPPT. I renamed py files created in gen\_py. I am using 2.7.12 64 bit.
  ImportError: No module named MSO
  Please suggest ?
- **Afiz** _30 Jan 2016 10:17 am_:
  Hi Anand,
  Thanks for this wonderful tutorial. I tried to run makepy.py file as you mentioned above, but I didn't see any files getting created after running the file. Could you please tell me , what I might be missing??
  Thanks again.
- **Sruti** _24 Jul 2017 8:23 am_:
  Hi Anand,
  I'm facing an issue similar to Vasanth's
  I'm not able to find “Microsoft PowerPoint 12.0 Object Library”. Also I get the error shown below:
  for c in dir(PSO.constants): g[c] = getattr(PSO.constants, c)
  AttributeError: 'module' object has no attribute 'constants'
  Any help here is appreciated. Mine is a 64 bit system using Python 2.7.13 version
- **Balu** _6 Mar 2016 12:22 pm_:
  Hi Anand,
  How to add buttons in powerpoint 2013 ribbon through python?
  Thanks for the support.
- **[scratch](http://www.halifa.net)** _16 Jan 2017 2:02 am_:
  your python is very good ,I benifit from it ,thanks. I am a chinese,my english is not good ,sorry.
- **Mj** _10 Mar 2018 12:37 am_:
  Why not try www.pptxbuilder.com. Upload your data, customize your data in visual form, then download everything in a powerpoint presentation.
- **Sailakshmi** _18 Jul 2017 6:39 am_:
  Is there any method by which I could automate slideshow using python?

<!-- wp-comments-end -->
