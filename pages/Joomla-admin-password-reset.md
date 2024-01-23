--- 
date: 2015-09-08 00:00:00
category: joomla
tags: Joomla, password reset
---
#Joomla! Admin Passwort reset

Lost the admin password of your Joomla! page or have no possibility to login on backend?

The admin password can be reset by database (e.g. phpMyAdmin).<br>
Login to your database server and navigate to table '_users'.


Put the following hash to the password field of an Superadmin:
    
    433903e0a9d6a712e00251e44d29bf87:UJ0b9J5fufL3FKfCc0TLsYJBh2PFULvT
After that you can login with:
    
    admin / admin
Please don't forget to change the password by the user administration.
###With SQL-Script:

Take the easy way by an SQL-script:

    INSERT INTO _users`
    (`name`, `username`, `password`, `params`)
    VALUES ('tempadmin', 'tempadmin',
    '433903e0a9d6a712e00251e44d29bf87:UJ0b9J5fufL3FKfCc0TLsYJBh2PFULvT', '');
    INSERT INTO `_user_usergroup_map` (`user_id`,`group_id`)
    VALUES (LAST_INSERT_ID(),'8');

Please be careful with da table prefix!
<br><br>
Login with:
<pre>tempadmin / admin</pre>

To give a user rights on a root privileged command:

    vi /etc/sudoers
    <USER> ALL = NOPASSWD: /bin/systemctl restart httpd
Now the user could restart the httpd deamon:

    sudo systemctl restart httpd
