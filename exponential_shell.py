import numpy as np

def factorial(num):
    if num == 0:
        return 1.0
    prod = 1.0
    for i in range(1,num +1):
        prod*=i 
    return prod

#  Input values x, num_terms   
x = float(raw_input('Enter value for x: '))
num_terms = int(raw_input('Enter number of terms in sum: '))

#  Compute taylor series
approx = 0.0
for i in range(0, num_terms):
	approx += (x**i)/factorial(i)

#  Print results (code challenge 1)
print 'approximation is', approx

#  Print error (code challenge 2)
print 'error is', abs(approx - np.exp(x))

#  Computing approximation with tolerance
terms = 0
approx2 = 0
error = abs(approx2 - np.exp(x))
tolerance = 10**-8
while (error > tolerance):
	approx2 += (x**terms)/factorial(terms)
	terms +=1
	error = abs(approx2 - np.exp(x))
print 'approximation with tolerance is', approx2, 'after', terms, 'terms'

