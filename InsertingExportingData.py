# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:20:18 2017

@author: nishant
"""

'Reading in CSV files and displaying AREA NAME for 1st 5 rows
import pandas as pd
d = pd.read_csv('C:/Users/nishant/Desktop/FilesForPython/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv')
d[0:5]['AREA NAME']

'Writing to a CSV file
d = {'c1': pd.Series(['A', 'B', 'C']),
     'c2': pd.Series([1, 2., 3., 4.])}
df = pd.DataFrame(d)
df
'Automatically makes a csv file in the path with contents already in it
df.to_csv('C:/Users/nishant/Desktop/FilesForPython/sample_data.csv')

'Opening a JSON file
import json
json_data = open('C:/Users/nishant/Desktop/FilesForPython/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.json')
data = json.load(json_data)
'Next line prints out all the json
data
json.close()

