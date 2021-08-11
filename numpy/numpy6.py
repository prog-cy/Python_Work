# reshape the matrix
import numpy as np

a = np.array([(1,2,3), (4,5,6)])

print('Array is ', a)

print('Reshaped array')
a = a.reshape(3,2)
print(a)

print('Array after applying line space')
b = np.linspace(1,3,10)
print(b)