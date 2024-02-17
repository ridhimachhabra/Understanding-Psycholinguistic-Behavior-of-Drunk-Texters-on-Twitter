# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:42:37 2020

@author: Ridhima
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as s
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import statsmodels.formula.api as smf
dataset = pd.read_csv(r"C:\Users\Ridhima\Desktop\Final Project\First paper\Project\datasets\merged_data.csv")
dataset.drop(dataset.columns[[0,3,5]],axis = 1,inplace = True);
dataset.shape
dataset.describe()
types = ('Q1','Q2','Q3')
df = pd.DataFrame(types,columns = ['Types'])
labelencoder = LabelEncoder();
df['Types_cat'] = labelencoder.fit_transform(df['Types'])
df

clean = {"Q1":     {1: "yes", 0: "no"},"Q2":{1:"yes",0:"no"},"Q3":{1:"yes",0:"no"}}
dataset.replace(clean, inplace = True)
dataset['Q1'].value_counts().plot(kind="barh")
dataset['Q2'].value_counts().plot(kind="barh")
dataset['Q3'].value_counts().plot(kind="barh")
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
lm = smf.ols('id ~ C(Q1)+C(Q2)+C(Q3)', data = dataset).fit()
lm.summary()




