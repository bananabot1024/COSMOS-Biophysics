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

num_walks = int(raw_input('Enter number of walks to do (0-5): '))
line_type = ['r-', 'b-', 'k-', 'g-', 'm-']
num_steps = 1000
x = range(num_steps + 1)
for i in range(0,num_walks):
	walk = random_walk(num_steps)
	plt.plot(x, walk, line_type[i], label = "walk " + str(i+1))
plt.title('One-dimensional random walk(s)')
plt.grid(True)
plt.legend(loc="upper left")
plt.show()

