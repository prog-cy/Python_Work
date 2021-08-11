# program for slicing of an array
import numpy as np

a1 = np.array([[1,2,3,4,5],[4,5,6,7,8]])

for i in range(5):
    print('col'+str(i+1))
    print(a1[0:, i])
    print('\n')

print('\nrow1')
print(a1[0, 0:])

print('\nrow2')
print(a1[1, 0:])
