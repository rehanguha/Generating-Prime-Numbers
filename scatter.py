import numpy as np
from pylab import *
import matplotlib.pyplot as plt

start = 2
end = 10000

out_file = open("prime_number", "w")

count = 0
colors = ('#FF4500', '#3CB371', '#4682B4', '#DB7093', '#FFD700')

for num in range(start, end):
    ++count
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            break
    else:
        plt.scatter(num, 1, c = colors[num % len(colors)])
        
        '''if count % 2 == 0:
            plt.scatter(num, 1.0)
        else:
            plt.scatter(num, 2.0)'''
        
        out_file.write(str(num)+ str("\n"))

out_file.close()
plt.show()
