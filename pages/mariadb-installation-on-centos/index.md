
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MariaDB Installation on CentsOS7</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h2>MariaDB Installation on CentsOS7</h2>
    <div class="published">&#128198; published: 17.09.2015</div>
    <div class="modified">&#128198; modified: 13.07.2020</div>
    <div class="tags">&#128204; centos, mariadb, mysql</div>
    <hr>
    Setup a Maria DB Server on CentOS7:<br>
    <pre>yum -y install mariadb-server mariadb
systemctl enable mariadb
systemctl status mariadb
mysql</pre>
    Create MariaDB Server admin password:
<pre>mysqladmin -u root password <PASSWORD></pre>
    Config external access from remote host/Tool to database Server:
<pre>cd /etc/my.cnf.d
vi server.cnf</pre>       
Set to [mysqld] block:
<pre>[mysqld]
bind-address    = 0.0.0.0</pre>
        Create User with external access rights:
    <pre>mysql -u root -p <PASSWORD>
create user 'root'@'%' IDENTIFIED BY '<PASSWORD>';
grant all on test to 'root'@'%';
flush privileges;</pre>
        Grant all privileges to database server admin user from extern!!<br><br>
        Be careful!
        <pre>GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' with grant option;
flush privileges;</pre>

            Install phpmyadmin on CentOS:<br><br>
            For the usage of phpmyadmin install the EPEL (Extra Packages for Enterprise Linux)
        <pre>yum install epel-release
yum install phpmyadmin</pre>
        Links:
       <a href="https://mariadb.org">https://mariadb.org</a>
</body>
</html>
