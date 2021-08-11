import numpy as np
import time
import sys

s = range(100000)

print(sys.getsizeof(5)*len(s))

d = np.arange(100000)

a = np.array([1,2,3,4,5])
print(a)

print(d.size*d.itemsize)