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

nint = 0.1 								# Interval between two lines
lnum = 10								# Assintotes to left
rnum = 10 								# Assintotes to right

tg.plot(f) 								# plot f(x)

for i in range(-lnum, rnum):
	tg.k = i*nint
	tg.plot(tg.tangent, [1, 100, 100])		# Tip: 'i' Varies the colour 
										# for each tangent line

getch() 			 					# Wait for key event