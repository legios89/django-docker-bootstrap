# coding: utf-8
# Core and 3th party packages
import click

# Utils Imports
from runutils import runbash, run_cmd, getvar, ensure_dir, run_daemon


@click.group()
def run():
    ensure_dir('/data/static/react', owner='developer', group='developer')
    run_cmd(['npm', 'config', 'set', 'static_root', getvar('STATIC_ROOT')],
            user='developer')
    run_daemon(['npm', 'install'], user='developer', exit_on_finish=False)


@run.command()
@click.argument('user', default='developer')
def shell(user):
    runbash(user)


@run.command()
def start_watchify():
    run_daemon(['npm', 'run', 'watch'], user='developer')


@run.command()
def start_build():
    run_cmd(['npm', 'config', 'set', 'NODE_ENV', 'production'],
            user='developer')
    run_cmd(['npm', 'run', 'build'], message="npm run build", user='developer')


if __name__ == '__main__':
    run()
