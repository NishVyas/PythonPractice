# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'Getting familiar with NumPy
import numpy as np
n_array = np.array([[0, 1, 2, 3],
 [4, 5, 6, 7],
 [8, 9, 10, 11]])
n_array.ndim
a = np.array( [11, 12, 13, 14])
b = np.array( [ 1, 2, 3, 4])
c=a-b
c
n_array[0,1]
n_array[0,0:3]
n_array[0,:]
n_array.ravel()
n_array.shape=(6,2)
n_array
n_array.transpose()

'Working with Pandas and Series
'Series are 1D arrays that hold any type of data
import pandas as pd
pd.Series(np.random.randn(5))
pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
d={'A':10,'B':20,'C':30}
pd.Series(d)

'Working with Dataframes here
'2D data structure w/ columns that can be of different data types
d = {'c1': pd.Series(['A', 'B', 'C']),
      'c2': pd.Series([1, 2., 3., 4.])}
df = pd.DataFrame(d)
df

d = {'c1': ['A', 'B', 'C', 'D'],
     'c2': [1, 2.0, 3.0, 4.0]}
df = pd.DataFrame(d)
print (df)

'Working with panels
'Panel is a data structure that handles 3D data
d = {'Item1': pd.DataFrame(np.random.randn(4, 3)),
     'Item2': pd.DataFrame(np.random.randn(4, 2))}
pd.Panel(d)
print (d)

