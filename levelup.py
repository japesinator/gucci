#!/usr/bin/python

from random import randint
import os
from pwd import getpwnam

password = raw_input("Enter the password:")

if password == "HASH1":
    user = str(randint(100000, 999999))
    os.system("adduser --disabled-password --gecos \"\" " + user)
    os.system("cp /resources/.bashrc1 /Users/" + user + "/.bashrc")
    uid = getpwnam(user).pw_uid
    os.setuid(uid)
    os.system("bash")
