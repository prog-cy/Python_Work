# performing some operation upon the array
import numpy as np

a = np.array([(10,30,50,2,3,70)])

print('Max value in the array is: ', a.max())

print('Min value in the array is: ', a.min())

print('Sum of the array is: ', a.sum())

a1 = np.array([(1,2,3,4),(7,8,9,1)])
print('Sum of row')
print(a1.sum(axis=0))

print('Square root ')
print(np.sqrt(a1))

print('Standard deviation')
print(np.std(a1))

a2 = np.array([(1,2,3), (3,4,5)])
a3 = np.array([(5,6,7), (1,2,3)])

print('sum is')
print(a2+a3)

print('Subtraction is')
print(a2-a3)

print('Multiplication is')
print(a2*a3)

print('Division is')
print(a2/a3)

print('Vertical stack')
print(np.vstack((a2,a3)))

print('Horizontal stack')
print(np.hstack((a2,a3)))

print('Converting array in single column')
print(a2.ravel())
