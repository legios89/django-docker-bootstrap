import signal
import time
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
    ensure_dir('/data/sock', owner='django', group='django',
               permsission_str='777')
    start = ["uwsgi", "--ini", UWSGI_CONF]
    run_daemon(start, signal_to_send=signal.SIGQUIT, user='django',
               waitfunc=waitfordb, initfunc=init)


if __name__ == '__main__':
    run()
