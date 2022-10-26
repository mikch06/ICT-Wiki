# CentOS7 to CentOS8 in place Upgrade
<!-- date: 2020-09-17 00:00:00 -->
<!-- category: centos -->
<!-- tags: Centos, Linux -->
***
#<q>DRAFT</q>

<h3>Update procedure</h3>

<pre>
    Update to the last level

    Install epel repo
    Make cache fast

yum makecache fast

    Install utils, rpmconfg

yum install -y yum-utils rpmconf 

    Rpmconf: Locate and remove conflicting config files

rpmconf -a

Your choice: N (default choice)

    List packages that are not required

package-cleanup --leaves

    List packages that are older or duplicate

package-cleanup --orphans

    Remove those packages

</pre>
<p>To give a user rights on a root privileged command:</p>
<pre>vi /etc/sudoers​<br />&lt;USER&gt; ALL = NOPASSWD: /bin/systemctl restart httpd</pre>
<p>Now the user could restart the httpd deamon:</p>
<pre>sudo systemctl restart httpd</pre>
