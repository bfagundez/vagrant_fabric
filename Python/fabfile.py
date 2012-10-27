####
#### This fabric script must be used with ubuntu machines (or anything that can run apt-get)
#### Creates an environment with Python 2.7.3, Setuptools, Mysql, subversion and git
#### [Optional] uncommenting install_requirements() in provision_box() will look for the requirements.txt freezed by pip.
####

from fabric.api import *
import pdb

# Sometimes localhost can't be resolved, using ip instead.
env.hosts = ['127.0.0.1']
env.user = 'vagrant'
env.password = 'vagrant'
env.port = 2222

def debug_shell():
    pdb.set_trace()
    
def provision_box():
    
    install_base()
    install_python()
    install_setuptools()
    install_pip()
    #install_requirements()
    
def install_base():
    apt_get('make gcc git-core subversion python-mysqldb mysql-server-core-5.1 mysql-client-core-5.1 libmysqlclient-dev')

def install_python():
    sudo('wget http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz')
    sudo('tar xfzv Python-2.7.3.tgz')
    with cd('Python-2.7.3'):
        sudo('./configure')
        sudo('make')
        sudo('make install')

def install_setuptools():
    run('rm -rf setuptools')
    run('mkdir setuptools')
    with cd('setuptools'):
        sudo('wget http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea')
        sudo('sh setuptools-0.6c11-py2.7.egg')

def install_requirements():
    put('requirements.txt','.')
    sudo('pip install -r requirements.txt')

def install_pip():
    sudo('easy_install pip')
    
def apt_get(*packages):
    sudo('apt-get -y --no-upgrade install %s' % ' '.join(packages), shell=False)
