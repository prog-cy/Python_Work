# import pandas library
import pandas as pd

# make list of names
ls = ['Rupesh', 'Rohan', 'Rahul', 'Ram', 'Riya', 'Raju']


# create a series
series_obj = pd.Series(ls)
print("Given Series:\n", series_obj)

# convert series object into array
arr = series_obj.values

# reshaping series
reshaped_arr = arr.reshape((2, 3))
# show
print("\n\nAfter Reshaping: \n", reshaped_arr)

