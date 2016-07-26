import random
import numpy as np
import matplotlib.pyplot as plt

p1 = float(raw_input("Enter the probability of gambler 1 winning: "))
if p1 < 0 or p1 > 1:
	print 'Probability must be between 0 and 1'
	sys.exit(0)
g1_amount = int(raw_input("Enter the starting amount for gambler 1: "))
if g1_amount < 0:
	print 'Starting amount must be greater than 0'
	sys.exit(0)
g2_amount = int(raw_input("Enter the starting amount for gambler 2: "))
if g2_amount < 0:
	print 'Starting amount must be greater than 0'
	sys.exit(0)
numSimulations = int(raw_input('Enter the number of simulations to run: '))
if numSimulations < 1:
	print 'Number of simulations must be at least 1'
	sys.exit(0)
g1_sequence = [g1_amount]
g2_sequence = [g2_amount]
stepsArray = np.zeros(numSimulations)
g1Wins = 0

def gamble(g1_amount, g2_amount, g1_sequence, g2_sequence, steps, g1Wins):
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
	if g2_amount == 0:
		g1Wins += 1
	return steps, g1Wins

for i in range(0,numSimulations):
	stepsArray[i], g1Wins = gamble(g1_amount, g2_amount, g1_sequence, g2_sequence, 0, g1Wins)

print 'Statistics for gamblers ruin with %d simulations:' % numSimulations
print 'Prob g1 = %f , g1 bankroll = %d ,  g2 bankroll = %d' % (p1,g1_amount,g2_amount) 
print 'Gambler1 wins', round (100.0*(g1Wins/float(numSimulations))), '% of the time'
print 'Average number of steps to ruin is: %f ' %  int(np.mean(stepsArray))
print 'Largest number of steps to ruin is: %f ' %  int(np.max(stepsArray)) 
#  Print histogram of results
plt.hist(stepsArray, bins=50, color='blue')      
plt.title(' Gambler\'s ruin: p='+ str(p1)+ ', g1 = \$'+ str(g1_amount)+ ', g2 = \$'+ str(g2_amount))
plt.grid(True)
plt.xlabel('Number of steps')  
plt.show()
