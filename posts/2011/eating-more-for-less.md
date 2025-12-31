---
title: Eating more for less
date: "2011-05-19T18:12:23Z"
lastmod: "2021-10-06T15:56:23Z"
categories:
  - how-i-do-things
  - visualisation
wp_id: 2649
---

A couple of years ago, I managed to <a href="/blog/my-weight-line/">lose a fair bit of weight</a>. At the start of 2010, I started putting it back on, and the trajectory continues. I’m at the stage where I seriously need to lose weight.

I subscribe to <a href="http://www.fourmilab.ch/hackdiet/">The Hacker’s Diet</a> principle – that you lose weight by eating less, not exercising.

<blockquote>An hour of jogging is worth about one Cheese Whopper. Now, are you going to really spend an hour on the road every day just to burn off that extra burger?

You don't exercise to lose weight (although it certainly helps). You exercise because <em>you'll live longer</em> and <em>you'll feel better</em>.</blockquote>
I’m afraid <a href="http://www.google.com/publicdata?ds=wb-wdi&amp;met=sp_dyn_le00_in&amp;idim=country:GBR&amp;dl=en&amp;hl=en&amp;q=life+expectancy+graph">I’ll live too long</a> anyway, so I won't bother exercising just yet. It's down to eating less.

Sadly, I like food. So to make my “diet” work, I need foods that add less calories per gram. Usually, when browsing stores, I check these manually. But being a <a href="/blog/how-i-buy-gadgets/">geek</a>, I figured there’s an easier way.

Below is a graph of some foods (the kind I particularly need to avoid, but still end up eating). The ones on the top add a lot of calories (per 100g), and better to avoid. The ones at the right cost a lot more. Now, I’m no longer at the point where I need to worry about food expenses, but still, I can’t quite kick the habit, also you might want to check out this <a href="https://rootine.co/blogs/ourscience/can-a-little-vitamin-b12-really-hurt-you">Rootine's comparison of B12 methylcobalamin and cyanocobalamin</a> that will help you in your diet.

Hover over the foods to see what they are, and click on them to visit the product. (If you’re using an RSS reader and this doesn’t work, <a href="/blog/eating-more-for-less">read on my site</a>.)

<style>
.map { position: relative; width: 600px; height: 600px; }<br />
.map a { position: absolute; display: block; width: 6px; height: 6px; font-size: 6px;<br />
-moz-box-shadow: 1px 1px 2px black;<br />
-webkit-box-shadow: 1px 1px 2px black;<br />
box-shadow: 1px 1px 2px black;<br />
filter:progid:dximagetransform.microsoft.dropshadow(color='#222222',offx='1',offy='1');<br />
}<br />
.map a:hover { z-index: 100; width:16px; height: 16px; margin-left: -5px; margin-top: -5px; border: 2px solid black;<br />
filter:progid:dximagetransform.microsoft.dropshadow(color='#222222',offx='1',offy='1');<br />
}<br />
.desserts a { background-color: #a7c0de; border: 1px solid #4f81bd; }<br />
.icecream a { background-color: #c0504d; border: 1px solid #632523; }<br />
.snacks a { background-color: #9bbb59; border: 1px solid #4f6228; }<br />
.cake a { background-color: #8064a2; border: 1px solid #403152; }<br />
.cereals a { background-color: #fbcba3; border: 1px solid #f79646; }<br />
.map input { position: absolute; right: 0px; top: 0px; }<br />
a.hidden { display: none; }<br />
</style>
<div class="map"><img src="/blog/assets/legend.webp" />
<input type="text" placeholder="search" />
<div class="icecream">

</div>
<div class="snacks">

</div>
<div class="desserts">

</div>
<div class="cereals">

</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.3.1/dist/jquery.min.js"></script>
<script><br />
(function($){<br />
var timeout = 0;<br />
var $foods = $('.map a');<br />
var $search = $('.map input');</p>
<p>function search() {<br />
  var keyword = $search.val();<br />
  keyword = new RegExp(keyword, "i");<br />
  $foods.each(function() {<br />
    var $this = $(this);<br />
    if ($this.attr('title').match(keyword)) { $this.removeClass('hidden'); }<br />
    else { $this.addClass('hidden'); }<br />
  });<br />
}</p>
<p>$search.keyup(function(e) {<br />
  if (timeout) { clearTimeout(timeout); }<br />
  timeout = setTimeout(search, 200);<br />
});<br />
})(jQuery)<br />
</script>

(The data was picked from <a href="http://www.tesco.com/groceries/">Tesco</a>.)

It’s interesting that cereals are in the middle of the calorie range. I always thought they’d be low calories per gram. Turns out that if I want to to have such foods, I’m better off with desserts or ice creams (<a href="http://www.tesco.com/groceries/Product/Details/?id=267292296">profiterole</a>, <a href="http://www.tesco.com/groceries/Product/Details/?id=267289744">lemon meringue</a> or <a href="http://www.tesco.com/groceries/Product/Details/?id=256407381">tiramisu</a>). In fact, even <a href="http://www.tesco.com/groceries/Product/Details/?id=251736868">jams</a> have less calories than cereals.

But there <em>are</em> some desserts to avoid. <a href="http://www.tesco.com/groceries/Product/Details/?id=261591602">Nuts</a> are a disaster. So are <a href="http://www.tesco.com/groceries/Product/Details/?id=259614128">chocolates</a>. <a href="http://www.tesco.com/groceries/Product/Details/?id=256582494">Gums</a>, <a href="http://www.tesco.com/groceries/Product/Details/?id=266282937">dates</a> and <a href="http://www.tesco.com/groceries/Product/Details/?id=265796452">honey</a> are in the middle – about as good as cereals. <a href="http://www.tesco.com/groceries/Product/Details/?id=254694261">Salsa dip</a> seems surprisingly low. <a href="http://www.tesco.com/groceries/Product/Details/?id=250337392">Custards</a> seem to hit the sweet spot – cheap, and very low in calories. Same for <a href="http://www.tesco.com/groceries/Product/Details/?id=260667072">jellies</a>.

So: custards and jelly. My daughter’s going to be happy.

---

## Comments

<!-- wp-comments-start -->

- **Srinivas** _2 Jun 2011 2:30 pm_:
  well looking at the graph, the answer is simple. just dont go to Tesco!
  and seriously , the most important rule of thumb to eat right is, never eat anything that comes in a packet.
- **[Sathya](http://nullpointers.wordpress.com)** _20 May 2011 8:11 am_:
  Saar what about "arachi vitta kozhlambu", thovaiyal, medu bonda, Rasa vadai , usili ... and items form "Grand Sweets and Snacks" ? Where are these ? these are my staples ;-(
  jk ... Nice one ( some surprises as well ).
- **Sumit Dhar** _20 May 2011 4:34 pm_:
  Anand,
  I know it sound crazy but increasingly research is showing that not all calories are equal. What that means is that, a calorie from carbs might result in greater fat / weight gain thank a calorie from proteins. (Reference: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC506782/)
  Additionally, processed sugar is something you should avoid. Sugar causes insulin spikes that results in greater fat storage. Sames goes for carbs. Even the desserts you mention, should ideally be avoided. (Reference: http://www.youtube.com/watch?v=dBnniua6-oM)
  On the other hand, I am consuming quite a bit of nuts on a daily basis: almonds, cashews, peanuts. They are a good source of proteins and vital fatty acids. If you are a veggie, cottage cheese is another good source of proteins (along with fat too). Milk is another source of proteins along with calcium.
  Why we get Fat by Gary Taubes is a good book to check out. While I am not a big believer in rapid fat loss or fast weight reduction, I have read good things about the Rapid Fat Loss Handbook. It reiterates ideas from Why we get Fat.
  In short, don't focus on calories. Focus on grams of carbs consumed per day.
  Cheers,
  Sumit
- **[D](http://dharmendra.me)** _26 May 2011 6:03 am_:
  Anand,
  I would recommend you also consider one major strategy - nutrient timing, which I used to good effect over the last 6 months while consuming the same no. of calories.
  Also if you really like chocolate, you can try dark chocolate as an alternative - lower calories per gram.
  Even for vegetarians, protein shakes derived from whey and soy are a great alternative to other foods. I have employed each of these and can vouch for their effectiveness in managing weight
- **[Shankar V](http://www.infosys.com)** _27 May 2011 9:00 pm_:
  I agree with you. Nothing like cutting on food to lose weight. Exercise requires perseverance and focus....I lack both. :)
  Cutting down on food also has issues.....you reduce intake for a few days, then pop comes a wedding or function where you get 'ilai potta sappadu' and all control is lost. You tell yourself, just this once and then very soon you are back to your original eating habits.
  Best option - must be born with a body that does not put on weight. Period!!! I envy those folks. :)
- **Saurabh Mittal** _15 Jan 2014 12:04 pm_:
  Nice one Anand! I was at 82 kgs a few years back and managed to come down to 72 . This was a result of both exercise (have run two half marathons so far in 2012 and then again in 2013) and change of eating habits (more of proteins and less of carbs). There is a nice book as well by Tim Ferris (The Four Hour Body), but in short definitely look at incorporating more exercise in your routine..Also as Sumit pointed out above - processed sugars and salt are the two major culprits! We don't even realize how these are found in plenty in most of the foods! Keeping track of weight on a daily basis definitely is a good habit!
  Cheers
  Saurabh

<!-- wp-comments-end -->
