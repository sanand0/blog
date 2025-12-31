---
title: Shortening sentences
date: "2010-11-10T08:16:37Z"
categories:
  - coding
  - data
wp_id: 2554
---

<p>When writing <a href="http://www.mixamail.com/">Mixamail</a>, I wanted tweets automatically shortened to 140 characters – but in the most readable manner. </p> <p>Some steps are obvious. Removing redundant spaces, for example. And <a href="http://en.wikipedia.org/wiki/URL_shortening">URL shortening</a>. I use <a href="http://bit.ly/">bit.ly</a> because it has an API. I’ll switch to <a href="http://goo.gl/">Goo.gl</a>, once theirs is out. </p> <p>I tried a few more strategies:</p> <ol> <li>Replace words with short forms. “u” for “you”, “&amp;” for and, etc.  </li><li>Remove articles – a, an, the  </li><li>Remove optional punctuation – comma, semicolon, colon and quotes, in particular  </li><li>Replace “one” with “1”, “to” or “too” with 2, etc. “Before” becomes “Be4”, for example  </li><li>Remove spaces after punctuations. So “a, b” becomes “a,b” – the space after the comma is removed  </li><li>Remove vowels in the middle. nglsh s lgbl wtht vwls.</li></ol> <p>How did they pan out? I tested out these on the English sentences on the <a href="http://www.edrdg.org/wiki/index.php/Tanaka_Corpus">Tanaka Corpus</a>, which has about 150,000 sentences. (No, they’re not typical tweets, but hey…). By just doing these, <em>independently</em>, here is the percentage reduction in the size of text:</p> <table class="lines" border="0" cellspacing="0" cellpadding="0" width="600"> <tbody> <tr> <td valign="top" width="65">2.0%</td> <td valign="top" width="535">Remove optional punctuations – comma, semicolon, colon and quotes</td></tr> <tr> <td valign="top" width="65">2.2%</td> <td valign="top" width="535">Remove spaces after punctuations. So “a, b” becomes “a,b” </td></tr> <tr> <td valign="top" width="65">3.3%</td> <td valign="top" width="535">Replace words with short forms. “u” for “you”, “&amp;” for and, etc.</td></tr> <tr> <td valign="top" width="65">3.3%</td> <td valign="top" width="535">Replace “one” with “1”, “to” or “too” with 2, etc.</td></tr> <tr> <td valign="top" width="65">6.7%</td> <td valign="top" width="535">Remove articles – a, an, the</td></tr> <tr> <td valign="top" width="65">18.2%</td> <td valign="top" width="535">Remove vowels in the middle</td></tr></tbody></table> <p>Touching punctuations doesn’t have much impact. There aren’t that many of them anyway. Word substitution helps, but not too much. I could’ve gone in for a wider base, but the key is the last one: removing vowels in the middle kills a whopping 18%! That’s tough to beat with any strategy. So I decided to just stop there.</p> <p>The overall reduction, applying all of the above, is about 22%. So there’s a decent chance you can type in a 180-character tweet, and <a href="http://www.mixamail.com/">Mixamail.com</a> will still tweet it intelligibly.</p> <p>I had one such tweet a few days ago. I try and stay well within 140, but this one was just too long.</p> <blockquote>The Lesson: If you're writing an app (or building anything), find a use for yourself. There's no better motivation -- and it won't ever be a wasted effort.</blockquote> <p>That was 156 characters. It <a href="http://twitter.com/#!/sanand0/status/1550404978483200">got shortened to</a>:</p> <blockquote>Lesson If u're writing app (or building anything) find use 4 yourself. There's no better motivation -- &amp; it won't ever be wasted ef4t.</blockquote> <p>Perfectly acceptable.</p> <p>You may notice that Mixamail didn’t have to employ vowel shortening. It makes the most readable shortenings first, checks if it’s within 140, and tries the next only if required.</p> <p>If anyone has a simple, readable way of shortening Tweets further, please let me know!</p>

---

## Comments

<!-- wp-comments-start -->

- **408wij** _11 Nov 2010 5:17 am_:
  1. Are removing punctuation and removing spaces after punctuation mutually exclusive, or do you have a rule for determining which punctuation is optional?
  2. You give the example of "before" going to "be4." It could go to "b4" with the rule that the "be" and "de" prefixes reduce to "b" and "d."
  3. You have "you're" going to "u're." You could expand "you're" to "you are" and then reducing to "u r."
  4. For readability, I suggest preserving the first and last letters of words. (Compare with http://www.boingboing.net/2003/09/14/scrambled-words-are-.html) E.g., reduce "English" to "Englsh" instead of to "nglsh."
     Finally, I the point of the 140-char limit is to limit the scope of a tweet to a simple thought. Shortening words is cheating. But, if you're going to cheat, I suggest an unshortener for the receiver of tweets.
     408wij
- **Arthi** _10 Nov 2010 12:38 pm_:
  I prefer tweetlonger.com.
  Tweets look much better when they don't go through reductions.
- **V** _26 Nov 2010 8:36 am_:
  I am writing something similar. Will share once done.
  But my preliminary attempts brought down the characters atleast 10% lesser than this. For eg. You have got 133 chars , whereas my system results in 123. I shall implement some more NLP techniques and bring it down to an acceptable level without sacrificing the semantics
- **iwebtalk** _11 Jan 2011 8:41 pm_:
  I use utwitmore.com .. no need to worry about 140 characters

<!-- wp-comments-end -->
