
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SOCKS(5) Proxy Know How</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h2>SOCKS(5) Proxy Know How</h2>
    <div class="published">&#128198; published: 15.07.2020</div>
    <div class="modified">&#128198; modified: 23.07.2020</div>
    <div class="tags">&#128204; linux, socks5, putty, foxyproxy</div>
    <hr>

    <h3>SOCKS Proxy with Putty and FoxyProxy:</h3>
    <img src="../images/socks5-proxy-putty-config.png">
    <br>
    <br>
    Define your free proxy Port (2409)
    <br><br>
    <img src="../images/foxyproxy-config.png">
    <br>
    After enabling FoxyProxy you're able to connect your home by ssh and browse local services.
    <hr>
    SOCKS Proxy tunnel by shell:
    <pre>ssh -L 2409:localhost:2409 'user'@'host'
on cyon host:
ssh -D 2409 'user'@'host'</pre>
SOCKS Proxy tunnel over another hop:
<pre>
connection to 1. host:
ssh -L 2409:localhost:2409 user@1host.ch

connection on 1. to 2. host:
ssh -D 2409 user@2host.ch

Browser (e.g. firefox) / or FoxyProxy config from above
-> Settings -> Network Settings -> Manual proxy configuration 
SOCKS Host: localhost, Port: 2409
</pre>
</body>
</html>
