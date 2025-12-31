---
title: How to convert APR to interest rate
date: "2007-01-12T12:00:00Z"
lastmod: "2019-10-14T08:07:57Z"
categories:
  - simple-explanations
wp_id: 130
---

If you don't know your interest rate (IRR), but only have your APR, there is a way of figuring out the actual interest rate on Excel.

For this, you need to know your EMI (monthly payment), duration of the loan (number of months) and principal (amount you borrowed).

Let's assume your EMI is 2,000 and you are paying over 5 years (60 months) on a loan of 100,000. Use **Excel's RATE function**. In this example:

> =RATE(60, 2000, -100000) \* 12 = 7.42%

I multiplied by 12 to convert the monthly interest rate to annual. Since the payment is in months (60 months), Excel returns the interest rate in months as well.

Note that this method does not require the APR. Just the EMI, duration and principal will suffice. [Everyday Loans](https://www.everyday-loans.co.uk/) can help those of you who are not very financially literate, there's no shame in getting help from experts.

---

## Comments

<!-- wp-comments-start -->

- **Graeme** _12 Jan 2007 12:00 pm_:
  Can you figure out the interest rate from the info you got
- **Pradeep** _12 Jan 2007 12:00 pm_:
  Cool!...Anand, i was trying to find a formula to calculate real interest rate and came across your article..quite informative and you mentioned the RATE formula in excel sheet also so my search is done as far as excel is concerned THANKS :)
- **Matt** _12 Jan 2007 12:00 pm_:
  Very good - helped me figure out how much I could save by paying off a loan early

<!-- wp-comments-end -->
