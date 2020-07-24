![Screenshot](screenshot.png)

# Teenygraph
A teeny tiny code that plot Python functions.

## How to use
Import _tg.py_.

```
vp1147@debian-ideapad:~/Documentos/GitHub/teenygraph$ python3
Python 3.7.3 (default, Dec 20 2019, 18:57:59) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tg
>>> 
```

Call the *init* function
```
>>> tg.init(640,0.1)
```
A 4:3 window will be created. To plot a function, let's define one first:
```
>>> def Sin(x):
...     return math.sin(x)
...
>>>
```
_Note: The function have to receive a integer (x) and return a float._
To plot this *wonderful* senoid function function:
```
>>> tg.plot(Sin)
```

## Examples
Some examples are avaliable in the _ex.py_ file.
```
$ python3 ex.py
```
