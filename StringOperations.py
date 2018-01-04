# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:20:05 2017

@author: nishant
"""

# String Operations
# Read in the first five rows of AREA NAME of Student Weight CSV
import pandas as pd
df = pd.read_csv('C:/Users/nishant/Desktop/FilesForPython/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv') 
df['AREA NAME'][0:5]
# Extract the first word from this column
df['AREA NAME'][0:5].str.extract('(\w+)')
# Extract the first and second word
df['AREA NAME'][0:5].str.extract('(\w+)\s(\w+)')
# Filter rows with data on ELEMENTARY schools
df[df['GRADE LEVEL']=='ELEMENTARY']
# Convert area name to upper case
df['AREA NAME'][0:5].str.upper()
# Now convert to lower case
df['AREA NAME'][0:5].str.lower()
# Find the length of each element in the column
df['AREA NAME'][0:5].str.len()
# Split AREA NAME based on a white space
df['AREA NAME'][0:5].str.split(' ')
# Replace all area names that have STATEWIDE to STATE
df['AREA NAME'][0:5].str.replace('STATEWIDE', 'STATE')
