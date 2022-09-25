#### Examples and tests involving calculus and its main properties

import math
from getch import getch

import tg

x = 1024								# Window width
r = 7									# Window/Graph ratio(ratio = 10^r)
xs = x/(2**r)							# Graph width
g = 1									# Distance between grid lines

tg.Mkrs = [0.5]


tg.theme("dark.json")					# Select color scheme

tg.init(x,xs,g) 						# Call the init function
										# with the given paramenters

## Derivates

										# Function: f(x) = 2x²
def f(x):
	return 2*x**2

def df(x): 								# df/dx
	h = 0.0001							# lim x->0 
	a = 0.5
	m = (f(a+h)-f(a))/h
	return m*(x-a) + f(a)	    		# y = m(x-a) + f(a)

tg.plot(f)
tg.plot(df, [-100, 100, 0])


getch() 			 					# Wait for key event