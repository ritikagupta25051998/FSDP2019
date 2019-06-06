# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:42:07 2019

@author: HP WORLD
"""

import pandas as pd
import numpy as np
from apyori import apriori
import matplotlib.pyplot as plt

dataset=pd.read_csv("Market_Basket_Optimisation.csv",header=None)
list1=[]

for var in range(0,7501):
    list1.append([])