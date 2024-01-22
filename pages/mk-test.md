---
date: "2010-12-03 00:00:00"
category: "centos"
tags: 
  - "centos"
  - "fail2ban"
---
# CentOS Linux fail2ban



On exposed systems to the internet fail2ban is used to avoid attacks e.g. on ssh deamon. 
This shows the install and config on the CentOS 7.2 release with using firewalld (preinstalled). 
First install fail2ban from repo:
<pre>yum -y install fail2ban</pre>
For own settings the main config ‘jail.conf’ could be copied.
<pre>cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local</pre>
Now you can edit ‘jail.local’ with your own fonfigurations.

<pre>[sshd] #--> uncommend to activate fail2ban for sshd
enabled = true #--> use firewalld not iptables
ignoreip = 192.168.2.0 #--> fail2ban ignores these ip's
destemail =  e-mail@address.ch #--> fail2ban sends ban informations to this address
sendername = Fail2Ban - hostname #--> hostinfos in e-mail
usedns = no #--> don't resolve dns names</pre>
Now you can enable and start the fail2ban deamon:
<pre>systemctl enable fail2ban
systemctl start fail2ban</pre>

To status of fail2ban and banned ip’s use:
<pre>fail2ban-client status sshd
Status for the jail: sshd
|- Filter
|  |- Currently failed: 0
|  |- Total failed:     37
|  `- File list:        /var/log/secure
`- Actions
        |- Currently banned: 0
        |- Total banned:     4
        `- Banned IP list:</pre>

###Links:
<a href="http://www.fail2ban.org" target="_blank">http://www.fail2ban.org
