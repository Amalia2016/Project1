# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 01:55:13 2016

@author: amali
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:02:01 2016

@author: amali
"""
# Source of data
# https://data.cityofnewyork.us/Public-Safety/NYPD-7-Major-Felony-Incidents/hyij-8hr7

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

df_ini = pd.read_csv('NYPD_7_Major_Felony_Incidents.csv',index_col=0,parse_dates=True)

# Check for missing values and drop them
def missing_values_table(df): 
        mis_val = df.isnull().sum()
        mis_val_percent = 100 * df.isnull().sum()/len(df)
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0: 'Missing Values', 1 : '% of Total Values'})
        return mis_val_table_ren_columns 
print(missing_values_table(df_ini))
df_clean = df_ini.dropna()
print(missing_values_table(df_clean))

# Any duplicate rows??
dfx = df_clean.duplicated(subset='Identifier', keep=False)
dfx = df_clean[df_clean.Identifier == True].copy()
dfx.head(10)

# Take columns that are interesting for now
interest_col = ['Offense', 'Day of Week', 'Occurrence Year', 'Occurrence Month', 'Occurrence Day', 'XCoordinate', 'YCoordinate', 'Borough']
df1 = df_clean[interest_col].copy()

# Look up offenses in file
all_offenses = df_clean['Offense'].unique()
print(all_offenses)
all_offenses = ['BURGLARY' 'GRAND LARCENY' 'GRAND LARCENY OF MOTOR VEHICLE' 'RAPE'
 'ROBBERY' 'FELONY ASSAULT' 'MURDER & NON-NEGL. MANSLAUGHTE']

#scipy.stats has methods trim1 and trimboth - outliers
# Plot dataframe
def My_Plots(dfp, offense, col1, col2, ordinal1, ordinal2, categorical):
   print('Offense:', offense, '   Columns:', col1, ' - ', col2)
   if categorical: print(pd.crosstab(dfp[col1], dfp[col2],margins=True))
   if ordinal1 and categorical: dfp[col1].hist()
   if ordinal2 and categorical: dfp[col2].hist()
   if categorical == False:
       dfp[((dfp[col1] - dfp[col1].mean()) / dfp[col1].std()).abs() < 3]
       dfp[((dfp[col2] - dfp[col2].mean()) / dfp[col2].std()).abs() < 3]
       dfp.plot.scatter(x = col1, y = col2)
   return
My_Plots(df1,'All', 'XCoordinate', 'YCoordinate', True,True,False)

# Change values for 'Day of Week', 'Occurrence Month', 'Offense'
DayOfWeek_dictionary = {'Monday': 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5, 'Saturday' : 6, 'Sunday' : 7}
Month_dictionary = {'Jan': 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug': 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12}
Offense_dictionary = {'BURGLARY': 'BU', 'GRAND LARCENY': 'GL', 'GRAND LARCENY OF MOTOR VEHICLE': 'GM', 'RAPE': 'RA',
                      'ROBBERY': 'RO', 'FELONY ASSAULT': 'FA', 'MURDER & NON-NEGL. MANSLAUGHTE': 'MM'}
df1 = df1.replace({'Day of Week': DayOfWeek_dictionary})
df1 = df1.replace({'Occurrence Month': Month_dictionary})
df1 = df1.replace({'Offense': Offense_dictionary})
df1.sort_values(['Offense'])

# Create dataframes per offense
df_BU = df1[df1.Offense == 'BU'].copy()
df_BU.drop('Offense', axis=1, inplace=True)
df_GL = df1[df1.Offense == 'GL'].copy()
df_GL.drop('Offense', axis=1, inplace=True)
df_GM = df1[df1.Offense == 'GM'].copy()
df_GM.drop('Offense', axis=1, inplace=True)
df_RA = df1[df1.Offense == 'RA'].copy()
df_RA.drop('Offense', axis=1, inplace=True)
df_RO = df1[df1.Offense == 'RO'].copy()
df_RO.drop('Offense', axis=1, inplace=True)
df_FA = df1[df1.Offense == 'FA'].copy()
df_FA.drop('Offense', axis=1, inplace=True)
df_MM = df1[df1.Offense == 'MM'].copy()
df_MM.drop('Offense', axis=1, inplace=True)

# Create plots
My_Plots(df_BU,'BURGLARY', 'XCoordinate', 'YCoordinate', True,True,False)
My_Plots(df_BU,'BURGLARY', 'Day of Week', 'Borough',True,False,True)
My_Plots(df_BU,'BURGLARY', 'Occurrence Month', 'Borough',True,False,True)
My_Plots(df_BU,'BURGLARY', 'Occurrence Year', 'Borough',True,False,True)
My_Plots(df_BU,'BURGLARY', 'Occurrence Day', 'Borough',True,False,True)



