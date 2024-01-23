# Remove old kernels
--- 
date: 2020-03-24 00:00:00
category: centos
tags: centos, linux
---

***
Current running kernel

    uname -an

Show installed kernels:
    
    rpm -q kernel

<b>CentOS 7:</b> 
Remove old kernels with package-cleanup (yum-utils required)

    package-cleanup --oldkernels package-cleanup --oldkernels --count=2

<b>CentOS 8:</b> Remove old kernels with dnf

    dnf remove --oldinstallonly
    dnf remove --oldinstallonly --setopt installonly_limit=2
