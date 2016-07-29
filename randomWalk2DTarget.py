import random, numpy
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
random.seed(None)

def randomAngle(xWalk1, yWalk1):
    randomAngle = random.uniform(0, 2*numpy.pi)
    xdelta = numpy.cos(randomAngle)
    ydelta = numpy.sin(randomAngle)
    return xdelta, ydelta

def randomWalk2D(steps):
    xWalk = [0]
    yWalk = [0]
    stepsTaken = 0
    while stepsTaken < steps:
        # Check if target reached
        if xWalk[-1] > targetX - targetWidth/2 and xWalk[-1] < targetX + targetWidth/2 and yWalk[-1] > targetY - targetHeight/2 and yWalk[-1] < targetY + targetHeight/2:
            targetReached = True
            print 'Number of steps taken:', stepsTaken
            break
	    # Create trial move
        xdelta, ydelta = randomAngle(xWalk, yWalk)
        xtrial = xWalk[stepsTaken] + xdelta
        ytrial = yWalk[stepsTaken] + ydelta
    	# Check if trial move is inside boundary. If so, accept it
    	if abs(xtrial) < boxWidth/2 and abs(ytrial) < boxHeight/2:
			stepsTaken += 1
			xWalk.append(xtrial)
			yWalk.append(ytrial)
    if not targetReached:
        print 'Target not reached in 10,000 steps'
    return xWalk, yWalk

def draw_box(width, height):
    plt.gca().add_patch(Rectangle((-width/2,-height/2), width, height,  fill=False, edgecolor='b',lw=4))
    plt.xlim([-width/2 - 3,width/2 + 3])
    plt.ylim([-height/2 - 3,height/2 + 3])
    return

def draw_target(x, y, width, height):
    plt.gca().add_patch(Rectangle((x-targetWidth/2, y-targetHeight/2), width, height, fill = True, edgecolor='k', lw=2))
    return

global startX, startY, boxWidth, boxHeight, targetX, targetY, targetWidth, targetHeight, targetReached
targetReached = False
startX = int(raw_input('Enter starting location (x): '))
startY = int(raw_input('Enter starting location (y): '))
boxWidth = int(raw_input('Enter (even) width of box: '))
boxHeight = int(raw_input('Enter (even) height of box: '))
targetX = int(raw_input('Enter center of target (x): '))
targetY = int(raw_input('Enter center of target (y): '))
targetWidth = int(raw_input('Enter (even) width of target: '))
targetHeight = int(raw_input('Enter (even) height of target: '))

maxSteps = 10000
xwalk1, ywalk1 = randomWalk2D(maxSteps)
plt.plot(xwalk1, ywalk1, 'r-')
plt.plot(xwalk1[-1],ywalk1[-1], 'k*', ms=16)
plt.axhline(0, color='black', lw=1)  
plt.axvline(0, color='black', lw=1) 
plt.title('2D Random Walk Inside Box With Target')
draw_box(boxWidth, boxHeight)
draw_target(targetX, targetY, targetWidth, targetHeight)
plt.grid(True)
plt.show()
