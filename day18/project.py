# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:31:03 2019

@author: HP WORLD
"""

import pandas as pd 
import numpy as np

dataset1=pd.read_csv("train.csv")
dataset2=pd.read_csv("test.csv")

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])