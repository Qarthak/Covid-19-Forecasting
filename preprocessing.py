import os
import pandas as pd
cwd = os.path.abspath('') 
files = os.listdir(cwd)
print(cwd)
print(files)
df = pd.DataFrame()
for file in files:
    if(file.endswith('.csv') & file.startswith('state_wise_daily')): 
        df = df.append(pd.read_csv(file))

#print(df.head())

df1 = df.iloc[::3]
df2 = df.iloc[1::3]
df3 = df.iloc[2::3]

df3.to_csv('Deceased.csv')
df1.to_csv('Confirmed.csv')
df2.to_csv('Recovered.csv')
