# Disable ipv6 on CentOS8
<!-- date: 2020-06-03 00:00:00 -->
<!-- category: centos -->
<!-- tags: CentOS, Linux, ipv6 -->
***
Disable ipv6 on CentOS8:
        
    # vi /etc/sysctl.conf

    net.ipv6.conf.all.disable_ipv6 = 1
    net.ipv6.conf.default.disable_ipv6 = 1


    sysctl -p