# Nginx Basic Auth config
<!-- date: 2020-04-05 00:00:00 -->
<!-- category: nginx -->
<!-- tags: nginx, Basic Auth, Linux -->
***

Configure location:

        location / {
        auth_basic "closed site";
        auth_basic_user_file htpasswd;
        }

Create password file:

    yum install httpd-tools</pre>
    
New file:

    htpasswd -c htpasswd-file "username"
    
New password:

Append user to existing file:

    htpasswd htpasswd-file "username"