#### Examples and tests involving calculus and its main properties

import math
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

										# Function: f(x) = 2x²
def f(x):
	return x**2 -2*x

global k
def df(x): 								# df/dx
	h = 0.0001							# lim x->0 
	a = k
	return (f(a+h)-f(a))/h
	

def tangent(x):							# # y = m(x-a) + f(a)
	m = df(x)
	a = k
	return m*(x-a) + f(a)

nint = 0.5 								# Interval between two lines
num = 10								# Number of lines (minus h-assintotes)
tg.plot(f)
for i in range(-int(num/2)-1, int(num/2)):
	k = i*nint
	tg.plot(tangent, [1, 100, 100])		# Tip: Varies the colour for each tangent line
	#tg.clear()


getch() 			 					# Wait for key event