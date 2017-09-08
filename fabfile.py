from fabric.api import *
from datetime import datetime


env.user="root"
env.hosts=['47.94.137.148']
env.password="Xxx5211314"
env.port=22


def hello():
    remote_tmp_tar="/opt"
    run('rm -f %s' % remote_tmp_tar)


def local_test():
    local("ls -la")
