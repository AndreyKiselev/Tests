from timeit import default_timer as timer
import numpy as np

#data = np.random.normal(0, 1, 10000)
data = np.arange(12000)
a = 0
s = timer()
for k in range(0 , data.size):
    a += data
e = timer()
print('execution time of for = ' + str(e-s) + 's')
a = 0
k = 0
e_1 = timer()
while k < data.size:
    a += data
    k += 1
e_2 = timer()
print('execution time of while = ' + str(e_2 -e_1) + 's')
