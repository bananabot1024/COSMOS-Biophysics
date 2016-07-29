#
#  Module contains a number of functions useful
#  for conducting 2D random walks
#
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle  # Used to draw rectangle
np.random.seed(None)        # Seed generator, None => system clock

def rand_angle():
    rand_angle = random.uniform(0,2.*np.pi)
    xdelta = np.sin(rand_angle)
    ydelta = np.cos(rand_angle)
    return xdelta, ydelta

def setup_box( box_loc , width, height):
    xloc,yloc = box_loc
    low_left  = (xloc - .5 * width, yloc -.5 * height)
    top_right = (xloc + .5 * width, yloc +.5 * height)    
    return low_left, top_right

def check_inside_box(xvalue, yvalue, low_left, top_right):
    x1, y1 = low_left
    x2, y2 = top_right
    if xvalue > x1 and xvalue < x2 and yvalue > y1 and yvalue < y2:
        return True
    else:
        return False

def draw_box(low_left, top_right, start_loc):
    xmin, ymin = low_left
    xmax, ymax = top_right
    plt.gca().add_patch(Rectangle((xmin,ymin), xmax-xmin, ymax-ymin,  fill=False, edgecolor='b',lw=4))
    plt.xlim([xmin-3,xmax+3])
    plt.ylim([ymin-3,ymax+3])
    plt.axvline(start_loc[0], color='grey', lw=2)
    plt.axhline(start_loc[1], color='grey', lw=2)  
    return

def randomWalk2DBox(start_loc, num_steps, low_left, top_right):
	xpos = start_loc[0]
	ypos = start_loc[1]
	xwalk = [xpos]
	ywalk = [ypos]
	steps_taken = 0     
	while steps_taken < num_steps :
		# Create trial move
		xdelta, ydelta = rand_angle()
		xtrial = xpos + xdelta
		ytrial = ypos + ydelta
		# Check if trial move is inside boundary. If so, accept it
		if check_inside_box(xtrial, ytrial, low_left, top_right) :
		    xpos = xtrial
		    ypos = ytrial
		    xwalk.append(xpos)
		    ywalk.append(ypos)
		    steps_taken += 1
	return xwalk, ywalk	
