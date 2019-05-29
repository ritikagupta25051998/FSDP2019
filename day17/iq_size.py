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

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)

Pred = regressor.predict(features_test)

import pandas as pd
import numpy as np
print (pd.DataFrame(Pred, labels_test))

x = [90,70,150]
x = np.array(x)
regressor.predict(x.reshape(1, -1))

#by back elimination
import statsmodels.api as sm
features = sm.add_constant(features)


features_opt = features[:, [0, 1, 2, 3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:, [1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()



features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

regressor_OLS.predict(90)






