## Examples on plotting simple and defined functions

import math
import random
from getch import getch

import tg

x = 1024								# Window width
r = 5									# Window/Graph ratio(ratio = 10^r)
xs = x/(2**r)							# Graph width
g = 1									# Distance between grid lines

 tg.theme("dark.json")					# Select color scheme
# tg.theme("paper.json")

tg.Mkrs = [0]							# Choose markers (testing):
										# Markers are defined by 
										# points on the x axis


# Example functions

def Log(x): 				# f(x) = log2(x)
	return math.log(x,2)

def Arit(x): 				# f(x) = 2x
	return 2*x

def Sin(x): 				# f(x) = sin(x)
	return math.sin(x)

def Exp(x): 				# f(x) = 2^x
	return 2**x

def Mod(x): 				# f(x) = |x|
	return math.sqrt(x**2)

def Rad(x):
	return math.sqrt(x)

def Quad(x): 				# f(x) = x²
	return x**2

def Rand(x): 				# Random generator
	return random.randint(0, 10)


tg.init(x,xs,g) 			# Call the init function
							# with the given paramenters

tg.plot(tg.Id)				# Plot internal Identity function

tg.plot(Exp)				# Inverse functions
tg.plot(Log)

getch()						# Wait for keyboard event