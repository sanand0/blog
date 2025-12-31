---
title: User defined array functions in Excel
date: "2007-02-23T12:00:00Z"
lastmod: "2009-03-23T15:38:16Z"
categories:
  - excel-tips
wp_id: 109
---

Many languages have functions to process lists (array). These functions usually return a list, so you can pass that to another list function. This chaining of functions is really powerful.

UNIX provides this sort of chaining capability. If I had a cities (with some repetitions) and I wanted to find out how many started with the letter 'A', I'd just type:

```bash
cat cities | sort | uniq | grep "^A" | wc
```

```yaml
cat: types the cities.
sort: sorts the cities alphabetically.
uniq: finds unique cities (works only if sorted - that's why we had to sort the list).
grep: filters the cities. Only allows cities beginning with A.
wc: word count
```

To do this on Excel, the only way is to

1. **get the unique values**. Data - Filter - Advanced Filter, and select "Unique records only", "Copy the list to another location", and select a location
2. **get the first letter**. =LEFT(cell,1) returns the first letter of the cell.
3. **count the number of "A"s**. =COUNT(range, "A") counts the number of "A"s.

But ideally, I'd like a 1-line formula like

```excel
=LENGTH(UNIQUE(GREP("^A", range)))
```

Excel doesn't provide these functions by default, but you can add them as [user defined functions](/User-defined_functions_in_Excel.html). Doing this **lets you condense several cells into one**. Instead of having to copy all your data into a set of unique values, and then adding a column for the first cell, the entire operation can be condensed into one formula.

I consider the following functions the a basic set for list processing.

- LENGTH(list) counts the number of elements in a list
- INDEX(list, n) returns the nth element of the list
- GREP(string, list) returns elements of the list that have the string
- UNIQUE(list) filters unique values
- UNION(list, list) returns elements in at least one of the lists
- INTERSECTION(list, list) returns elements in both lists
- DIFFERENCE(list, list) returns the elements in the first list but not the second
- REVERSE(list) reverses the order of the list
- STRJOIN(separator, list) joins the elements of the list into a string, separated by a separator
- STRSPLIT(separator, string) splits the string into a list, using a separator
- MVLOOKUP(value, lookup, result) looks up value in "lookup", and returns the corresponding MULTIPLE values from "result"

I created these UDFs. You can [download the functions](https://files.s-anand.net/images/Macros.xls) and play with them. Below are some tasks that you can do with them, that are difficult otherwise.

- Get the file name from a path.
  ```excel
  ```

=INDEX(REVERSE(STRSPLIT("\", filename)), 1)

````
- Count the number of unique elements in a range.
  ```excel
=LENGTH(UNIQUE(range))
````

- How many common elements are there in range 1 and range 2?
  ```excel
  ```

=LENGTH(INTERSECTION(range1, range2))

````
- How many words are there in a string?
  ```excel
=LENGTH(STRSPLIT(" ", string))
````

- Get the smallest unique numbers in a range
  ```excel
  ```

=SMALL(UNIQUE(range), 5)

````
- Count the number of mismatches between two lists.
  ```excel
=COUNT(Range1)+COUNT(Range2) - COUNT(INTERSECTION(Range1,Range2))
````

- Get a list of mismatches between two lists.
  ```excel
  ```

=STRJOIN(",",UNION(DIFFERENCE(Range1,Range2), DIFFERENCE(Range2,Range1)))

````
- Count duplicate entries in a range.
  ```excel
=LENGTH(Range)-LENGTH(UNIQUE(Range))
````

- VLOOKUP multiple values
  ```excel
  ```

=MVLOOKUP(A1,Lookup_Range,Return_Range)

````
- Count the unique matches in a VLOOKUP
  ```excel
=COUNT(UNIQUE(MVLOOKUP(A1,Lookup_Range,Return_Range)
````

This is a small sample. The power of list processing is phenomenal, especially when combined with array formulas. [Download these macros](https://files.s-anand.net/images/Macros.xls) and play with them!

---

## Comments

<!-- wp-comments-start -->

- **Krishna** _24 Feb 2007 4:10 am_:
  Anand, thanks for an extremely useful stuff.In connection to our discussion on enhancing my excel skills, i think it would help me largely. Krishna
- **Sundar** _26 Feb 2007 4:06 am_:
  Very neat job Anand. Congrats for a super job. Waht is your e-mail address? Thanx in advance............S.
- **Anand Srini** _26 Feb 2007 9:40 pm_:
  Hi I reproduce this extract from your article "Instead of having to copy all your data into a set of unique values, and then adding a column for the first cell, the entire operation can be condensed into one formula" can you explain why a column has to be added for the first cell ?
- **ashwin** _27 Feb 2007 4:41 pm_:
  Dear Anand, As usual; another useful post from you. Thanks, Ashwin
- **Kabir** _5 Mar 2007 9:01 pm_:
  you truly are a genius
- **Shiva** _6 Mar 2007 2:03 pm_:
  Your site is turning to a Dexters Laboratory
- **Ramly** _19 Mar 2007 4:35 pm_:
  Thank you very much this will help a lot
- **Mansi** _11 Apr 2007 4:22 am_:
  Hi, was just randomly searching for how to generate unique values on excel.. and came across your website. Must say, truly impressive work and this has helped me a lot! Thank you and keep up the good work! :)
- **James** _23 Feb 2007 12:00 pm_:
  Cheers, a lot of great stuff here, makes my Excel work much easier. My hat off to you!
- **Pete Watkins** _23 Feb 2007 12:00 pm_:
  Thanks ever so much for your work in developing these functions, as these have allowed me to avoid a huge amount of drudgery in processing data!

<!-- wp-comments-end -->
