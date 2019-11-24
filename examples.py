import pygame, math
from getch import getch

import teenygraph as tg

clock = pygame.time.Clock()

x = 700 # Window heigh
y = 700 # Window width
Zoom = 1 # Graphic zoom STILL IN DEV

def Log(x,Zoom):
	return math.sqrt(x)

def Arit(x,Zoom):
	return (2*x)/Zoom

def Sin(x,Zoom):
	return math.sin(x)

def Exp(x,Zoom):
	return (2**x)

tg.Start(x,y,(255,255,255))

tg.DrawGraph(Log,x,y,Zoom,(255,0,0))
tg.DrawGraph(Arit,x,y,Zoom,(0,255,0))
tg.DrawGraph(Exp,x,y,Zoom,(0,0,255))
tg.DrawGraph(Sin,x,y,Zoom,(0,255,255))
getch()

