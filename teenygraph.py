# --- TeenyGraph (PyGraph) --- By Vinícius Pavão - VP1147 ---
# --- November 2019

import pygame

clock = pygame.time.Clock()

def DrawGraph(Fx,SX,SY,Zoom,rgb):
	Px = int((SX/2)*-1)
	for i in range (1,SX):
		try:
			if SX*-2 < ((SX/2)-Fx(Px,Zoom)) < SX*2:
				print(Fx(Px,Zoom))
				pygame.draw.line(screen, (rgb[0], rgb[1], rgb[2]),[i, (SX/2)-Fx(Px,Zoom)],[i, ((SX+1)/2)-Fx(Px+1,Zoom)],1)
			else: pass
		except ValueError: pass
		Px += 1
	pygame.display.flip()

def Start(SX,SY,rgb):
	pygame.init()
	global screen
	screen = pygame.display.set_mode([SX,SY])
	for i in range (1,SX): pygame.draw.rect(screen, (rgb[0], rgb[1], rgb[2]), [i, SX/2, 1, 1])
	for i in range (1,SY): pygame.draw.rect(screen, (rgb[0], rgb[1], rgb[2]), [SY/2, i, 1, 1])
	pygame.display.flip()

