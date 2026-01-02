---
title: Website load distribution using Javascript
date: "2007-09-01T12:00:00Z"
lastmod: "2009-02-25T08:57:09Z"
categories:
  - coding
wp_id: 75
---

My [music search engine](/hindi) shows a list of songs as you type -- sort of like Google's [autosuggest](http://www.google.nl/webhp?complete=1&hl=en) feature. I load my entire list of songs upfront for this to work. Though it's [compressed to load fast](/blog/hindi-songs-online/), each time you load the page, it downloads about 500KB worth of song titles.

My allotted bandwidth on [my hosting service](http://www.100webspace.com) is 3GB per month. To ensure I don't exceed it, I uploaded the songs list to an alternate free server: [Freehostia](http://www.freehostia.com/). This keeps my load down. If I exceed Freehostia's limit, my main site won't be affected -- just the songs. I also uploaded half of them to [Google Pages](http://pages.google.com/), to be safe.

This all worked fine... until recently. Google Pages has a relatively low bandwidth restriction. (Not sure what, and they won't reveal it, but my site is affected.) Freehostia is doing some maintenance, and their site goes down relatively often. So my song search goes down when any of these go down.

Now, these are rarely down simultaneously. Just one or the other. But whenever Freehostia is down, I can't listen to one bunch of songs. When Google Pages is down, I can't listen to another.

What I needed was a load distribution set-up. So I've made one in JavaScript.

Normally, I load the song list using an external javascript. I have a line that says:

```html
<script src="http://sanand.freehostia.com/songs/..."></script>
```

... and the song's loaded from Freehostia.

What I'd like to do is:

```javascript
loadscripts(
  "list.hasLoaded()",
  [
    "http://sanand.freehostia.com/songs/...",
    "http://root.node.googlepages.com/...",
    "http://www.s-anand.net/songs/...",
  ],
);
```

If the function can't load it from the first link, it loads it from the second, and so on, until `list.hasLoaded()` returns true.

Here's how I've implemented the function:

```javascript
function loadscripts(check, libs) {
  document.write(
    "<script src=\"" + libs.shift()
      + "\"><" + "/script>",
  );

  if (libs.length > 0) {
    document.write(
      "<script>if (!(" + check + ")) {"
        + "loadscripts(\"" + check + "\",[\"" + libs.join("\",\"") + "\"])"
        + "}</" + "script>",
    );
  }
}
```

The first `document.write` loads the first script in the list. The `if` condition checks if there's more scripts to load. If yes, the second `document.write` writes a script that

- checks whether the script is already loaded, and
- if not, loads the rest of the scripts using the same function.

I've expanded the sites that have these free songs as well. So now, as long as my [main site](/hindi) works, and **at least one** of the other sites work, the search engine will work.

PS: You can easily expand this to do random load distribution as well.

---

## Comments

<!-- wp-comments-start -->

- **Saurabh** _1 Sep 2007 12:00 pm_:
  I think its time for you now to start your own company..:) Guess you have some great ideas and u just need to put them on paper and start executing!
- **RK** _1 Sep 2007 12:00 pm_:
  Have you looked at the DOJO toolkit. It does have the feature you are looking for namely including scripts and verifying if the included script loaded. You might have to customize it a bit to suit your needs as its an entire toolkit.
- **S Anand** _1 Sep 2007 12:00 pm_:
  Saurabh -- you''re right. Problem is, I''m way to conservative!

  RK -- I know of Dojo, but didn''t know of this functionality: thanks! You''re right, I probably won''t want the entire toolkit, it''s quite bulky. But I''m sure I could learn from their implementation.
- **jawahar** _1 Sep 2007 12:00 pm_:
  Hai anand, can u suggest or give an insight on how to keep track of files which we work on?? not program codes ? but reports we read ,write n edit.. so as to retrieve it faster .. since ur working in such an environment can u share ur exp on naming files and organising it. thanks, jawahar
- **kgnanasekaran** _1 Sep 2007 12:00 pm_:
  Dear Mr.Anand, I really enjoyd in this website lot. R u tamilan??? superb site.. plz carry on.. thanks a lot..?? if u like we will bcome frnds.. am always available in my gmail..kgnanasekaran@gmai.com keep n touch. with warm regards, shekar.
- **x_Vanity_!** _1 Sep 2007 12:00 pm_:
  I really enjoy your website. Thanks for all the information you share.
- **Ramesk K palleri** _1 Sep 2007 12:00 pm_:
  Kudos anand.. u have done a great job on yous music site. keep going..
- **RAVINDRA** _1 Sep 2007 12:00 pm_:
  I REALLY ENJOY YOUR WEBSITE. BUT I WANT LISTEN SONGS IN YOUR MEDIA PLAYER.
- **oracle** _1 Sep 2007 12:00 pm_:
  where are you oflate?missing your post
- **krishna rao jallipalli** _1 Sep 2007 12:00 pm_:
  DEAR MR. ANAND, INFACT YOUR WEBSITE... SONGS..SUPERB. YOU ARE DOING A GREAT JOB. THOUGH YOU IN AMERICA...INFACT.. THESE TYPE OF WEBSITES.. SO MANY.. ARE BEING MAINTAINED BY NRIs. REALLY GREAT. MY HEARTY WISHES. REALLY I AM ENJOYING. WITH BEST REGARDS J KRISHNA RAO GUNTUR A.P CELL:9949517103

<!-- wp-comments-end -->
