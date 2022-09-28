# Nextcloud calendar SQL commands
<!-- date: 2020-09-03 00:00:00 -->
<!-- category: nextcloud -->
<!-- tags: Nextcloud -->
***
Nextcloud: Use Nextcloud with SQL commands

- Nextcloud calendar:

    Select all calendar events older than ...

        SELECT * FROM `oc_calendarobjects` WHERE calendarid = 2 AND lastoccurence >= 1583323200
        - calendarid -> e.g. your birthday calendar
        - lastoccurence -> timestamp in unixtime

