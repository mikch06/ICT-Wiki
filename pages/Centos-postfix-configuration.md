--- 
date: 2017-04-22 00:00:00
category: centos
tags: centos, linux
---
# CentOS Postfix Configuration

Scenario: Homeserver should send e-mails by your ISP-hosted domain:

Packages:

    yum -y install postfix

Edit the following lines in the postfix main config:
    
    /etc/postfix/main.cf

    mydomain = "MY-DOMAIN"
    myorigin = $myhostname
    myorigin = $mydomain
    inet_interfaces = all
    inet_interfaces = localhost
    inet_protocols = ipv4
    mydestination = $myhostname, localhost.$mydomain, localhost
    mynetworks_style = host
    relayhost = <STMP.HOST.ADDRESS>:<PORT>
    smtpd_sasl_auth_enable = yes
    smtpd_sasl_path = smtpd
    smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
    smtp_sasl_type = cyrus
    smtp_sasl_auth_enable = yes
    smtp_sasl_security_options = noanonymous
