
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Systemd</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h2>Systemd</h2>
    <div class="published">&#128198; published: 11.01.2017</div>
    <div class="modified">&#128198; modified:</div>
    <div class="tags">&#128204; linux, systemd, systemctl</div>
    <hr>

    Helps for system administration with systemd:<br>
    Control and manipulate services
    <pre>systemctl
systemctl enable [servicename]
systemctl stop/start [servicename]
systemctl disable [servicename]
</pre>
Remove services from systemd
<pre>systemctl stop [servicename]
systemctl disable [servicename]
rm /etc/systemd/system/[servicename]
systemctl daemon-reload
systemctl reset-failed</pre>
</body>
</html>
