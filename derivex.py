### DerivEx: 20 - 12 - 23
## A simple example involving derivation using
## the functions of tg.py

import math
from getch import getch

import tg

x = 1024								# Window width
r = 5									# Window/Graph ratio(ratio = 10^r)
xs = x/(2**r)							# Graph width
g = 1									# Distance between grid lines

#tg.Mkrs = [0.5]


tg.theme("dark.json")					# Select color scheme

tg.init(x,xs,g) 						# Call the init function
										# with the given paramenters

## Derivates

										# Function: f(x) = x² + x
def f(x):
	return x**2 + x

start = -5								# Assintotes to left
stop = 5 								# Assintotes to right
step = 0.1

tg.plot(f) 								# plot f(x)

global a
def tangent(x):							# Draws the derivative function
										# of f(x): y = m(x-a) + f(a)
	m = tg.df(f, a)						# Derivative of f on point x
	return m*(x-a) + f(a)

for i in range(start, stop):
	a = i*step
	tg.plot(tangent, [1, 100, 100])		# Tip: 'i' Varies the colour 
												# for each tangent line

getch() 			 							# Wait for key event