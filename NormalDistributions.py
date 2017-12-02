# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:24:59 2017

@author: nishant
"""

'Inferential Statistics
'Lets apply Normal Distributions by importing some useful packages
from scipy.stats import binom
import matplotlib.pyplot as plt

'Lets plot a binomial distribution
'plt.subplots helps in generating multiple plots on a screen
'binom function takes in # of attempts and probability of success (the n and p variables)
'ax.vlines used to draw the vertical lines
'rv.pmf within it helps it in calculating probabilities for various values of x
'ax.legend adds legend to the graph, plt.show() displays the graph
'Must run all the code at once
fig, ax = plt.subplots(1,1)
x = [0, 1, 2, 3, 4, 5, 6]
n, p = 6, 0.5
rv = binom(n, p)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='Probablity')
ax.legend(loc='best', frameon=False)
plt.show()
'Graph shows that if coin was flipped 6 times, getting 3 heads has max prob.
'Getting 1 or 5 heads has least probability

'Lets increase # of attempts and see the distribution
fig, ax = plt.subplots(1,1)
x = range(101)
n, p = 100, 0.6
rv = binom(n, p)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='Probablity')
ax.legend(loc='best', frameon=False)
plt.show()
'You can play around with the value for the probability (change 0.5 to other values)