![Arithmetic function](arit.png)

# Teenygraph
A teeny tiny code that plot Python functions.

![Multiple functions](multiple2.png)
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
>>> tg.init(1024,0.01,2)
```
A window will be created. To plot a function, let's define one first:
```
>>> def Sin(x):
...     return math.sin(x)
...
>>>
```
_Note: The function have to receive [x] and return [sin(x)] a float._
To plot this *wonderful* sine wave function function:
```
>>> tg.plot(Sin)
```
![Sinusoid function](sin.png)
## Examples
Some examples are avaliable in the _ex.py_ file.
```
$ python3 ex.py
```
