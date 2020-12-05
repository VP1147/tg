import math
from getch import getch

import tg

x = 1024	# Window width
xs = 10
g = 1		# Distance between grid lines


def Log(x):
	return math.log(x,10)

def Arit(x):
	return 2*x

def Sin(x):
	return math.sin(x)

def Exp(x):
	return 2**x

def Mod(x):
	return math.sqrt(x**2)

def Quad(x):
	return x**2

tg.init(x,xs,g)

#tg.plot(Quad)	# Quadratic
tg.plot(Sin)	# Sinusoid
#tg.plot(Log)	# Logarithmic
#tg.plot(Arit)	# Arithmetic
#tg.plot(Exp)	# Exponential
#tg.plot(Mod)	# Modular

getch()