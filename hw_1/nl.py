import click
import sys


@click.command()
@click.argument('file', required=False, type=click.File('r'), default=sys.stdin)
def cli(file):
    for idx, line in enumerate(file):
        click.echo('{:6d}  {}'.format(idx, line.rstrip()))


if __name__ == "__main__":
    cli()
