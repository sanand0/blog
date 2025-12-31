---
title: In search of a good editor
date: "2008-05-29T12:00:00Z"
categories:
  - coding
wp_id: 51
---

<p>It's amazing how hard it is to get a good programming editor. I've played around with more editors/IDEs than I care to remember: <a href="http://en.wikipedia.org/wiki/E_%28text_editor%29">e</a> <a href="http://en.wikipedia.org/wiki/Notepad%2B%2B">Notepad++</a> <a href="http://en.wikipedia.org/wiki/NoteTab">NoteTab</a> <a href="http://en.wikipedia.org/wiki/SciTE">SciTE</a> <a href="http://en.wikipedia.org/wiki/Crimson_Editor">Crimson Editor</a> <a href="http://en.wikipedia.org/wiki/ActiveState_Komodo">Komodo</a> <a href="http://en.wikipedia.org/wiki/Eclipse_%28software%29">Eclipse</a> <a href="http://en.wikipedia.org/wiki/Aptana">Aptana</a> ...</p>
<p>There are four features that are critical to me.</p>
<ul style='overflow:hidden'>
    <li><b>Syntax highlighting</b>. Over time, I've found this to increase readability dramatically. Look at this piece of code with and without syntax highlighting: <br /><a href="/blog/assets/flickr-syntax-highlighting_2534400368_o-gif.webp" title="Syntax Highlighting"><img src="/blog/assets/flickr-syntax-highlighting_2534400368_o-gif.webp" width="500" height="360" alt="Syntax Highlighting"></a> <br />Doesn't the structure of the document just jump out with syntax highlighting? Anyway, I've gotten used to that.</li>
    <li><b>Column editing</b>. I want to be able to do this: <br /><a href="/blog/assets/flickr-column-editing_2533597469_o-gif.webp" title="Column Editing"><img src="/blog/assets/flickr-column-editing_2533597469_o-gif.webp" width="160" height="150" alt="Column Editing"></a> <br />Being able to type across rows is incredibly useful. I use it both for programming as well as to complement data-processing on Excel.</li>
    <li><b>Unicode support</b>. I often work with non-ASCII files, particularly in Tamil. Unicode support comes in handy when debugging pages for my <a href="/tamil">songs site</a>.</li>
    <li><b>Auto-completion</b>. This is 10 times more productive than having to look up the manual for each function. <br /><a href="/blog/assets/flickr-autocompletion_2534433048_o-gif.webp" title="AutoCompletion"><img src="/blog/assets/flickr-autocompletion_2534433048_o-gif.webp" width="250" height="125" alt="AutoCompletion"></a></li>
</ul>
<p>(Oh, and it's got to be free too. Except for e Text Editor, all the others qualify.)</p>
<p>The problem is, none of the browsers that I've looked at support all of these features.</p>
<table><thead>
    <tr><th>Editor</th><th>Syntax highlighting</th><th>Column editing</th><th>Unicode support</th><th>Auto-completion</th></tr>
</thead><tbody>
    <tr><td>e&nbsp;Text&nbsp;Editor </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td><td style='background-color:#cfc'> Yes </td></tr>
    <tr><td>Crimson&nbsp;Editor     </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td><td style='background-color:#fcc'> No  </td></tr>
    <tr><td>Notepad++               </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td></tr>
    <tr><td>NoteTab-Lite            </td><td style='background-color:#fcc'> No  </td><td style='background-color:#fcc'> No  </td><td style='background-color:#fcc'> No  </td><td style='background-color:#fcc'> No  </td></tr>
    <tr><td>SciTE                   </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#cfc'> Yes </td></tr>
    <tr><td>TextPad                 </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td></tr>
    <tr><td>UltraEdit               </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td><td style='background-color:#fcc'> No  </td><td style='background-color:#ccc'> ?   </td></tr>
    <tr><td>Aptana                  </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#cfc'> Yes </td></tr>
    <tr><td>Eclipse                 </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#cfc'> Yes </td></tr>
    <tr><td>Komodo                  </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#fcc'> No  </td><td style='background-color:#cfc'> Yes </td><td style='background-color:#cfc'> Yes </td></tr>
</tbody></table>
<p><i>Wikipedia has a more in-depth <a href="http://en.wikipedia.org/wiki/Comparison_of_text_editors">comparison of text editors</a>.</i></p>
<p>Actually, there's another parameter that's pretty important: <b>responsiveness</b>. When I type something, I want to see it on the screen. Right that millisecond. With some of the features added by these editors, there's so much bloat that it often takes up to <b>one second</b> between the keypress and the refresh. That's just not OK.</p>
<p>I've settled on <a href="http://en.wikipedia.org/wiki/Crimson_Editor">Crimson Editor</a> as my default editor these days, simply because it's quick and has column editing. (Column editing on <a href="http://en.wikipedia.org/wiki/E_%28text_editor%29">e Text Editor</a> is a bit harder to use.) When I am writing Unicode, I switch over to <a href="http://en.wikipedia.org/wiki/Notepad%2B%2B">Notepad++</a>. For large programs, I'm leaning towards <a href="http://en.wikipedia.org/wiki/ActiveState_Komodo">Komodo</a> right now, largely because Eclipse is bloated and Aptana was slow. (Komodo is slow too. Maybe I'll switch back.)</p>
<p>There's many other things on my "would love to have" features, like regular-expression search and replace, line sorting, code folding, brace matching, word wrapping, etc. Most of those, though, are either not too important, or most browsers already have them.</p>
<p>Well, there's the sad thing. I've been hunting for a good text editor for over 10 years now. May someone write a lightweight IDE with column editing.</p>

---

## Comments

<!-- wp-comments-start -->

- **Vinay** _29 May 2008 12:00 pm_:
  Anand:\
  \
  This is in response to your blog post at http://s-anand.net/In\_search\_of\_a\_good\_editor.html\
  \
  For some reason, couldn't post my comment through your web site.\
  \
  Notepad 2 is my favorite. Though even that doesn't have a "yes" in all four columns of your matrix. Auto-completion is missing and IMO for good reason (think responsiveness).\
  \
  http://www.flos-freeware.ch/doc/notepad2-Unicode.html
- **Roland** _16 Dec 2008 5:31 pm_:
  On Windows boxes, I use UltraEdit32 exclusively. AFAIK, it doesn't have autocompletion, but it loads and responds super-quickly, has column editing, syntax highlighting, and a gazillion other features that somehow don't hog any resources. Sadly, there is no Mac version, so I'm forced to use the inferior TextWrangler.
- **[Ben Karel](http://eschew.org/)** _4 Apr 2009 2:54 am_:
  How about jEdit and Vim?
- **[Software for my new laptop 2 | s-anand.net](http://www.s-anand.net/blog/software-for-my-new-laptop-2/)** _27 Sep 2011 7:16 pm_ _(pingback)_:
  [...] Editor: Didn’t have Unicode support a long time ago, so I [...]

<!-- wp-comments-end -->
