---
title: Correlating subjects
date: "2012-02-12T04:08:02Z"
lastmod: "2012-02-12T04:09:04Z"
categories:
  - visualisation
wp_id: 2724
---

<p>A <a href="https://www.facebook.com/groups/chennaigeeks/358823254142720/">question</a> from <a href="https://www.facebook.com/dorai.thodla">Dorai</a> get me thinking: does being good at maths help in programming?</p> <p>I don’t have a personal view. But since <a href="http://www.reportbee.com/">Reportbee</a> has data on the Class 12 examination results for the last three years, we thought we could do a bit of analysis.</p> <p>Here’s the correlation of the scores of various subjects with Computer Science.</p> <table style="color: #444" class="lines numbers"> <tbody> <tr> <th>Correlation</th> <th>Subject</th></tr> <tr> <td style="background: #63be7b">0.79</td> <td>CHEMISTRY</td></tr> <tr> <td style="background: #68c07c">0.79</td> <td>PHYSICS</td></tr> <tr> <td style="background: #95cd7e">0.75</td> <td>ENGLISH</td></tr> <tr> <td style="background: #9ecf7f">0.75</td> <td>MATHEMATICS</td></tr> <tr> <td style="background: #b9d780">0.72</td> <td>LANGUAGE</td></tr> <tr> <td style="background: #feea83">0.67</td> <td>BIOLOGY</td></tr> <tr> <td style="background: #fee382">0.66</td> <td>ECONOMICS</td></tr> <tr> <td style="background: #fee282">0.66</td> <td>COMMERCE</td></tr> <tr> <td style="background: #fede81">0.65</td> <td>ACCOUNTANCY</td></tr> <tr> <td style="background: #f98c71">0.56</td> <td>HISTORY</td></tr> <tr> <td style="background: #f8696b">0.52</td> <td>GEOGRAPHY</td></tr></tbody></table> <p>It almost breaks neatly into four groups.</p> <ol> <li><strong>Physics &amp; Chemistry</strong>, both of which have a correlation of 0.79, and clearly are the most correlated with Computer Science  </li><li><strong>Maths, English &amp; Language</strong>, which have a correlation of 0.72 – 0.75  </li><li><strong>Biology, Economics, Commerce and Accountancy</strong>, which hover at around 0.66  </li><li><strong>History &amp; Geography</strong>, which are 0.52 – 0.56</li></ol> <p>The results in 2010 are almost exactly the same.</p> <table style="color: #444" class="lines numbers"> <tbody> <tr> <th>Correlation</th> <th>Subject</th></tr> <tr> <td style="background: #70c27c">0.78</td> <td>PHYSICS</td></tr> <tr> <td style="background: #74c37c">0.78</td> <td>CHEMISTRY</td></tr> <tr> <td style="background: #94cd7e">0.75</td> <td>ENGLISH</td></tr> <tr> <td style="background: #9dcf7f">0.75</td> <td>MATHEMATICS</td></tr> <tr> <td style="background: #afd480">0.73</td> <td>LANGUAGE</td></tr> <tr> <td style="background: #ffeb84">0.67</td> <td>ACCOUNTANCY</td></tr> <tr> <td style="background: #fede81">0.65</td> <td>ECONOMICS</td></tr> <tr> <td style="background: #fed880">0.65</td> <td>COMMERCE</td></tr> <tr> <td style="background: #fdcf7e">0.64</td> <td>BIOLOGY</td></tr> <tr> <td style="background: #fbaa77">0.60</td> <td>GEOGRAPHY</td></tr> <tr> <td style="background: #f97f6f">0.55</td> <td>HISTORY</td></tr></tbody></table> <p>I’m not sure what it is that leads to this kind of correlation. In fact, the full correlation between every pair of subjects (for 2011) is below:</p> <p><a href="/blog/assets/subject-correlation.webp"><img style="background-image: none; border-bottom: 0px; border-left: 0px; padding-left: 0px; padding-right: 0px; display: inline; border-top: 0px; border-right: 0px; padding-top: 0px" title="subject-correlation" border="0" alt="subject-correlation" src="/blog/assets/subject-correlation.webp" width="533" height="376"></a></p> <p>What inferences would <em>you</em> draw from this?</p> <p>And what do you think is the <em>reason</em> for this?</p>

---

## Comments

<!-- wp-comments-start -->

- **[Arun Ravindran](http://arunrocks.com/)** _12 Feb 2012 5:53 am_:
  My inference is purely anecdotal but might be helpful in explaining this data. I had chosen Computer Science for my +2 in 1998. It was taught in C++ and mostly involved memorising operations on Data Structures such as Lists, Stacks and Queues. The C++ standard library had to be memorized including I/O, string and file functions.
  The exams were basically a test of memory rather than attacking a new problem space mathematically. Guess which are the other subjects which involve memorising a huge set of symbolic facts? -- Chemistry and to a certain extend, Physics.
  I believe the data is more revealing of our Computer Science pedagogical and evaluation methods than the subject itself.
- **[S Anand](http://www.s-anand.net/)** _12 Feb 2012 6:46 am_:
  Good point. It's quite debatable whether marks in computer science are indicative of programming ability.
- **[Anamika](http://thenmozhi.yolasite.com)** _12 Feb 2012 10:21 am_:
  Netruvarai neram poga villaiyae,
  unadhu arugae neram podhavillaiyae...!
- **[Sathya](http://nullpointers.wordpress.com)** _16 Feb 2012 12:56 pm_:
  In my experience, I've come across rock star programmers who have sound grasp of mathematics. But i dont have statistics to prove them. As we all know, programming (esp functional) is heavily influenced by mathematics. Coming to inferences, I would take the dataset with a pinch of salt. Is it diverse enough to be statistically significant ? I agree with most of the comments on relating "mugging up programs" to being good at Chemistry in particular.
- **Sathyaraj** _12 Feb 2012 7:44 pm_:
  My 2 cents based on experience.
  People who take the computer science group generally have to always take one language and English subject apart from taking Physics, Chemistry, Maths. They would not be able to take classes in accountancy, economics, history, etc.
  Some of the students at the top of the class would have realized that in order to differentiate in terms of coming first in class/school, one would need to excel in language and english. It is given that one needs to get excellent scores in physics, chemistry and maths to get an overall good percentage. Also the fact, that scoring a big total would enable them to get admission in colleges in like BITS pilani which looks at overall score.
  Students who take the biology or accountancy group have no such pressure for them to excel in English and language subjects.
  Hope it makes sense.
  Also, if you can do a correlation between computer science students and the language that they take, I believe you will find that the majority of students would have chosen french rather than Tamil or English.
- **Shankar V** _13 Feb 2012 6:23 am_:
  Anand
  Correlation is a misleading statistic if the dependent and independent variables are not "really" related that way. There could be compounding effects within the independent variables leading to wrong correlation coefficients.
  There are ways to detect and cleanse compounding - design of experiments (in statistics) deals in depth on this. It is quite possible that there could be some relationship in how the computer science and math exams are scheduled and the scores in these subjects. If they are too close to each other, the student may have had lesser time to prepare for the math exam. For example, if Physics and Math were scheduled one after the other, and Computer Science test is after the Math test, the student may have prepared better for Physics, not have had enough time for Math and then recovered to do well in Computer Science. This can be a pattern in the entire class as it is normal for kids to focus more on Physics (the dreaded subject!) v/s Math.
  The statistic may not reveal ability or natural alignment of the subjects.
- **[Evgeni](http://outputlogic.com)** _11 Dec 2012 3:37 am_:
  I'd rearrange subjects such that they're more clustered together by correlation, like in a TreeMap view. That way it's easier to see the relationships.
- **amanjot kaur** _10 Sep 2015 12:28 pm_:
  i need correlation of commerce with language

<!-- wp-comments-end -->
