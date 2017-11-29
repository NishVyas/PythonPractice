# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 18:56:14 2017

@author: nishant
"""

'Read in CSV file for Student Weight
import pandas as pd
d = pd.read_csv('C:/Users/nishant/Desktop/FilesForPython/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv')
'Display all rows where there is a missing value in the LOCATION 1 coulmn
d['Location 1'].isnull()
'Check how many rows have missing values
d['Location 1'].isnull().value_counts()
'Drop rows with missing values under LOCATION 1
d = d['Location 1'].dropna()
'Drop all rows with an instance of a missing value
d = d.dropna(how='any')
'Now check to see how many rows have missing values
d.isnull().value_counts()
'Notice there arent any True values

'Lets work on filling in missing data
'Lets define data frames to work with
df = pd.DataFrame(np.random.randn(5, 3), index=['a0', 'a10','a20', 'a30', 'a40'],columns=['X', 'Y', 'Z'])
df
'Lets add some extra rows for null values
df2 = df.reindex(['a0', 'a1', 'a10', 'a11', 'a20', 'a21', 'a30', 'a31', 'a40', 'a41'])
df2
'Fill in the empty rows with 0
df2.fillna(0)
