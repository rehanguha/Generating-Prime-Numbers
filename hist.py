import numpy as np
from pylab import *
import matplotlib.pyplot as plt

start = 0
end = 10000

out_file = open("prime_number", "w")
prime = []

for num in range(start, end):
    if num == 0 or num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            break
    else:
        prime.append(num)
        out_file.write(str(num)+ str("\n"))

out_file.close()

prime_array = np.array(prime, 'float64')

plt.grid(True)
plt.xlabel('Bins')
plt.ylabel('Total Prime No.')
plt.hist(prime_array, bins =end/100, orientation='vertical')

plt.show()
