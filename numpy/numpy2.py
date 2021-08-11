# program for performing different-2 operations
import numpy as np

a = np.array([[1,2,3,4], [3,4,5,6]])

b = np.array([[1,2,3,5],[3,4,5,6]])

c = a*b
print('Multiplication of each element with next array element')
print(c)


d = np.add(a, b)
print('\nAddition of the element of arrays')
print(d)