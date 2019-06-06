# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:44:59 2019

@author: HP WORLD
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv("affairs.csv")

features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6,7])
features = onehotencoder.fit_transform(features).toarray()

features=features[:,1:]




from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)




# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

score=classifier.score(features_test,labels_test)

x = [3,25,3,1,5,16,4,2]
x = np.array(x)
regressor.predict(x.reshape(1, -1))






