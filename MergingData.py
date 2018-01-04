# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:22:11 2017

@author: nishant
"""

# Merging Data
# Read in the CSV file
import pandas as pd
import numpy as np
d = pd.read_csv('C:/Users/nishant/Desktop/FilesForPython/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv')
# Lets take area name and county from 1st five rows
d[['AREA NAME', 'COUNTY']][0:5]
# Notice the null values, insert ALBANY for these nulls
d = d.replace(np.nan, 'ALBANY', regex=True)
d[['AREA NAME', 'COUNTY']][0:5]
# Divide the data up
p1 = d[['AREA NAME', 'COUNTY']][0:2]
p2 = d[['AREA NAME', 'COUNTY']][2:5]
# First 2 rows in p1, last 2 rows in p2, lets concatenate both rows
concatenated = pd.concat([p1,p2], keys = ['p1', 'p2'])
concatenated
# Using keys, concatenated data can be extracted back
concatenated.ix['p1']
