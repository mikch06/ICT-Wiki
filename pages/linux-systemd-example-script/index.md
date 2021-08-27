
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Systemd: Example service script</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h2>Systemd: Example service script</h2>
    <div class="published">&#128198; published: 25.05.2020</div>
    <div class="modified">&#128198; modified: </div>
    <div class="tags">&#128204; linux, systemd</div>
    <hr>
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
