---
title: JPath - XPath for Javascript
date: "2008-05-29T12:00:00Z"
categories:
  - coding
wp_id: 50
---

<p><a href="http://www.w3.org/TR/xpath">XPath</a> is a neat way of navigating deep XML structures. It's like using a directory structure. <code>/table//td</code> gets all the TDs somewhere below TABLE.</p>
<p>Usually, you don't need this sort of a thing for data structures, particularly in JavaScript. Something like <code>table.td</code> would already work. But sometimes, it does help to have something like XPath even for data structures, so I built a simple XPath-like processor for Javascript called <a href="http://js-tables.googlecode.com/svn/trunk/jpath.js">JPath</a>.</p>
<p>Here are some examples of how it would work:</p>
<table>
<tr><td>jpath(context, "para")                      </td><td>returns context.para                                       </td></tr>
<tr><td>jpath(context, "*")                         </td><td>returns all values of context (for both arrays and objects)</td></tr>
<tr><td>jpath(context, "para[0]")                   </td><td>returns context.para[0]                                    </td></tr>
<tr><td>jpath(context, "para[last()]")              </td><td>returns context.para[context.para.length]                  </td></tr>
<tr><td>jpath(context, "*/para")                    </td><td>returns context[<i>all children</i>].para                  </td></tr>
<tr><td>jpath(context, "/doc/chapter[5]/section[2]")</td><td>returns context.doc.chapter[5].section[2]                  </td></tr>
<tr><td>jpath(context, "chapter//para")             </td><td>returns all para elements inside context.chapter           </td></tr>
<tr><td>jpath(context, "//para")                    </td><td>returns all para elements inside context                   </td></tr>
<tr><td>jpath(context, "//olist/item")              </td><td>returns all olist.item elements inside context             </td></tr>
<tr><td>jpath(context, ".")                         </td><td>returns the context                                        </td></tr>
<tr><td>jpath(context, ".//para")                   </td><td>same as //para                                             </td></tr>
<tr><td>jpath(context, "//para/..")                 </td><td>returns the parent of all para elements inside context     </td></tr>
</table>
<p>Some caveats:</p>
<ul>
<li>This is an implementation of the abbreviated syntax of XPath. You can't use axis::nodetest</li>
<li>No functions are supported other than last()</li>
<li>Only node name tests are allowed, no nodetype tests. So you can't do text() and node()</li>
<li>Indices are zero-based, not 1-based</li>
</ul>
<p>There are a couple of reasons why this sort of thing is useful.</p>
<ul>
<li><b>Extracting attributes deep down</b>. Suppose you had an array of arrays, and you wanted the first element of each array.<br /><a href="/blog/assets/flickr-column-selection_2533734151_o-gif.webp" title="First elements of an array of arrays"><img src="/blog/assets/flickr-column-selection_2533734151_o-gif.webp" width="160" height="128" alt="Column Selection"></a> <br />You could do this the long way:

```javascript
for (var list = [], i = 0; i < data.length; i++) {
  list.push(data[i][0]);
}
```

<p>... or the short way:</p>

```javascript
$.map(data, function(v) {
  return v[1];
});
```

<p>But the best would be something like:</p>

```javascript
jpath(data, "//1");
```

</li>
<li><b>Ragged data structures</b>. Take for example the results from <a href="http://code.google.com/apis/ajaxfeeds/documentation/">Google's AJAX feed API</a>.

```json
{"responseData": {
 "feed": {
  "title": "Digg",
  "link": "http://digg.com/",
  "author": "",
  "description": "Digg",
  "type": "rss20",
  "entries": [
   {
    "title": "The Pirate Bay Moves Servers to Egypt Due to Copyright Laws",
    "link": "http://digg.com/tech_news/The_Pirate_Bay_Moves_Servers_to_Egypt_Due_to_Copyright_Laws",
    "author": "",
    "publishedDate": "Mon, 31 Mar 2008 23:13:33 -0700",
    "contentSnippet": "Due to the new copyright legislation that are going ...",
    "content": "Due to the new copyright legislation that are going to take...",
    "categories": [
    ]
   },
   {
    "title": "Millions Dead/Dying in Recent Mass-Rick-Rolling by YouTube.",
    "link": "http://digg.com/comedy/Millions_Dead_Dying_in_Recent_Mass_Rick_Rolling_by_YouTube",
    "author": "",
    "publishedDate": "Mon, 31 Mar 2008 22:53:30 -0700",
    "contentSnippet": "Click on any \u0022Featured Videos\u0022. When will the insanity stop?",
    "content": "Click on any \u0022Featured Videos\u0022. When will the insanity stop?",
    "categories": [
    ]
   },
   ...
  ]
 }
}
, "responseDetails": null, "responseStatus": 200}
```

<p>If you wanted all the <code>title</code> entries, <i>including the feed title</i>, the choice is between:</p>

```javascript
var titles = [ result.feed.title ];
for (var i=0, l=result.feed.entries.length; i<l; i++) {
    titles.push(result.feed.entries[i].title;
}
```

<p>... versus...</p>

```javascript
titles = jpath(result, "//title");
```

<p>If, further, you wanted the list of all categories at one shot, you could use:</p>

```javascript
jpath(result, "//categories/*");
```

</li>
</ul>

---

## Comments

<!-- wp-comments-start -->

- **Will** _7 Mar 2010 1:15 pm_:
  See also: http://www.w3schools.com/xpath/tryit.asp?filename=try\_xpath\_select\_pricenodes\_text

<!-- wp-comments-end -->
