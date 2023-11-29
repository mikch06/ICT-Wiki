# Nextcloud calendar SQL commands
<!-- date: 2020-09-03 00:00:00 -->
<!-- category: nextcloud -->
<!-- tags: Nextcloud -->
***
Nextcloud: Use Nextcloud with SQL commands

- Nextcloud calendar:

    Select all calendar events older than 31.12.2021 - 23:55:55

        SELECT * FROM `oc_calendarobjects` WHERE calendarid = 2 AND lastoccurence <= 1640991355;
          
        - calendarid -> e.g. your birthday calendar
        - lastoccurence -> timestamp in unixtime

