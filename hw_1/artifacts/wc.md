```
$ wc nl.py tail.py wc.py
  13   24  275 nl.py
  27   55  545 tail.py
  45  100  970 wc.py
  85  179 1790 total
``` 

```
$ python3 wc.py nl.py
    13     24    275  nl.py
```

```
$ python3 wc.py nl.py tail.py wc.py
    13     24    275  nl.py
    27     55    545  tail.py
    45    100    970  wc.py
    85    179   1790  total
```

```
$ cat tail.py | python3 wc.py
    27     55    545 
```