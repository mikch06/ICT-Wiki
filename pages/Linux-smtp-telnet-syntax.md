--- 
date: 2015-09-15 00:00:00
category: linux
tags: linux, smtp, telnet
---
# Smtp telnet syntax

    telnet <MAILSERVER> 25

    HELO <MAILSERVER>

    mail from: test-mail@wiki.kissel.ch

    rcpt to: receiver@<MAILSERVER>

    data
    from: test-mail@wiki.kissel.ch
    to: receiver@<MAILSERVER>
    subject: TestMessage
    
    Hello World!
    
    .
    
    quit