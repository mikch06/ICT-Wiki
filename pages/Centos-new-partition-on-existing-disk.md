# CentOS New Partition on existing disk
<!-- date: 2020-07-08 00:00:00 -->
<!-- category: linux -->
<!-- tags: centos, linux, partitioning, fdisk -->
***

### Partitioning

    fdisk -l

    fdisk /dev/sda
    Welcome to fdisk (util-linux 2.23.2).
     
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.
     
     
    Command (m for help): p
     
    Disk /dev/sda: 322.1 GB, 322122547200 bytes, 629145600 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x000a6c5c
     
       Device Boot      Start         End      Blocks   Id  System
    /dev/sda1   *        2048     2099199     1048576   83  Linux
    /dev/sda2         2099200    16777215     7339008   8e  Linux LVM
     
     
    Command (m for help): n
    Partition type:
       p   primary (2 primary, 0 extended, 2 free)
       e   extended
    Select (default p):
    Using default response p
    Partition number (3,4, default 3):
    First sector (16777216-629145599, default 16777216):
    Using default value 16777216
    Last sector, +sectors or +size{K,M,G} (16777216-629145599, default 629145599):
    Using default value 629145599
    Partition 3 of type Linux and of size 292 GiB is set
     
    Command (m for help): t
    Partition number (1-3, default 3):
    Hex code (type L to list all codes): L
     
     0  Empty           24  NEC DOS         81  Minix / old Lin bf  Solaris
     1  FAT12           27  Hidden NTFS Win 82  Linux swap / So c1  DRDOS/sec (FAT-
     2  XENIX root      39  Plan 9          83  Linux           c4  DRDOS/sec (FAT-
     3  XENIX usr       3c  PartitionMagic  84  OS/2 hidden C:  c6  DRDOS/sec (FAT-
     4  FAT16 <32M      40  Venix 80286     85  Linux extended  c7  Syrinx
     5  Extended        41  PPC PReP Boot   86  NTFS volume set da  Non-FS data
     6  FAT16           42  SFS             87  NTFS volume set db  CP/M / CTOS / .
     7  HPFS/NTFS/exFAT 4d  QNX4.x          88  Linux plaintext de  Dell Utility
     8  AIX             4e  QNX4.x 2nd part 8e  Linux LVM       df  BootIt
     9  AIX bootable    4f  QNX4.x 3rd part 93  Amoeba          e1  DOS access
     a  OS/2 Boot Manag 50  OnTrack DM      94  Amoeba BBT      e3  DOS R/O
     b  W95 FAT32       51  OnTrack DM6 Aux 9f  BSD/OS          e4  SpeedStor
     c  W95 FAT32 (LBA) 52  CP/M            a0  IBM Thinkpad hi eb  BeOS fs
     e  W95 FAT16 (LBA) 53  OnTrack DM6 Aux a5  FreeBSD         ee  GPT
     f  W95 Ext'd (LBA) 54  OnTrackDM6      a6  OpenBSD         ef  EFI (FAT-12/16/
    10  OPUS            55  EZ-Drive        a7  NeXTSTEP        f0  Linux/PA-RISC b
    11  Hidden FAT12    56  Golden Bow      a8  Darwin UFS      f1  SpeedStor
    12  Compaq diagnost 5c  Priam Edisk     a9  NetBSD          f4  SpeedStor
    14  Hidden FAT16 <3 61  SpeedStor       ab  Darwin boot     f2  DOS secondary
    16  Hidden FAT16    63  GNU HURD or Sys af  HFS / HFS+      fb  VMware VMFS
    17  Hidden HPFS/NTF 64  Novell Netware  b7  BSDI fs         fc  VMware VMKCORE
    18  AST SmartSleep  65  Novell Netware  b8  BSDI swap       fd  Linux raid auto
    1b  Hidden W95 FAT3 70  DiskSecure Mult bb  Boot Wizard hid fe  LANstep
    1c  Hidden W95 FAT3 75  PC/IX           be  Solaris boot    ff  BBT
    1e  Hidden W95 FAT1 80  Old Minix
    Hex code (type L to list all codes): 8e
    Changed type of partition 'Linux' to 'Linux LVM'
     
    Command (m for help): w
    The partition table has been altered!
     
    Calling ioctl() to re-read partition table.
     
    WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
    The kernel still uses the old table. The new table will be used at
    the next reboot or after you run partprobe(8) or kpartx(8)
    Syncing disks.
     
    partprobe
    [root@sourcerepos ~]# lsblk
    NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    sda               8:0    0  300G  0 disk
    ├─sda1            8:1    0    1G  0 part /boot
    ├─sda2            8:2    0    7G  0 part
    │ ├─centos-root 253:0    0  6.2G  0 lvm  /
    │ └─centos-swap 253:1    0  820M  0 lvm  [SWAP]
    └─sda3            8:3    0  292G  0 part
    sr0              11:0    1 1024M  0 rom


To give a user rights on a root privileged command:

    vi /etc/sudoers
    <USER> ALL = NOPASSWD: /bin/systemctl restart httpd

Now the user could restart the httpd deamon:
    
    sudo systemctl restart httpd
