# 2 gamblers play against each other, simulate a random walk 
#  starting from 0 until either g1 or g2 loses

import random, numpy
import matplotlib.pyplot as plt

p1 = float(raw_input("Enter the probability of gambler 1 winning: "))
g1_amount = int(raw_input("Enter the starting amount for gambler 1: "))
g2_amount = int(raw_input("Enter the starting amount for gambler 2: "))

g1_sequence = [g1_amount]
g2_sequence = [g2_amount]
steps = 0

def gamble(g1_amount, g2_amount, g1_sequence, g2_sequence, steps):
	while (g1_amount != 0 and g2_amount != 0):
		winner = random.uniform(0,1)
		if winner < p1:
			g1_amount += 1
			g2_amount -= 1
			g1_sequence.append(g1_amount)
			g2_sequence.append(g2_amount)
		else:
			g1_amount -= 1
			g2_amount += 1
			g1_sequence.append(g1_amount)
			g2_sequence.append(g2_amount)
		steps += 1
	return steps

steps = gamble(g1_amount, g2_amount, g1_sequence, g2_sequence, steps)
x = range(steps + 1)
plt.plot(x, g1_sequence, 'r-', label = 'Gambler 1')
plt.plot(x, g2_sequence, 'b-', label = 'Gambler 2')
plt.legend(loc = 'upper left')
plt.title('Gambler\'s ruin: p=' + str(p1) + ', g1 = $' + str(g1_amount) + ', g2 = $' + str(g2_amount))
plt.grid(True)
plt.show()
