# Linear congruential RNG
# Generates random numbers in (0,1) interval
def RNG_function():
    global idum
    m = 134456
    n = 8121
    k = 28411
    idum = (idum*n+k) % m
    return idum/float(m)     

seed = 89053    
idum = seed
print ' idum     random number '
for i in range(20):
    print idum, ' ', RNG_function()

