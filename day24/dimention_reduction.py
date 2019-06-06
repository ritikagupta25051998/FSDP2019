# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:55:27 2019

@author: HP WORLD
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("crime_data.csv") 

features=dataset.iloc[:,[1,2,4]]


from sklearn.model_selection import train_test_split
features_train, features_test= train_test_split(features, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_
