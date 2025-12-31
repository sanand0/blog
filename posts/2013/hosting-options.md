---
title: Hosting options
date: "2013-06-01T05:48:55Z"
categories:
  - how-i-do-things
wp_id: 2847
---

<p>I've been trying out a number of options for hosting recently, and have settled on <a href="http://aws.amazon.com/ec2/spot-instances/">Amazon spot instances</a>.</p> <p>Here were my options:</p> <ul> <li>Application hosting, like <a href="http://appengine.google.com/">Google AppEngine</a>. I used this a lot until 2 years ago. Then they changed their pricing, and I realised what “lock-in” means. I can’t just take that code and move it to another server. Besides, I’m a bit wary of <a href="/blog/goodbye-google/">Google pulling the plug</a>. <a href="https://www.heroku.com/">Heroku</a>? Same problem. I just want to take the code elsewhere and run it.  </li><li>Shared hosting, like <a href="http://www.hostgator.com/">Hostgator</a>. <a href="http://www.s-anand.net/">This blog</a> is run on Hostgator and I’m extremely happy with them. But the trouble is, with shared hosting, I don’t get to run long-running processes on any ports I like.  </li><li>Run you own servers. The problem here is quite simple: power cuts in India.  </li><li>Dedicated hosting, like <a href="http://aws.amazon.com/ec2/">Amazon EC2</a>, <a href="http://www.windowsazure.com/en-us/">Azure</a>, <a href="https://cloud.google.com/products/compute-engine">GCE</a>, etc. This remains as pretty much the main hosting option</li></ul> <p>I’m a price optimisation freak. So I ran the numbers for a year’s worth of usage. I was looking at the CPU cost of a large machine with 7-8GB RAM. Bandwidth and storage are negligible. The cost per hour worked out to:</p> <ul> <li>Amazon: $0.32 / hr in Singapore, $0.24 in Virginia  </li><li>Google: $0.29 / hr in Europe  </li><li>Microsoft: $0.32 / hr in US</li></ul> <p>The price is not all that different, but I need <a href="http://cloudharmony.com/speedtest">low latency</a>, so Singapore it what it’ll have to be.</p> <table class="numbers lines" style="color: #444"> <thead> <tr> <th>EC2 location</th> <th>Latency (ms)</th></tr></thead> <tbody> <tr> <td>Singapore</td> <td>139</td></tr> <tr> <td>Oregon, US</td> <td>334</td></tr> <tr> <td>Japan</td> <td>517</td></tr> <tr> <td>Ireland</td> <td>618</td></tr> <tr> <td>Australia</td> <td>620</td></tr> <tr> <td>California, US</td> <td>677</td></tr> <tr> <td>Virginia, US</td> <td>710</td></tr></tbody></table> <p>Now comes the choice of the right model. At $0.32 per hour, that’s $230 a month.</p> <p>Amazon offers some ways of getting this down. Instead of <a href="http://aws.amazon.com/ec2/pricing/#on-demand">on-demand instances</a>, I could go for <a href="http://aws.amazon.com/ec2/pricing/#reserved">reserved instances</a>. For a year of usage, that’d get the price down to about $131 a month, nearly halving it. ($739 upfront for a heavy utilisation large reserved instance, with $0.095 * 24 * 365.25 for the year.)</p> <p>In this case, I know I’ll need the servers for a year. Probably more, but then, I might want to switch later. So this isn’t a bad move. But we can do better. Amazon also offers <a href="http://aws.amazon.com/ec2/pricing/#spot">spot instances</a>. Spot instances might get shut down any time – but in reality, so can on-demand instances. I need to plan for it anyway. I’m not going to host anything that’s so sensitive that if it’s down for a few hours, I’ll have a problem.</p> <p>But what’s attractive is the pricing. Typically, it’s $0.04 per hour, making it about $29 per month. Even if it shoots up to twice that, at $58, it’s less than a fourth of the on-demand price and less than half the reserved instance price.</p> <p>I’ve managed to script the entire setup up sequence as shell scripts, and it takes less than an hour to get a new server up and running the software I need. I need to work out a decent backup mechanism. Plus, I could use more reliable storage like like <a href="http://aws.amazon.com/ebs/">Amazon’s EBS</a> to preserve the data. But on the whole, the pricing is far too attractive and makes the risks worthwhile.</p>

---

## Comments

<!-- wp-comments-start -->

- **[Anand Chitipothu](http://anandology.com/)** _2 Jun 2013 3:36 pm_:
  Did you look at Linode? I've been using Linode for couple of years and pretty happy with it. The 8GB RAM model costs about $160 per month. Sadly, they don't have a data center in Singapore. You can test the download speeds and latency of their data centers from https://www.linode.com/speedtest/.
- **[jouko](http://www.bestdoorlocksets.com)** _7 Jul 2013 4:21 pm_:
  I am using Inmotion hosting for my blog. May be i should also shift to amazon cloud.
- **[S Anand](http://www.s-anand.net/)** _3 Jun 2013 7:30 am_:
  I did try Linode early on, and it's a fairly decent option. It's just that for my needs, the $29/month that I can get with Amazon is too attractive.
- **Amit Chakradeo** _3 Jun 2013 8:33 pm_:
  If you don't mind occasional downtimes and occasional ummm complete loss of data :-), you can consider low end VPS boxes. (http://lowendbox.com/) You can find some decent deals if you check out the posts there...
- **Sriram** _15 Jan 2014 4:18 pm_:
  have u tried openshift ?

<!-- wp-comments-end -->
