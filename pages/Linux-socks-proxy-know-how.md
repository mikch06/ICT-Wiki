--- 
date: 2020-07-15 00:00:00
category: linux
tags: linux, socks5, putty, foxyproxy
---
# SOCKS(5) Proxy Know How

<h3>SOCKS Proxy with Putty and FoxyProxy:</h3>
![](https://kissel.ch/ict/images/putty-socks5-config1.png)
![](https://kissel.ch/ict/images/putty-socks5-config2.png)
<br>
<br>
Define your free proxy Port (2409)
<br><br>
![](https://kissel.ch/ict/images/foxyproxy-config.png)
<br>
After enabling FoxyProxy you're able to connect your home by ssh and browse local services.
<hr>
SOCKS Proxy tunnel by shell:
<pre>ssh -L 2409:localhost:2409 'user'@'host'
on cyon host:
ssh -D 2409 'user'@'host'</pre>
SOCKS Proxy tunnel over another hop:
<pre>
connection to 1. host:
ssh -L 2409:localhost:2409 user@1host.ch

connection on 1. to 2. host:
ssh -D 2409 user@2host.ch

Browser (e.g. firefox) / or FoxyProxy config from above
-> Settings -> Network Settings -> Manual proxy configuration 
SOCKS Host: localhost, Port: 2409
</pre>
