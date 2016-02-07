# coding: utf-8
# Core and 3th party packages
import click

# Utils Imports
from runutils import runbash, run_daemon


@click.group()
def run():
    pass


@run.command()
@click.argument('user', default='developer')
def shell(user):
    runbash(user)


@run.command()
def start():
    run_daemon(['npm', 'run', 'build'], user='developer')


if __name__ == '__main__':
    run()
