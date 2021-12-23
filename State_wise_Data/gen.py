import os
import pandas as pd

df_tested = pd.read_csv('Confirmed.csv')
df_recovered = pd.read_csv('Recovered.csv')
df_deceased = pd.read_csv('Deceased.csv')

states  = []
numOfCol = df_recovered.columns.size
for i in range(3, numOfCol):
  states.append(df_recovered.columns[i])

dataFrames = []

for i in range(len(states)):
  temp_df = df_tested[states[i]].rename('Tested')
  temp_df = temp_df.to_frame()
  temp_df = temp_df.join(df_recovered[states[i]].rename('Recovered'))
  temp_df = temp_df.join(df_deceased[states[i]].rename('Deceased'))
  dataFrames.append(temp_df)

for i in range(len(states)):
    dataFrames[i].reset_index(drop=True, inplace=True)
    dataFrames[i].to_csv('sam'+str(i+1)+'_'+states[i]+'.csv', header = None, index = None)