# Systemd: Example service script
--- 
date: 2020-05-25 00:00:00
category: linux
tags: linux, systemd
Example service script:<br>
e.g. daphne application server with a django app.
<pre># vi /etc/systemd/system/daphne.service</pre>
<pre>[Unit]
Description=daphne service to run django application
After=network.target
After=nginx.service

[Service]
Type=simple
User=mik
Group=mik
WorkingDirectory=/opt/app/
ExecStart=/opt/app/wine-env/bin/daphne djangoapp.asgi:application
ExecStop=/bin/kill -s TERM $MAINPID
Restart=always

[Install]
WantedBy=multi-user.target</pre>
</body>
</html>
