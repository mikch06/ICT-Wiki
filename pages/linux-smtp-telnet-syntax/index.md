
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Template</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h2>Title</h2>
    <div class="published">&#128198; published: 15.09.2015</div>
    <div class="modified">&#128198; modified: </div>
    <div class="tags">&#128204; linux, telnet</div>
    <hr>

    Template Text

    <pre>telnet <MAILSERVER> 25

HELO <MAILSERVER>

mail from: test-mail@wiki.kissel.ch

rcpt to: receiver@<MAILSERVER>

data
from: test-mail@wiki.kissel.ch
to: receiver@<MAILSERVER>
subject: TestMessage

Hello World!

.

quit
</body>
</html>
