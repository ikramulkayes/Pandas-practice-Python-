import pandas as pd
df = pd.read_csv('pokemon_data.csv')
print(df.columns)
print(df.Name[0:6])
print(df[["Name","Type 1","HP"]])

