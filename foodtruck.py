# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:33:56 2019

@author: HP WORLD
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
dataset = pd.read_csv('Foodtruck.csv')  
dataset.plot(x='Population', y='Profit',style='o')  
plt.title('Population vs Profit')  
plt.xlabel('Population')  
plt.ylabel('Profit')  
plt.show()
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values   



from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels)

x=[3.073]
x=np.array(x)
x=x.reshape(1,1)
print (regressor.predict(x))
 




