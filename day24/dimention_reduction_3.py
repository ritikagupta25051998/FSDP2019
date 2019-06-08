# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:26:03 2019

@author: HP WORLD
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset=pd.read_csv("data.csv")
series= dataset['Country'].value_counts()

plt.pie(series.values,explode=None,labels=series.index,radius=1)
plt.show



