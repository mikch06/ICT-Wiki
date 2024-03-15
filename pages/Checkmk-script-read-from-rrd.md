--- 
date: 2024-03-15 00:00:00
category: checkmk
tags: checkmk, linux, monitoring
---

Checkmk local script:

Read out data from an rrd file and show the values e.g. bandwith up- and downstream:

    # /usr/lib/check_mk_agent/local

    #!/bin/bash
    # set -x
  
    workdir='/opt/iperfmon'
    #get data for altoo_office
    downstream=$(/usr/bin/rrdtool lastupdate $workdir/iperfmon.rrd |tail -1|awk '{ print $2}')
    upstream=$(/usr/bin/rrdtool lastupdate $workdir/iperfmon.rrd |tail -1|awk '{ print $3}')
    
    echo "0 Iperfmon downstream=$downstream|upstream=$upstream Iperf up- and downstream: $upstream | $downstream (MBit/s)"
    
    #echo "0 My service myvalue=73 My output text which may contain spaces"
