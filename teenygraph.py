# --- TeenyGraph (PyGraph) --- By Vinícius Pavão - VP1147 ---
# --- November 2019

import pygame

clock = pygame.time.Clock()

def DrawGraph(Fx,SX,SY,Factor,rgb):
	Count = ((SX/2)*-1)*Factor
	for i in range (1,SX):
		try:
			if SX*-10 < (SX/2)-Fx(Count) < SX*10:
				print(Fx(Count))
				Actual = [i, ((SX/2)-Fx(Count))] # Line start
				Next = [i+1, (((SX+1)/2)-Fx(Count+(1*Factor)))] # Line end
				pygame.draw.aaline(screen,rgb,Actual,Next,10)
			else: pass
		except ValueError: pass
		except OverflowError: pass
		Count += Factor
	pygame.display.flip()

def Start(SX,SY,rgb):
	pygame.init()
	global screen
	screen = pygame.display.set_mode([SX,SY])
	pygame.draw.aaline(screen,rgb,(SX/2,1),(SX/2,SX))
	pygame.draw.aaline(screen,rgb,(SY,SY/2),(1,SY/2),1)
	pygame.display.flip()

