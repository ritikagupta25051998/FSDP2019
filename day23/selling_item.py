# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:38:13 2019

@author: HP WORLD
"""

import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv("BreadBasket_DMS.csv")

dataset["Item"]=dataset["Item"].replace("NONE",np.nan)
dataset=dataset.dropna()
count=dataset["Item"].value_counts()
data=count.head(15)

plt.pie(data,labels=data.index,autopct="%1.2f")
plt.show()
d=dataset.groupby("Transaction")["Item"]
T=list(d.apply(lambda x : list(set(x))))
rules =list(apriori(T, min_support = 0.0025, min_confidence = 0.2, min_lift = 3))



