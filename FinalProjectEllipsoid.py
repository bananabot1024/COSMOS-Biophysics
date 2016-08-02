#
#  Executes target seeking random walk inside a
#  confining boundary. 
#
#  Following parameters can be specified:
#    1- Shape, size, and location of boundary
#    2- Shape, size, and location of target
#    3- Random step type (continuous angle or on a grid) 
#    4 -Starting location for random walk 
#
import sys, random
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import shapes3d as shapes
import randwalk3d as rw3d

random.seed(None)        # Seed generator, None => system clock
#   Sets maximum number of steps in each random walk    
max_steps = 5000

#  Choices are defined in shapes3d_class:  
#         Sphere( (x,y,z), radius)   
#         Rectangle3d( (x,y,z), width,depth, height)
#         Ellipsoid( (x,y,z) , a , b, c) 

boundary      = shapes.Ellipsoid((0.0, 0.0, 0.0), 25, 44, 25) 
#    boundary  = shapes.Rectangle3d((0.0, 0.0,0.0), 20, 20, 40)
#	 boundary  = shapes.Sphere((0.0, 0.0, 0.0), 30)

target_loc = (5.0, 5.0, 5.0)
#target = shapes.Rectangle3d(target_loc, 4 , 4, 4) 
target = shapes.Sphere(target_loc, 6)

start_loc   = (0.0,0.0,0.0)
move_target_flag = False

rand_function = rw3d.rand_direct

target_loc = target.get_location()
if not boundary.check_inside(target_loc):
    print " Sorry, your target is not inside the current boundary "
    print " Current target  : " +str(target)
    print " Current boundary: " +str(boundary)
    print " Change target location or boundary size to correct problem"
    sys.exit(0) 

totalHits = 0;
totalSteps = 0;
walk_steps = np.zeros(100)  # Tracks number of steps for each walk

for n in range(0, 100):
	rand_walk = rw3d.RandomWalk3d(start_loc, max_steps, rand_function, boundary, target, move_target_flag)
	rand_walk.conduct_walk() 
	totalSteps = totalSteps + rand_walk.get_num_steps()
	walk_steps[n] = rand_walk.get_num_steps();

	if rand_walk.get_num_steps() < max_steps :
		totalHits = totalHits + 1;

	if n == 5:
		#
		#  Graph 
		#
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		ax.set_aspect("equal","datalim")
		rand_walk.plot_walk(ax,'r-')

		boundary.draw_shape(ax,'b',.2)    
		target.draw_shape(ax,'k',.2)
		boundary.set_plot_size(ax)
		ax.set_title('Sample Random Walker in an Ellipsoid')
		ax.text(-40, 75, 0.5, 'Starting location = ' + str(start_loc), transform = ax.transAxes)
		ax.text(.75, 5, 0.5, 'Target location = ' + str(target_loc), transform = ax.transAxes)
		print 'Close graph to continue...'	
		plt.savefig("ellipsoid_walk.png") 	
		plt.show() 
		

prob = (totalHits)
aveSteps = int(np.mean(walk_steps))

#
#  Create histogram of steps to target for all simulations 
#
fig = plt.figure()
ax  = fig.add_subplot(1,1,1)  
ax.hist(walk_steps, bins=50, color='red')      
plt.title('Histogram of Steps to Target for an Ellipsoid ' )
#  Place text with statistics on graph
ax.text(.75,.8, 'Ave steps: %d' %(aveSteps), transform = ax.transAxes)
ax.text(.55,.7, 'Probability of hitting target: %d' %(prob)+ '%', transform = ax.transAxes)

if move_target_flag:
    ax.text(.75,.70,'Target moves!!',transform = ax.transAxes)    
plt.grid(True)
plt.savefig("ellipsoid_hist.png") 
plt.show()


