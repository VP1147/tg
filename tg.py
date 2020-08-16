# --- TeenyGraph (tg) --- By Vinícius Pavão - VP1147 --- #
# --- November 2019 --- #

import graphics as gfx
from random import randint

def plot(Fx):
	r,g,b = randint(0,255),randint(0,255),randint(0,255)
	Count = ((Sx/2)*-1)*Factor
	for i in range (1,Sx):
		try:
			if Sx*-1 < (Sx/2)-Fx(Count)/Factor < Sx:
				Actual = Fx(Count)/Factor
				Next = Fx(Count+(1*Factor))/Factor
				ActualCord = gfx.Point(i, ((Sy/2)-Actual))		# Starting point
				NextCord = gfx.Point((i+1), (((Sy+1)/2)-Next)) 	# Ending point
				line = gfx.Line(ActualCord,NextCord); 
				line.setFill(gfx.color_rgb(r,g,b)); line.draw(Win)
			else: pass
		except ValueError: pass
		except OverflowError: pass
		except ZeroDivisionError: pass
		Count += Factor

def init(s,f,g): 		# s - Window size # f - x/y factor
	global Win; global Sx; global Sy; global Factor; 	# Def global variables
	Sx, Sy = s, int(s*(3/4))							# XY axis
	Win = gfx.GraphWin("Teenygraph", Sx, Sy) 			# Starting 4/3 window
	Factor = f											
	grid(g)												# Draw grid
	axis()												# Draw axis

def axis():	
	l1 = gfx.Line(gfx.Point(Sx/2,0),gfx.Point(Sx/2,Sx)); l1.setFill('white'); l1.draw(Win)
	l2 = gfx.Line(gfx.Point(Sx,Sy/2),gfx.Point(1,Sy/2)); l2.setFill('white'); l2.draw(Win)

def grid(m): # m - Def the distance between 2 lines
	e = 0
	for i in range(0, int((Sx/2)/(m/Factor))+1):
		l = gfx.Line(gfx.Point((e/Factor)+(Sx/2),0),gfx.Point((e/Factor)+(Sx/2),Sy))
		l.setFill(gfx.color_rgb(40,40,40)); l.draw(Win)
		l = gfx.Line(gfx.Point((Sx/2)-(e/Factor),0),gfx.Point(Sx/2-(e/Factor),Sy))
		l.setFill(gfx.color_rgb(40,40,40)); l.draw(Win)
		e+=m
	e = 0
	for i in range(0, int((Sy/2)/(m/Factor))+1):
		l = gfx.Line(gfx.Point(0,(e/Factor)+(Sy/2)),gfx.Point(Sx,(e/Factor)+(Sy/2)))
		l.setFill(gfx.color_rgb(40,40,40)); l.draw(Win)
		l = gfx.Line(gfx.Point(0,(Sy/2)-(e/Factor)),gfx.Point(Sx,(Sy/2)-(e/Factor)))
		l.setFill(gfx.color_rgb(40,40,40)); l.draw(Win)
		e+=m
		


def clear():
    for i in Win.items[:]:
        i.undraw()
    Win.update()