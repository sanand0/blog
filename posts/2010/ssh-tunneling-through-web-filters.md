---
title: SSH Tunneling through web filters
date: "2010-01-09T19:46:39Z"
lastmod: "2010-12-21T09:19:00Z"
categories:
  - coding
  - how-i-do-things
wp_id: 2431
---

You can defeat most [web filters](http://www.google.co.in/search?q=web+filter) by spending ~~[around 8 cents/hr](http://aws.amazon.com/ec2/#pricing)~~ [0 cents/hr](http://aws.amazon.com/free/) on Amazon EC2. (It’s usually worth the money. It’s a fraction of the cost a phone call or a sandwich. And I usually end up wasting that money anyway on calling someone or eating my way out of the misery of corporate proxies.)
Most web filters and proxies block all ports except the [HTTP port (80)](http://en.wikipedia.org/wiki/Http) and the [HTTPS port (443)](http://en.wikipedia.org/wiki/Https). But it’s used to carry encrypted traffic, and, [as Mark explains](http://proxytunnel.sourceforge.net/paper.php):

> since all the traffic that passed through the tunnel is supposed to be SSL encrypted (so as to form an unhindered SSL session between the browser and the HTTPS server), there are little or no access controls possible on such a tunnel

That means web filters can’t really block HTTPS traffic. So we can redirect web traffic to a local HTTPS server, and set up a server outside the firewall that redirects them back to the regular servers.
[Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) will be our local HTTPS server. [Amazon EC2](http://aws.amazon.com/ec2/) gives us a server outside the firewall.
So here’s a 16-step recipe to bypass your web filter. (This is the simplest I could make it.)
In Steps 1-7, we’ll launch a server on Amazon EC2 with 2 tweaks. Step 1 enables Port 443, and step 6 re-configures SSH to run on Port 443 instead of on Port 22. (Remember: most proxies block all ports other than 80 and 443). [Alestic](http://alestic.com/)’s article on how to [Automate EC2 Instance Setup with user-data Scripts](http://alestic.com/2009/06/ec2-user-data-scripts) and this thread on [running SSH on port 443](http://developer.amazonwebservices.com/connect/thread.jspa?messageID=126265&#126265) are invaluable.
In Steps 8-13, we’ll set up Putty as our local HTTPS server. Read how to set up [Putty as a SOCKS server](http://digitalpbk.blogspot.com/2009/05/ssh-proxy-windows-linux-orkut-bypass.html) and how to use [Putty with a HTTP proxy](http://meinit.nl/using-putty-and-an-http-proxy-to-ssh-anywhere-through-firewalls). All I did was to combine the two.
In steps 14-16, we’ll configure the browser to use the Putty as the SOCKS server.
**Ingredients**

1. [Amazon AWS account](http://aws.amazon.com/) (sign up for free – you won’t be charged until you use it)
2. [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) (which may be available on your Intranet, if you’re lucky)

**Directions**

1. On the [AWS EC2 Console](https://console.aws.amazon.com/ec2/), click on **Security Groups** and select the **default** security group. At the bottom, select **HTTPS** as the connection method, and save it.
   [![](/blog/assets/ec2security.webp)](/blog/assets/ec2security.webp)
2. Click on **Key Pairs**, select **Create Key Pair** and type in some name. Click on the **Create** button and you’ll be asked to download a key file. Save it somewhere safe.[![](/blog/assets/ec2keypair.webp)](/blog/assets/ec2keypair.webp)
3. Run PuttyGen (it comes with Putty), click **Load** and select the key file you just saved. Now click on **Save private key** and save it as **privatekey.ppk**.
4. Back on the [AWS EC2 Console](https://console.aws.amazon.com/ec2/), click on **Launch Instance**.
   [![](/blog/assets/ec20.webp)](/blog/assets/ec20.webp)
5. Select **Community AMIs** and find **ami-ccf615a5**. It’s a Ubunty Jaunty 9.04 instance that's been customised to run scripts passed as user-data. You may pick any other alestic instance. (The screenshot below picks a different instance. Ignore that.)
   [![](/blog/assets/ec2launch.webp)](/blog/assets/ec2launch.webp)
6. Continue until you get to **Advanced Instance Options**. Here, copy and paste the following under **User Data**. **Do not make a mistake here!**
   ```bash
   ```

#!/bin/bash
mv /etc/ssh/sshd_config /etc/ssh/x
sed "s/^#\?Port.*/Port 443/" /etc/ssh/x > /etc/ssh/sshd_config
/etc/init.d/ssh restart

```
   [![](/blog/assets/ec2userdata.webp)](/blog/assets/ec2userdata.webp)
7. Keep pressing **Continue** and **Launch** the instance. Once launched, click on “Instances” on the left, and keep refreshing the page until the status turns green (running). Now, copy the **Public DNS** of the instance.
   [![](/blog/assets/ec2instancerunning.webp)](/blog/assets/ec2instancerunning.webp)
8. Run Putty. Type in **root@****<the-public-DNS-you-just-copied>** as the host name, and **443** as the port
   [![](/blog/assets/putty1.webp)](/blog/assets/putty1.webp)
9. Under **Connection > Proxy**, set **HTTP** as the proxy type. Type in the **Proxy hostname** and **Port** you normally use to access the Internet. Select **Yes** for **Do DNS name lookup at proxy end**. Type in your Windows login ID and password.
   [![](/blog/assets/putty2.webp)](/blog/assets/putty2.webp)
10. Under **Connection > SSH**, select **Enable Compression**.
    [![](/blog/assets/putty5.webp)](/blog/assets/putty5.webp)
11. Under **Connection > SSH > Auth**, click **Browse** and select the **privatekey.ppk** file you’d saved earlier.
    [![](/blog/assets/putty3.webp)](/blog/assets/putty3.webp)
12. Under **Connection > SSH > Tunnels**, type **9090** as the **Source port**, **Dynamic** as the **Destination**, and click **Add**.
    [![](/blog/assets/putty4.webp)](/blog/assets/putty4.webp)
13. Now click **Open**. You should get a terminal into your Amazon EC2 instance.
14. Open your Browser, and set the SOCKS server to localhost:9090. For Internet Explorer, go to **Tools – Options – Connections – LAN Settings**, select **Use a proxy ...**, click on **Advanced**, and type **localhost**:**9090** as the **Socks** server. Leave all other fields blank.
    [![](/blog/assets/ieconfig.webp)](/blog/assets/ieconfig.webp)
15. For Firefox, go to **Tools – Options – Advanced – Network – Settings** and select **Manual proxy configuration**. Set the Socks Host to **localhost**:**9090** and leave all other fields blank.
    [![](/blog/assets/ffconfig.webp)](/blog/assets/ffconfig.webp)
16. Also, go to URL **about:config**, and make sure that **network.proxy.socks\_remote\_dns** is set to **true**.

That’s it. You should now be able to check [most blocked sites](http://www.moon-blog.com/2009/02/top-ten-most-blocked-websites.html) like [Facebook](http://www.facebook.com/) and [YouTube](http://www.youtube.com/).
Those who favour the command line may want to automate Steps 1-7 by downloading Amazon’s [EC2 API tools](http://developer.amazonwebservices.com/connect/entry.jspa?externalID=351). [EC2 API tools work from behind a proxy too](http://developer.amazonwebservices.com/connect/message.jspa?messageID=52178). The commands you’ll need to use to setup are:
`set EC2_HOME=your-ec2-home-directory
set EC2_CERT=your-ec2-certificate
set EC2_PRIVATE_KEY=your-ec2-private-key
ec2-add-keypair mykeypair
ec2-authorize default -p 443
set EC2_JVM_ARGS=-DproxySet=true -DproxyHost=yourproxy \
-DproxyPort=yourport -Dhttps.proxySet=true \
-Dhttps.proxyHost=yourproxy -Dhttps.proxyPort=yourport \
-Dhttp.proxyUser=yourusername -Dhttps.proxyUser=yourusername \
-Dhttp.proxyPass=yourpassword -Dhttps.proxyPass=yourpassword
ec2-run-instances ami-ccf615a5 --key mykeypair --user-data-file your-startup-file-containing-lines-in-step-6`
You can go further and use any software (such as Skype) if you install [FreeCap](http://www.freecap.ru/eng/). More details are in this article on [Secure Firefox and IM with Putty](http://thinkhole.org/wp/2006/05/10/howto-secure-firefox-and-im-with-putty/).
Linux users may want to check out [ProxyTunnel](http://proxytunnel.sourceforge.net/) and this article on [Tunneling SSH over HTTP(S)](http://dag.wieers.com/howto/ssh-http-tunneling/).
**Update**: Follow-ups on [hacker news comments](http://news.ycombinator.com/item?id=1043413), [twitter](http://tweetmeme.com/story/427812352/ssh-tunneling-through-web-filters-s-anandnet), [delicious](http://delicious.com/url/0a6b39e211f481515ae02cab92cec1e7) and [digg](http://digg.com/security/SSH_Tunneling_through_web_filters_s_anand_net).

---

## Comments

<!-- wp-comments-start -->
- **[SSH Tunneling via Rackspacecloud | s-anand.net](http://www.s-anand.net/blog/ssh-tunneling-via-rackspacecloud/)** _11 Feb 2010 5:42 pm_ _(pingback)_:
  [...] Tunneling via Rackspacecloud February 11th, 2010 How I do things S Anand I wrote about SSH Tunneling through web filters using Amazon’s EC2 at 8 cents/hr. With Rackspacecloud, you can get that down to 1.5 cents/hr. [...]
- **[Janitha](http://www.janitha.com)** _10 Jan 2010 7:36 pm_:
  Good writeup, ssh tunnels are something I can't live without...
  Step 9 can be skipped completely if no proxy is needed to be configured.
  Also don't forget, doing all of this still sends the DNS requests in the clear to the usual/old dns server and not through EC2. If the DNS server is also meant to filter and redirect, this can be a issue. To go around that, in firefox you can go to about:config and set network.proxy.socks\_remote\_dns = true
- **[Janitha](http://www.janitha.com)** _10 Jan 2010 7:38 pm_:
  And for linux folks, you can simply run the ssh command with the -D switch.
- **[uberVU - social comments](http://www.ubervu.com/conversations/www.s-anand.net/blog/ssh-tunneling-through-web-filters/)** _10 Jan 2010 8:42 pm_ _(trackback)_:
  **Social comments and analytics for this post...**
  This post was mentioned on Twitter by proactivedefend: News Update: SSH Tunneling through web filters http://ow.ly/16iWFp...
- **[SSH Tunneling through web filters | s-anand.net &laquo; Netcrema &#8211; creme de la social news via digg + delicious + stumpleupon + reddit](http://www.netcrema.com/?p=24319)** _10 Jan 2010 10:16 pm_ _(pingback)_:
  [...] SSH Tunneling through web filters | s-anand.nets-anand.net [...]
- **[=== popurls.com === popular today](http://popurls.com/pop)** _10 Jan 2010 10:40 pm_ _(trackback)_:
  **=== popurls.com === popular today...**
  yeah! this story has entered the popular today section on popurls.com...
- **Kiril** _10 Jan 2010 10:52 pm_:
  Thanks for great tutorial. I have set it all up and it works!
  The only thing is that step 6 commands didn't execute after I started new instance. I had to log in and execute each line from the terminal.
- **kyle** _11 Jan 2010 1:27 am_:
  If you have access to a webserver that has sshd running you can do this as well. You use the 'D' flag with ssh for dynamic port forwarding. Its the same thing you are doing here just without aws. I use:
  ssh -D 1080 username@site.com and set firefox to use a socks proxy localhost 1080
- **[SSH Tunneling through web filters | s-anand.net : Popular Links : eConsultant](http://popular.econsultant.com/ssh-tunneling-through-web-filters-s-anand-net/)** _11 Jan 2010 2:43 am_ _(pingback)_:
  [...] rest is here: SSH Tunneling through web filters | s-anand.net 10 January 2010 | Uncategorized | Trackback | del.icio.us | Stumble it! | View Count : 0 Next [...]
- **dataminer** _11 Jan 2010 5:29 pm_:
  Or you can use a cheap linode / slicehost / prgmr virtual server and openvpn
- **spif** _11 Jan 2010 8:09 pm_:
  Good endpoint security can prevent this sort of thing, and even more sophisticated methods. But many organizations don't implement endpoint security at all, and others don't block or even monitor for this sort of thing.
- **Andrew** _10 Jan 2010 6:50 pm_:
  You should make sure in Firefox to set "network.proxy.socks\_remote\_dns" to TRUE under about:config. Otherwise, DNS requests will not be passed through your proxy and it will still be pretty obvious which sites you're browsing.
- **[S Anand](http://www.s-anand.net/)** _29 Jan 2010 8:34 am_:
  Thanks Coop, I fixed it. (Actually, I changed it to "/etc/init.d/ssh restart" which works for me. Haven't tried reload.)
- **Coop** _28 Jan 2010 4:04 pm_:
  FYI. There's a typo in the instructions on step 6 for those of you trying to get this to work.
  The final line of the command reads:
  /etc/init.d/sshd reload
  It should read:
  /etc/init.d/ssh reload
  Change that and it'll work. Pretty speedy too. The only downside to this is the need to constantly stop and start instances because you're cheap like me. Wish I could somehow trigger a new instance and terminate it after a set amount of time whilst updating the public DNS entry in putty. Un-likely.
- **[TTA](http://www.tarunactivity.com)** _18 Jan 2010 3:49 pm_:
  Good .. except for the fact that ~most if not all offices would forbid tunnelling for this very reason :P ...
- **[&raquo; How to get through your office&#8230; Thej Live](http://thej.in/?p=4583)** _18 Jan 2010 4:02 pm_ _(pingback)_:
  [...] to get through your office proxy using AWS http://www.s-anand.net/blog/ssh-tunneling-through-web-filters/ [...]
- **[S Anand](http://www.s-anand.net/)** _3 Feb 2010 5:26 pm_:
  Incidentally, with Rackspace Cloud's 1.5 cents per hour pricing, this becomes significantly more attractive.
- **anderbill** _19 Jan 2010 11:05 am_:
  I use ssh tunnel easy, get it from http://www.networktunnel.net
  Ssh Tunnel Easy is an innovative ssh tunneling software, it can make an encrypted ssh tunnel between your machine and ssh server host, then tunnel your program TCP connection automatically through this encrypted tunnel to data forwarded. It help you unblock and surf securely in the internet.
  Main features
  All in One
  A simple all in one solution, you do not need a complex sockscap/firefox + autoproxy + myentunnel + putty combination, and only a few mouse click, all config completed. Auto reconnect, support https proxy and NTLM authentication.
  Multi channel load balancing
  Under normal circumstances, because the SSH server is limiting the number of simultaneous connections, if you have too much TCP concurrent connections in one tunnel, may be cause your SSH tunnel freeze. Therefore, Ssh Tunnel Easy use similar to IE's LCIE (Loosely-Coupled IE) multi-channel load-balancing technology to improve it. In other words, Ssh Tunnel Easy will automatically create multiple ssh tunnel, then your browser's tcp connections will automatically be distributed to each ssh channel average, so that each channel ssh connections will not be too much, solve this problem perfect, and it can also significantly speed up your browsing speed.
- **Morbius** _14 Feb 2010 12:28 am_:
  I have read with interest the articles related to SSH Tunneling (through Web Filters and RackSpaceCloud) published on this web site.
  The problem I am trying to solve is slightly different, but I believe that someone might be able to guide me towards a solution.
  DESCRIPTION OF MY PROBLEM
  I would like to connect to several multi-media web sites located in several countries (namely France, Netherlands and Germany) and access some of the contents present on those sites. However, I am located in another country (I am based in Asia), and the problem is that those websites filter the access to their contents based on location: for instance, the French web site only allows access to its contents to users located in France. The filtering seems to be done via the IP address.
  Are their any tools that I could use and which could allow me to bypass this filtering, by making me appear like someone being based in the said country (for instance, in the example given above, France) ? I imagine that I should be able to select the country I want to appear being in.
  Could someone kindly help me and guide me towards a possible solution to my problem ?
  Thanks for reading, and I would just like to add that I use a client platform based on Windows 7.
- **[S Anand](http://www.s-anand.net/)** _14 Feb 2010 4:56 pm_:
  @Morbius: Not sure... you'd need a server in each of those countries. EC2 has a Europe instance that's based in Dublin. Not sure which cloud vendors have servers in those places, though.
- **[S Anand](http://www.s-anand.net/)** _5 Mar 2010 2:24 pm_:
  http://www.mtu.net/~engstrom/ssh-proxy.php explains how to use corkscrew on Linux machines to use SSH via a proxy.
- **Morbius** _18 Feb 2010 1:11 pm_:
  Thank you for your answer, S.Anand.
  Do you think that using the Tor Network (I am afraid it might be a little slow, given that the data I need to access are video files...) or XeroBank (heard of it, but never used it...) could help?
- **[Ravi Atluri](http://blog.raviatluri.in)** _12 Nov 2010 5:19 pm_:
  I am having some problems with proxy authentication while SSH tunneling.
  Did you face any issue with ISA authentication ?
- **[Using sshuttle to remain Safe on Insecure Wi-Fi | Thejesh GN](http://thejeshgn.com/2012/06/28/using-sshuttle-to-remain-safe-on-insecure-free-wifi/)** _28 Jun 2012 12:57 pm_ _(pingback)_:
  [...] If you are on Windows try Anand’s method. [...]
- **[It&#8217;s Raining min()!: Running SEASR&#8217;s MEANDRE software as an Amazon Cloud Instance | devolution](http://www.devingriffiths.com/archive/2011/06/its-raining-min-running-seasrs-meandre-software-as-an-amazon-cloud-instance/)** _29 Jun 2011 6:07 pm_ _(pingback)_:
  [...] path viable.  But in the short term, all I needed to do was bind those ports on my local PC to an ssh tunnel, and configure my Firefox browser to use the linux box as a proxy using the ssh tunnel. [...]
- **[How to remain anonymous online | Thejesh GN](http://thejeshgn.com/2012/04/10/howto-remain-anonymous-online/)** _10 Apr 2012 9:23 am_ _(pingback)_:
  [...] is similar to the one explained in this blog title Tor on SSH. Its not very difficult to build an SSH tunnel yourself. [g] SSHing over Tor is very [...]
- **[Nikolay Kolev](http://nikolay.com)** _4 Dec 2011 8:21 pm_:
  I've been using Hamachi for the same purposes (now part of LogMeIn) and, just in case, I SSH over Hamachi's connection: [LogMeIn Hamachi](https://secure.logmein.com/products/hamachi/).
- **[Software for my new laptop 2 | s-anand.net](http://www.s-anand.net/blog/software-for-my-new-laptop-2/)** _27 Sep 2011 7:16 pm_ _(pingback)_:
  [...] Putty [new]: SSH for Windows, but can also act as an SSH tunnel [...]
- **[S Anand](http://www.s-anand.net/)** _17 Jul 2011 8:15 am_:
  @Lemming, as long as you have PuTTY running on your machine, others can use YOUR machine as a Socks proxy. Or you could create a non-root account for them on the EC2 server to log into.
- **Lemming** _15 Jul 2011 1:49 am_:
  Hi S Anand, I followed your instructions and the SOCKS server/proxy is working great on my machine. Thanks for the detailed instructions!
  I'm wondering if I could share the SSH server with some friends. A number of them face restrictive proxies like you described, while others have to travel to China for work. How would I share my SSH server, without giving away my private key and root access to the EC2 instance? My friends would also be using Windows/PuTTY.
- **Lemming** _20 Jul 2011 3:46 pm_:
  Hi S Anand, thanks for the info. I'll look into a non-root account solution.
- **Mohamed Infaz** _11 Jun 2012 3:40 am_:
  Sir, lets say i have successfully done this!! can i use this sock5 proxy to by pass torrent block in my university network?! We are using a proxy sever to connect to the internet in our university and otherwise we are not able to connect to the network! I have successfully used ultrasurf software to good effect to bypass download limits! so i am sure that i would be able to pent 9996 port. Can i use that port, as the source port for incoming connection in utorrent?! Please help! :)
<!-- wp-comments-end -->
```
