---
title: Animated charts in Excel
date: "2008-08-19T12:00:00Z"
lastmod: "2009-03-23T15:37:44Z"
categories:
  - excel-tips
  - tools
wp_id: 21
---

<p>Watch <a href="http://en.wikipedia.org/wiki/Hans_Rosling">Hans Rosling</a>'s <a href="http://www.ted.com/">TED Talks</a> on <a href="http://www.ted.com/index.php/talks/hans_rosling_shows_the_best_stats_you_ve_ever_seen.html">debunking third world myths</a> and <a href="http://www.ted.com/index.php/talks/hans_rosling_reveals_new_insights_on_poverty.html">new insights on poverty</a> and ask yourself: <b>could I do this with my own data?</b></p>
<p>Yes. Google has a gadget called <a href="http://www.google.com/ig/directory?url=www.google.com/ig/modules/motionchart.xml">MotionChart</a> that lets you do this.</p>
<p>Now, you could put this up on your web page, but that's not quite useful when presenting to a client. (It is shocking, but there are many practical problems getting an Internet connection at a client site. The room doesn't have a connection. The cable isn't long enough. You can't access the LAN. Their proxy requires authentication. The connection is too slow. Whatever.)</p>
<p>So you need this in Excel. Let me explain a variant of the technique I described <a href="/Excel_-_Make_your_model_visually_obvious.html">earlier</a>.</p>
<p>Let's start by creating a simple bubble chart. </p>
<p><a title="Bubble chart" href="/blog/assets/flickr-1-scatter_2777902130_o-png.webp"><img height="374" alt="" src="/blog/assets/flickr-1-scatter_2777902130_o-png.webp" width="480"></a></p>
<p>For each item in a bubble chart, you need 3 pieces of data: the X-axis, Y-axis and size. This graph shows three items A, B and C in one year: 2001. To animate this, you need data for more years, so let's create that.</p>
<p><a title="Data for multiple years" href="/blog/assets/flickr-2-data_2777043817_o-png.webp"><img height="221" alt="" src="/blog/assets/flickr-2-data_2777043817_o-png.webp" width="269"></a></p>
<p>The first 3 rows contain the same data as before, except that I've added a &quot;Year&quot; column and a &quot;Key&quot; column (which is just a concatenation of the Year and the Item). The data now goes on for many more years. </p>
<p>Now we need to create a scroll bar that can be used to change the year. So add a scroll bar below the bubble chart...</p>
<p><a title="Adding a Scroll Bar" href="/blog/assets/flickr-3-format-control_2777043857_o-png.webp"><img height="250" alt="" src="/blog/assets/flickr-3-format-control_2777043857_o-png.webp" width="496"></a></p>
<p>... and right click the scroll bar and go to Format Control. Now, select the cell link to some cell ($H$1 in this case). Now, if you move the scroll bar, the cell value will change.</p>
<p><a title="Scroll bar format control" href="/blog/assets/flickr-4-link_2777902264_o-png.webp"><img height="469" alt="" src="/blog/assets/flickr-4-link_2777902264_o-png.webp" width="497"></a></p>
<p>All you need to do is to now change the source data for the chart based on the year. From the table on the left, VLOOKUP the year + item, and put this into the table on the right. When the year in the cell H1 changes, the data updates itself. So now, as you move the scroll bar, cell H1 changes, then so does the data and hence the graph. </p>
<p><a title="Using VLOOKUP to change the source data" href="/blog/assets/flickr-5-formula_2777902326_o-png.webp"><img height="303" alt="" src="/blog/assets/flickr-5-formula_2777902326_o-png.webp" width="500"></a></p>
<p>This is what the animation looks like.</p>
<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0" width="485" height="342">
    <param name="movie" value="/gapminder.swf">
    <param name="quality" value="high">
    <param name="bgcolor" value="#ffffff">
    <embed src="/gapminder.swf" quality=high bgcolor="#ffffff" width="485" height="342" name="Gapminder.swf" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer"></embed>
</object>

And here's the <a href="https://files.s-anand.net/images/gapminder.xls">Excel file</a>.

---

## Comments

<!-- wp-comments-start -->

- **S Anand** _29 Jan 2009 9:47 am_:
  For this particular example, Ganesh, you're probably better of not\
  using the scheme I described. It's probably better to reduce the data\
  to fewer dimensions (e.g. in pairs: dimensions (A,B), (A,C), (B,C),\
  etc.). Sorry, without a sense of what the data is about, I'm not sure\
  I can think of a good way of doing this.
- **S Ganesh** _3 Feb 2009 3:21 am_:
  Hi Anand
  As I told you earlier, I came up with something like the above image. 5 processes each measured on 4 Dimensions.
  I was trying to get each of these respective xl charts one on top of the other on Z-axis which could make the representation in 3D.. But I could not.
  Regards
  - S Ganesh
- **S Anand** _21 Jan 2009 6:38 am_:
  I think it would depend on the dimensions, SG. The best way of modelling up\
  to 4 dimensions I've seen are using Hans Rosling's charts at gapminder.org.\
  But you'd need the 4 dimensions to be mappable to X, Y, size and time.
- **SG** _21 Jan 2009 7:03 am_:
  Thanks Anand for the immediate response. A bit more to explain myself.\
  \
  The things that I would like to depict are these.\
  To model the system A, I have 4 dimensions each with varying weights. The response score for each dimension is expressed as %. In bubble chart terms- Say, one of the dimension is represented as a bubble, then the outer circle diameter denote the Relative weight of the dimension and a circle inside denote the actual score.\
  \
  Roughly, I visualize to represent the Model as a stack for 4 bubbles (dimmensions)one on top of other. something like a 3D color model\
  \
  In the example, that you referred.. Size and time are something which is common to X and Y..\
  \
  Thanks\
  Ganesh S
- **l b** _13 Nov 2008 12:16 pm_:
  size can be the annual sales value of a product\
  x can be year\
  y growth
- **Shaun** _24 Nov 2008 10:18 am_:
  Hi. Very useful way of doing this - thanks!\
  \
  Is there any way to automate the scroll bar so that I can click just one button and the graph updates itself automatically?\
  \
  Thanks
- **Theertharao n** _8 Dec 2008 2:44 am_:
  very nice and simple
- **SG** _21 Jan 2009 6:27 am_:
  Hi Anand,\
  \
  This is very nice, I landed on this page googling for something I wanted for in xl charting.\
  \
  Can you help ? I am trying to model a "System A". I have 4 identified dimensions D1, D2, D3, D4 for it, each on a scale of say, 1 to 400.\
  \
  I wanted to represent them in one composite chart to show, this is how the "System A" looks like. Is there anyway out ?\
  \
  Thanks
- **Thejesh GN** _20 Aug 2008 2:45 am_:
  cool tip. I will use it.
- **Sundar R** _1 Sep 2008 8:20 pm_:
  Does this method work only in MS Excel 2007? I am using MS Excel 2003 and I was not able to get the "Control" tab in the properties of the scroll bar.
- **S Anand** _2 Sep 2008 12:11 am_:
  @Sundar: It works on Excel 2003 as well, except I'm not sure what the menu shortcuts are.
- **Sundar R** _3 Sep 2008 12:16 am_:
  After some googling I found out the problem: There are scroll bar object in both "Control toolbox" and "Forms" tool bars. The scroll bar in the "Control toolbox" does not have the "Control" tab in its properties. The scroll bar in the "Forms" does have the "Control" tab in its properties. I was adding the scroll bar object from the Control toolbox toolbar. That's the reason I was not able to get it working earlier.
- **Sridhar** _17 Sep 2008 10:06 am_:
  I don't understand what the "size" could be in the data.. can u help?
- **S Anand** _17 Sep 2008 11:09 am_:
  @Sridhar: The size is the radius of the circles. You'll notice that this changes in the animation as well. Initially, the circles are of the same size, but over time, they become bigger or smaller.
- **[Phil](http://www.animatexl.com)** _13 Oct 2009 4:31 pm_:
  Hi there,
  I've created a little Excel add-in that does a similar thing, but without the need for adding controls to your Excel worksheet. The user simply creates a table of data, creates a chart from the top row of the table and then uses the add-in's menu to run the animation.
  It is free - for now at least :) - and can be downloaded from my website - http://www.animatexl.com.
  I'd be very interested to know what anyone thinks of it.
  Regards
  Phil.
- **Mercy** _12 Aug 2010 2:59 am_:
  Hi -
  Your idea is so fantastic!
  I am trying to use it with a line/area graph, and it is more or less taking shape - got all the filters and vlookups all in place like you recommended; I even put in place 3 scroll bars so that it is now a dynamic graph that is getting controlled by 3 different variables.
  The only thing I wondered about was how to get the scroll bar to display the value of its position as it is getting scrolled.
  Also I wanted to display the variable names that each of the scroll bars are representing and their max and min points.
  I ma sure there is some VB code that can be pasted somewhere - but I needed to get this done by tomorrow, so I'm writing this SOS in the hope you'll read.
- **Ash** _4 May 2010 5:19 pm_:
  Hi everyone,
  Ive been playing about with this technique (which is highly appreciated by the way). For anyone working with percentages, i.e. you want the slider to affect a percentage scoring, you need to do this in a different way (or so I have found - if anyone has a simpler way of doing this, please post).
  Since Excel stores a percentage number as a decimal (e.g. 10% is stored as 0.1), you will need to have a separate reference cell to that where the percentage is stored.
  For example, in cell A2, type the number 5.
  In cell A1, Type ' =A2/100' and then change the cell format to Percentage.
  Add in the slider and set the parameters as per the instructions above, making the cell reference A2, minimum value 0, and maximum value 10.
  The slider will now change the percentage by increments of 10%
  To get greater accuracy, change the formula in cell A1 to reflect how many decimals you wish to go to. For example, for 1 d.p. use ' =A2/1000', for 2d.p. use ' =A2/10000.
  You will also need to change the parameters in the maximum/minimum values in the slider control options to allow you to reach 100%. You will see what i mean once you play about with it.
  Ash
- **Mercy** _12 Aug 2010 3:00 am_:
  Thanks, meanwhile for this really helpful website.
- **LexiK** _15 Jun 2012 12:20 pm_:
  These are amazing, thanks!
  Just a quick query-I can build these in excel no problem, however, if I try to build the same within an excel macro-enabled insert in powerpoint although if I manually scroll along the bar, the graphics change, they don't seem to when the scroll is moved by the 'play' button. Any ideas as to how to get around this?
- **[Daniel Ferry](http://excelhero.com/blog/)** _18 May 2011 6:08 pm_:
  Hello.
  I just found your site. I thought you might be interested in the dozens of Excel animated charts on my blog:
  http://www.excelhero.com/blog/2010/05/animated-business-chart.html
  Kind regards,
  Daniel Ferry
  Excel Hero Academy
- **Arun** _1 Jan 2012 5:21 am_:
  This is not working with the months level data , as numerical conversion of the months not possible , pl help
- **vinoth** _11 Aug 2012 4:23 am_:
  whether the animation will work if i copy it in ppt.
- **Gustavo** _16 Feb 2014 5:11 pm_:
  Hi Anand,
  Do you know if this works with Excel for Mac or Numbers? I use Excel for Mac and get an error for the animation button when it looks for Kernes32, I'm using your data for the animated chart where you inserted a button with code.
  thanks in advance
- **Jayan** _6 Feb 2019 12:58 pm_:
  Hi Ananad. Your blog on bubble chart was very useful and I Created a test case bubble chart. It work fine in when using the scroll bar, however when executing the vba script using the play button it doesn't work. The excel data are changing as per the dimension, however the bubble charts not moving as they moves in scroll bar. Could you kindly advise...please
- **David Ashley** _22 Apr 2020 8:39 pm_:
  Hi Anand -
  I am using the code for the animated bubble charts. I don’t know what the “Sleep (100)” is for as I keep getting an error (compile error sub or function not defined) related to that when I run the script. It highlights “Sleep” in the error. Thanks for any help you can provide.

<!-- wp-comments-end -->
