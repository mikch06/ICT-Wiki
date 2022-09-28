# OpenBSD on apu pcengine
<!-- date: 2018-05-01 00:00:00 -->
<!-- category: openbsd -->
<!-- tags: OpenBSD, apu, pcengines -->
***

1. Download the small minirootXX.fs from OpenBSD.org<br>
2. Prepare an USB Stick:


    dd if=minirootXX.fs of=/dev/usb-device bs=1


3. Prepare your serial console: 115200,8n1.<br>
4. Insert Memory stick and boot.<br>
5. At the console prompt choose Nr. 2, boot from USB Stick<br>
6. For just a few seconds the BSD boot prompt will appear. Now you have to redirect the serial console:<br>


    stty com0 115200
    set tty com0
    => press Enter

after the installation fix it in the boot.conf

    set tty com0
    -> the system will ask for that while the installation process.