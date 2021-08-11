import pandas as pd

data = pd.read_excel("F:\\SEM-4\\DATA SCIENCE\\LAB\\data.xlsx")

print(data.head())

print(data.tail())

print(data.to_string())