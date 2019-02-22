import numpy as np
from pylab import *

def prime(x):
    print type(x)
    print x
    x = 6
    if x == 2:
        return x
    else:
        flag = 0
        for i in range(2, x/2):
            if x % i == 0:
                flag = 1
            else:
                flag = 0
                break
        if flag == 1:
            return x
        else:
            return
        
def fx(x):
    for i in x:
        return prime(i)

size = 10

X = np.linspace(0,size,endpoint=False)
C = fx(X)
plot(X,C,color="blue", linewidth=.5)
show()
