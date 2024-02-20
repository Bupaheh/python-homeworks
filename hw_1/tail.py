import click
import sys


@click.command()
@click.argument('files', nargs=-1, type=click.File('r'))
def cli(files):
    limit = 10

    if not files:
        files = (sys.stdin,)
        limit = 17

    for idx, file in enumerate(files):
        if len(files) > 1:
            if idx > 0:
                prefix = '\n'
            else:
                prefix = ''
            click.echo(f'{prefix}==> {file.name} <==')

        for line in file.readlines()[-limit:]:
            click.echo(line.rstrip())


if __name__ == "__main__":
    cli()
