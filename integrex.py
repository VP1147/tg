### IntegrEx
## A simple example involving integration using
## the functions of tg.py

import math as m
from getch import getch

import tg

x = 1024								# Window width
r = 7									# Window/Graph ratio (ratio = 2^r)
xs = x/(2**r)							# Graph width
g = 1									# Distance between grid lines (units)

tg.theme("dark.json")					# Select color scheme

tg.init(x,xs,g) 						# Call the init function
										# with the given paramenters

										# Function: f(x) = sin(x²)
def f(x):
	return m.sin(x**2)

a = -1									# Integrate f(x) dx from a to b
b = 1

tg.Mkrs = [a, b]						# Setting a and b as optional markers
tg.plot(f) 								# Plotting the function f(x)

tg.intplot(f, a, b)						# Plotting the integral of f(x) dx from
										# a to b. Also displays the numeric result
										# of the integration.

getch() 								# Wait for keystroke