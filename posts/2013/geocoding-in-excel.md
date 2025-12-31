---
title: Geocoding in Excel
date: "2013-05-08T09:17:03Z"
categories:
  - coding
wp_id: 2843
---

It’s easy to convert addresses into latitudes and longitudes into addresses in Excel. Here's the [Github project](https://github.com/sanand0/geocode-excel) with a downloadable [Excel file](https://github.com/sanand0/geocode-excel/raw/master/Geocode.xlsm).

This is via Visual Basic code for a `GoogleGeocode` function that [geocodes](https://developers.google.com/maps/documentation/geocoding/) addresses.

```javascript
Function GoogleGeocode(address As String) As String
    Dim xDoc As New MSXML2.DOMDocument
    xDoc.async = False
    xDoc.Load ("http://maps.googleapis.com/maps/api/geocode/" + _
        "xml?address=" + address + "&sensor=false")
    If xDoc.parseError.ErrorCode <> 0 Then
        GoogleGeocode = xDoc.parseError.reason
    Else
        xDoc.setProperty "SelectionLanguage", "XPath"
        lat = xDoc.SelectSingleNode("//lat").Text
        lng = xDoc.SelectSingleNode("//lng").Text
        GoogleGeocode = lat & "," & lng
    End If
End Function
```

---

## Comments

<!-- wp-comments-start -->

- **Ryan** _8 Jun 2015 9:28 pm_:
  I find this isn't working and says, Compile Error; User defined type not defined
  xDoc As New MSXML2.DOMDocument what do I change to fix it?
  Thank you
- **Richie Lionell** _27 Jul 2016 6:40 am_:
  Ryan, Inside the VBE, Go to Tools -> References, then Select Microsoft XML, v6.0 . If that doesn't work unselect that and select Microsoft XML, v3.0

<!-- wp-comments-end -->
