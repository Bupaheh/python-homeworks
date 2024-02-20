```
$ cat hw_1/tail.py | python3 hw_1/tail.py
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
```

```
$ python3 hw_1/tail.py hw_1/nl.py

@click.command()
@click.argument('file', required=False, type=click.File('r'), default=sys.stdin)
def cli(file):
    for idx, line in enumerate(file):
        click.echo('{:6d}  {}'.format(idx, line.rstrip()))


if __name__ == "__main__":
    cli()
```

```
$ python3 hw_1/tail.py hw_1/nl.py hw_1/tail.py
==> hw_1/nl.py <==

@click.command()
@click.argument('file', required=False, type=click.File('r'), default=sys.stdin)
def cli(file):
    for idx, line in enumerate(file):
        click.echo('{:6d}  {}'.format(idx, line.rstrip()))


if __name__ == "__main__":
    cli()

==> hw_1/tail.py <==
            else:
                prefix = ''
            click.echo(f'{prefix}==> {file.name} <==')

        for line in file.readlines()[-limit:]:
            click.echo(line.rstrip())


if __name__ == "__main__":
    cli()
```