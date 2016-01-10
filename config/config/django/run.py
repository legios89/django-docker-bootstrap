import signal
import time
import os

import click
import psycopg2

from runutils import run_daemon, runbash, ensure_dir, getvar, run_cmd


UWSGI_CONF = '/config/uwsgi.conf'
PG_SEMAFOR = '/data/sock/pg_semafor'


def waitfordb(stopper):
    """
    Wait for the database to accept connections.
    """
    tick = 0.1
    intervals = 10 * [5] + 100 * [10]

    for i in intervals:
        click.echo('checking semafor ...')
        if os.path.isfile(PG_SEMAFOR):
            click.echo('checking connection ...')
            try:
                psycopg2.connect(host='postgres',
                                 port=5432,
                                 database="postgres",
                                 user="postgres",
                                 password=getvar('DB_PASSWORD'))
            except:
                click.echo('could not connect yet')
            else:
                return
        else:
            click.echo('no semafor yet')

        for w in range(i):
            if stopper.stopped:
                return
            time.sleep(tick)


################################################
# INIT: WILL RUN BEFORE ANY COMMAND AND START  #
# Modify it according to container needs       #
# Init functions should be fast and idempotent #
################################################


def init(stopper):
    ensure_dir('/data/static',
               owner='django', group='django', permsission_str='777')

    if not stopper.stopped:
        run_cmd(['django-admin', 'migrate'], user='django')
        run_cmd(['django-admin', 'collectstatic', '--noinput'], user='django')

    # This is mainly for demonstartive purposes, but can be handy in
    # development
    if stopper.stopped:
        return

    import django
    django.setup()
    from django.contrib.auth.models import User

    try:
        User._default_manager.create_superuser(
            'admin', 'admin@mycompany.com', 'admin')
    except:
        click.echo('Superuser exists')


######################################################################
# COMMANDS                                                           #
# Add your own if needed, remove or comment out what is unnecessary. #
######################################################################

@click.group()
def run():
    pass


@run.command()
@click.argument('user', default='developer')
def shell(user):
    runbash(user)


@run.command()
def start_runserver():
    start = ['django-admin.py', 'runserver', '0.0.0.0:8000']
    run_daemon(start, signal_to_send=signal.SIGINT, user='django',
               waitfunc=waitfordb, initfunc=init)


@run.command()
def start_uwsgi():
    """Starts the service."""
    start = ["uwsgi", "--ini", UWSGI_CONF]
    run_daemon(start, signal_to_send=signal.SIGQUIT, user='django',
               waitfunc=waitfordb, initfunc=init)


if __name__ == '__main__':
    run()
