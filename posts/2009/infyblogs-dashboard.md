---
title: Infyblogs dashboard
date: "2009-01-26T12:00:00Z"
lastmod: "2009-03-09T08:34:56Z"
categories:
  - coding
wp_id: 15
---

I just finished [Stephen Few](http://www.perceptualedge.com/)'s book on [Information Dashboard Design](http://www.amazon.com/Information-Dashboard-Design-Effective-Communication/dp/0596100167). It talks about what's wrong with the dashboards most Business Intelligence vendors ([Business Objects](http://www.sap.com/solutions/sapbusinessobjects/index.epx), [Oracle](http://www.oracle.com/), [Informatica](http://www.informatica.com/), [Cognos](http://www.cognos.com/), [Hyperion](http://www.oracle.com/hyperion/index.html), etc.), and brings [Tuftian](http://www.edwardtufte.com/) principles of chart design to dashboards.

So I took a shot at designing a dashboard based on those principles, and made this dashboard for [InfyBLOGS](http://blogs.ad.infosys.com/).

![Infyblog dashboard](/blog/assets/infyblogs-dashboard.webp)

You can try for yourself. Go to <http://www.s-anand.net/reco/>\
****Note: This only works within the Infosys intranet.****

1. Right click on the "Infyblog Dashboard" link and click "Add to Favourites..." (Non-IE users -- drag and drop it to your links bar)
2. If you get a security alert, say "Yes" to continue
3. Return to InfyBLOGS, **make sure you're logged in** (that's important) and click on the "Infyblog Dashboard" bookmark
4. You'll see a dashboard for **your account**, with comments and statistics

The rest of this article discusses design principles and the technology behind the implementation. (It's long. Skim by reading just the **bold headlines**.)

**Dashboards are minimalist**

I'll use the design of the dashboard to highlight some of the concepts in the book.

I designed the dashboard first on Powerpoint, keeping these principles in mind.

1. **Fits in one screen**. No scrolling. Otherwise, it isn't a dashboard.
2. **Shows only what I need to see**. Ideally, from this dashboard, I should receive all the information I need to act on, and no more.
3. **Minimises the** [**data-ink ratio**](http://www.infovis-wiki.net/index.php/Data-Ink_Ratio). Don't draw a single pixel that's not required.

The first was easy. I just constrained myself to one page of PowerPoint, though if you had a lot of toolbars, the viewing area of your browser may be less than mine.

The second is a matter of picking what you want to see. For me, these are the things I look for when I log into InfyBLOGS:

1. Any new comments?
2. Any new posts from my friends?
3. What's new? What's hot?

Then I dig deeper, occasionally, into popular entries, popular referrers, how fast the blogs are growing, etc. So I've put in what I think are the useful things.

The third is reflected in the way some of this information is shown. Let me explain.

**Keep the charts bare**

Consider the graphs on the right. They look like this.

Notice the wiggly line to the right. It's a graph called [sparkline](http://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0001OR&topic_id=1), and was introduced by Edward Tufte. Sparklines are great to show trends in a compact way. Forget the axes. Forget the axes labels. Forget the gridlines. The text on the left ("visitors per day") tells you what it is. The number (10475) is the current value. And the line is the trend. Clearly the number of visitors has exploded recently, from a relatively slow and flat start. The labels and axes aren't going to tell you much more.

**Boldly highlight what's important**

The most important thing here, the title, is on top. It's pure black, in large font, positioned right on top, and has a line segregating it from the rest of the page.

The sections are highlighted by a bigger font, different colour, and a line, but the effect is a bit more muted.

The numbers on the right are prominent only by virtue of size and position. If anything, the colour de-emphasizes them. This is to make sure that they don't overwhelm your attention. (They would if they were in red, for instance.)

The number 10475 is carefully set to occupy exactly two line spaces. That alignment is very important. The small lines are at a font size of 11px, and line spacing is 1.5. So at a font size of 2 x 11px x 1.5 = 33px, the size of the large number covers exactly two rows.

The labels, such as "visitors" or "sites" are in blue, bold. Nothing too out of the way, but visible enough that they stand out.

The "View more..." links just use colour to stand out. They're pretty unimportant.

The bulk of the text is actually made of links, unlike traditional links, they're not underlined and they're not blue. It would just add to the noise if everything where underlined. But on mouseover, they turn blue and are underlined, clearly indicating that they're links.

I've used four mechanisms to highlight relative importance: position, size, colour and lines. There are many more: font, **styling**, boxes, underlining, indentation, etc.

The purpose of good design is to draw attention to what's important, to direct the flow of the eye in a way that builds a good narrative. Don't be shy of using every tool at your disposal in doing that. While on the topic, the [Non-Designer's Design Book](http://www.amazon.com/Non-Designers-Design-Book-3rd-Designers/dp/0321534042/) is a fantastic and readable book on design for engineers.

**Always use grids to display**

I can't say this any better than [Mark Boulton](http://markboulton.co.uk/) of [subtraction.com](http://subtraction.com), in his presentation [Grids are Good](http://www.slideshare.net/huer1278ft/grids-are-good-right). Grids are pervasive in **every form of good design**. It's a fantastic starting point as well. Just read the slideshow and follow it blindly. You can't go wrong.

This dashboard uses 12-grid. The page is divided into two vertically. The left half has mostly text and the right half has statistics and help. There are 3 blocks within each, **and they're all the same size** (alignment is critical in good design)**.** Two of the blocks on the left are subdivided into halves, while the bottom right "Links and help" section is subdivided into three. Well, it's easier to show it than explain it:

![Picture of grid](/blog/assets/infyblogs-dashboard-grid.webp)

**Copy shamelessly**

The design for this dashboard was copied in part from [Wordpress 2.7's new dashboard](http://iammattthomas.com/27/1.png), part from the dashboards on Stephen Few's book, and part from the winners of the [2008 Excel dashboard competition](http://www.bonavistasystems.com/NewsMicroChartsCompetition.html).

Most of these designs are minimalist. There's no extra graphics, jazzy logos, etc. that detract from the **informational** content. This is an informational dashboard, not a painting.

Good design is everywhere. View this presentation on [How to be a Creative Sponge](http://www.slideshare.net/hicksdesign/how-to-be-a-creative-sponge) to get a sense of the many sources where you can draw inspiration from. You're much much better of copying good design than inventing bad ones.

**You can hack the dashboard yourself**

I've uploaded the source for the dashboard at [http://infyblog-dashboard.googlecode.com/](http://infyblog-dashboard.googlecode.com/ "http://infyblog-dashboard.googlecode.com/")

Please feel free to browse through it, but **don't stop there!** Go ahead and tweak it to suit what **you** think should be on an ideal dashboard. I'll give access to the project to anyone who asks (leave a comment, mail me or call me at +44 7957 440 260).

Please hack at it. Besides, it's great fun learning jQuery and working on a distributed open source project.

Now for some notes on how this thing works.

**Bookmarklets bring Greasemonkey to any browser**

This is implemented as a [bookmarklet](http://en.wikipedia.org/wiki/Bookmarklet) (a bookmark written in Javascript). It just loads the file <http://www.s-anand.net/infyblog-dashboard.js> which does all the grunt work. This is the code for the bookmarklet.

```javascript
// Create a new a script element
var s = document.createElement("script");

// Set the source of the script element to my bookmarklet script
s.setAttribute("src", "http://www.s-anand.net/infyblog-dashboard.js");

// Add the script element to the head
// This does the the equivalent of:
// <head><script src="..."></script></head>
document.getElementsByTagName("head")[0]
  .appendChild(s);

// Return void. Not sure why, but this is required
void s;
```

This form of the bookmarklet is perhaps it's most powerful use. It lets you inject any script into any site. If you want to change it's appearance, content, anything, just write it as a bookmarklet. (Think of it as the IE and Safari equivalent of Firefox's [Greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/748).)

So if you wanted to load [jQuery](http://jquery.com/) into any page:

1. Change the URL in line 5 above to the [jQuery URL](http://ajax.googleapis.com/ajax/libs/jquery/1.3.1/jquery.min.js) and add it as a bookmark. (Or use [Karl's jQuery bookmarklet](http://www.learningjquery.com/2006/12/jquerify-bookmarklet). It's better)
2. Go to any page, say the [IMDB Top 250](http://www.imdb.com/chart/top) for instance
3. Click on the bookmarklet. Now your page is jQueryified. (If you used Karl's bookmarklet, it'll tell you so.)
4. On the address bar, type "javascript:alert($('table:eq(10) tr').length)" and press enter.
5. You should see 252, the number of rows on main table of the [IMDB Top 250](http://www.imdb.com/chart/top)

Notes:

- There are other [ways of adding Greasemonkey functionality to your browser](http://www.robertnyman.com/2009/01/19/extending-web-browser-functionality-greasemonkey-for-all-web-browsers/)
- There are [many](http://www.bookmarklets.com/) [bookmarklet](https://www.squarefree.com/bookmarklets/) [directories](http://subsimple.com/bookmarklets/default.asp) [where](http://www.yourhtmlsource.com/accessibility/bookmarklets.html) [you](http://www.philburns.com/bookmarklets.html) [can](http://pimpmysafari.com/bookmarklets/) [find](http://www.sitepoint.com/article/bookmarklets/) [bookmarklets](http://www.lifeclever.com/17-powerful-bookmarklets-for-your-iphone/)
- The dashboard is better written as a server-side app, but I don't own any servers in our Intranet

**jQuery is a powerful Javascript library**

Firstly, you don't want to program Javascript without a library. You just don't. The state of browser incompatibilities and DOM usability is just to pathetic to contemplate. Stop learning DOM methods. Pick any library instead.

Going by popularity, you would do well to pick [jQuery](http://jquery.com/). Here's a graph of searches on Google for the popular Javascript libraries, and jQuery leads the pack.

https://trends.google.com/trends/explore?date=all&q=jquery,prototype,dojo,ext,yui

I picked it in early 2007, and my reasons were that it:

1. **Is small**. At that time, it was 19KB and was the smallest of the libraries. (Today it's 18KB and has more features.)
2. **Makes your code compact**. It lets you [chain functions](http://www.s-anand.net/Chaining_functions_in_Javascript.html), and overloads the $() function to work with DOM elements, HTML strings, arrays, objects, anything.
3. **Doesn't pollute the namespace**. Just 2 global variables: jQuery and $. And you can make it not use $ if you like.
4. **Is very intuitive**. You can learn it in an hour, and the [documention](http://docs.jquery.com/) is extremely helpful.
5. **Is fully functional**. Apart from DOM manipulation, it covers CSS, animations and AJAX, which is all I want from a library.

These days, I have some additional reasons:

1. **It's extensible**. The [plugin ecosystem](http://plugins.jquery.com/) is rich.
2. [**It's hosted at Google**](http://code.google.com/apis/ajax/), and is really fast to load. Most often, it's already cached in your users' browser.
3. [**John Resig**](http://ejohn.org/) is a genius. After [env.js](http://ejohn.org/projects/bringing-the-browser-to-the-server/) and [processing.js](http://ejohn.org/blog/processingjs/), I trust him to advance jQuery better than other libraries.

So anyway, the first thing I do in [the dashboard script](http://www.s-anand.net/infyblog-dashboard.js) is to load jQuery, using the same code outlined in the bookmarklet section above. The only addition is:

```javascript
script.onload = script.onreadystatechange = function() {
  if (
    !this.readyState || this.readyState == "loaded"
    || this.readyState == "complete"
  ) {
    callback();
  }
};
```

This tells the browser to run the script "callback" once the script is loaded. My main dashboard function runs once jQuery is loaded.

**InfyBLOGS has most statistics the dashboard needs**

Thanks to posts from [Utkarsh](http://blogs.ad.infosys.com/users/utkarshraj_atmaram/) and [Simon](http://blogs.ad.infosys.com/users/simon_jose/), I knew where to find most of the information for the dashboard:

- [Comments page](http://blogs.ad.infosys.com/tools/recent_comments.bml) for your latest comments
- [Profile page](http://blogs.ad.infosys.com/userinfo.bml?mode=full) for your statistics: number of entries, interests, friends, etc.
- [Directory page](http://blogs.ad.infosys.com/directory.bml?ut_days=7) for recently updated blogs
- [Communities page](http://blogs.ad.infosys.com/directory.bml?com_do=1) for recently updated communities
- [Usage page](http://blogs.ad.infosys.com/usage/) for Infyblog statistics and popular referrers
- [Meme page](http://blogs.ad.infosys.com/meme.bml) for recently popular links

The only things I couldn't find were:

- **Friends posts**. I'd have liked to show the titles of recent posts by friends. Yeah, I know: blogs/user\_name/friends has it, but thanks to user styles, it's nearly impossible to parse in a standard way across users. I'd really like an RSS feed for friends.
- **Interests posts**. Would be cool to show recent posts by users who shared your your interest.
- **Communities posts**. Again, I'd have liked to show the recent posts in communities, rather than just the names of communities.

**Using IFRAMEs, we can load these statistics onto any page**

Let's say we want the latest 10 comments. These are available on the [comments page](http://blogs.ad.infosys.com/tools/recent_comments.bml). To load data from another page, we'd normally use XMLHTTPRequest, get the data, and parse it — perhaps using [regular expressions](http://en.wikipedia.org/wiki/Regular_expressions).

```javascript
$.get('/tools/recent_comments.bml').function(data) {
    // Do some regular expression parsing with data
});
```

But from a readability and maintainability perspective, regular expressions suck. A cleaner way is to use jQuery itself to parse the HTML.

```javascript
$.get('/tools/recent_comments.bml').function(data) {
    var doc = $(data);
    // Now process the document
});
```

This works very well for simple pages, but sadly, for our statistics, this throws a stack overflow error (at least on Firefox; I didn't have the guts to try it on IE.)

So on to a third approach. Why bother using Javascript to parse HTML, when we're running the whole application in a browser, the most perfect HTML parser? Using IFRAMEs, we can load the whole page within the same page, let the browser do the HTML parsing.

```javascript
$("<iframe src=\"/tools/recent_comments.bml\"></iframe>")
  .appendTo("body")
  .load(function() {
    var doc = $(this).contents();
    // Now process the document
  });
```

This way, you can read any page from Javascript **within** the same domain. Since both the bookmarklet and statistics are on the [InfyBLOGS](http://blogs.ad.infosys.com/) domain, we're fine.

**jQuery parses these statistics rather well**

Now the `doc` variable contains the entire comments page, and we can start process it. For example, the comments are on the rows of the **second** table in the page. (The first table is the navigation on the left.). So

```javascript
doc.find("table:eq(1) tr");
```

gets the rows in the second table (`table:eq(0)` is the first table). Now, we can go through each row, extract the user, when the comment was made, links to the entry and to the comment.

```javascript
doc.find('table:eq(1) tr').slice(0,8).map(function() {
    var e = $(this),
        user = e.find('td:eq(0) b').text(),
        when = e.find('td:eq(0)').text().replace(user, ''),
        post = e.find('td:eq(1) a:contains(Entry Link)').attr('href'),
        cmnt = e.find('td:eq(1) a:contains(Comment Link)').attr('href'),
        // return HTML constructed using the above information
    });
```

**Google Charts API displays dynamic charts**

Another cool thing is that we can use [Google Charts](http://code.google.com/apis/chart/) to display charts without having to create an image beforehand. For instance, the URL:

`http://quickchart.io/chart?cht=lc&chs=300x200&chd=t:5,10,20,40,80`

shows an image with a line chart through the values (5,10,20,40,80).

![Google chart example](http://quickchart.io/chart?cht=lc&chs=300x200&chd=t:5,10,20,40,80)

The dashboard uses [sparklines](http://en.wikipedia.org/wiki/Sparklines) to plot the trends in InfyBLOG statistics. These are supported by Google Charts. We can extract the data form the [usage page](http://blogs.ad.infosys.com/usage/) and create a new image using Google Charts that contains the sparkline.

If you want to play around with Google Charts without mucking around with the URL structure, I have a relatively easy to use [chart constructor](http://www.s-anand.net/chart).

**Always use CSS frameworks**

Libraries aren't restricted to Javascript. [CSS frameworks](http://en.wikipedia.org/wiki/CSS_framework) exist, and as with Javascript libraries, these are a no-brainer. It's not worth hand-coding CSS from scratch. Just build on top of one of these.

The state of CSS frameworks isn't as advanced as in Javascript. Yahoo has it's [UI grids](http://developer.yahoo.com/yui/grids/), [Blueprint](http://www.blueprintcss.org/)'s pretty popular and I found [Tripoli](http://monc.se/tripoli/) to be nice, but the one I'm using here is [960.gs](http://960.gs/). It lets you create a 12-grid and 16-grid on a 960-pixel wide frame, which is good enough for my purposes.

---

At nearly 2,500 words, this is the longest post I've ever written. It took a day to design and code the dashboard, but longer to write this post. Like Paul Buchheit says, it's easier to [communicate with code](http://paulbuchheit.blogspot.com/2009/01/communicating-with-code.html). I've also violated my principle of [Less is More](http://www.s-anand.net/Less_is_more.html). My apologies. But to re-iterate:

**Please hack it**

The code is at [http://infyblog-dashboard.googlecode.com/](http://infyblog-dashboard.googlecode.com/ "http://infyblog-dashboard.googlecode.com/"). You can join the project and make changes. Leave a comment, mail me or call me.

---

## Comments

<!-- wp-comments-start -->

- **sujays** _26 Jan 2009 7:14 am_:
  am an x-infy guy and my id(sujaychandiran\_s) still works in ur "suggest friends" feature.. does this connect 2 infy DB?.. if yes, doesnt this pose a security threat ? am jus curious !\
  \
  me cant hack, so cant confirm :)\
  \
  Sujay
- **S Anand** _26 Jan 2009 9:23 am_:
  @Sujay: nah, it's not a security risk. It's just a static dump of data, and\
  is a bit out-dated in any case. If anything, it may be a privacy risk:\
  recruiters might try to mine for interests and pick people that way. But in\
  this economy, I guess no one's worried about that.
- **gwatts** _26 Jan 2009 6:52 pm_:
  If you like jQuery, and you like sparklines then you can combine the two and avoid the browser roundtrips to fetch externally rendered images:\
  http://omnipotent.net/jquery.sparkline/
- **Thejesh GN** _26 Jan 2009 10:33 pm_:
  Very cool.\
  I guess we can add buttons for add/edit posts.
- **S Anand** _31 Jan 2009 5:59 am_:
  That's a great plugin, Gareth! Look forward to using it. Thanks.

<!-- wp-comments-end -->
