# Mount nfs share
--- 
date: 2015-09-07 00:00:00
category: centos
tags: linux, nfs, mount, fstab
---

***
1. Setup NFS Client:

    
    yum -y install nfs-utils

2. Create mountpoint:

    
    mkdir -p /mnt/nfs/example-share

Mount NFS share:

    mount <HOST>:/example-share /mnt/nfs/example-share
    hint: –> df -h
    hint: –> mount – show all mounts

3. Add mount to fstab for remounting after reboot:


    vi /etc/fstab <HOST>:/example-share /mnt/nfs/