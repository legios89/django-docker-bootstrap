# coding: utf-8
# Core and 3th party packages
import click

# Utils Imports
from runutils import runbash, run_daemon, ensure_dir


NGINIX_CONF = '/config/nginx.conf'


@click.group()
def run():
    ensure_dir('/data/logs/nginx/', owner='nginx', group='nginx',
               permsission_str='777')


@run.command()
@click.argument('user', default='nginx')
def shell(user):
    runbash(user)


@run.command()
def start():
    params = ['nginx', '-c', NGINIX_CONF]
    run_daemon(params)


if __name__ == '__main__':
    run()
