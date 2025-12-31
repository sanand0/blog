---
title: How to extend Markdown with custom blocks
date: "2021-01-08T09:37:48Z"
lastmod: "2021-01-08T09:37:52Z"
categories:
  - coding
wp_id: 3059
---

One problem I've had in Markdown is rendering a content in columns.

On Bootstrap, the markup would look like this:

```markup
<div class="row">
  <div class="col">...</div>
  <div class="col">...</div>
</div>
```

How do we get that into Markdown without writing HTML?

On Python, the [attribute lists extension](https://python-markdown.github.io/extensions/attr_list/) lets you add a class. For example:

```markdown
This is some content
{: .row}
```

... renders `<p class="row">This is some content</p>`.

But I can't do that to multiple paragraphs. Nor can I next content, i.e. add a `.col` inside the `.row`.

Enter [markdown-customblocks](https://pypi.org/project/markdown-customblocks/). It's a Python module that extends [Python Markdown](https://python-markdown.github.io/). This lets me write:

```markdown
::: row
::: col
Content in column 1
::: col
Content in column 2
::: row
::: col
Content in column 1
::: col
Content in column 2
```

This translates to:

```markup
<div class="row">
  <div class="col">Content in column 1</div>
  <div class="col">Content in column 2</div>
</div>
```

Better yet, we can create our own custom HTML block types. For example, this code:

```python
from markdown import Markdown
from customblocks import CustomBlocksExtension

def audio(ctx, src, type="audio/mp3"):
    return f'''<audio src="{src}" type="{type}">
      {ctx.content}
    </audio>'''

md = Markdown(extensions=[
    CustomBlocksExtension(generators={
        'audio': audio
    }),
])
```

... lets you convert this piece of Markdown:

```python
md.convert("""
::: audio src="mymusic.ogg" type="audio/ogg"
    Your browser does not support `audio`.
""")
```

... into this HTML:

```markup
<audio src="mymusic.ogg" type="audio/ogg">
  Your browser does not support <code>audio</code>.
</audio>
```

[markdown-customblocks](https://pypi.org/project/markdown-customblocks/) is easily the most useful Python module I discovered last quarter.
