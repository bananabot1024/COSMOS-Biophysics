# Plots p vs P(G1 wins) keeping g1 and g2 constant at 100
import matplotlib.pyplot as plt
g1 = 100
g2 = 100
pList = []
probabilityList = []
for i in range (470, 499):
    p = float(i)/1000.0
    pList.append(p)
    numerator = ((1-p)/p)**g1 -1
    denominator = ((1-p)/p)**(g1+g2) -1
    probability = numerator / denominator
    probabilityList.append(probability)
plt.plot(pList, probabilityList, 'r-')
plt.title('Gambler\'s ruin: p vs probability that G1 wins')
plt.grid(True)
plt.xlabel('Probability Gambler 1 wins each round')
plt.ylabel('Probability Gambler 1 wins entire game')
plt.show()
plt.savefig('p_vs_pwin.png')
