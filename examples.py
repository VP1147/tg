import pygame, math
from getch import getch

import teenygraph as tg

clock = pygame.time.Clock()

x = 700 # Window heigh
y = 700 # Window width
f = 0.1 # Zoom factor

def Log(x):
	return math.sqrt(x)

def Arit(x):
	return (2*x)

def Sin(x):
	return math.sin(x)*20

def Exp(x):
	return (2**x)

tg.Start(x,y,(255,255,255))

#tg.DrawGraph(Log,x,y,f,(255,0,0))
#tg.DrawGraph(Arit,x,y,f,(0,255,0))
#tg.DrawGraph(Exp,x,y,f,(0,255,255))
tg.DrawGraph(Sin,x,y,f,(0,255,100))
getch()

