import math
from getch import getch

import tg

x = 700
f = 1


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

tg.init(x,f)

tg.plot(Sin)	# Sinusoid
tg.plot(Log)	# Logarithmic
tg.plot(Arit)	# Arithmetic
tg.plot(Exp)	# Exponential
tg.plot(Mod)	# Modular

getch()