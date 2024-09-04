# -*- coding: gb2312 -*-
from typing import Any
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
import matplotlib
import joblib
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
from sklearn.tree._export import export_text
from sklearn import metrics
from sklearn import tree
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# �����ݼ����ֳ�ѵ�����Ͳ��Լ�
data = pd.read_csv('bankdebt.csv', index_col=0, header=None)
# ת��Ϊ����
data.loc[data[1] == 'Yes',1]=1
data.loc[data[1]=='No',1]=0
data.loc[data[4]=='Yes',4]=1
data.loc[data[4]=='No',4]=0
data.loc[data[2]=='Single',2]=1
data.loc[data[2]=='Married',2]=2
data.loc[data[2]=='Divorced',2]=3

X = data.iloc[:,0:3]
Y = data.iloc[:,3]
x_train,x_test,y_train,y_test = model_selection.train_test_split(X,Y,test_size=0.3,random_state=1) #30%��Ϊ���Լ�
clf  = tree.DecisionTreeClassifier()
clf = clf.fit(x_train,y_train.astype(int))
# �����������accuracy
print(clf.score(x_train,y_train.astype(int)))
# 1.0
predicted_y = clf.predict(x_test)
print(metrics.classification_report(y_test.astype(int),predicted_y.astype(int)))
print('Confusion Matrix')
print(metrics.confusion_matrix(y_test.astype(int),predicted_y.astype(int)))


# 1.0
# precision recall f1-score support
# 0 1.00 0.67 0.80 3
# 1 0.67 1.00 0.80 2
# accuracy 0.80 5
# macro avg 0.83 0.83 0.80 5
# weighted avg 0.87 0.80 0.80 5
# Confusion Matrix
# [[2 1]
# [0 2]]

#    - ��׼ȷ��Ϊ0.80����ʾ�����������������ϵ�Ԥ��׼ȷ��Ϊ80%��
#    - ��ƽ����ȷ�ȡ��ٻ��ʺ�F1������Ϊ0.83����ʾ�������������϶���������ǩ��Ԥ��������ԽϺá�
# ����������ǩ��Ԥ��������ԽϺã��������ڱ�ǩ0���ٻ�������һЩ�Ľ��Ŀռ䡣