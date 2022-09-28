# Filesystem operations (rescan, create, resize, xfs)
<!-- date: 2020-07-02 00:00:00 -->
<!-- category: centos -->
<!-- tags: logical volume, lvresize, xfs, lvm, physical volume, pvresize, xfs_growfs -->

### Disks</h3>
Rescan existing disks:
<pre>echo 1 > /sys/class/scsi_device/1\:0\:1\:0/device/rescan</pre>
Check new disk:
<pre>fdisk -l /dev/sdb</pre>
<h3>Volumes</h3>
<p>Physical / Logical Volumes</p>
Create physical volume
<pre>pvcreate /dev/sda3
    Physical volume "/dev/sda3" successfully created.</pre>
Resize physical volume (e.g. extended in VMware)   
<pre>pvresize /dev/sdb</pre>
<pre>pvdisplay</pre>
Extend physical volume group 
<pre>vgextend centos /dev/sda3
    Volume group "centos" successfully extended​</pre>
<pre>vgdisplay</pre>
Extend logical volume<br>
in G'igs
<pre>lvextend -L +8G /dev/system/volume</pre>
or full (using everything)
<pre>lvextend -l 100%FREE /dev/mapper/volume</pre>
Grow filesystem
<pre>xfs_growfs /dev/system/volume</pre>
Create new logical volume
<pre>mkfs.xfs /dev/centos/volume</pre>
see: <a href="centos-new-partition-on-existing-disk.html">CentOS New Partition on existing disk</a>
