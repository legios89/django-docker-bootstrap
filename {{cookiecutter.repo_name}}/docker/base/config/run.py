# coding: utf-8
# Core and 3th party packages
import click

# Utils Imports
from runutils import runbash, ensure_dir, sleep


@click.group()
def run():
    ensure_dir('/data/logs/', owner='developer', group='developer')


@run.command()
@click.argument('user', default='developer')
def shell(user):
    runbash(user)


@run.command()
def start():
    sleep()


if __name__ == '__main__':
    run()
