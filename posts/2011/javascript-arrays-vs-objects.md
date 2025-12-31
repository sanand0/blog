---
title: Javascript arrays vs objects
date: "2011-10-06T13:43:22Z"
categories:
  - coding
wp_id: 2690
---

<p><strong>Summary</strong>: Arrays are a lot smaller than objects, but only slightly faster on newer browsers.</p> <p>I’m writing an in-memory Javascript app that handles several thousand rows. Each row could be stored either as an array <code>[1,2,3]</code> or an object <code>{"x":1,"y":2,"z":3}</code>. Having read up on the <a href="http://news.qooxdoo.org/javascript-array-performance-oddities-characteristics">performance of arrays vs objects</a>, I thought I’d do a few tests on storing numbers from 0 to 1 million. The results for Chrome are below. (Firefox 7 was similar.)</p> <table style="color: #444" class="numbers lines"> <tbody> <tr> <td>&nbsp;</td> <td>Time</td> <td>Size (MB)</td></tr> <tr> <td>Array: <code>x[i] = i</code></td> <td>2.44s</td> <td>8</td></tr> <tr> <td>Object: <code>x[i] = i</code></td> <td>3.02s</td> <td>57</td></tr> <tr> <td>Object: <code>x["a_long_dummy_testing_string"+i]=i</code></td> <td>4.21s</td> <td>238</td></tr></tbody></table> <p>The key lessons for me were:</p> <ul> <li>Browsers used to process arrays MUCH faster than objects. This gap has now shrunk.</li> <li>However, arrays are still better: not for their speed, but for their space efficiency. </li> <li>If you’re processing a million rows or less, don’t worry about memory. If you’re storing stuff as arrays, you can store 128 columns in 1GB of RAM (1024/8=128).</li></ul>

---

## Comments

<!-- wp-comments-start -->

- **dineshsaravanank** _11 Oct 2011 5:27 am_:
  Also, I got completely different numbers than yours. Array x[i]=i, 43ms | Object x[i]=i, 43ms | Object x["akey"+i]=i, 2443ms. I tested in chrome, as you can see the keyed object is \*significantly\* slower in my case...
- **[S Anand](http://www.s-anand.net/)** _11 Oct 2011 10:38 pm_:
  @dinesh: When object keys are integers, browsers tend to optimise them in an array-like fashion. That explains the {1:1, 2:2} being faster than {"a1":1,"a2":2}.
  @kalpesh, the main point of this,actually, was that performance is increasingly less of a worry for most applications. Browsers are fast enough. So the choice of language is becoming increasingly less performance driven and more ease driven.
- **dineshsaravanank** _11 Oct 2011 5:18 am_:
  After reading this I was curious about 1) How is the read performance, 2) How does the object with long key perform.
  So I ran some tests. And,
  1. as expected reads are much faster than the writes and there is no significant difference between array and object when it came to read.
  2. Longer keys take more time to execute, smaller keys are significantly faster than very long keys. But there are some surprises here. An object {"1":1,"2":2,"3":3} is much faster than {"a1":1, "a2":2, "a3":4}, while object {"a1":1,"a2":2} and object {"alittlelong1":1, "alittlelong2":2} are almost same.
     You can see the tests here http://jsfiddle.net/ETAb9/
- **Kalpesh** _12 Oct 2011 4:56 pm_:
  I agree. My question was to think of it, in terms of memory consumption.
  Your thoughts?
- **Kalpesh** _10 Oct 2011 10:50 am_:
  Considering this, do you think OO based languages add overhead to space it occupies when run, in memory?
- **[Arun](http://www.arunrocks.com)** _13 Oct 2011 6:09 pm_:
  Anand,
  This is because **object** is a fundamental data type in Javascript and an **Array** is implemented as a special kind of **object**. Hence the lookups (the Time column) would be implemented as a hash map lookup in both cases.
  However the storage could be an interesting case. As one of the early gotchas of Javascript teaches us:
  `Person.Name` is equivalent to `Person['Name']`
  But in the case of Array's some magic is applied leading to optimisations in storage. Hence I suppose rather than storing unicode strings for "0", "1" etc., they are stored as integers.
  Javascript, like English, is berry phunny language :)
- **Joe** _29 Feb 2016 1:02 pm_:
  I ran some tests and was surprised that array access is only slightly faster. Something strange has to be going on with that. My test compares numeric entries either way. The object implementation normally has the extra work of casting to string and hashing. I have a feeling it will be different with non-numeric versus numeric keys. Still, it hints at something strange going on.

<!-- wp-comments-end -->
