#
#  Program solves for intersection of
#     y = ax +b and y = cx + d
#  Inputs: a, b, c, d 
#  Outputs: Point of intersection(x,y) - if any     
#
import sys
import matplotlib.pyplot as plt
import numpy as np

#   Input coefficients a, b, c, d   
a = float(raw_input('Enter value for a: '))
b = float(raw_input('Enter value for b: '))
c = float(raw_input('Enter value for c: '))
d = float(raw_input('Enter value for d: '))

#  If lines identical
if a == c && b==d:
	print 'lines identical'
	sys.exit(0)
#  If lines parallel
elif a ==c:
	print 'lines parallel'
	sys.exit(0)
else:
	xvalue = (d-b)/(a-c)
	yvalue = c*xvalue + d

#  Print results 
print ' Lines intersect at x,y = (%f, %f)' % (xvalue,yvalue)

#  Plot intersection
x = np.linspace(xvalue-5,xvalue+5,200)
y1 = a*x + b
y2 = c*x + d
plt.plot(x,y1,'r-',x,y2,'r-')
plt.plot(xvalue,yvalue,'b*',ms= 15)
# Add title and x and y axis here
plt.title('Intersection of two lines')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
