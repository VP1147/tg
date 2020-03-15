# teenygraph
A teeny tiny program that plot function graphs using _PyGame_.

## How to use
First, you'll need to import _teenygraph.py_ file.

```
Python 3.7.5 (default, Oct 27 2019, 15:43:29) 
[GCC 9.2.1 20191022] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tg
pygame 1.9.4.post1
Hello from the pygame community. https://www.pygame.org/contribute.html
```

Now, call the *init* function
```
>>> tg.init(700,0.1)
```
A 700x700 PyGame window will be created, with a blank graph. To plot a function, let's define one first:
```
>>> def Mod(x):
...     return math.sqrt((x**2+5*x-30)**2)
...
>>>
```
_Note: The function have to receive a integer (x) and return a float._
Here, we have a modular function, _f(x) = |x²+5x-30|_. To plot that function:
```
>>> tg.plot(Mod)
```

## Examples
Some examples are avaliable in the _examples.py_ file.
```
$ python3 examples.py
```