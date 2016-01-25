# coding: utf-8
# Core and 3th party packages
import signal
import time
import click
import psycopg2

# Utils Imports
from runutils import run_daemon, runbash, ensure_dir, getvar, run_cmd


UWSGI_CONF = '/config/uwsgi.conf'
PG_SEMAFOR = '/data/sock/pg_semafor'


def waitfordb(stopper):
    """
    Wait for the database to accept connections.
    """
    tick = 0.1
    intervals = 100 * [10]

    for i in intervals:
        click.echo('checking connection ...')
        try:
            psycopg2.connect(host='postgres',
                             port=5432,
                             database="django",
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


{% if cookiecutter.use_rosetta == 'True' -%}
def generate_makemessages_command():
    from django.conf import settings
    command = ['django-admin', 'makemessages']

    for lang in settings.LANGUAGES:
        if lang[0] != settings.LANGUAGE_CODE:
            command.append('-l=' + lang[0])
    return command
{%- endif %}

################################################
# INIT: WILL RUN BEFORE ANY COMMAND AND START  #
# Modify it according to container needs       #
# Init functions should be fast and idempotent #
################################################


def init(stopper):
    ensure_dir('/data/logs/django',
               owner='developer', group='developer', permsission_str='777')
    ensure_dir('/data/static',
               owner='developer', group='developer', permsission_str='777')
    {% if cookiecutter.use_rosetta == 'True' -%}
    ensure_dir('/src/locale',
               owner='developer', group='developer', permsission_str='777')
    {%- endif %}

    if not stopper.stopped:
        run_cmd(['django-admin', 'migrate'], user='developer')
        run_cmd(['django-admin', 'collectstatic', '--noinput'],
                user='developer')
        {% if cookiecutter.use_rosetta == 'True' -%}
        run_cmd(generate_makemessages_command(), user='developer')
        {%- endif %}

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
    run_daemon(start, signal_to_send=signal.SIGINT, user='developer',
               waitfunc=waitfordb, initfunc=init)


@run.command()
def start_uwsgi():
    """Starts the service."""
    ensure_dir('/data/sock', owner='developer', group='developer',
               permsission_str='777')
    start = ["uwsgi", "--ini", UWSGI_CONF]
    run_daemon(start, signal_to_send=signal.SIGQUIT, user='developer',
               waitfunc=waitfordb, initfunc=init)


if __name__ == '__main__':
    run()
