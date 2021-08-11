import pandas as pd
# make an array
array = [2, 4, 6, 8, 10, 12]

# create a series
series_obj = pd.Series(array)
print(series_obj)

# convert series object into array
arr = series_obj.values
print('Original array:\n', arr)

# reshaping series
reshaped_arr = arr.reshape(3, 2)

# show
print('\nReshaped array:\n',reshaped_arr)
