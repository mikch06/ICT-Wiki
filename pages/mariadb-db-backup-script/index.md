
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Template</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h2>Title</h2>
    <div class="published">&#128198; published: 06.10.2015</div>
    <div class="modified">&#128198; modified: 13.07.2020</div>
    <div class="tags">&#128204; mariadb, mysql, backup, linux</div>
    <hr>
    <pre>WORKDIR=/home/bak
DB=<Datenbankname>
USER=<Username>
PW=<Passwort>
HOST=<Hostname>
DUMPFILE=$DB.sql
DUMPCOPY=$DB-$(date +%Y-%m-%d-%H-%M-%S).sql
/usr/local/bin/mysqldump
$DB -u $USER -h $HOST --password=$PW > $WORKDIR/$DUMPFILE
cp $WORKDIR/$DUMPFILE $WORKDIR/$DUMPCOPY
</pre>
# Delete backup files older than 3 days:
<pre>find $WORKDIR/*.sql -mtime +3 -exec rm -r {} \;</pre>
</body>
</html>
