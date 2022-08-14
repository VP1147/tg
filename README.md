![Arithmetic function](arit.png)

# Teenygraph
A teeny tiny code that plot Python functions.

![Multiple functions](multiple2.png)

## Pre-requisites
The required Python libraries are listed below:
	- Random
	- Json
	- Graphics.py
	- Getch
Those can be installed with PIP, for example:
```
python3 -m pip install graphics.py getch
```

## Initializing
Import _tg.py_. For this example, you will also need _math_.

```
vp1147@debian-ideapad:~/Documentos/GitHub/teenygraph$ python3
Python 3.7.3 (default, Dec 20 2019, 18:57:59) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tg
>>> import math
```

Call the **init** function
```
>>> tg.init(1024,10,1)
```
![Empty graph](empty_graph.png)
A graph will be created with the following values:  
**Size (Window):** 1024x768  
**Size (X axis):** 10 (-5 to 5)  

To plot a function, you have to create one first:  
```
>>> def Sin(x):
...     return math.sin(x)
...
>>>
```
So, the graph will read:  
**x:** x  
**y:** math.sin(x)  

Plotting this **wonderful** sine wave:
```
>>> tg.plot(Sin)
```
![Sinusoid function](sin.png)

More examples are avaliable on _examples.py_.
