from fabric.api import run, execute

def host_type():
    run('uname -s')

def update_apt():
    run('apt-get update')

def install_pip():
    run('apt-get -y install python-pip')

def install_tornado():
    run('apt-get install -y build-essential python-dev')
    run('pip install tornado')

def deploy():
    execute(update_apt)
    execute(install_pip)
    execute(install_tornado)
