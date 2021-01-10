# --- TeenyGraph (tg) --- By Vinícius Pavão - VP1147 --- #
# --- November 2019 --- #

import json
import graphics as gfx
from random import randint

# Setting colors
#Color1 = [255,255,255]
#Color2 = [40,40,40]

# Global variables
global Mkrs
Mkrs = 0

def theme(file):
	global Color1 	# Background Color
	global Color2	# Axis Color
	global Color3	# Grid Color
	theme_file = json.load(open(file))
	Color1 = theme_file.get("Color1")
	Color2 = theme_file.get("Color2")
	Color3 = theme_file.get("Color3")

def plot(Fx):
	r,g,b = randint(0,255),randint(0,255),randint(0,255)
	Count = ((Sx/2)*-1)*Factor; mc = 0
	for i in range (1,Sx):
		try:
			if Sx*-1 < (Sx/2)-Fx(Count)/Factor < Sx:
				Actual = Fx(Count)/Factor
				Next = Fx(Count+(1*Factor))/Factor
				ActualCord = gfx.Point(i, ((Sy/2)-Actual))		# Starting point
				NextCord = gfx.Point((i+1), (((Sy+1)/2)-Next)) 	# Ending point
				line = gfx.Line(ActualCord,NextCord); 
				line.setFill(gfx.color_rgb(r,g,b)); line.draw(Win)
				if Mkrs != 0 and Count == Mkrs[mc]:
					print(ActualCord, "x: "+str(Count)+" y: "+str(Fx(Count)))
					label = gfx.Text(ActualCord, "x: "+str(Count)+" y: "+str(Fx(Count)))
					label.setFill(gfx.color_rgb(r,g,b)); label.draw(Win)
					mc+=1
			else: pass
		except ValueError: 			pass
		except OverflowError: 		pass
		except ZeroDivisionError: 	pass
		except IndexError:			pass
		Count += Factor

def init(s,xs,g): 		# s - Window size # xs - x axis size
	global Win; global Sx; global Sy; global Factor; 	# Def global variables
	global x; global y
	x, y = s, int(s*(3/4))								# XY max value ( x: 0,s ; y: 0,s*(3/4) )
	Win = gfx.GraphWin("Teenygraph", x, y) 				# Show window
	Sx, Sy = x,y #(x-200,y-200)
	Factor = xs/x 										# Ratio between graphic and window size
	Win.setBackground(gfx.color_rgb(Color1[0],Color1[1],Color1[2]))	
	grid(g*2)											# Draw grid
	axis(x,y)											# Draw axis

def axis(x,y):	
	l1 = gfx.Line(gfx.Point(x/2,0),gfx.Point(x/2,x)); 
	l1.setFill(gfx.color_rgb(Color2[0],Color2[1],Color2[2])); l1.draw(Win)

	l2 = gfx.Line(gfx.Point(x,Sy/2),gfx.Point(1,y/2)); 
	l2.setFill(gfx.color_rgb(Color2[0],Color2[1],Color2[2])); l2.draw(Win)

def grid(m): # m - Def the distance between 2 lines
	e = 0
	for i in range(0, int((Sx)/(m/Factor))+1):
		l = gfx.Line(gfx.Point((e/Factor)+(Sx/2),0),gfx.Point((e/Factor)+(Sx/2),Sy))
		l.setFill(gfx.color_rgb(Color3[0],Color3[1],Color3[2])); l.draw(Win)

		l = gfx.Line(gfx.Point((Sx/2)-(e/Factor),0),gfx.Point(Sx/2-(e/Factor),Sy))
		l.setFill(gfx.color_rgb(Color3[0],Color3[1],Color3[2])); l.draw(Win)
		e+=m/2
	e = 0
	for i in range(0, int((Sy)/(m/Factor))+1):
		l = gfx.Line(gfx.Point(0,(e/Factor)+(Sy/2)),gfx.Point(Sx,(e/Factor)+(Sy/2)))
		l.setFill(gfx.color_rgb(Color3[0],Color3[1],Color3[2])); l.draw(Win)

		l = gfx.Line(gfx.Point(0,(Sy/2)-(e/Factor)),gfx.Point(Sx,(Sy/2)-(e/Factor)))
		l.setFill(gfx.color_rgb(Color3[0],Color3[1],Color3[2])); l.draw(Win)
		e+=m/2
		


def clear():
	for i in Win.items[:]:
		i.undraw()
	Win.update()