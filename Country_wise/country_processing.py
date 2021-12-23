import os
import pandas as pd
import numpy as np
df_tested = pd.read_csv('Confirmed.csv')
df_recovered = pd.read_csv('Recovered.csv')
df_deceased = pd.read_csv('Deceased.csv')




states  = []
numOfCol = df_recovered.columns.size
for i in range(3, numOfCol):
  states.append(df_recovered.columns[i])


indexes = ['Recovered', 'Deceased', 'Confirmed']
df_country = pd.DataFrame(0, index = np.arange(1, df_deceased.shape[0]), columns=indexes)



for state in states: 
    df_country['Recovered'] += df_recovered[state]
for state in states: 
    df_country['Deceased'] += df_deceased[state]
for state in states: 
    df_country['Confirmed'] += df_tested[state]

df_country.to_csv('Country.csv', header = None, index = None)
# print(df_country)
