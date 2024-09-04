import  scienceplots
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
import matplotlib
from sklearn.preprocessing import MinMaxScaler
from sklearn import model_selection
from sklearn import preprocessing
plt.style.use('science')
df = pd.read_csv('train.csv')
# OBJECT->FLOAT
df.loc[df['Drug'] == 'D-penicillamine', 'Drug'] = 1 #青霉胺明显更严重
df.loc[df['Drug'] == 'Placebo', 'Drug'] = 0
df.loc[df['Sex'] == 'F', 'Sex'] = 1
df.loc[df['Sex'] == 'M', 'Sex'] = 0
df.loc[df['Ascites'] == 'N', 'Ascites'] = 0
df.loc[df['Ascites'] == 'Y', 'Ascites'] = 1
df.loc[df['Hepatomegaly'] == 'N', 'Hepatomegaly'] = 0
df.loc[df['Hepatomegaly'] == 'Y', 'Hepatomegaly'] = 1
df.loc[df['Spiders'] == 'N', 'Spiders'] = 0
df.loc[df['Spiders'] == 'Y', 'Spiders'] = 1
df.loc[df['Edema'] == 'N', 'Edema'] = 0
df.loc[df['Edema'] == 'S', 'Edema'] = 1
df.loc[df['Edema'] == 'Y', 'Edema'] = 2
df['sign_merged'] = df['Ascites'] + df['Spiders'] + df['Edema']+df['Hepatomegaly']+df['Drug']
df.drop(['Ascites','Spiders','Edema','Hepatomegaly','Drug'], axis=1, inplace=True)
# 对AGE和N-days 进行处理
df['Age'] = df['Age']/365
df['N_Days'] = df['N_Days']/365
df.loc[df['Status']=='C','Status'] = 0
df.loc[df['Status']=='CL','Status']= 1
df.loc[df['Status']=='D','Status'] =  2
scaler = MinMaxScaler()
columns_to_fit = ['N_Days', 'Age', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper',
       'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin',]
df[columns_to_fit] = scaler.fit_transform(df[columns_to_fit])

fig = plt.figure(figsize = (10,8))
corr = df.corr()
sns.heatmap(corr,annot=True,cmap='rainbow',fmt='.2f')
plt.savefig('corr.svg')