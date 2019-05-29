# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:44:59 2019

@author: HP WORLD
"""
# Polynomial Regression

# Importing the libraries

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Importing the dataset
dataset=pd.read_csv("bluegills.csv")

features=dataset.iloc[:,:1].values
labels=dataset.iloc[:,1].values

#let's first analyze the data
# Visualising the Linear Regression results
plt.scatter(features,labels)

from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)

# Fitting Linear Regression to the dataset

plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_1.predict(features), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('age')
plt.ylabel('length')
plt.show()



# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
features_poly = poly_object.fit_transform(features)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
x=np.arange(min(features),max(features),0.01).reshape(-1,1)

plt.scatter(features, labels, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_object.fit_transform(x)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('age')
plt.ylabel('length')
plt.show()




