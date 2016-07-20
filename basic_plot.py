#
#  Shows basic matplotlib 2D plot
#  of x vs sin(x). X and Y values 
#  are created using numpy arrays     
#

import numpy as np
import matplotlib.pyplot as plt
# Program plots x vs sin(x) in [0,2*PI]
xvalues = np.linspace(0, 2*np.pi, 1000)
yvalues = np.sin(xvalues)
plt.plot(xvalues, yvalues, 'b-', label='sin(x)')
zvalues = np.cos(xvalues)
plt.plot(xvalues, zvalues, 'r-', label='cos(x)')
plt.title('Plot of x vs sin(x) and cos(x)')
plt.xlabel('x')
plt.ylabel('Trig functions sin(x) and cos(x)')
plt.legend()
plt.show()
plt.savefig('trig_plot.png')

