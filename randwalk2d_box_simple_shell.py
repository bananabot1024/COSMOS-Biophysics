#
#  Executes random walk inside a confining
#  boundary(rectangle).Following parameters can be changed:
#    1- Size and location of box
#    2 -Starting location for random walk 
#
import sys, random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle  # Used to draw rectangle
random.seed(None)        # Seed generator, None => system clock

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

num_steps = 1000
low_left, top_right = setup_box((0.0, 0.0), 40, 40)
start_loc   = ( 0.0, 0.0)
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
#  Plot random walk inside box. Put large star at end of walk.
plt.plot(xwalk, ywalk, 'r-')
plt.plot(xwalk[-1],ywalk[-1], 'b*', ms=16)
draw_box(low_left, top_right ,start_loc)
plt.title('2D walk inside box ' )
plt.grid(True)
plt.show() 

