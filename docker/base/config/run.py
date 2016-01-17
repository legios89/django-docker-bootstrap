import click
import time
import signal
from runutils import runbash, ensure_dir


@click.group()
def run():
    ensure_dir('/data/logs/', owner='root', group='root',
               permsission_str='777')


@run.command()
@click.argument('user', default='developer')
def shell(user):
    runbash(user)


@run.command()
def start():
    class Stopper(object):
        def __init__(self):
            self.stopped = False

    stopper = Stopper()

    def stop_sleep(signum, frame):
        stopper.stopped = True

    signal.signal(signal.SIGTERM, stop_sleep)
    while not stopper.stopped:
        time.sleep(1)


if __name__ == '__main__':
    run()
