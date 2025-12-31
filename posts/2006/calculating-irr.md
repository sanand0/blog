---
title: Calculating IRR
date: "2006-08-25T12:00:00Z"
lastmod: "2019-09-27T04:27:55Z"
categories:
  - simple-explanations
wp_id: 251
---

<p>Recently, I was helping a bank define <a href="http://en.wikipedia.org/wiki/Basel_2">Basel 2</a> requirements.</p>
<p>For every dollar a bank lends, at least 8 cents should come from its own pocket, and the rest from its depositors. But a risky $1 loan may be like a $1.5 loan, whereas a $1 Government loan may be like a $0.5 loan. This is the "risk-weighted asset" (RWA) value. <b>Basel 2 says 8% of risk-weighted assets should come from the bank's pocket.</b></p>
<p>I was trying to convince the people who were maintaining the leasing software that the RWA of a lease is the <a href="http://en.wikipedia.org/wiki/Net_present_value">NPV</a> of its future cash flows, and they had a whole lot of questions.</p>
<p><b>"What is this NPV?"</b></p>
<p>You can put 90 cents in the bank today at 11% and get $1 next year. So $1 next year is worth 90 cents today. When a customer pays $100 over the next 10 months, it's worth less than $1000 today. That's the NPV. <b>The NPV is what you put in the bank today to get that cash flow</b>: $100 over the next 10 months</p>
<p><b>"So why should we use NPV for leases?"</b></p>
<p>That's because <b>when a lease is cancelled, the closure payment is the NPV</b>. If you take a lease for 10 months at $100 a month, this includes the interest. If you terminate the lease after 5 months, you won't pay $500 for the remaining 5 months. You'll pay less -- the NPV of those $100 for 5 months. So there is some logic to using NPV as the RWA.</p>
<p><b>"OK, so how do we calculate the NPV?"</b></p>
<p>You divide each cash flow by (1 + r)^n, where r is the <a href="http://en.wikipedia.org/wiki/Internal_rate_of_return">internal rate of return</a>, and n is the number of years. Then you add them up. You'll get a number less than the sum of cash flows.</p>
<p><b>"And how do we calculate this IRR?"</b></p>
<p>(sheepishly) The IRR is that interest rate for which the NPV is zero.</p>
<p>And we got stuck here, because their software didn't have an IRR function, and <b>the definitions for IRR and NPV are circular</b>.</p>
<p>To do this in Excel is simple. Just enter the cash flow values. So, if on a <a href="https://qvcredit.sg/personal-loans-singapore/">cash loan</a> of $500, you paid $100 for 6 months, and use the IRR function, as shown below. Your monthly IRR is 5.47%.</p>
<p><iframe src="http://spreadsheets.google.com/pub?key=poz40xh4E1ueTl7xngr7hNg&amp;output=html&amp;gid=0&amp;single=true&amp;widget=true" width="300" height="250" frameborder="0"></iframe></p>
<p>But we needed their AS/400 system to do it as well, and it didn't have the IRR function.</p>
<p>After a few weeks of digging around, I found a paper that said <b>you can calculate the IRR iteratively</b>. Let</p>
<ul>
<p><li><i>npv</i> be the NPV given an IRR and cash flows</li>
 	<li><i>sum</i> be the sum of cash flows</li>
 	<li><i>p</i> be the principal amount</li></p>
</ul>
<p>Then <b>irr = irr * log(p/sum) / log(npv/sum)</b> is the iteration you need to successively apply.</p>
<p>We decided to start with 1.85 times the stated interest rate (which was a pretty good guess for most leases), and kept applying this formula until it stays more or less the same. Worked like a charm.</p>
<p>Here's the <a href="http://spreadsheets.google.com/ccc?key=poz40xh4E1udoDeQXhwk7PQ">spreadsheet</a> with the calculation.</p>
<p><iframe src="http://spreadsheets.google.com/pub?key=poz40xh4E1udoDeQXhwk7PQ&amp;output=html&amp;gid=0&amp;single=true&amp;widget=true" width="500" height="750" frameborder="0"></iframe></p>

---

## Comments

<!-- wp-comments-start -->

- **pegasus** _26 Dec 2006 5:38 am_:
  very informative article
- **URap** _28 Feb 2007 12:45 am_:
  Thank you! This helped with my assignment.
- **Easy** _10 Apr 2007 10:39 am_:
  Is it possible to calculate IRR manualy and if it is, how?
- **ganesh** _12 Apr 2007 10:46 am_:
  how to calculate remaining EMIs (new tenure ) keeping the amount of EMI constant.
- **Farah** _25 Aug 2006 12:00 pm_:
  Thanks, but i need to know how to calcualte it manualy.
- **Haseeb** _25 Aug 2006 12:00 pm_:
  Farah IRR can only be calculated manually by using hit and trial method. It the interest rate at which the NPV should equal zero. So try with different values. However if you have a financial calculator then you can find IRR just by inputing the data into it. thanks
- **NAGARAJA M** _25 Aug 2006 12:00 pm_:
  Suppose this is the scenario: Principal 100,000 IRR 10% Number of months 12 Monthly payment 8,792 Total interest 4,627 But you only have this information Principal 100,000 = p Monthly payment 8,792 Number of years 12 APR 4.63% Here's how you can calculate IRR Month Payment 1 8,792 2 8,792 3 8,792 4 8,792 5 8,792 6 8,792 7 8,792 8 8,792 9 8,792 10 8,792 11 8,792 12 8,792 Total payment 105,499 = sum First guess of IRR 8.56% 1.85 times APR NPV using first guess 100,766 = npv Second guess of IRR 9.98% irr x log(p/sum) / log(npv/sum) NPV using second guess 100,009 = npv Third guess of IRR 10.00% irr x log(p/sum) / log(npv/sum) NPV using third guess 100,000 Stop iteration
- **JITENDRA** _25 Aug 2006 12:00 pm_:
  pls attached finance dictionary like irr,roi,and all related collection sales
- **sanjeev kumar** _19 Sep 2008 9:00 am_:
  I want to ask that at what basis i can guess first IRR ,second IRR & what is about about APR.
- **Shishir** _30 Sep 2008 12:01 pm_:
  Hi,\
  Had a question regarding building a cashflow table when only IRR and the initial outlay are stated along with the period.\
  \
  The project has an $80,000 investment outlay and is expected to yield an IRR of 30% over a 5 year economic life and the investment outlay is depreciated on a straight line basis towards a zero estimated salvage value\
  \
  Could you please help me with this?\
  \
  Thanks
- **Khan Nuzhat** _14 Dec 2008 4:30 am_:
  the data is good but there should be more examples of different cases, so that it surve all purpose.\
  \
  Thank You
- **Wayne** _21 Jan 2009 4:10 pm_:
  Seems to be some mix ups between Months and Years, If you do monthly calculations, isn't the IRR then a monthly percentage rate not an anual percentage rate?
- **S Anand** _21 Jan 2009 4:25 pm_:
  IRR by itself does typically refer to an annual rate, Wayne. I happen to\
  have used a monthly IRR in the example, and you're right in pointing out\
  that it makes things a little confusing. Please replace "month" with "year"\
  right through the article, and I believe it would read right then.
- **Su** _10 Feb 2009 10:32 pm_:
  This is so fantastic. Thank you!\
  \
  However I want to know how annual interest is 4627 when the sum of 8792 x12 months = 105504 and the difference between the principal amount = 5,504.\
  \
  Can you explain?\
  Su
- **S Anand** _14 Feb 2009 5:26 am_:
  The interest is not on 100000, Su. It's on a DIMINISHING balance that\
  just happens to be 100000 at the beginning. After making the first\
  payment of 8792, the principal reduces, and it's not easy to find out\
  how much of that 8792 was for the principal, and how much of it was\
  for the interest. That's what the article tries to explain.
- **[Abhijit Sen](http://abhijitsen.webs.com)** _10 Feb 2010 12:23 am_:
  Anand, can you tell me how to learn excel quickly? i dont even know how to use pivot table. Need to ramp up quickly, any suggestions?
- **Thomas** _18 Mar 2009 9:06 am_:
  Hi,
  could you state a reference to the paper you dug out? Since this will provide a good starting point for further research on my site.
  Thx in advance
  Thomas
- **[S Anand](http://www.s-anand.net/)** _18 Mar 2009 12:56 pm_:
  I'm afraid I couldn't find it when I searched again, Thomas. Maybe a fresh Google search will work, except I can't remember what I looked for, except that it was in a PDF file.
- **[S Anand](http://www.s-anand.net/)** _25 Mar 2009 4:41 pm_:
  Just type in the date, and the amount you received or paid on that date (as positive or negative values respectively). Then use Excel's IRR function.
- **George Venesis** _25 Mar 2009 2:47 pm_:
  Hello,
  I have a question regarding IRR. If I have a portfolio of stocks how it is possible to calculate the IRR? For example, suppose that I invest $100.000 and I'm buying few stocks for $10.000 and $30.000. In total I have paid $40.000.The next day I have a 10% profit, that makes me $4.000 better off. How it is possible to calculate IRR?
  Regards
  George
- **[S Anand](http://www.s-anand.net/)** _10 Feb 2010 4:51 pm_:
  [Excel for Dummies](http://www.amazon.com/gp/product/1568840500?ie=UTF8&tag=sanand-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=1568840500) is a good starting point.
- **Saravna Kumar** _5 Aug 2010 7:03 am_:
  Sir,
  Realy your excell tips and macros are very usefull to every one those who are not familiar in excell
  thankfull to you
  thanking you
- **Moin Siddiqui, Dubai** _20 Jul 2010 8:28 pm_:
  Hi Anand,
  Nice Examples and answers above, unfortunately i never worked on this before, but this
  method is using in my new job, i want to learn IRR & ROI in detail with practical. Dear anand pls help me to learn it in a very easy and quick way, new job is in OIL & GAS Sector. Request for quick reply
  Thnx in advance
  Moin Siddiqui
- **Jean** _29 Sep 2010 10:46 pm_:
  If one is calculating the IRR on a project that requires debt capital, in determining the annual net income of the project does one have to include principal repayment on the loan
- **Fahad** _17 Oct 2011 2:27 pm_:
  Internal rate of return (IRR) is the rate of return at which the project will generate returns of a PV of 0 or simply at which the NPV of the project will be zero. it is calculated using a test & trail method.Formula is first you will calculate 2 NPVs of projected cashflows of the project using any 2 cost of capital rates. suppose if company's Own cost of capital is 8% you will calculate the NPV first @ 8% and a second NPV at any rate higher than 8 % .....say 15%.The answer with the higher NPV will result in negative NPV then apply the rates to this formula to get the IRR
  Lower rate + (NPV @ Lower rate /(Npv @ Lower rate - Npv @ Higher Rate)) x (Higher rate -Lower rate)
  suppose LR = 8%
  HR =15 %
  NPV @ LR = 1000
  NPV @ HR=500
  IRR will be 14.5 %
- **Albert Akankwasa** _25 Nov 2011 8:52 am_:
  Suppose a cost of the project is 84,418,780, the annual return is 20,000,000 and the annual growth rate is 20%. What is the IRR and PAY BACK PERIOD?
- **sagar** _9 Aug 2011 9:05 am_:
  what is meaning of IRR and how it is calculate. where it is use /
- **Sunidhi Gupta** _22 Nov 2011 7:05 pm_:
  that was really helpful and understandable. can I access daily updates of it on my id.
- **Srinivas** _2 Feb 2012 2:36 pm_:
  In the context of a finance company, how to calculate cost of capital of an entity and then compare it with IRR of a loan proposal, to arrive at the break-even rate. Pls. elucidate with an example.

<!-- wp-comments-end -->
