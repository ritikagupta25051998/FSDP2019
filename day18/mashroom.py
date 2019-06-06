# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:51:48 2019

@author: HP WORLD
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset=pd.read_csv("mushrooms.csv")
features=dataset.iloc[:,[5,-2,-1]].values
labels=dataset.iloc[:,0].values

from sklearn.preprocessing import LabelEncoder
lc1 = LabelEncoder()
features[:, 0] = lc1.fit_transform(features[:,0])

lc2 = LabelEncoder()
features[:, 1] = lc2.fit_transform(features[:,1])

lc3 = LabelEncoder()
features[:, 2] = lc3.fit_transform(features[:,2])


from sklearn.preprocessing import OneHotEncoder
oe1 = OneHotEncoder(categorical_features = [-1])
features = oe1.fit_transform(features).toarray()

features=features[:,1:]

oe2 = OneHotEncoder(categorical_features = [-1])
features = oe2.fit_transform(features).toarray()
features=features[:,1:]

oe3 = OneHotEncoder(categorical_features = [-1])
features = oe3.fit_transform(features).toarray()
features=features[:,1:]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)


                      