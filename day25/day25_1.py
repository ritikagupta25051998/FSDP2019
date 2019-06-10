# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:08:50 2019

@author: HP WORLD
"""

import pandas as pd
import numpy as np

test=pd.read_csv("test.csv")
train=pd.read_csv("train.csv")

features_test=test.iloc[:,:-1].values
labels_test=test.iloc[:,-1].values

features_train=train.iloc[:,:-1].values
labels_train=train.iloc[:,-1].values
#####decision tree#####
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

from sklearn.metrics import confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  


print(accuracy_score(labels_test, labels_pred))

##random forest###

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))   
print(accuracy_score(labels_test, labels_pred))

####logistic regression###

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
from sklearn.metrics import confusion_matrix, accuracy_score

from sklearn.metrics import confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))   
print(accuracy_score(labels_test, labels_pred))

##KNN classification#######


# Fitting Logistic Regression to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


from sklearn.metrics import confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))   
print(accuracy_score(labels_test, labels_pred))

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features_train = labelencoder.fit_transform(features_train)
features_test = labelencoder.fit_transform(features_test)

features_train = features_train[:, 1:]
features_test = festures_test[:,1:]
import statsmodels.api as sm

features_train = sm.add_constant(features_train)
features_test=sm.add_constant(features_test)






