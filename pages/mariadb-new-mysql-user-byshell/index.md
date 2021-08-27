
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MySQL Create new MySQL user by shell</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h2>MySQL Create new MySQL user by shell</h2>
    <div class="published">&#128198; published: 08.09.2015</div>
    <div class="modified">&#128198; modified: 13.07.2020</div>
    <div class="tags">&#128204; centos, mariadb, mysql, user, shell</div>
    <hr>

    Set a new user with access from a remote host:
    <pre>CREATE USER 'DummyUser1'@'localhost' IDENTIFIED BY 'PASSWORD';
CREATE USER 'DummyUser2'@'%' IDENTIFIED BY 'PASSWORD';
    </pre>
Grant access to the users on both databses (DummyDB1, DummyDB2):
    <pre>CREATE USER 'DummyUser1'@'localhost' IDENTIFIED BY 'PASSWORD';
        CREATE USER 'DummyUser2'@'%' IDENTIFIED BY 'PASSWORD';</pre>

    <p>To give a user rights on a root privileged command:</p>
    <pre>vi /etc/sudoers​<br />&lt;USER&gt; ALL = NOPASSWD: /bin/systemctl restart httpd</pre>
    <p>Now the user could restart the httpd deamon:</p>
    <pre>sudo systemctl restart httpd</pre>
</body>
</html>
