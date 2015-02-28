import os
from sys import argv
import string
import random
import getpass

def random_user():
    return ''.join(random.choice(string.ascii_uppercase) for i in range(12))

def do_stuff(level, user2):
    print "We are doing stuff for level {}.".format(1)

def user_change(username):
    os.system('sudo -u {} /bin/bash'.format(username))

def create_user(username):
    os.system('useradd -m -s /bin/bash {}'.format(username))

def add_user_upgrade(user1, user2):
    os.system('echo "{}     ALL=({}) NOPASSWD: /bin/bash" > /etc/sudoers.d/{}'.format(user1, user2, user1+user2))
    os.system('echo "{} ALL=NOPASSWD: /usr/bin/python /retrogarde/user.py*" > /etc/sudoers.d/{}'.format(user2, user1+user2))

def upgrade_user():
   new_user = random_user()
   create_user(new_user)
   add_user_upgrade(getpass.getuser(), new_user)
   do_stuff(1, new_user)
   user_change(new_user)

if __name__ == "__main__":
   upgrade_user()
