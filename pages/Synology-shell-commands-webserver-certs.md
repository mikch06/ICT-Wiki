# Synology certificates
--- 
date: 2018-01-06 00:00:00
category: Synology
tags: Synology,certs,tls

Is it possible to change certificates for the file stations and synology ui by shell?<br><br>
Yes, it is.<br><br>
You can find and replace the certs here:
<pre>/usr/syno/etc/certificate/system/default</pre>
After editing the certificates you can use the syno-cli to manipulate the services:<br><br>
Work with the root user (careful):
<pre># synoservice </pre>
you'll get the help and see --status
<pre># synoservice --status</pre>
Now you have all syno services listed.<br><br>
For restarting the webserver (nginx) you can restart the nginx service which you find in the status list:
<pre>=======================================
Service [nginx] status=[enable]
required upstart job:
    [nginx] is start.
=======================================</pre>
Use the synoservicectl tool to restart the service:
<pre># synoservicectl --restart nginx</pre>
