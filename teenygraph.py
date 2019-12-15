# --- TeenyGraph (PyGraph) --- By Vinícius Pavão - VP1147 ---
# --- November 2019

import pygame

clock = pygame.time.Clock()

def plot(Fx,rgb):
	Count = ((Sx/2)*-1)*Factor
	for i in range (1,Sx):
		try:
			if Sx*-10 < (Sx/2)-Fx(Count) < Sx*10:
				print(Fx(Count))
				Actual = [i, ((Sx/2)-Fx(Count))] # Line start
				Next = [(i+1), (((Sx+1)/2)-Fx(Count+(1*Factor)))] # Line end
				pygame.draw.aaline(screen,rgb,Actual,Next,10)
			else: pass
		except ValueError: pass
		except OverflowError: pass
		except ZeroDivisionError: pass
		Count += Factor
	pygame.display.flip()

def init(x,y,f,rgb):
	pygame.init()
	global screen; global Sx; global Sy; global Factor
	screen = pygame.display.set_mode([x,y])
	Sx = x
	Sy = y
	Factor = f
	pygame.draw.aaline(screen,rgb,(x/2,1),(x/2,x))
	pygame.draw.aaline(screen,rgb,(y,y/2),(1,y/2),1)
	pygame.display.flip()

