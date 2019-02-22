import numpy as np
from pylab import *
import matplotlib.pyplot as plt

prime_array = np.loadtxt('0-541.dat')

plt.grid(True)
plt.xlabel('Bins')
plt.ylabel('Total Prime No.')
plt.hist(prime_array,bins= 100, orientation='vertical')

plt.show()
