# How to clear blocked IP list
<!-- date: 2015-09-03 00:00:00 -->
<!-- category: synology -->
<!-- tags: Synology, IP block -->
***
Login to your NAS by ssh:

May take a backup from the autoblock databse:

    cp /etc/synoautoblock.db
    /etc/synoautoblock.db.bak

Change to database sqlite mode:

    sqlite3 "Enter"
    open the database:
    sqlite> .open /etc/synoautoblock.db

Show tables:
    
    sqlite> .tables
    > AutoBlockIP

Show all entries:
    
    sqlite> select * from AutoBlockIP;

Delete all entries from database:    
    
    sqlite> delete from AutoBlockIP;

Show all entries again:

    sqlite> select * from AutoBlockIP;

Delete a single entry:

    sqlite> delete from AutoBlockIP where IP = "192.168.2.12";

Leave sqlite
