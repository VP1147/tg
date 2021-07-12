import math
import random
from getch import getch

import tg

x = 1024		# Window width
r = 5			# Window/Graph ratio(ratio = 10^r)
xs = x/(2**r)	# Graph width
g = 1			# Distance between grid lines

tg.theme("dark.json")
tg.Mkrs = [-8, -4, 0, 1, 2, 3, 4]


def Log(x): # f(x) = log x
	return math.log(x,10)

def Arit(x): # f(x) = 2x
	return 2*x

def Sin(x): # f(x) = sin(x)
	return math.sin(x)

def Exp(x): # f(x) = 2^x
	return 2**x

def Mod(x): # f(x) = |x|
	return math.sqrt(x**2)

def Quad(x): # f(x) = x²
	return x**2

def Rand(x): # Random generator
	return random.randint(0, 10)


tg.init(x,xs,g) # Call the init function
				# with the given paramenters

tg.plot(Exp)	# Plot a defined function

getch()