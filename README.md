# SMTP-VRFY_Users
Quick and dirty.
Use SMTP 'VRFY user' command to verify whether the users are valid.
The input list is a newline separated list of names.

# Usage
```shell
python3 smtp_vrfy.py 10.11.1.227 25 users
<<--: b'220 jd.acme.local Microsoft ESMTP MAIL Service, Version: 5.0.2195.5329 ready at  Mon, 8 Nov 2021 11:04:53 +0200 \r\n'
-->>: b'VRFY users\r\n'
<<--: b'252 2.1.5 Cannot VRFY user, but will take message for <users@jd.acme.local>\r\n'
-->>: b'VRFY users\r\n'
<<--: b'252 2.1.5 Cannot VRFY user, but will take message for <users@jd.acme.local>\r\n'
-->>: b'VRFY users\r\n'
<<--: b'252 2.1.5 Cannot VRFY user, but will take message for <users@jd.acme.local>\r\n'
-->>: b'VRFY users\r\n'
<<--: b'252 2.1.5 Cannot VRFY user, but will take message for <users@jd.acme.local>\r\n'
-->>: b'VRFY users\r\n'
<<--: b'252 2.1.5 Cannot VRFY user, but will take message for <users@jd.acme.local>\r\n'
```

```shell
$ cat users
root
user
test
admin
```
