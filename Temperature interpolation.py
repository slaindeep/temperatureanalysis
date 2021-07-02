
import numpy as np

import pandas as pd

 

data = pd.read_csv('Temperature Data.csv')

 

df = pd.DataFrame(data)

 

df['location_date'] = pd.to_datetime(df['location_date'])

 

##cities = df.groupby(['name','location_date']).agg({'temp_mean_c':'mean'})

 

cities = df.groupby(['name','location_date']).mean()

dt = pd.date_range('01-01-2015','04-20-2021')

idx = pd.DatetimeIndex(dt)

 

df_temp=pd.DataFrame(columns=['name','location_date'])

 

dfs=[]

 

 

for city in df.name.drop_duplicates():

 

    df_temp.loc[:,'location_date']=idx

    df_temp.loc[:,'name']=city

    #print(len(idx))

    #print(len(dt))

    df_new=pd.merge(df_temp,cities.reset_index(),left_on=['name','location_date'],right_on=['name','location_date'],how='left')

    filled_df = df_new.interpolate()

    dfs.append(filled_df)

 
pd.concat(dfs).to_csv('output.csv')

 


 

 

 

 

 

pd.concat(dfs).to_csv('output.csv')
