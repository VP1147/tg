### IntegrEx
## A simple example involving integration using
## the functions of tg.py


import math as m
from getch import getch

import tg

x = 1024								# Window width
r = 7									# Window/Graph ratio(ratio = 10^r)
xs = x/(2**r)							# Graph width
g = 1									# Distance between grid lines

#tg.Mkrs = [0.5]


tg.theme("dark.json")					# Select color scheme

tg.init(x,xs,g) 						# Call the init function
										# with the given paramenters

## Derivates

										# Function: f(x) = x² + x
def f(x):
	return m.e**(x**2)

a = -1									# Assintotes to left
b = 1 									# Assintotes to right

tg.plot(f) 								# plot f(x)

tg.intplot(f, a, b)						# Integral of f(x) dx from
										# a to b

getch() 