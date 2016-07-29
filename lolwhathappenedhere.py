import random, numpy
import matplotlib.pyplot as plt
random.seed(None)

def randomAngle(xWalk1, yWalk1):
    randomAngle = random.uniform(0, 2*numpy.pi)
    xdelta = numpy.cos(randomAngle)
    ydelta = numpy.sin(randomAngle)
    return xdelta, ydelta

def randomWalk2D(steps):
    xWalk = numpy.zeros(steps)
    yWalk = numpy.zeros(steps)
    stepsTaken = 0
    while stepsTaken < steps:
	    # Create trial move
        xdelta, ydelta = randomAngle(xWalk, yWalk)
        xtrial = xWalk[stepsTaken] + xdelta
        ytrial = yWalk[stepsTaken] + ydelta
    	# Check if trial move is inside boundary. If so, accept it
    	if abs(xtrial) < width/2 and abs(ytrial) < height/2:
        	xWalk[stepsTaken] = xtrial
        	yWalk[stepsTaken] = ytrial
        	stepsTaken += 1
    return xWalk, yWalk

num_walks = int(raw_input('Enter number of walks to do (1-5):'))
if num_walks <= 0 or num_walks >5:
    print 'Number of walks selected = ', num_walks,' - must be between 1 and 5'
    sys.exit(0)
global width, height
width = int(raw_input('Enter (even) width of box: '))
height = int(raw_input('Enter (even) height of box: '))
num_steps = 1000 
line_type = ['r-','b-','k-','g-','m-']
for i in range(num_walks):    
    xwalk1, ywalk1 = randomWalk2D(num_steps)
    plt.plot(xwalk1, ywalk1, line_type[i], label = 'walk'+ str(i+1))
    plt.plot(xwalk1[-1],ywalk1[-1], 'k*', ms=16)
plt.axhline(0, color='black', lw=1)  
plt.axvline(0, color='black', lw=1) 
plt.title('Two-dimensional random walks(' + str(num_walks) + ')' )
plt.legend(loc="upper left")
plt.grid(True)
plt.show() 
