# Sudoers
<!-- date: 2015-12-23 00:00:00 -->
<!-- category: centos -->
<!-- tags: CentOS, Linux, sudo -->
***
To give a user rights on a root privileged command:
    
    vi /etc/sudoers
    <USER> ALL = NOPASSWD: /bin/systemctl restart httpd

Now the user could restart the httpd deamon:

    sudo systemctl restart httpd
