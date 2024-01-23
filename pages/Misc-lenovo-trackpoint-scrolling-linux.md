--- 
date: 2016-07-22 00:00:00
category: linux
tags: Lenovo, Thinkpad, Trackpoint, Scrolling
---
# Lenovo Thinkpad Trackpoint Scrolling on Linux (debian derivatives)

How to configure Linux to use Trackpoint Scrolling on Lenovo Thinkpads:
<br><br>
Create a file '20-thinkpad.conf'
<pre>in /usr/share/X11/xorg.conf.d/</pre>
<br>
with content:
<pre>Section "InputClass"
    Identifier "Trackpoint Wheel Emulation"
    MatchProduct       "TPPS/2 IBM TrackPoint|DualPoint Stick|Synaptics Inc.<br>
    Composite TouchPad / TrackPoint|ThinkPad USB Keyboard with TrackPoint|ThinkPad<br>  Compact USB Keyboard with TrackPoint|USB Trackpoint pointing device"
    MatchDevicePath    "/dev/input/event*"
    Option             "EmulateWheel"          "true"
    Option             "EmulateWheelButton"    "2"
    Option             "Emulate3Buttons"       "true"
    Option             "XAxisMapping"          "6 7"
    Option             "YAxisMapping"          "4 5"
EndSection</pre>
<pre>restart mdm (for LinuxMint Cinnamon) or reboot.</pre>