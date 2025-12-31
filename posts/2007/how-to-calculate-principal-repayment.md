---
title: How to calculate principal repayment
date: "2007-01-10T12:00:00Z"
categories:
  - simple-explanations
wp_id: 133
---

<blockquote><p>Answer: use the CUMPRINC function in Excel</p></blockquote>
<p>Say you take a 10-year lease for 100,000 at an interest rate (IRR) of 10%, paid annually. The installment for this lease is 16,275. You can calculate this using the PMT function in Excel:</p>
<blockquote><p>PMT(10%, 10, 100000) = -16275</p></blockquote>
<p>You've made 5 payments over 5 years. At this point, if you decide you want to repay the full lease, how much do you have to repay? In other words, <b>what's the principal outstanding</b> after 5 years?</p>
<p>This is not trivial calculation. The answer is not 50,000. In fact, it is 61,693. Here's how it works.</p>
<table class="numbers">
<tr><th>Year</th><th>Balance</th><th>Principal</th><th>Interest</th><th>EMI</th></tr>
<tr><td>1</td><td>100000</td><td>6275</td><td>10000</td><td>16275</td></tr>
<tr><td>2</td><td>93725</td><td>6902</td><td>9373</td><td>16275</td></tr>
<tr><td>3</td><td>86823</td><td>7592</td><td>8682</td><td>16275</td></tr>
<tr><td>4</td><td>79231</td><td>8351</td><td>7923</td><td>16275</td></tr>
<tr><td>5</td><td>70880</td><td>9187</td><td>7088</td><td>16275</td></tr>
<tr><td>6</td><td style="color:red">61693</td><td>10105</td><td>6169</td><td>16275</td></tr>
<tr><td>7</td><td>51588</td><td>11116</td><td>5159</td><td>16275</td></tr>
<tr><td>8</td><td>40472</td><td>12227</td><td>4047</td><td>16275</td></tr>
<tr><td>9</td><td>28245</td><td>13450</td><td>2825</td><td>16275</td></tr>
<tr><td>10</td><td>14795</td><td>14795</td><td>1480</td><td>16275</td></tr>
</table>
<p>The <b>EMI contains an interest component as well as a principal component</b>. The interest component is always 10% of the balance -- because the interest rate is 10%. The remaining amount is the principal repayment.</p>
<p>In the first year, you pay an interest of 10% x 100,000 = 10,000, and the remaining 6,275 (from your 16,275 EMI) is the principal repayment. This brings the balance down to 93,725.</p>
<p>The next year, you pay an interest of 10% x 93,725 = 9,373, and the remaining 6,902 (from your 16,275 EMI) is the principal repayment. This brings the balance down to 86,823. And so on..</p>
<p>So after 5 years, you just have to repay 61,693, the balance after 5 payments.</p>
<p><b>Excel has two functions: PPMT and IPMT that calculate the principal and interest components</b>. For example:</p>

```excel
PPMT(10%, 1, 10, -100000) = 6275 (principal payment in year 1)
IPMT(10%, 1, 10, -100000) = 10000 (interest payment in year 1)
```

<p>Excel also has the cumulative versions of these functions: <b>CUMIPMT and CUMPRINC</b>. You can calculate the balance outstanding using the CUMPRINC function. For example:</p>
<blockquote><p>CUMPRINC(10%, 10, 100000, 1, 5, 0) = -38307 (principal paid in first 5 years)</p></blockquote>
<p>The balance outstanding is 100,000 - 38,307 = 61,693</p>
<hr />
<p>As you saw, the balance you have to repay midway is usually more than half the amount you borrowed. This is because you spend most of the first half paying off the interest. The typical shape of the balance outstanding over time is below.</p>
<p><a href="/blog/assets/flickr-balance-outstanding-in-a-lease-over-time_353702984_o-gif.webp"><img src="/blog/assets/flickr-balance-outstanding-in-a-lease-over-time_353702984_o-gif.webp" width="450" height="320" alt="Balance outstanding in a lease, over time"></a></p>
<p>The typical shape of the principal and interest component of the EMI over time is shown below.</p>
<p><a href="/blog/assets/flickr-principal-and-interest-components-of-an-emi-over-time_353702986_o-gif.webp"><img src="/blog/assets/flickr-principal-and-interest-components-of-an-emi-over-time_353702986_o-gif.webp" width="450" height="320" alt="Principal and interest components of an EMI, over time"></a></p>
<p>While this may take customers by surprise, this has confused banks as well, and has an <a href="/Calculating_IRR.html">interesting side-effect, thanks to Basel 2</a>. Most banks use the book value of the lease for risk calculations. This is typically based on a straight-line depreciation. So after 5 years, the lease is worth 50,000 in the books, and they would have to provide capital for that 50,000. But Basel 2 now says they need to provide for the principal outstanding, which is 61,693 -- meaning banks have to provide <i>more</i> capital than they have been so far. (I wouldn't be surprised if many banks <i>don't</i> know this.)</p>

---

## Comments

<!-- wp-comments-start -->

- **Anand** _10 Jan 2007 8:53 pm_:
  I know my EMI, the duration of the loan and the interest rate (not the IRR). Can i use any of these functions to determine how much principal i owe at a certain point in time ? if not do I have to determine the IRR and then plug it into these functions to find the value i am looking for ?
- **S Anand** _10 Jan 2007 10:40 pm_:
  Unfortunately, all the functions require the IRR. But given the EMI, duration and principal, you can determine the IRR using goal seek on the PMT function.
- **Frankie** _16 Mar 2007 4:03 am_:
  how do i calculate NPV of Lease Payments in Excel given the following scenarios: Payment in arrears/advance(kindly articulate for both options, payment in arrears and due) and on a monthly basis, say current FMV is $100K,Interest rate=6%, Period is 60 months. I find your explanations marvellously simple....I think you should write a book on Excel for Finance or some such...thanks Sir.
- **S Anand** _16 Mar 2007 9:43 am_:
  Frankie, the best way to do this is using the NPV function in Excel. It allows for any arbitrary cash flow patters.
- **khais** _10 Jan 2007 12:00 pm_:
  ICICI BANK OFFERS Rs. 200000 personal loan with 19.5% interest, they told emi Rs.3017 for 4 years (48 monthly installment vis). How should I calculate that how much interest rate I am giving? How to cross verify? Please suggest or give calculation. Thanks
- **pronab halder** _10 Jan 2007 12:00 pm_:
  I wanted to know how would i calculate the total amount,principle and interest
- **ganesh** _10 Jan 2007 12:00 pm_:
  # And how EMI is calulated when intrest rate changes but EMI reamins same (default choice given by all banks when intrest rate changes.) # How to calculate new tenure in above case.
- **TAMMY** _10 Jan 2007 12:00 pm_:
  There is no sample by # of months instead of # yrs: Please show me how to calculate monthly principal and interest for the following: Loan Amount $11,000.00 Rate 10% 64 months Thanks
- **shanti kumar** _10 Jan 2007 12:00 pm_:
  sir,
  can i know a bit briefly how emi amount is decided mannual work out required explaining the formulae. i know multiply divide which you have mentioned in the table but what is the 1+r pls explain.
- **Santhosh** _10 Jan 2007 12:00 pm_:
  I know the interest rate,EMI,Loan amount. I have to repay the amount by 60 months. how can i calculate the actual interest and principal payment on each months.
- **S Anand** _10 Jan 2007 12:00 pm_:
  Santhosh, I suggest you have a look at the help for the IPMT and PPMT functions in Excel. That will do the job for you. (BTW, you'd only need the interest rate, loan amount and number of months. EMI can be calculated using the PMT function, or by adding IPMT + PPMT)
- **[S Anand](http://www.s-anand.net/)** _19 Mar 2009 2:13 pm_:
  For the 11th period, it would be
  =IPMT(7.5%/4, 11, 20, 750000)
  =PPMT(7.5%/4, 11, 20, 750000)
- **Vivian** _19 Mar 2009 12:34 am_:
  If I want to put the IPMT and PPMT function for the following, what would the formula look like?
  Loan $750,000, Annual Rate 7.50%, Years 5, Periods per year 4, Rate per Period 1.88%, Number of Periods 20, Period Payment (PMT) is ($45,316) I need to be able to calculate the Interest Payment. Then I need to find the PPMT function to calculate the principal payment for the current payment period. Please help!
- **Divya** _4 Aug 2009 7:05 pm_:
  Is the above process of calculation the same as used by banks in case of education loans?
- **Shravan** _12 Feb 2010 7:30 pm_:
  http://www.hindu.com/pp/2009/05/09/stories/2009050984820600.htm
- **mythili** _10 May 2010 10:17 am_:
  this was very useful for me in doing project, thanks for those who done it
- **G Prajeet** _25 Jul 2011 1:13 pm_:
  Thank you for the wonderful calculation Sir
- **Rajesh Jain** _27 Apr 2012 2:42 pm_:
  Dear sir, i Have install amount, Rate of int and installment left details. How would i calculate the outs tanding principal. The solution is here www.calcxml.com/calculators/loan-balance
  But How? Can you kindly help
- **K SUBRAMANYAM** _16 Jan 2012 5:11 pm_:
  Dear sir,
  what is the formula for calculating the interest for a year if i know the loan amount(opening balance) ,rate of interest,emi,loan tenure in monthly rests
- **n** _7 Jan 2013 2:29 pm_:
  The formula PMT is correct but the parameter format is incorrect. The correct format for the given example is PMT((10%)/12,120,100000) = 1321.51

<!-- wp-comments-end -->
