# -*- coding: utf-8 -*-
"""gradiant.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-eZLBtULGuM9hZY3wz7LnwjeKGmeCx79
"""

from google.colab import files


uploaded = files.upload()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mt

df=pd.read_csv("Churn_Modelling (3).csv")

df.columns

df.head(10)

df.describe

df.info

df.shape

df.size

x=df.drop(['Geography','Gender','Surname','Exited'],axis=1)

x

y=df['Exited']

y

sns.countplot(x=y)

#feature scaling
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

x_scale=scaler.fit_transform(x)

x_scale

#cross validation
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scale,y,test_size=0.9,random_state=9)

x_train.shape

x_scale.shape

x_test.shape

from sklearn.neural_network import MLPClassifier
neural=MLPClassifier(hidden_layer_sizes=(100,100,100),max_iter=100,activation="relu",random_state=9)

neural.fit(x_train,y_train)

y_pred=neural.predict(x_test)

y_pred

from sklearn.metrics import ConfusionMatrixDisplay,accuracy_score,classification_report

ConfusionMatrixDisplay.from_predictions(y_test,y_pred)

accuracy_score (y_test,y_pred)

print(classification_report(y_test,y_pred))

!pip install imbalanced-learn

from imblearn.over_sampling import RandomOverSampler
ros=RandomOverSampler(random_state=0)
x_balance,y_balance=ros.fit_resample(x,y)

sns.countplot(x=y_balance)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_scale=scaler.fit_transform(x_balance)

x_scale

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scale,y_balance,test_size=0.3,random_state=0)

x_train.shape

x_test.shape

x_scale.shape

from sklearn.neural_network import MLPClassifier
neural=MLPClassifier(hidden_layer_sizes=(100,100,100),max_iter=100,activation="relu",random_state=0)

neural.fit(x_train,y_train)

y_pred=neural.predict(x_test)

y_pred

from sklearn.metrics import ConfusionMatrixDisplay,accuracy_score,classification_report

ConfusionMatrixDisplay.from_predictions(y_test,y_pred)

accuracy_score (y_test,y_pred)