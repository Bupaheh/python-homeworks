import click
import sys


def print_formatted(lines, words, characters, filename):
    click.echo('{:6d} {:6d} {:6d}  {}'.format(lines, words, characters, filename))


@click.command()
@click.argument('files', nargs=-1, type=click.File('r'))
def cli(files):
    if not files:
        files = (sys.stdin,)

    total_lines = 0
    total_words = 0
    total_characters = 0

    for file in files:
        lines = 0
        words = 0
        characters = 0

        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)

        total_lines += lines
        total_words += words
        total_characters += characters

        if file != sys.stdin:
            name = file.name
        else:
            name = ''

        print_formatted(lines, words, characters, name)

    if len(files) > 1:
        print_formatted(total_lines, total_words, total_characters, 'total')


if __name__ == "__main__":
    cli()
