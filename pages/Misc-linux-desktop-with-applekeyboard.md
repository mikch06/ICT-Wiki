# Linux Desktop with Apple Keyboard
<!-- date: 2015-01-01 00:00:00 -->
<!-- category: linux -->
<!-- tags:  -->
***
I like to have < > ° etc. in a correct way of use on my keyboard. <br><br>
    Usage:

- temoporary setting:


    vi /sys/module/hid_apple/parameters/iso_layout
    1 -> 0
    
- permanent setting:

    
    vi /etc/modprobe.d/hid_apple.conf
    options hid_apple iso_layout=0

Update initramfs bootfile:
    
    update-initframs
