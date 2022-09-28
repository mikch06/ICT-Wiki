#  status / set-locale
<!-- date: 2015-09-09 00:00:00 -->
<!-- category: centos -->
<!-- tags: centos,linux,locale,locale-status -->

Show and edit locale status on CentOS:

Show locale status:
<pre>[root@host]# localectl status
System Locale: LANG=de_DE.UTF-8
VC Keymap: sg
X11 Layout: ch
Show all possible locaels:
localectl list-locales
</pre>
Setzen der neuen locale:
<pre>localectl set-locale LANG="locale name"
locale</pre>