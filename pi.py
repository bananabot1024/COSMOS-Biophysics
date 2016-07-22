import numpy as np
import random

inside = 0
total = int(raw_input("Enter the number of points to generate: "))
for i in range(0,total):
	#generate random x, y
	x = random.uniform(-1,1)
	y = random.uniform(-1,1)
	if x*x + y*y <= 1:
		inside += 1
estimate = 4.0*inside/total
print "pi estimate is", estimate
print "percent error is", abs(np.pi - estimate)/np.pi
