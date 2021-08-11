# Program to create a 1-D array to 4-D array
import numpy as np

arr = np.array([(1,2,3,4)])

print('1-D array')
print(arr)
print('Dimension: ', arr.ndim)

arr1 = np.array([(1,2,3,4), (2,3,4,5)])

print('\n2-D array')
print(arr1)
print('Dimension: ', arr1.ndim)

arr2 = np.array([[(1,2,3), (1,4,5), (6,7,8)]])

print('\n3-D array')
print(arr2)
print('Dimension: ', arr2.ndim)

arr3 = np.array([[[[1,2,3],[4,5,6],[7,8,9],[3,2,1]]]])

print('\n4-D array')
print(arr3)
print('Dimension: ', arr3.ndim)