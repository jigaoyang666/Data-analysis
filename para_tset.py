# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:42:38 2020

@author: JGY
"""


import pandas as pd
import numpy as np
from scipy import stats
from pylab import *
#times= pd.read_csv('AlgorithmData.csv')
data= pd.read_csv('results.csv')

'''
result_male = data.Ave_result[data.Sex=='M']
result_female = data.Ave_result[data.Sex=='F']
tstats, pvalue = stats.ttest_ind(result_male, result_female)
print(tstats)
print(pvalue)

#t=0.7478401328463943
#p=0.4549095817022496
'''

'''
result_t12= data.Ave_result_T12
result_t34 = data.Ave_result_T34
u, pvalue = stats.mannwhitneyu(result_t12, result_t34)
print(u)
print(pvalue)

u=69643.5
p=3.951613212160763e-34
'''
nation_a = data.Ave_result[data.Nationality =='A']
nation_b = data.Ave_result[data.Nationality =='B']
nation_c = data.Ave_result[data.Nationality =='C']
tstats, pvalue = stats.ttest_ind(nation_b,nation_c)
print(tstats)
print(pvalue)