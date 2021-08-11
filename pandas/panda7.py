# creating DataFrames using dict
import pandas as pd

data = {
            'Name':['Rupesh', 'Rohan', 'Rahul', 'Ram', 'Riya', 'Raju'],
            'Age':[20, 21, 22, 20, 19, 18]
        }

df = pd.DataFrame(data, index=['R1', 'R2', 'R3', 'R4', 'R5','R6'])

print(df)