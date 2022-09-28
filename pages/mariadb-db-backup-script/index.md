# MariaDB backup script
<!-- date: 2010-09-07 00:00:00 -->
<!-- category: MariaDB -->
<!-- tags: mariadb, mysql, backup, linux -->
    WORKDIR=/home/bak
    DB=<Datenbankname>
    USER=<Username>
    PW=<Passwort>
    HOST=<Hostname>
    DUMPFILE=$DB.sql
    DUMPCOPY=$DB-$(date +%Y-%m-%d-%H-%M-%S).sql
    /usr/local/bin/mysqldump
    $DB -u $USER -h $HOST --password=$PW > $WORKDIR/$DUMPFILE
    cp $WORKDIR/$DUMPFILE $WORKDIR/$DUMPCOPY

# Delete backup files older than 3 days:
    
    find $WORKDIR/*.sql -mtime +3 -exec rm -r {} \;

