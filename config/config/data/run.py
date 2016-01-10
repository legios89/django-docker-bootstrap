import click

from runutils import runbash


@click.group()
def run():
    pass


@run.command()
@click.argument('user', default='developer')
def shell(user):
    runbash(user)


@run.command()
def start():
    pass


if __name__ == '__main__':
    run()
