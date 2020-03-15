# --- TeenyGraph (PyGraph) --- By Vinícius Pavão - VP1147 ---
# --- November 2019

import pygame
from random import randint

clock = pygame.time.Clock()

aa = True # Change to False if executed in low hardware. Default: True 

def plot(Fx):
	rgb = (randint(0,255),randint(0,255),(randint(0,255)))
	Count = ((Sx/2)*-1)*Factor
	for i in range (1,Sx):
		try:
			if Sx*-10 < (Sx/2)-Fx(Count) < Sx*10:
				print(Fx(Count))
				Actual = [i, ((Sx/2)-Fx(Count))] # Line start
				Next = [(i+1), (((Sx+1)/2)-Fx(Count+(1*Factor)))] # Line end
				if aa == True: pygame.draw.aaline(Sgraph,rgb,Actual,Next,10)
				else: pygame.draw.line(Sgraph,rgb,Actual,Next)
			else: pass
		except ValueError: pass
		except OverflowError: pass
		except ZeroDivisionError: pass
		Count += Factor
	pygame.display.flip()

def init(size,factor): # x -Window height # y -Window width # f -Size factor
	pygame.init()
	global Sgraph; global Sgrid; # Pygame layers
	global Sx; global Sy; global Factor; # Global variables
	pygame.display.set_caption('TeenyGraph')
	Sgraph = pygame.display.set_mode([size,size])
	Sgrid = pygame.display.set_mode([size,size])
	Sx,Sy = size,size
	Factor = factor
	grid()
	pygame.display.flip()

def grid():
	if aa == True:
		pygame.draw.aaline(Sgrid,(255,255,255),(Sx/2,1),(Sx/2,Sx),10)
		pygame.draw.aaline(Sgrid,(255,255,255),(Sy,Sy/2),(1,Sy/2),10)
	else:
		pygame.draw.line(Sgrid,(255,255,255),(Sx/2,1),(Sx/2,Sx))
		pygame.draw.line(Sgrid,(255,255,255),(Sy,Sy/2),(1,Sy/2))
	pygame.display.flip()

def clear():
	Sgraph.fill((0,0,0))
	grid()
	#pygame.display.flip()