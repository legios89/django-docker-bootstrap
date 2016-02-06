# coding: utf-8
# Core and 3th party packages
import os
import re
import sys
import subprocess
import time
import signal
from contextlib import contextmanager
import click

# Utils Imports
from runutils import (
    run_daemon, getvar, runbash, id, run_cmd, setuser, ensure_dir)


PGDATA = getvar('PGDATA')
CONFIG_FILE = '/config/postgresql.conf'
SOCKET_DIR = '/data/sock'
BACKUP_DIR = '/data/backup'
SEMAFOR = '/data/sock/pg_semafor'
start_postgres = ['postgres', '-c', 'config_file=%s' % CONFIG_FILE]


#############
# Functions #
#############

def psqlparams(command=None, database='django'):
    """Returns a list of command line arguments to run psql."""
    if command is None:
        return ['psql', '-d', database, '-h', SOCKET_DIR]
    return ['psql', '-d', database, '-h', SOCKET_DIR, '-c', command]


@contextmanager
def running_db():
    """
    Starts and stops postgres (if it is not running) so the block
    inside the with statement can execute command against it.
    """

    subproc = None
    if not os.path.isfile(os.path.join(PGDATA, 'postmaster.pid')):
        setpostgresuser = setuser('postgres')
        subproc = subprocess.Popen(
            start_postgres,
            preexec_fn=setpostgresuser,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        click.echo('Waiting for database to start...')
        time.sleep(1)

    try:
        yield
    finally:
        if subproc:
            subproc.send_signal(signal.SIGTERM)
            click.echo('Waiting for database to stop...')
            subproc.wait()


def _initdb():
    """Initialize the database."""
    run_cmd(['initdb'], user='postgres', message='Initializing the database')
    _createdb('django', 'postgres')


def _setpwd(username, password):
    """Sets the password for the given user."""
    sql = "ALTER USER %s WITH PASSWORD '%s'" % (username, password)
    with running_db():
        run_cmd(psqlparams(sql), 'Setting password', user='postgres')


def _createdb(dbname, owner):
    """Creates a database."""
    sql = "CREATE DATABASE %s WITH ENCODING 'UTF8' OWNER %s" % (dbname, owner)
    with running_db():
        run_cmd(psqlparams(sql, database='postgres'), 'Creating database',
                user='postgres')


def _backup(backupname):
    """Backs up the database with pg_dump."""
    # We have some restrictions on the backupname
    if re.match('[a-z0-9_-]+$', backupname) is None:
        click.secho('Invalid backupname.', fg='red')
        sys.exit(1)

    # The file must not exist
    filename = os.path.join(BACKUP_DIR, backupname)
    if os.path.isfile(filename):
        click.secho('File %s exists.' % filename, fg='red')
        sys.exit(1)

    params = ['pg_dump', '-h', SOCKET_DIR, '-O', '-x', '-U', 'postgres',
              'django']
    with open(filename, 'w') as f, running_db():
        ret = subprocess.call(params, stdout=f, preexec_fn=setuser('postgres'))

    uid, gid, _ = id('postgres')
    os.chown(filename, uid, gid)

    if ret == 0:
        click.secho('Successful backup: %s' % filename, fg='green')
    else:
        try:
            os.remove(filename)
        except:
            pass
        click.secho('Backup (%s) failed' % filename, fg='red')
        sys.exit(1)


def _restore(backupname):
    filename = os.path.join(BACKUP_DIR, backupname)
    if not os.path.isfile(filename):
        click.secho('File %s does not exist.' % filename, fg='red')
        sys.exit(1)

    with running_db():
        run_cmd(['psql', '-h', SOCKET_DIR, '-c', 'DROP DATABASE django'],
                message='Dropping database django', user='postgres')

        _createdb('django', 'postgres')
        run_cmd(psqlparams() + ['-f', filename],  message='Restoring',
                user='postgres')


################################################
# INIT: WILL RUN BEFORE ANY COMMAND AND START  #
################################################
def init(stopper=None):
    ensure_dir(os.path.split(PGDATA)[0], owner='postgres', group='postgres')
    ensure_dir(SOCKET_DIR, owner='postgres', group='postgres')
    ensure_dir(BACKUP_DIR, owner='postgres', group='postgres')
    ensure_dir('/data/logs/postgres', owner='postgres', group='postgres')

    if not os.path.isdir(PGDATA):
        _initdb()
        _setpwd('postgres', getvar('DB_PASSWORD'))


#############
# COMMANDS  #
#############
@click.group()
def run():
    pass


@run.command()
@click.argument('user', default='postgres')
def shell(user):
    init()
    runbash(user)


@run.command()
@click.option('--backupname', prompt=True)
def restore(backupname):
    _restore(backupname)


@run.command()
@click.option('--backupname', prompt=True)
def backup(backupname):
    _backup(backupname)


@run.command()
def start():
    run_daemon(start_postgres, user='postgres', semafor=SEMAFOR, initfunc=init)


if __name__ == '__main__':
    run()
