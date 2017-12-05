# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 23:44:53 2017

@author: nishant
"""

'Poisson Distribution
'# of cars that pass through a bridge in an hour is 20
'Probability the 23 pass through that bridge in an hour?

'Import the right packages
from scipy import stats
from scipy.stats import poisson
rv = poisson(20)
rv.pmf(23)
'We defined the mean value with 20 cars
'rv.pmf gives probability (around 6%) that 23 cars will cross bridge

'Z-score: score that expresses value of a distribution in standard deviation w.r.t a mean
'Example: Classroom has 60 students, got their math scores
'Lets simulate score of 60 students with normal dist.
import numpy as np
classScore = np.random.normal(50, 10, 60).round()
classScore
'NumPy has a random module with normal function
'We pick the mean to be 50, std. dev. is 10, and we generate 60 observations
'Lets plot the normal dist.
plt.hist(classcore, 30, normed=True)
'Now lets convert each students score to a z-score
stats.zscore(classScore)
'We can say a student with a score of 54/100 has a z-score of 0.538
'So whats the probability above 54?
'Could use standard normal table, but we have python (and the cdf function)
prob = 1 - stats.norm.cdf(0.538)
prob
'So there is a 29.5% probability of getting marks above 54

'How many students made it to the top 20% of the class?
'To get z-score in which the top 20% marks we use ppf function
stats.norm.ppf(0.8)
(0.84*classScore.std())+classScore.mean()
'We multiply the result of getting the z-score for top 20% of the class by the std.dev.
'Add this valus by the standard mean 
'This converts the z-score to a value in the distribution
'So students who have marks more than 57.22 are in the top 20% of the class