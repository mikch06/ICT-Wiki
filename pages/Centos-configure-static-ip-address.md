--- 
date: 2015-09-09 00:00:00
category: centos
tags: centos, linux, ip, addr
---

# Configure static IP address

Position of the interface configuration files:

    /etc/sysconfig/network-scripts

    
ip addr

shows the names of available interfaces:

    enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc
    pfifo_fast state UP qlen 1000
    link/ether 08:00:27:66:c7:99 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.40/24 brd 192.168.0.255 scope global enp0s3
    valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe66:c799/64 scope link
    valid_lft forever preferred_lft forever


Now the config file ifcfg-enp0s3 can be edited with the static config:

    TYPE="Ethernet"
    NAME="enp0s3"
    ONBOOT="yes"
    IPADDR="192.168.0.40"  
    BOOTPROTO="static" 
    GATEWAY="192.168.0.1"