import click
import signal
import shutil
import os

from runutils import runbash, run_daemon, id


SSHD_CONFIG = '/config/sshd_config'
SSH_CONFIG = '/config/ssh_config'
SSH_HOST = 'myhost.com'
SECRET_FILES_ROOT = '/host_ssh'


def init(stopper):
    for f in os.listdir(SECRET_FILES_ROOT):
        fn = os.path.join(SECRET_FILES_ROOT, f)
        shutil.copy(fn, '/.ssh')
        fn = os.path.join('/.ssh', f)
        uid, gid, _ = id('ssh')
        os.chown(fn, uid, gid)


@click.group()
def run():
    pass


@run.command()
@click.argument('user', default='ssh')
def shell(user):
    runbash(user)


@run.command()
def start_server():
    start = ['/usr/sbin/sshd', '-D', '-f', SSHD_CONFIG, '-e']
    run_daemon(start, signal_to_send=signal.SIGTERM, initfunc=init)


@run.command()
def start_client():
    start = ['ssh', '-N', '-F', SSH_CONFIG, SSH_HOST]
    run_daemon(start, signal_to_send=signal.SIGTERM, initfunc=init)


if __name__ == '__main__':
    run()
