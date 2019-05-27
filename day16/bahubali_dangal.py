# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:08:37 2019

@author: HP WORLD
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  

features_bahu = dataset.iloc[:, :1].values  
labels_bahu = dataset.iloc[:, 1].values 

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_bahu, labels_bahu)

x=[10]
x=np.array(x)
x=x.reshape(1,1)
y=regressor.predict(x)
print(y)

features_dan = dataset.iloc[:, :1].values  
labels_dan = dataset.iloc[:, 2].values 

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_dan, labels_dan)

z=regressor.predict(x)
print(z)
if y > z:
    print("bhahubali win")
else:
    print("dangal win" )




