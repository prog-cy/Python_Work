import pandas as pd
import numpy as np

# Series in pandas
arr = np.array([10, 2, 3, 4, 5])

s = pd.Series(arr)

print(s)

s1 = pd.Series(arr, index = [i for i in range(1, len(arr)+1)])

print(s1)

s2 = pd.Series(arr, index = ['a', 'b', 'c', 'd', 'e'])
print(s2[:3])

print(s2[1:3])
