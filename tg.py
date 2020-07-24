# --- TeenyGraph (PyGraph) --- By Vinícius Pavão - VP1147 ---
# --- November 2019

import graphics as gfx
from random import randint

def plot(Fx):
	r,g,b = randint(0,255),randint(0,255),randint(0,255)
	Count = ((Sx/2)*-1)*Factor
	for i in range (1,Sx):
		try:
			if Sx*-1 < (Sx/2)-Fx(Count) < Sx:
				Actual = Fx(Count)
				Next = Fx(Count+(1*Factor))
				ActualCord = gfx.Point(i, ((Sy/2)-Actual))		# Starting point
				NextCord = gfx.Point((i+1), (((Sy+1)/2)-Next)) 	# Ending point
				line = gfx.Line(ActualCord,NextCord); 
				line.setFill(gfx.color_rgb(r,g,b)); line.draw(Win)
			else: pass
		except ValueError: pass
		except OverflowError: pass
		except ZeroDivisionError: pass
		Count += Factor

def init(s,f): 		# s - Window size # f - x/y factor
	global Win; global Sx; global Sy; global Factor; 	# Def global variables
	Sx, Sy = s, int(s*(3/4))							# XY axis
	Win = gfx.GraphWin("Teenygraph", Sx, Sy) 			# Starting 4/3 window
	Factor = f
	grid()											# Draw graph grid

def grid():	# m - Def the distance between 2 markers
	l1 = gfx.Line(gfx.Point(Sx/2,0),gfx.Point(Sx/2,Sx)); l1.setFill('white'); l1.draw(Win)
	l2 = gfx.Line(gfx.Point(Sx,Sy/2),gfx.Point(1,Sy/2)); l2.setFill('white'); l2.draw(Win)

# def clear():
# 	Sgraph.fill((0,0,0))
# 	#pygame.display.flip()
