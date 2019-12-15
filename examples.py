import pygame, math
from getch import getch

import teenygraph as tg

clock = pygame.time.Clock()

x = 700 # Window heigh
y = 700 # Window width
f = 0.1 # Zoom factor

def Log(x):
	return math.log(x,10)

def Arit(x):
	return (2*x)

def Sin(x):
	return math.sin(x)*20

def Exp(x):
	return (2**x)

def Mod(x):
	return math.sqrt(x**2)


tg.init(x,y,f,(255,255,255))

tg.plot(Log,(255,0,0))
tg.plot(Arit,(0,255,0))
tg.plot(Exp,(0,255,255))
tg.plot(Sin,(0,255,100))
tg.plot(Mod,(255,255,0))
getch()

