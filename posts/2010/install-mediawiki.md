---
title: Install Mediawiki
date: "2010-07-15T05:30:17Z"
categories:
  - open-source
wp_id: 2526
---

<p>Once you’ve <a href="/blog/install-xampp/">installed XAMPP</a>, <a href="http://www.mediawiki.org/wiki/Download">download MediaWiki</a> and unzip it into your xampp/htdocs folder. You may need <a href="http://7-zip.org/">7-Zip</a> to extract tar.gz files. Rename the mediawiki folder to wiki.</p> <p>You’ll first need to create a database, which you can do by visiting <a href="http://localhost/phpmyadmin/">/phpmyadmin/</a> on your localhost, typing in the database name and pressing ‘Create’.</p> <p>Now go to <a href="http://localhost/wiki/">/wiki/</a> and fill out the form. Make sure you select “Use superuser account” since you haven’t really created a user for your database.</p> <p>Click on the “Install Mediawiki” button, and you should have a wiki.</p> <p><object width="600" height="475"><param name="movie" value="http://www.youtube.com/v/tEakNApBTeg&amp;hl=en_GB&amp;fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/tEakNApBTeg&amp;hl=en_GB&amp;fs=1" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="600" height="475"></embed></object></p>

---

## Comments

<!-- wp-comments-start -->

- **ankur** _15 Jul 2010 10:01 pm_:
  how did you change the version of PHP, i get :
  PHP 5.3.1 is not compatible with MediaWiki due to a bug involving reference parameters to \_\_call. Upgrade to PHP 5.3.2 or higher, or downgrade to PHP 5.3.0 to fix this. ABORTING (see http://bugs.php.net/bug.php?id=50394 for details)

<!-- wp-comments-end -->
