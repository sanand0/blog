---
title: Modular CSS frameworks
date: "2010-09-19T21:34:37Z"
categories:
  - coding
wp_id: 2532
---

A fair number of the CSS frameworks I’ve seen – [Blueprint](http://www.blueprintcss.org/), [Tripoli](http://devkick.com/lab/tripoli/), [YUI](http://developer.yahoo.com/yui/3/), [SenCSS](http://sencss.kilianvalkhof.com/) – are monolithic. What I’d like is to be able to mix and match specific components of these.

For example, [960.gs](http://960.gs/) has a simple grid system that I’d love to combine with the vertical rhythm that [SenCSS](http://sencss.kilianvalkhof.com/) offers. (Vertical rhythm ensures that sentences align vertically.) I’d love to have a CSS framework that just sets the fonts, for example, and touches nothing else. Or something that defines the colour schemes, and lets you change the theme like Microsoft Office does.

## LessCSS

[Less CSS](http://lesscss.org/) has been invaluable in helping with this. It extends the CSS language without deviating significantly from it. Compared to [SASS](http://sass-lang.com/) and [CleverCSS](http://sandbox.pocoo.org/clevercss/), I’d say it has a better chance of getting incorporated as into, say, CSS4.

**LessCSS offers variables**. I can define a variable:

```css
@foreground : #112233;
```

and use it like this:

```css
h1 { color: @foreground; }
a:hover { background-color: @foreground; }
```

When I change @foreground, it’s replaced everywhere.

**LessCSS offers multiple inheritance**.

```css
.highlight { color: red; }
.button { border-radius: 10px; }
.action {
  .highlight;
  .button;
}
```

This assigns the properties of the highlight and the button classes to the action class. Any changes made to the parents automatically get inherited.

**LessCSS has a Javascript pre-processor**. So I can include it directly in the HTML, and add the pre-processor, which converts it into CSS.

```xml
<link href="style.less" rel="stylesheet/less"/>
<script src="less.js"></script>
```

I now use LessCSS as the basis of all new projects.

## CSS libraries

My first attempt to consolidate modular CSS libraries is at [bitbucket.org/sanand0/csslibs](http://bitbucket.org/sanand0/csslibs). As far as possible, I’ve tried to avoid creating new libraries, or even tweaking existing ones. Over time, I hope to completely eliminate any new code.

There are two types 2 types of libraries. Some just have variable definitions. Others actually define styles. For example, I’ve got three libraries that just define variables:

- **color\_themes.less**: Defines a standard set of color themes (based on the Office 2007 color themes)
- **font\_stacks.less**: Defines Web-safe font stacks (based on [Sitepoint's article](http://www.sitepoint.com/article/eight-definitive-font-stacks/))
- **backgrounds.less**: Transparent background patterns (randomly useful images)

Including the above libraries will have no effect. You need to explicitly use them. For example:

```css
@import "font_stacks.less";         // Does nothing
h1 { font-family: .font[@serif]; }  // Makes H1 a serif font
```

The following libraries define styles. Including them will define new classes or change the style of tags / classes.

- **reset.less**: Resets default styles consistently across browsers. I chose [YUI3 CSS Reset](http://github.com/yui/yui3/blob/master/src/cssreset/css/reset.css) arbitrarily. I think [HTML5boilerplate](http://github.com/paulirish/html5-boilerplate)’s CSS reset may be a better choice, though.
- **grids.less**: Defines classes for fixed and fluid grids. I choose [YUI3 CSS Grids](http://github.com/yui/yui3/blob/master/src/cssgrids/css/grids.css) over [960.gs](http://960.gs/) (which I’ve used for some years) because of its ability to offer fixed as well as fluid layouts, and the sheer brilliance of its minimality.
- **lineheight.less**: Sets font sizes, ensuring that lines have a vertical rhythm. This is a stripped-down version of [SenCSS](http://sencss.kilianvalkhof.com/source/sen.css), but over time, I’ll phase this out and use some standard framework someone comes up with.

Between these, I think the base infrastructure for most applications is in place. What’s required next are widgets. Specifically, I’d like:

- **Buttons**. A really good, cross-browser, non-image-based button that offers rounded corners, gradients and borders.
- **Forms**. Consistent form styling, without forcing me to use a specific form layout.
- **Icons**. A standard icon library with replaceable CSS sprite-sets.

I’ll try keep the [code](http://bitbucket.org/sanand0/csslibs) updated as I find these. Do pass me any suggestions you may have.

---

## Comments

<!-- wp-comments-start -->

- **Abhishek Singh** _20 Sep 2010 6:23 pm_:
  This is really cool... I think i wont be facing any build kit issues from now on :-)

<!-- wp-comments-end -->
