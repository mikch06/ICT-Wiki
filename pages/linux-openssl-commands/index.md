
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Linux OpenSSL commands</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h2>Linux OpenSSL commands</h2>
    <div class="published">&#128198; published: 11.02.2017</div>
    <div class="modified">&#128198; modified:</div>
    <div class="tags">&#128204; openssl, cert, key</div>
    <hr>
    Check a certificate

    <pre>openssl x509 -in server.crt -text -noout</pre>
    Check a key
    
    <pre>openssl rsa -in server.key -check</pre>
    Check a CSR
    <pre>openssl req -text -noout -verify -in server.csr</pre>
    Verify a certificate and key matches
    <pre>openssl x509 -noout -modulus -in server.crt| openssl md5<br>
openssl rsa -noout -modulus -in server.key| openssl md5</pre>
    Create a self signed cert & private key<br><br>
    - valid: 1y<br>
- key: 2048 bit
    
    <pre>openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout selfsigned.key -out selfsigned.crt</pre>
</body>
</html>
