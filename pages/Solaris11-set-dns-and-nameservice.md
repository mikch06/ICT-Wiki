#Configure DNS Client
<!-- date: 2015-09-07 00:00:00 -->
<!-- category: solaris -->
<!-- tags: Solaris11, Unix, DNS -->
***
Configure DNS Client:

    svccfg -s network/dns/client
    svc:/network/dns/client> setprop config/nameserver =
    (DNSSERVER1 DNSSERVER2)
    svc:/network/dns/client> setprop config/search = "Your Search Domain"
    svc:/network/dns/client> setprop config/domain = "YourDomain.ch"
    svcadm refresh network/dns/client
    svcadm restart network/dns/client

Configure name service (nsswitch.conf):

    svccfg -s system/name-service/switch
    listprop config
    setprop config/host = "files dns"
    setprop config/ipnode = astring: "files dns"
    end
    svcadm refresh name-service/switch
    sv