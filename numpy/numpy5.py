import numpy as np

a = np.array([(1,2,3,4,5,6)])

print('Size of the item in the array')
print(a.itemsize)

print('Dimension of the array')
print(a.ndim)

print('Data type of the item defined in the array')
print(a.dtype)

print('Size and shape of the array')
print(a.size, ' ', a.shape)