--- 
date: 2017-02-11 00:00:00
category: linux
tags: openssl, cert, key
---
# Linux OpenSSL commands

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
