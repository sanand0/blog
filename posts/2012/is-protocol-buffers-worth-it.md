---
title: Is Protocol buffers worth it?
date: "2012-08-01T05:48:22Z"
lastmod: "2012-08-15T12:58:42Z"
categories:
  - coding
wp_id: 2779
---

Google’s [Protocol Buffers](https://developers.google.com/protocol-buffers/) is a “language-neutral, platform-neutral, extensible mechanism for serializing structured data – **think XML, but smaller, faster, and simpler**”

XML is slow and large. There’s no doubting that. JSON’s my default alternative, though it’s a bit large. CSV’s ideal for tabular data, but ragged hierarchies are a bit difficult.

I was trying to see if Protocol Buffers would be smaller and faster, at least when using Python. I took JSON as the base, and checked the write speed, read speed and file sizes. Here’s the comparison:

[![image](/blog/assets/image-png.webp "image")](/blog/assets/image-png.webp)

Protocol Buffers are 17 times slower to write and almost 6 times slower to read than JSON files. File sizes are smaller, but then, all it takes is a simple gzip operation to compress the JSON files even smaller. Reading json.gz files is just 2% slower than JSON files, and writing them is only 4 times slower.

The code base is at <https://bitbucket.org/sanand0/protobuftest>

On the whole, it appears that GZipped JSON files are smaller, faster, and just as simple as Protocol Buffers. What am I missing?

**Update**: When you add GZipped CSV to the mix, it's twice as fast as GZipped JSON to read: clearly a huge win. It's only slightly slower to write, and but compresses a tiny bit more than JSON.

---

## Comments

<!-- wp-comments-start -->

- **Kaushik** _23 Aug 2012 7:40 am_:
  1. Typed data elements
  2. Language bindings
  3. Evolution via backward compatibility (as mentioned by Krishna in the comment above)
- **[Krishna](http://www.unclassroom.com/)** _1 Aug 2012 7:50 am_:
  Protocol Buffers offers the ability to version schema changes in a backwards compatible way. So, especially in analytics (client based - mobile / flash clients) that have custom analytics, you will have changes to the schema due to product changes / feature additions or removals and protocol buffers offers a painless way to deal with these changes.
  From:
  https://developers.google.com/protocol-buffers/docs/overview#whynotxml
  New fields could be easily introduced, and intermediate servers that didn't need to inspect the data could simply parse it and pass through the data without needing to know about all the fields.
  You would have to handle these in application code if you use JSON.
  Specifically, you don't want this:
  if (version == 3) {
  ...
  } else if (version > 4) {
  if (version == 5) {
  ...
  }
  ...
  }
- **Zheng** _1 Aug 2012 8:53 am_:
  Even within Google, Protocol Buffer processing in pure python is known to be extremely slow, about 100 times slower than optimized C implementation. It is recommended to use swigged C implementation within Python. Not sure if the C implementation has been open sourced.
- **[paintball equipment guy](http://68sports.com)** _16 Dec 2012 6:34 pm_:
  I've read on stackoverflow that in c#, the protobuf vs xml and json is much faster. very interesting this is not the case for py...
- **Ray Luo** _7 Aug 2013 8:24 am_:
  @Krishna, those versioning things are \*NOT\* the pitfalls of json. Nor even that google link suggests that. Json object is always flexible to contain new fields in new version, and old version servers can read only known fields.
- **Dean** _10 Jun 2013 7:20 am_:
  The python implementation of protocol buffers is horribly slow. It basically uses meta classes and reflection, whereas all other language bindings use compile-time generated code -- which is orders of magnitude faster.
  So while this comparison is probably fair for Python, other languages will have quite different results (in particular, I'd expect protocol buffers to be faster than JSON in C/C++ and Java).
- **Paul** _19 Oct 2014 8:14 am_:
  Protocol Buffers are able to contain strings with line endings etc. without breaking the container's syntax. You can also GZip protobuffer messages.

<!-- wp-comments-end -->
