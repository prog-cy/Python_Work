# Creating DataFrames using list
import pandas as pd

ls = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [10,20,30,40,50,60], [5,6,7,8,9,10]]

df = pd.DataFrame(ls, columns=['a', 'b', 'c', 'd', 'e', 'f'], index=['R1', 'R2', 'R3', 'R4'])

print(df)
