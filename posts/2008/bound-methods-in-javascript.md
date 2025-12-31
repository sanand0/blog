---
title: Bound methods in Javascript
date: "2008-11-12T12:00:00Z"
lastmod: "2011-12-02T22:11:39Z"
categories:
  - coding
wp_id: 24
---

The [popular](https://developer.mozilla.org/en/Core_JavaScript_1.5_Guide/Class-Based_vs._Prototype-Based_Languages) [way](http://javascript.crockford.com/prototypal.html) to create a class in Javascript is to define a function and add methods to its prototype. For example, let's create a class `Node` that has a method `hide().`

```javascript
var Node = function(id) {
  this.element = document.getElementById(id);
};
Node.prototype.hide = function() {
  this.style.display = "none";
};
```

If you had a header, say <h1 id="header">Heading</h1>, then this piece of code will hide the element.

```javascript
var node = new Node("header");
node.hide();
```

If I wanted to hide the element a second later, I am tempted to use:

```javascript
var node = new Node("header");
setTimeout(node.hide, 1000);
```

... except that it won't work. `setTimeout` has no idea that the function `node.hide` has anything to do with the object `node`. It just runs the function. When `node.hide()` is called by setTimeout, the `this` object isn't set to `node`, it's set to `window`. `node.hide()` ends up trying to hide `window`, not `node`.

The standard way around this is:

```javascript
var node = new Node("header");
setTimeout(function() {
  node.hide();
}, 1000);
```

I've been using this for a while, but it gets tiring. It's so easy to forget to do this. Worse, it [doesn't work very well inside a loop](https://developer.mozilla.org/en/Core_JavaScript_1.5_Guide/Working_with_Closures#Creating_closures_in_loops.3a_A_common_mistake):

```javascript
for (var id in ["a", "b", "c"]) {
  var node = new Node(id);
  setTimeout(function() {
    node.hide();
  }, 1000);
}
```

This actually hides node "c" thrice, and doesn't touch nodes "a" and "b". You've got to remember to wrap every function that contains a function in a loop.

```javascript
for (var id in ["a", "b", "c"]) {
  (function() {
    var node = new Node(id);
    setTimeout(function() {
      node.hide();
    }, 1000);
  })();
}
```

Now, compare that with this:

```javascript
for (var id in ["a", "b", "c"]) {
  setTimeout((new Node(id)).hide, 1000);
}
```

Wouldn't something this compact be nice?

To do this, the method `node.hide` must be bound to the object node. That is, `node.hide` must know that it belongs to `node`. And when we call `another_node.hide`, it must know that it belongs to `another_node`. This, incidentally, is the way most other languages behave. For example, on [python](http://www.python.org/), try the following:

```python
>>> class Node:
...     def hide():
...             pass
...
>>> node = Node()
>>> node
<__main__.Node instance at 0x00BA32D8>
>>> node.hide
<bound method Node.hide of <__main__.Node instance at 0x00BA32D8>>
```

The method `hide` is bound to the object node.

To do this in Javascript, instead of adding the methods to the prototype, you need to do two things:

1. Add the methods to the object in the constructor
2. Don't use `this`. Set another variable called `that` to `this`, and use `that` instead.

```javascript
var Node = function(id) {
  var that = this;
  that.element = document.getElementById(id);
  that.hide = function() {
    that.element.style.display = "none";
  };
};
```

Now node.hide is bound to node. The following code will work.

```javascript
var node = new Node("header");
setTimeout(node.hide, 1000);
```

I've taken to using this pattern almost exclusively these days, rather than prototype-based methods. It saves a lot of trouble, and I find it makes the code a lot compacter and easier to read.

---

## Comments

<!-- wp-comments-start -->

- **Hari K T** _3 Jan 2009 6:52 am_:
  Good article . .. . .\
  Great work . I am trying to implement it tooo....
- **Mani** _2 Dec 2011 8:25 pm_:
  A small correction though
  var Node = function(id) {
  var that = this;
  that.element = document.getElementById(id);
  that.hide = function() {
  that.element.style.display = "none";
  }
  };
- **[S Anand](http://www.s-anand.net/)** _2 Dec 2011 10:12 pm_:
  Thanks Mani -- I've updated the code to reflect your correction.

<!-- wp-comments-end -->
