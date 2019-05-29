# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:13:44 2019

@author: HP WORLD
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("Female_Stats.csv")
features=dataset.iloc[:, 1:].values
labels=dataset.iloc[:, :1].values

import statsmodels.api as sm
features=sm.add_constant(features)

f1 = features[:,:]
regressor_OLS = sm.OLS(endog = labels, exog = f1).fit()
regressor_OLS.summary()
print("both are significant")

