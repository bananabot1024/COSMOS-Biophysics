#
#  Executes random walk inside a confining
#  boundary(rectangle).Following parameters can be changed:
#    1- Size and location of box
#    2 -Starting location for random walk 
#
import sys, random
import numpy as np
import matplotlib.pyplot as plt
import randomWalk2DModule as rw2d
from matplotlib.patches import Rectangle  # Used to draw rectangle
random.seed(None)        # Seed generator, None => system clock

num_steps = 1000
low_left, top_right = rw2d.setup_box((0.0, 0.0), 40, 40)
start_loc   = ( 0.0, 0.0)

xwalk, ywalk = rw2d.randomWalk2DBox(start_loc, num_steps, low_left, top_right)

#  Plot random walk inside box. Put large star at end of walk.
plt.plot(xwalk, ywalk, 'r-')
plt.plot(xwalk[-1],ywalk[-1], 'b*', ms=16)
rw2d.draw_box(low_left, top_right ,start_loc)
plt.title('2D walk inside box ' )
plt.grid(True)
plt.show() 

