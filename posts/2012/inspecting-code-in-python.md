---
title: Inspecting code in Python
date: "2012-09-04T03:49:08Z"
lastmod: "2012-09-04T03:53:33Z"
categories:
  - coding
wp_id: 2791
---

Lisp users would laugh, since they have [macros](http://en.wikipedia.org/wiki/Macro_(computer_science)), but Python supports some basic code inspection and modification.

Consider the following pieces of code:

```
margin = lambda v: 1 - v['cost'] / v['sales']
```

What if you wanted another function that lists all the dictionary indices used in the function? That is, you wanted to extract `cost` and `sales`?

This is a real-life problem I encountered this morning. I have 100 functions, each defining a metric. For example,

1. `lambda v: v['X'] + v['Y']`
2. `lambda v: v['X'] - v['Z']`
3. `lambda v: (v['X'] + v['Y']) / v['Z']`
4. ...

I had to plot the functions, as well as each of the corresponding elements ('X', 'Y' and 'Z') in the formula.

Two options. One: along with each formula, maintain a list of the elements used. Two: figure it out automatically.

Each function has a `func_code` attribute. So, when you take

```
margin = lambda v: 1 - v['cost'] / v['sales']
```

`margin.func_code` is a "code object". This has a bunch of interesting attributes, one of which is `co_consts`

```bash
>>> margin.func_code.co_consts
(None, 1, 'cost', 'sales')
```

There -- I just pick the strings out of that list and we're done (for simple functions at least.)

Check out <http://docs.python.org/reference/datamodel.html> and search for `func_` -- you'll find a number of interesting things you can do with functions, such as

1. Finding and changing the default parameters
2. Accessing the global variables of the namespace where the function was defined (!)
3. Replacing the function code with new code

Also search for `co_` -- you'll find some even more interesting things you can do with the code:

1. Find all local variable names
2. Find all constants used in the code
3. Find the filename and line number where the code was compiled from

Python also comes with a disassembly module [dis](http://docs.python.org/library/dis.html). A look at its [source](http://svn.python.org/projects/python/trunk/Lib/dis.py) is instructive.

---

## Comments

<!-- wp-comments-start -->

- **Kamaal** _4 Sep 2012 7:29 am_:
  This is cool. But Python needs to get Multiline Lambdas.
  One of the things Higher order Perl programmers miss in Python are muliline lamdas.
- **[S Anand](http://www.s-anand.net/)** _4 Sep 2012 11:40 am_:
  Yeah -- I miss that too. But I guess it'd go too strongly against the Python ethos of readability. I find it interesting that I miss multi-line lambdas ONLY when writing code. Never when reading it. So guess it isn't too bad a thing, given that I'm reading (my own, often) code 90% of the time, and writing it less than 10% :-)

<!-- wp-comments-end -->
