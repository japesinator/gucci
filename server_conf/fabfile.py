from fabric.api import run, execute, put

def host_type():
    run('uname -s')

def update_apt():
    run('apt-get update')

def install_pip():
    run('apt-get -y install python-pip')

def install_tornado():
    run('apt-get install -y build-essential python-dev')
    run('wget https://github.com/downloads/liftoff/GateOne/python-tornado_2.4-1_all.deb')
    run('dpkg -i python-tornado*.deb')

def install_sshkeys(folder):
    run('mkdir -p {}'.format(folder))
    run('ssh-keygen -t rsa -N "" -f {}/id_rsa'.format(folder))
    run('ssh-keygen -y -f {}/id_rsa > {}/id_rsa.pub'.format(folder, folder))

def create_user(username):
    run('useradd {}'.format(username))

def change_password(user, password):
    run('echo \"{}:{}\" | chpasswd '.format(user, password))

def setup_jump_user():
    run('echo test')

def copy_sshkeys(key_to_copy):
    run('mkdir -p /opt/gateone/users/ANONYMOUS/.ssh/')
    run('touch /opt/gateone/users/ANONYMOUS/.ssh/.default_ids')
    run('cat {} > /opt/gateone/users/ANONYMOUS/.ssh/.default_ids'.format(key_to_copy))

def sshkey_to_authed(key_to_auth):
    run('touch /home/jump_user/.ssh/authorized_keys')
    run('chmod 600 /home/jump_user/.ssh/authorized_keys')
    run('cat {} > /home/jump_user/.ssh/authorized_keys'.format(key_to_auth))

def remove_motd():
    run('rm /etc/motd')
    run('touch /etc/motd')

def install_gate_one():
    run('wget https://github.com/downloads/liftoff/GateOne/gateone_1.1-1_all.deb')
    run('mkdir -p /opt/gateone/')
    put('*.conf', '/opt/gateone/server.conf')
    run('dpkg -i gateone*.deb')
    run('rm gateone*.deb')
    run('mkdir -p /opt/gateone/logs/')
    run('touch /opt/gateone/logs/webserver.log')

def start_gateone():
    run('service gateone start')

def stop_gateone():
    run('service gateone stop')

def deploy():
    execute(update_apt)
    execute(install_pip)
    execute(install_tornado)
    execute(install_gate_one)
    init_user = "jump_user"
    execute(create_user, init_user)
    execute(change_password, init_user, 'ZP9fFPLwEf4gUg6dg6jKYb7U')
    execute(install_sshkeys, '/home/jump_user/.ssh/')
