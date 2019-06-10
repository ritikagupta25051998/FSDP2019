# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:28:45 2019

@author: HP WORLD
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("AB.csv")
we=df["make"].value_counts()
print(we.index[0:11])
print(we.values[0:11])
explode=(0.5,0,0,0,0,0,0,0,0,0,0)
plt.pie(we.values[0:11],explode=explode,labels=we.index[0:11], autopct='%2.2f%%')
plt.show()