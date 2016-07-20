import sys
import numpy as np
import matplotlib.pyplot as plt
#   Input coefficients a, b, c   
a = float(raw_input('Enter value for a :'))
b = float(raw_input('Enter value for b :'))
c = float(raw_input('Enter value for c :')) 
discriminant = b*b - 4*a*c
#   If real roots
if discriminant >= 0:
	root1 = (-b + np.sqrt(discriminant)) / (2*a)
	root2 = (-b - np.sqrt(discriminant)) / (2*a)
else:
	print 'imaginary roots'
	sys.exit(0)

print ' For quadratic equation : '
print ' %f * x**2 + %f *x  + %f  = 0' % (a,b,c) 
# If real roots found
print ' Real roots are: %f  and %f '  % (root1, root2) 

#  Plot quadratic equation
f = lambda x: a*x**2 + b*x + c 
xlim1 = min(root1,root2) -5
xlim2 = max(root1,root2) +5 
xvalues = np.linspace(xlim1,xlim2,500)
yvalues = np.array([ f(x)  for x in xvalues])
plt.plot(xvalues, yvalues, 'b-')
plt.axhline(0, color='black', lw=1)  #  line on x-axis
plt.axvline(0, color='black', lw=1)  #  line on y axis
plt.grid(True)                       #  Adds grid lines
plt.title('Plot of quadratic equation')
plt.show()
   

