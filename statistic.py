# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:48:40 2020

@author: JGY
"""

import pandas as pd
import numpy as np
from scipy import stats
from pylab import *
import matplotlib.pyplot as plt

#times= pd.read_csv('AlgorithmData.csv')
data= pd.read_csv('results.csv')

'''
r_male = data.Ave_result[data.Sex=='M']
r_female = data.Ave_result[data.Sex=='F']


desc_stats = list( map(stats.describe, [r_male,r_female]) )
means = [ x.mean for x in desc_stats ]
print(means)
mean=61.70
std=11.31
interval=stats.norm.interval(0.95,mean,std)
print(interval)
'''

'''
result_t12 = data.Ave_result_T12
result_t34 = data.Ave_result_T34
desc_stats = list( map(stats.describe, [result_t12,result_t34]) )
means = [ x.mean for x in desc_stats ]
print(means)
'''

nation_a = data.Ave_result[data.Nationality =='A']
nation_b = data.Ave_result[data.Nationality =='B']
nation_c = data.Ave_result[data.Nationality =='C']
desc_stats = list( map(stats.describe, [nation_a,nation_b,nation_c]) )
means = [ x.mean for x in desc_stats ]
print(means)