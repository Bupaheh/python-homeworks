```
$ python3 nl.py nl.py
     0  import click
     1  import sys
     2  
     3  
     4  @click.command()
     5  @click.argument('file', required=False, type=click.File('r'), default=sys.stdin)
     6  def cli(file):
     7      for idx, line in enumerate(file):
     8          click.echo('{:6d}  {}'.format(idx, line.rstrip()))
     9  
    10  
    11  if __name__ == "__main__":
    12      cli()
```


```
$ cat nl.py | python3 nl.py
     0  import click
     1  import sys
     2  
     3  
     4  @click.command()
     5  @click.argument('file', required=False, type=click.File('r'), default=sys.stdin)
     6  def cli(file):
     7      for idx, line in enumerate(file):
     8          click.echo('{:6d}  {}'.format(idx, line.rstrip()))
     9  
    10  
    11  if __name__ == "__main__":
    12      cli()
```



