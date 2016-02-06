# coding: utf-8
# Core and 3th party packages
import click

# Utils Imports
from runutils import runbash, run_daemon, ensure_dir


@click.group()
def run():
    ensure_dir('/data/logs/nginx/', owner='developer', group='developer')


@run.command()
@click.argument('user', default='developer')
def shell(user):
    runbash(user)


@run.command()
def start():
    run_daemon(['nginx', '-c', '/config/nginx.conf'])


if __name__ == '__main__':
    run()
