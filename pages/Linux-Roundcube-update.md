# Roundcube update
<!-- date: 2020-03-08 00:00:00 -->
<!-- category: linux -->
<!-- tags: Roundcube -->

<p>Download new roundcube version <strong>(complete package)</strong> from <a href="https://roundcube.net/download">https://roundcube.net/download</a> website or github:</p>
<pre>wget https://github.com/roundcube/roundcubemail/releases/download/1.4.3/roundcubemail-1.4.3-complete.tar.gz</pre>
<p>Unpack tar.gz package:  </p>
<pre>gunzip roundcubemail-1.4.3-complete.tar.gz</pre>
<p>Unpack tar package:</p>
<pre>tar -xvf roundcubemail-1.4.3-complete.tar</pre>
<p>Go to /bin directory:</p>
<pre>cd roundcubemail-1.4.3/bin/</pre>
<p>Run installto script to your install dir:</p>
<pre>./installto.sh ../../my.roundcube.installdir</pre>
