# Checkmk: Show current logins
--- 
date: 2023-05-09 00:00:00
category: checkmk
tags: checkmk, plugins
***
### Linux

    # Check disk free
    # mki, 2023.05.09
    count=$(df -h / |awk {'print $5'} |tail -1)
    echo "P "Container-Filesystem" count=$count;80;90 Overlay-Filesystem"



