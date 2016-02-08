# coding: utf-8
# Core and 3th party packages
import click

# Utils Imports
from runutils import runbash, run_cmd, getvar, sleep, ensure_dir


@click.group()
def run():
    ensure_dir('/data/static/react', owner='developer', group='developer')
    run_cmd(['npm', 'config', 'set', 'static_root', getvar('STATIC_ROOT')],
            user='developer')
    run_cmd(['npm', 'install'], message="npm install", user='developer')


@run.command()
@click.argument('user', default='developer')
def shell(user):
    runbash(user)


@run.command()
def start_watchify():
    run_cmd(['npm', 'run', 'watch'], message="npm run watch", user='developer')
    sleep()


@run.command()
def start_build():
    run_cmd(['npm', 'config', 'set', 'NODE_ENV', 'production'],
            user='developer')
    run_cmd(['npm', 'run', 'build'], message="npm run build", user='developer')
    sleep()


if __name__ == '__main__':
    run()
