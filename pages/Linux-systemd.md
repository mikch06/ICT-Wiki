# Systemd
<!-- date: 2017-01-11 00:00:00 -->
<!-- category: linux -->
<!-- tags: linux, systemd, systemctl -->
***


Helps for system administration with systemd:

Control and manipulate services

    systemctl
    systemctl enable [servicename]
    systemctl stop/start [servicename]
    systemctl disable [servicename]


Remove services from systemd

    systemctl stop [servicename]
    systemctl disable [servicename]
    rm /etc/systemd/system/[servicename]
    systemctl daemon-reload
    systemctl reset-failed