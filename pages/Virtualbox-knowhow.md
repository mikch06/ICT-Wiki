#VirtualBox KnowHow
--- 
date: 2015-10-16 00:00:00
category: virtualbox
tags: VirtualBox
***
Install Virtual Box Extension Pack:<br>
<br>
Download newest Extension Pack on Virtual Box Dwonloads and move it on your Server. 

Install with:

    vboxmanage extpack install Oracle_VM_VirtualBox_Extension_Pack-5.0.4-102546.vbox-extpack
    0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
    Successfully installed "Oracle VM VirtualBox Extension Pack".

Autostart Script for phpVirtualBox with systemd:

    cd /etc/systemd/system
    vi vboxwebsrv.service
    
    [Unit]
    Description=Start vboxwebsrv.service
    Before=shutdown.target reboot.target halt.target
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/vboxwebsrv
    RemainAfterExit=true
    KillMode=none
    
    [Install]
    WantedBy=multi-user.target
    
:x!

    systemctl enable vboxwebsrv.service
    systemctl start vboxwebsrv.service
