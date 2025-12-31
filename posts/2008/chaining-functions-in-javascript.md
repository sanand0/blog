---
title: Chaining functions in Javascript
date: "2008-02-18T12:00:00Z"
categories:
  - coding
wp_id: 58
---

One of the coolest features of [jQuery](http://jquery.com/) is the ability to chain functions. The output of a function is the calling object. So instead of writing:

```javascript
var a = $("<div></div>");
a.appendTo($("#id"));
a.hide();
```

... I can instead write:

```bash
$("<div></div>").appendTo($("#id")).hide();
```

A reasonable number of predefined Javascript functions can be used this way. I make extensive use of it with the `String.replace` function.

But where this feature is not available, you an create it in a fairly unobstrusive way. Just add this code to your script:

```javascript
Function.prototype.chain = function() {
  var that = this;
  return function() {
    // New function runs the old function
    var retVal = that.apply(this, arguments);
    // Returns "this" if old function returned nothing
    if (typeof retVal == "undefined") return this;
    // else returns old value
    else return retVal;
  };
};
var chain = function(obj) {
  for (var fn in obj) {
    if (typeof obj[fn] == "function") {
      obj[fn] = obj[fn].chain();
    }
  }
  return obj;
};
```

Now, `chain(object)` returns the same object, with all its functions replaced with chainable versions.

What's the use? Well, take the [Google AJAX search API](http://code.google.com/apis/ajaxsearch/). Normally, to search for the top 8 "Harry Potter" PDFs on esnips.com, I'd have to do:

```javascript
var searcher = new google.search.WebSearch();
searcher.setQueryAddition("filetype:PDF");
searcher.setResultSetSize(google.search.Search.LARGE_RESULTSET);
searcher.setSiteRestriction("esnips.com");
searcher.setSearchCompleteCallback(onSearch);
searcher.execute("Harry Potter");
```

Instead, I can now do this:

```javascript
chain(new google.search.WebSearch())
  .setQueryAddition("filetype:PDF")
  .setResultSetSize(google.search.Search.LARGE_RESULTSET)
  .setSiteRestriction("esnips.com")
  .setSearchCompleteCallback(onSearch)
  .execute("Harry Potter");
```

(On the whole, it's probably not worth the effort. Somehow, I just like code that looks like this.)

---

## Comments

<!-- wp-comments-start -->

- **T** _18 Feb 2008 12:00 pm_:
  looks sweet!

<!-- wp-comments-end -->
