# MariaDB Installation on CentsOS7
<!-- date: 2015-09-17 00:00:00 -->
<!-- category: centos -->
<!-- tags: centos, mariadb, mysql -->

Setup a Maria DB Server on CentOS7:
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

    yum install epel-release
    yum install phpmyadmin
        Links:
   <a href="https://mariadb.org">https://mariadb.org

