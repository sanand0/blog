---
title: Automating Internet Explorer with jQuery
date: "2008-05-18T12:00:00Z"
lastmod: "2009-03-17T13:04:50Z"
categories:
  - coding
wp_id: 52
---

<p>Most of my <a href="http://en.wikipedia.org/wiki/Screen_scraping">screen-scraping</a> so far has been through Perl (typically <a href="http://search.cpan.org/dist/WWW-Mechanize/lib/WWW/Mechanize.pm">WWW::Mechanize</a>). The big problem is that it doesn't support Javascript, which can often be an issue:</p>
<ul>
    <li><b>The content may be Javascript-based</b>. For example, <a href="http://www.amazon.com/">Amazon.com</a> shows the bestseller book list only if you have Javascript enabled. So if you're scraping the Amazon main page for the books bestseller list, you won't get it from the static HTML.</li>
    <li><b>The navigation may require Javascript</b>. Instead of links or buttons in forms, you might have Javascript functions. Many pages use these, and not all of them degrade gracefully into HTML. (Try using <a href="http://video.google.com/">Google Video</a> without Javascript.)</li>
    <li><b>The login page uses Javascript</b>. It creates some crazy session ID, and you need Javascript to reproduce what it does.</li>
    <li><b>You might be testing a Javascript-based web-page</b>. This was my main problem: how do I automate testing my pages, given that I <a href="http://localhost/Javascript_error_logging.html">make a lot of mistakes</a>?</li>
</ul>
<p>There are many approaches to overcoming this. The easiest is to use <a href="http://search.cpan.org/~abeltje/Win32-IE-Mechanize-0.009/lib/Win32/IE/Mechanize.pm">Win32::IE::Mechanize</a>, which uses Internet Explorer in the background to actually load the page and do the scraping. It's a bit slower than scraping just the HTML, but it'll get the job done.</p>
<p>Another is to use <a href="http://www.mozilla.org/rhino/">Rhino</a>. <a href="http://ejohn.org/">John Resig</a> has written <a href="http://ejohn.org/blog/bringing-the-browser-to-the-server/">env.js</a> that mimics the browser environment, and on most simple pages, it handles the Javascript quite well.</p>
<p>I would rather have a hybrid of both approaches. I don't like the WWW::Mechanize interface. I've gotten used to <a href="http://jquery.com">jQuery</a>'s rather powerful <a href="http://docs.jquery.com/Selectors">selectors</a> and <a href="/Chaining_functions_in_Javascript.html">chainability</a>. So I'll tell you a way of using jQuery to screen-scrape offline using <a href="http://www.activestate.com/Products/activepython/">Python</a>. (It doesn't have to be Python. <a href="http://www.activestate.com/Products/activeperl/">Perl</a>, <a href="http://www.ruby-lang.org/">Ruby</a>, <a href="http://msdn.microsoft.com/en-us/library/ey73d9d3(VS.85).aspx">Javascript</a>... any scripting language that can use COM on Windows will work.)</p>
<p>Let's take <a href="http://video.google.com/">Google Video</a>. Currently, it relies almost entirely on Javascript. The video marked in red below appears only if you have Javascript.</p>
<p><a href="/blog/assets/flickr-google-video_2508656885_o-png.webp" title="Google Video screenshot"><img src="/blog/assets/flickr-google-video_2508656885_o-png.webp" width="500" height="280" alt="The left box showing the top video uses Javascript"></a></p>
<p>I'd like an automated way of checking what video is on top on Google Video every hour, and save the details. Clearly a task for automation, and clearly not one for pure HTML-scraping.</p>
<p>I know the video's details are stored in elements with the following IDs (thanks to <a href="https://addons.mozilla.org/en-US/firefox/addon/1095">XPath checker</a>):</p>
<table>
<tr><th>ID</th><th>What's there</th></tr>
<tr><td>hs_title_link</td><td>Link to the video</td></tr>
<tr><td>hs_duration_date</td><td>Duration and date</td></tr>
<tr><td>hs_ratings</td><td>Ratings. The stars indicate the rating and the span.Votes element inside it has the number of people who rated it.</td></tr>
<tr><td>hs_site</td><td>The site that hosts the video</td></tr>
<tr><td>hs_description</td><td>Short description</td></tr>
</table>
<p>So I could do the following on Win32::IE::Mechanize.</p>

```perl
use Win32::IE::Mechanize;
my $ie = Win32::IE::Mechanize->new( visible => 1 );
$ie->get("http://video.google.com/");
my @links = $ie->links
# ... then what?
```

<p>I <i>could</i> go through each link to extract the <code>hs_title_link</code>, but there's no way to get the other stuff.</p>
<p>Instead, we could take advantage of a couple of facts:</p>
<ul>
    <li><b>Internet Explorer exposes a COM interface</b>. That's what Win32::IE::Mechanize uses. You can use it in any scripting language (<a href="http://www.activestate.com/Products/activeperl/">Perl</a>, <a href="http://www.ruby-lang.org/">Ruby</a>, <a href="http://msdn.microsoft.com/en-us/library/ey73d9d3(VS.85).aspx">Javascript</a>, ...) on Windows to control IE.</li>
    <li><b>You can load jQuery on to any page</b>. Just add a <code>&lt;script&gt;</code> tag pointing to jQuery. Then, <b>you can call jQuery from the scripting language!</b></li>
</ul>
<p>Let's take this step by step. This Python program opens IE, loads <a href="http://video.google.com/">Google Video</a> and prints the text.</p>

```python
# Start Internet Explorer
import win32com.client
ie = win32com.client.Dispatch("InternetExplorer.Application")

# Display IE, so you'll know what's happening
ie.visible = 1

# Go to Google Video
ie.navigate("http://video.google.com/")

# Wait till the page is loaded
from time import sleep
while ie.Busy: sleep(0.2)

# Print the contents
# Watch out for Unicode
print ie.document.body.innertext.encode("utf-8")
```

<p>The next step is to add jQuery to the Google Video page.</p>

```python
# Add the jQuery script to the browser
def addJQuery(browser,
    url="http://jqueryjs.googlecode.com/files/jquery-1.2.4.js"

    document = browser.document
    window = document.parentWindow
    head = document.getElementsByTagName("head")[0]
    script = document.createElement("script")
    script.type = "text/javascript"
    script.src = url
    head.appendChild(script)
    while not window.jQuery: sleep(0.1)
    return window.jQuery

jQuery = addJQuery(ie)
```

<p>Now the variable <code>jQuery</code> contains the Javascript jQuery object. From here on, you can hardly tell if you're working in Javascript or Python. Below are the expressions (<i>in Python!</i>) to get the video's details.</p>

```python
# Video title: "McCain's YouTube Problem ..."
jQuery("#hs_title_link").text()

# Title link: '/videoplay?docid=1750591377151076231'
jQuery("#hs_title_link").attr("href")

# Duration and date: '3 min - May 18, 2008 - '
jQuery("#hs_duration_date").text()

# Rating: 5.0
jQuery("#hs_ratings img").length

# Number of ratings '(8,288 Ratings) '
jQuery("#hs_ratings span.Votes").text()

# Site: 'Watch this video on youtube.com'
jQuery("#hs_site").text()

# Video description
jQuery("#hs_description").text()
```

<p>This wouldn't have worked out as neatly in Perl, simply because you'd need to use <code>-&gt;</code> instead of <code>.</code> (dot). With Python (and with Ruby and Javascript on cscript), you can almost cut-and-paste jQuery code.</p>
<p>If you want to click on the top video link, use:</p>

```python
jQuery("#hs_title_link").get(0).click()
```

<p>In addition, you can use the keyboard as well. If you want to type <code>username TAB password</code>, use this:</p>

```python
shell = win32com.client.Dispatch("WScript.Shell")
shell.sendkeys("username{TAB}password")
```

<p>You can use any of the arrow keys, control keys, etc. Refer to the <a href="http://msdn.microsoft.com/en-us/library/8c6yea83(VS.85).aspx">SendKeys Method on MSDN</a>.</p>

---

## Comments

<!-- wp-comments-start -->

- **Franky** _18 May 2008 12:00 pm_:
  Holy crap. I am in way over my head here, but this is pretty sweet stuff if I'm reading it correctly. Thanks for the info.
- **[Alessandro](http://www.mathema.com)** _5 Jul 2009 11:50 am_:
  The idea is really good. Unfortunately it doesn't seem to work under Perl. When a JS function/script is invoked (jQuery is a JS function) IE does not return a COM object and the control from Perl is lost.
  There are, of course, methods to overcome the obstacle but not as simple as $window->jQuery!
- **Anonymous** _5 Mar 2010 11:25 pm_:
  Wow, kick ass! Exactly what I was looking for. Used AutoIt on a host machine to instantiate the IE object and thanks to you was able to use jQuery to do my scraping. Combined with the IE Developer Toolbar, this has probably saved me weeks of time.
- **Manikandan** _19 Nov 2009 3:30 pm_:
  I am trying to do a screenscrape and the code executes jquery.
  Whenever I had to execute javascript i could execute it by
  ie.navigate(javascript:....)
  But when I tried the same thing with jquery it does not execute.
  The code behind is something like this
  I tried ie.navigate(jQuery1258644477483="2")
  It did not thing.
  Appreciate your help!!!
- **[Powershell: Including jQuery in InternetExplorer.Application | DeveloperQuestion.com](http://developerquestion.com/powershell-including-jquery-in-internetexplorer-application/)** _30 Oct 2010 1:32 pm_ _(pingback)_:
  [...] script document I Followed this article, explaining how to accomplish in Python what I want to do in Powershell. So now I have this [...]
- **Joe** _27 Nov 2010 2:42 pm_:
  Hello Mr. Anand,
  I am trying to do this in Ruby, but I am not sure how to start. Maybe I am lucky and you have you moved to ruby since May 2008? You start with import win32com.client, and I suppose that is to support an IE browser API. I have Firefox, Chrome, Safari and others available to me.
  The basic aim I guess is to inject JQuery into my page object. Mechanize provides me a page. I am that far. How do I it give it JQuery superpowers. Mechanize uses Nokogiri selectors under the hood. But I would love to standardize on JQuery because it's useful in so many other contexts...in the way that regex is.
  Joe
- **[Powershell: Using jQuery through InternetExplorer.Application](http://fatal-errors.com/powershell-using-jquery-through-internetexplorer-application/86850)** _12 Feb 2012 2:48 am_ _(pingback)_:
  [...] followed this article, explaining how to spice up an Internet Explorer COM-Object with jQuery. While the author used [...]

<!-- wp-comments-end -->
