import numpy as np


prime = []

prev_num = 0
num = 2
count = 0
while(1):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            break
    else:
        count = count + 1
        prime.append(num)
        if count % 100 == 0:
            print count
            location = str('prime_numbers/')
            filename = str(location + str(prev_num) + str('-') + str(num) + str('.dat'))
            prime_array = np.array(prime, 'float64')
            np.savetxt(filename, prime_array)
            prev_num = num
            prime = []
    num = num + 1
    if(count == 100000):
        break

