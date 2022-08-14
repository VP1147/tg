# --- TeenyGraph (tg) --- By Vinícius Pavão - VP1147 --- #
# --- Released on November 2019 --- #

import json
import graphics as gfx

# Global variables
global Mkrs
Mkrs = 0

def theme(file):
	global Color1 							# Background Color
	global Color2							# Axis Color
	global Color3							# Grid Color
	global Color4							# Function Color
	global Color5							# Markers Color

	theme_file = json.load(open(file))		# Load the selected theme
											# from a json file

											# Theme format:
											# {
											# "Color1": [r,g,b],
											# "Color2": [r,g,b],
											# "Color3": [r,g,b],
											# "Color4": [r,g,b],
											# "Color5": [r,g,b]
											# }
	Color1 = theme_file.get("Color1")
	Color2 = theme_file.get("Color2")
	Color3 = theme_file.get("Color3")
	Color4 = theme_file.get("Color4")
	Color5 = theme_file.get("Color5")

def plot(Fx):
	r,g,b = Color4[0], Color4[1], Color4[2] 					# Function colors
	Count = ((Sx/2)*-1)*Factor; mc = 0 							# Counter 

	for i in range (1,Sx):										# For every point
																# in the graph

		try:

			if Sx*-1 < (Sx/2)-Fx(Count)/Factor < Sx:			# Verify if the point
																# is inside the graph

				Actual = Fx(Count)/Factor						# Start point
				Next = Fx(Count+(1*Factor))/Factor				# End
																
				ActualCord = gfx.Point(i, ((Sy/2)-Actual))		# Start-End Cordinates 
				NextCord = gfx.Point((i+1), (((Sy+1)/2)-Next)) 	

				line = gfx.Line(ActualCord,NextCord); 				# Draw line from 
				line.setFill(gfx.color_rgb(r,g,b)); line.draw(Win)	# start to end

				if Mkrs != 0 and Count == Mkrs[mc]:				# Check for marker

					Text = int(Count)					# Just print a integer
														# pair on the graph

					print(ActualCord, "x: "+str(Count)+" y: "+str(Fx(Count)))	# Draw marker
					label = gfx.Text(ActualCord, "("+str(Text)+", "+str(Fx(Text))+")")
					label.setFill(gfx.color_rgb(Color5[0], Color5[1], Color5[2]))
					label.draw(Win)
					mc+=1

			else: pass

		except ValueError: 			pass				# Ignore all errors - 
		except OverflowError: 		pass				# This prevents useless errors
		except ZeroDivisionError: 	pass				# printed on term. Just ommit
		except IndexError:			pass				# them from the graph

		Count += Factor

def init(s,xs,g): 										# s - Window size # xs - x axis size
	global Win; global Sx; global Sy; global Factor; 	# Def global variables
	global x; global y; global G;
	x, y = s, int(s*(3/4))								# XY max value ( x: 0,s ; y: 0,s*(3/4) )
	Win = gfx.GraphWin("Teenygraph", x, y) 				# Show window
	Sx, Sy = x,y #(x-200,y-200)
	Factor = xs/x 										# Ratio between graphic and window size
	G = g
	Win.setBackground(gfx.color_rgb(Color1[0],Color1[1],Color1[2]))	
	grid(g*2)											# Draw grid
	axis(x,y)											# Draw axis

def axis(x,y):											# Function - Create a centered (x,y)
														# axis for the graph
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

def clear():											# Clear function
	for i in Win.items[:]:
		i.undraw()

	grid(G*2)											# Draw grid /w interval G*2
	axis(x,y)											# Draw axis (x,y)
	Win.update()										# Send data to screen

# Internal functions

def Id(x):				# Identity function -
						# Useful for visualizing 
						# inverse functions
	return x
