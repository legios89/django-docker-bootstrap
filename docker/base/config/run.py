import click

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
    pass


if __name__ == '__main__':
    run()
