# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:47:10 2019

@author: HP WORLD
"""

# Polynomial Regression
# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset=pd.read_csv("iq_size.csv")

features=dataset.iloc[:,1:].values
labels=dataset.iloc[:,0].values

plt.scatter(features, labels)
