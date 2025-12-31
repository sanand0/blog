---
title: Web lookup using Excel
date: "2007-05-03T12:00:00Z"
categories:
  - excel-tips
wp_id: 86
---

Take a look at the Excel screenshot below.

[![Amazon Web Prices](/blog/assets/flickr-amazon-web-prices_481952444_o-png.webp)](/blog/assets/flickr-amazon-web-prices_481952444_o-png.webp)

Yes, that's right. I have a [user-defined function](/User-defined_functions_in_Excel.html) called AMAZONPRICE. And it returns these cameras' **prices directly from Amazon.com**. (Given the category and some keywords, it returns the price of the bestselling item on Amazon.com.)

Here's the code behind the function.

```javascript
Function AmazonPrice(index As String, keywords As String) As String
  Dim xDoc As MSXML2.DOMDocument30
  Set xDoc = New MSXML2.DOMDocument30
  xDoc.async = False
  If xDoc.Load("http://ecs.amazonaws.com/onca/xml?Service=AWSECommerceService" _
    "&Version=2005-03-23&Operation=ItemSearch&SubscriptionId=03SDGQDFEB455W53SB82" _
    "&AssociateTag=sanand-20&MinimumPrice=10000&ResponseGroup=OfferSummary,Small" _
    "&Sort=salesrank&SearchIndex=" & index & "&Keywords=" & keywords) Then
    xDoc.setProperty "SelectionLanguage", "XPath"
    xDoc.setProperty "SelectionNamespaces", _
      "xmlns:a=""http://webservices.amazon.com/AWSECommerceService/2005-03-23"""
    AmazonPrice = xDoc.selectSingleNode("/a:ItemSearchResponse//a:Amount").Text
  End If
End Function
```

---

This is how it all started...

Flickr has a [camera finder](http://www.flickr.com/cameras/) that shows the most popular cameras in the Flickr community.

[![flickr Camera Finder](/blog/assets/flickr-flickr-camera-finder_481952446_o-png.webp)](/blog/assets/flickr-flickr-camera-finder_481952446_o-png.webp)

I [love comparing gadgets](/How_I_buy_gadgets.html), I'd been doing some research around these cameras, and the [Fuji series](http://www.flickr.com/cameras/fujifilm/) (because I own a [Fuji Finepix S5600](/My_Fuji_Finepix_S5600.html)). I'd normally make a spreadsheet that compares these cameras on various parameters, including price.

Since I believe in [never typing in data](/Excel_-_Never_type_in_data.html), wondered if there was a way to get the prices in automatically...

Two things made this possible.

1. Amazon offers [web services](http://www.amazon.com/gp/browse.html?node=3435361) which let you get price (and almost any other) data for their products
2. Visual Basic lets you use pretty much any ActiveX object as a control. Microsoft offers [MSXML](http://msdn2.microsoft.com/en-us/xml/bb291077.aspx) which you can use to load (or download) any XML file, and parse it.

The first task is to get the XML feed for a product you want. Amazon lets you do that through by typing in a URL. The best way to construct the URL is through [AWSZone](http://www.awszone.com/). I picked the [US ItemSearch](http://www.awszone.com/scratchpads/aws/ecs.us/ItemSearch.aws) method, which searches for a title or keyword within a category, and returns the matches. The feed for the Canon EOS Digital Rebel XT, based on this, would be at:

```text
http://ecs.amazonaws.com/onca/xml?
    Service=AWSECommerceService&
    Version=2005-03-23&
    Operation=ItemSearch&
    SubscriptionId=0525E2PQ81DD7ZTWTK82&
    SearchIndex=Electronics&
    Keywords=Canon EOS Digital Rebel XT&
    Sort=salesrank&
    ResponseGroup=Offers,Small
```

(You really need to replace the Subscription ID with your own.)

If you [retrieved this URL](http://ecs.amazonaws.com/onca/xml?Service=AWSECommerceService&Version=2005-03-23&Operation=ItemSearch&SubscriptionId=0525E2PQ81DD7ZTWTK82&SearchIndex=Electronics&Keywords=Canon%20EOS%20Digital%20Rebel%20XT&Sort=salesrank&ResponseGroup=Offers,Small), you have an XML file containing the details of all Canon EOS Digital Rebel XTs, sorted by sales rank.

To load this in Excel, you need to create a [UDF](/User-defined_functions_in_Excel.html) in Visual Basic. First, go to **Tools - References and enable Microsoft XML, v3.0 or v4.0**. Now, to load an XML document, do this:

```vb
Dim xDoc As MSXML2.DOMDocument30
Set xDoc = New MSXML2.DOMDocument30
xDoc.async = False
xDoc.Load(url)
```

If the load succeeds, then you can extract the information fairly easily, using [XPath](http://www.w3.org/TR/xpath).

```vb
xDoc.setProperty "SelectionLanguage", "XPath"
xDoc.setProperty "SelectionNamespaces", _
        "xmlns:a=""http://webservices.amazon.com/AWSECommerceService/2005-03-23"""
```

The first line says we'll be searching using XPath. The second line is a [workaround to support default namespaces](http://support.microsoft.com/kb/313372). (Don't worry about it. I don't quite get it either.)

Finally, you get the price from the XML tree. In this case, it's under ItemSearchResponse/Items/Item/OfferSummary/LowestNewPrice/Amount, and it's in cents.

```vb
AmazonPrice = xDoc.selectSingleNode("/a:ItemSearchResponse//a:Amount").Text
```

That's it! Now that this function is defined, just pass it the category and keywords, and you have the price of the first matching product. You can retrieve any other information about products as well -- like sales rank, weight, ratings, reviews, etc.

---

Here's the [spreadsheet](https://files.s-anand.net/images/AmazonPrices.xls) for you to play around with.

---

- [Excel 2003 Power Programming with VBA (Excel Power Programming With Vba](http://www.amazon.com/gp/product/0764540726)
- [Writing Excel Macros with VBA, 2nd Edition](http://www.amazon.com/gp/product/0596003595)

---

## Comments

<!-- wp-comments-start -->

- **Saurabh** _3 May 2007 7:38 am_:
  There is a simpler way as well. Use Data->Import External Data->New Web Query. While this is not as powerful as the user defined function that you have created, but definitely a good starting point for lesser geeks :) I use this, for example, to have a dashboard kind of view for the status of the multiple projects that I handle at my work. We rely heavily on Microsoft Sharepoint at work, and using the Web Query option, I can easily get a snapshot of the status of various projects. Same can also fetch shareprices from various websites.
- **S Anand** _3 May 2007 8:16 am_:
  Good point, Saurabh! Web Query does make getting stuff out of HTML very easy. My function operates in a different domain, though. It can access XML, which Web Query won't, but can't access HTML, which Web Query does. I'm planning a few more posts on how to extend this concept... that will explain what I mean.
- **rick sherrin** _3 May 2007 12:00 pm_:
  Hi, I work at a public library, in the acquisitions department. The majority of the work is manually keying in order information (that is available electronically elsewhere). I read your article about using Excel to retrieve amazon information. This is something that would be very useful to our library and would make my job easier. I have a little excel knowledge, but I have no experience with visual basic or xml, etc. So although it looks straightforward, it is still out of my reach. I would like to be able to enter a column of ISBN numbers in one column, and retrieve title, author, publisher, price, reviews, synopsis, cover image, in adjacent columns. I would appreciate your help if you would give me an example of how I could easily do this. Thanks Rick
- **dat** _12 Aug 2008 8:10 am_:
  useful article!
  Btw, how do I retrieve other info from amazon (published date, sales rank, customer review, etc)???
  thanks
- **S Anand** _13 Aug 2008 2:15 am_:
  @dat: Have a look at http://www.awszone.com/ for examples on other parameters.
- **Lydia** _3 May 2010 12:05 am_:
  this worked until august last year when amazon changed the way the query signs into their system...it now requires a signature with a timestamp in addition to the subscription ID
- **Bobby Baker** _10 Feb 2015 7:09 am_:
  Have you updated the search functions for this or do you have a new code for this?
- **Vlad** _26 Aug 2015 10:00 pm_:
  Hey Annand
  is it possible o get the racking status fro fedex for a column of tracking numbers?

<!-- wp-comments-end -->
