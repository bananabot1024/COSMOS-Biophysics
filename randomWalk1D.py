import random, numpy
import matplotlib.pyplot as plt
random.seed(None)

def random_walk(steps):
	walk = numpy.zeros(steps+1)
	walk[0] = 0
	for i in range(1, num_steps):
		rand = random.randint(0,1)
		if rand == 0:
			walk[i] = walk[i-1] -1
		else:
			walk[i] = walk[i-1] + 1
	return walk

num_steps = 1000
walk = random_walk(num_steps)
x = range(num_steps + 1)
plt.plot(x, walk, 'b-')
plt.title('One-dimensional random walk')
plt.grid(True)
plt.show()

