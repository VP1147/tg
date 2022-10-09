# --- TeenyGraph (tg) --- By Vinícius Pavão - VP1147 --- #
# --- 	Released on November 2019 	--- #
# --- 		v2.0 	August 2022	  	--- #

import json
import graphics as gfx

# Global variables
global Mkrs
Mkrs = 0

def theme(file):							# Match global colors
											# to theme file


	global Color1 							# Background Color
	global Color2							# Axis Color
	global Color3							# Grid Color
	global Color4							# Function Color
	global Color5							# Markers Color

	theme_file = json.load(open(file))		# Load the selected theme file

											# 	{
											# 		"Color1": [r,g,b],
											# 		"Color2": [r,g,b],
											# 		"Color3": [r,g,b],
											# 		"Color4": [r,g,b],
											# 		"Color5": [r,g,b]
											# 	}
	Color1 = theme_file.get("Color1")
	Color2 = theme_file.get("Color2")
	Color3 = theme_file.get("Color3")
	Color4 = theme_file.get("Color4")
	Color5 = theme_file.get("Color5")

def plot(Fx, *args):								# Plot a function Fx(x) on the graph
													# *args - (r_off, g_off, b_off)

	off = [0,0,0]									# Default offsets

	if args: off = args[0]							# Detects if any offsets
	(r,g,b) = (	int(Color4[0]+off[0]), 				# are declared, them sum
				int(Color4[1]+off[1]), 
				int(Color4[2]+off[2]))

	Count = ((Sx/2)*-1)*Factor; mc = 0 							# Counter (-X/2 -> X/2);
																# Marker count

	for i in range (1,Sx):										# Loop for every point
																# in the graph

		try:													# Check if a point is valid

			if Sx*-1 < (Sx/2)-Fx(Count)/Factor < Sx:				# Verify if the point
																	# is inside the graph

				Actual = Fx(Count)/Factor							# Start point
				Next = Fx(Count+(1*Factor))/Factor					# End Point
																
				ActualCord = gfx.Point(i, ((Sy/2)-Actual))			# Start-End Cordinates 
				NextCord = gfx.Point((i+1), (((Sy+1)/2)-Next)) 	

				line = gfx.Line(ActualCord,NextCord); 				# Draw line from 
				line.setFill(gfx.color_rgb(r,g,b)); line.draw(Win)	# start to end

				if Mkrs != 0 and Count <= Mkrs[mc] < Count+Factor:
					LabelCord = gfx.Point(i+60, ((Sy/2)-Actual)-15)	# Offsets for better viewing

					label = gfx.Text(LabelCord, "x: "+str(round(Count, 2))+" y: "+str(round(Fx(Count), 2)))
					label.setFill(gfx.color_rgb(r,g,b)); label.draw(Win)

					circle = gfx.Circle(ActualCord, 4)
					circle.setFill(gfx.color_rgb(r,g,b)); circle.draw(Win)
					
					mc+=1

				elif Mkrs != 0 and Mkrs[mc] < Count: mc +=1
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

# Calculus functions and utils

global k

def df(f, x): 							# Receives f(x) and x | returns df/dx
	h = 0.1								# lim x->0
	return (f(x+h)-f(x))/h 				# Derivative by definition

def tangent(x):							# y = m(x-a) + f(a)
	m = df(f, k)						# Derivative of x on point x = k
	return m*(x-k) + f(k)