import random, numpy
import matplotlib.pyplot as plt
random.seed(None)

def randomAngle():
	randomAngle = random.uniform(0, 2*numpy.pi)
	xdelta = numpy.cos(randomAngle)
	ydelta = numpy.sin(randomAngle)
	return xdelta, ydelta

def randomWalk2D(steps):
	xWalk = numpy.zeros(steps)
	yWalk = numpy.zeros(steps)
	for i in range(steps-1):
		xdelta, ydelta = randomAngle()
		xWalk[i+1] = xWalk[i] + xdelta
		yWalk[i+1] = yWalk[i] + ydelta
	return xWalk, yWalk

num_walks = int(raw_input('Enter number of walks to do (1-5):'))
if num_walks <= 0 or num_walks >5:
    print 'Number of walks selected = ', num_walks,' - must be between 1 and 5'
    sys.exit(0)
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
