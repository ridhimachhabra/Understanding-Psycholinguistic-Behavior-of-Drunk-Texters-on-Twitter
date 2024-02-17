# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot

dataset=pd.read_csv("full_text.txt", delimiter="\t",encoding='latin-1')

dataset.to_csv('geotagged_data.csv',encoding='utf-8',index='false')

df=pd.read_csv("geotagged_data.csv")
df.columns=['index','User_id','date-time','coordinates', 'longitude', 'latitude', 'Post' ]
del(df['index'])
df.shape
## removing null value
df.isnull().sum()

df[df['Post'].isnull()].index.tolist()
df=df.dropna(how='any',axis=0)

df.shape

import re

y=df.iloc[:,-1]    #converted to series form as default
type(y)
y_list=y.tolist()
type(y_list)


li=[]
l=len(y_list)
def filterData(data):
    count=0
    regexps = [
    re.compile(r'drunk|shit|beer|alcohol|vodka|drink|wine|tequila|hangover|drinking|hammered|take shot|get wasted|champagne|booze|ciroc|rum|whiskey', re.IGNORECASE)
    ]
    for res in regexps:
        for i in range(0,l):
            match = res.search(data[i])
            
            if match:
                count=count+1;
                li.append('1')
            else:
                li.append('0')
    print(count)
filterData(y_list)

## sampling 50000 rows
y_sample=df.iloc[:50000,-1]
y_sample=y_sample.to_frame()
y_sample.insert(1,"Keyword",li)
y_sample.to_csv(r'C:\Users\Ridhima\Desktop\Final Project\y_sample.csv')

#for full data set:
dataset=df.iloc[:,-1]
dataset=dataset.to_frame()
dataset.insert(1,"Keyword",li)
dataset.to_csv(r'C:\Users\Ridhima\Desktop\Final Project\dataset.csv')

#reading dataset from mechanical turk 
q1= pd.read_csv(r"C:\Users\Ridhima\Desktop\Final Project\q1.csv");
q2= pd.read_csv(r"C:\Users\Ridhima\Desktop\Final Project\q2.csv");
q3= pd.read_csv(r"C:\Users\Ridhima\Desktop\Final Project\q3.csv");

merged_data_q1 = pd.merge(q2,q3); 
merged_data = pd.merge(q1,merged_data_q1);
merged_data = pd.read_csv(r"C:\Users\Ridhima\Desktop\Final Project\merged_data.csv");
df = pd.DataFrame(merged_data);
df.drop(df.columns[[0,3,5]],axis = 1,inplace = True);

