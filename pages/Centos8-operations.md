# CentOS8: Operations
<!-- date: 2020-08-17 00:00:00 -->
<!-- category: linux -->
<!-- tags: entos, linux -->
***
### Restart Networking:

    systemctl stop NetworkManager.service
    systemctl start NetworkManager.service

OR:

    nmcli networking off
    nmcli networking on


    ->
    nmcli n off
    nmcli n on