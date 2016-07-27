# Computes P(G1 wins) given p, g1, and g2 based on the derived formula
p = float(raw_input('Enter p: '))
g1 = float(raw_input('Enter g1: '))
g2 = float(raw_input('Enter g2: '))
numerator = ((1-p)/p)**g1 -1
denominator = ((1-p)/p)**(g1+g2) -1
print 'probability g1 wins is', numerator / denominator
