--- 
date: 2015-09-08 00:00:00
category: MySQL
tags: centos, mariadb, mysql, user, shell
---
# MySQL Create new MySQL user by shell

Set a new user with access from a remote host:

    CREATE USER 'DummyUser1'@'localhost' IDENTIFIED BY 'PASSWORD';
    CREATE USER 'DummyUser2'@'%' IDENTIFIED BY 'PASSWORD';
Grant access to the users on both databses (DummyDB1, DummyDB2):
    
    CREATE USER 'DummyUser1'@'localhost' IDENTIFIED BY 'PASSWORD';
    CREATE USER 'DummyUser2'@'%' IDENTIFIED BY 'PASSWORD';</pre>

To give a user rights on a root privileged command:
    
    vi /etc/sudoers
    <USER> ALL = NOPASSWD: /bin/systemctl restart httpd
Now the user could restart the httpd deamon:
    
    sudo systemctl restart httpd