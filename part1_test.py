# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:39:14 2020

@author: JGY
"""

import pandas as pd
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from scipy import stats
data = pd.read_csv('results.csv')
#data.info()
#data[data.Sex == 'M']

grade_male = data.T1_result[data.Sex =='M']
grade_female = data.T1_result[data.Sex =='F']
#grade_male = data[data.Sex == 'M'].
bp = boxplot([grade_male, grade_female], labels=['Male', 'Femal'])
plt.ylabel("Score")
plt.xlabel("Gender")
plt.title("Average score of male and female")
scatter(x, y)
#print(grade_female)

