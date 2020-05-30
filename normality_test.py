# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:08:17 2020

@author: JGY
"""

import pandas as pd
import numpy as np
from scipy import stats
from pylab import *
#times= pd.read_csv('AlgorithmData.csv')
data= pd.read_csv('results.csv')
nation_a = data.Ave_result[data.Sex == 'M']
nation_b = data.Ave_result[data.Sex == 'F']
#nation_c = data.Ave_result[data.Nationality == 'C']

#times.info()
w, pvalue = stats.shapiro(nation_a)
print(w)
print(pvalue)



#the following comment is the result for assginment part three
#three independent datasets are Sex, Nationality and Ave_resulte
'''
1. the relationship between A and Ave_result
0.9948113560676575
p=0.8293322920799255>0.05 it is normality distribution
2. the relationship between B and Ave_result
0.9902130961418152
p=0.30620861053466797>0.05 it is normality distribution
3. the relationship between C and Ave_result
0.9902130961418152
p=0.30620861053466797>0.05 it is normality distribution

'''

#the following comment is the result for assginment part one
#two independent datasets are Sex and Ave_result
'''
the relationship between Sex(male) and Ave_result
0.9908305406570435
p=0.1460186392068863>0.05 it is normality distribution
the relationship between Sex(female) and Ave_result
0.991585910320282
p=0.13437996804714203>0.05 it is normality distribution

'''


#the following comment is the result for assignment part two
#two dependent datasets are average of t1 and t2, and average of t3 and t4
'''
mean of result T1 and T2
0.9932543039321899
p=0.024431906640529633<0.05 it is not normality
mean of result T3 and T4
0.983135998249054
p=1.5073329450387973e-05<0.05 it is not normality

'''


'''
A
0.8352423906326294
3.506665402497333e-09
B
0.9261152148246765
3.0161923859850504e-05
C
0.9839826226234436
0.2676215171813965

'''
#ANOVA
'''
fvalue, pvalue = stats.f_oneway(times.A, times.B, times.C)
print(fvalue)
print(pvalue)

0.7742858651953499
p=0.46196124653736703
'''
#Kruskal-Wallis
'''
h, pvalue = stats.kruskal(times.A, times.B, times.C)
print(h)
print(pvalue)

10.295957105291746
p=0.005811139775077802
'''


'''
to calculate median, standard deviation and 
c_ave.median()
c_ave.sem()
c_ave.std()
'''