# Plots G vs P(G1 wins) keeping g1 = g2, and p = 49.9%
import matplotlib.pyplot as plt
p = 0.499
gList = []
probabilityList = []
for g in range (100,2500):
    gList.append(g)
    numerator = ((1-p)/p)**g -1
    denominator = ((1-p)/p)**(g+g) -1
    probability = numerator / denominator
    probabilityList.append(probability)
plt.plot(gList, probabilityList, 'r-')
plt.title('Gambler\'s ruin: g=g1=g2 vs probability that G1 wins')
plt.grid(True)
plt.show()
