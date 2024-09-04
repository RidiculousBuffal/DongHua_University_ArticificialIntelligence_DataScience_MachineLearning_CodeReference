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
from sklearn import preprocessing
from sklearn import svm
import warnings
warnings.filterwarnings("ignore")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# ��ȡ�ļ�
data = pd.read_csv('bankpep.csv', index_col='id')
# ��YES��NO�滻��1,0;sex������ֵ�滻��1,0
seq = ['married', 'car', 'save_act', 'current_act', 'mortgage', 'pep']
for feature in seq :  # ������������滻
    data.loc[ data[feature] == 'YES', feature ] =1
    data.loc[ data[feature] == 'NO', feature ] =0

#���Ա�ת��Ϊ����1��0
data.loc[ data['sex'] == 'FEMALE', 'sex'] =1
data.loc[ data['sex'] == 'MALE', 'sex'] =0

#region ,children��ȡֵ��������,��Ҫ���ж��ȱ���
dumm_reg = pd.get_dummies(data['region'],prefix='region')
dumm_child =pd.get_dummies(data['children'],prefix='children')
#ɾ��ԭ������
df1 = data.drop(['region','children'],axis=1)
#ƴ��
df2 = df1.join([dumm_reg,dumm_child],how='outer')
#����0��1
#region ,children��ȡֵ��������,��Ҫ���ж��ȱ���
lis = ['region_INNER_CITY',
 'region_RURAL',
 'region_SUBURBAN',
 'region_TOWN',
 'children_0',
 'children_1',
 'children_2',
 'children_3']
for ls in lis:
    df2[ls]=df2[ls].astype(int)
print(df2.head())
#pep �Ƿ����ǩ��Ϊy,����ֵ��x
X = df2.drop(['pep'],axis=1)
y = df2['pep'].astype(int)
X_train,x_test,y_train,y_test = model_selection.train_test_split(X,y,test_size=0.3,random_state=1)
clf_tree = tree.DecisionTreeClassifier()
clf_tree.fit(X_train,y_train)#������ѵ��
print("������ѵ��������:",clf_tree.score(X_train,y_train))
print("���������Լ�����:",clf_tree.score(x_test,y_test))
predicted_y = clf_tree.predict(x_test)
print('��������������:')
print(metrics.classification_report(y_test,predicted_y))
clf_SVC = svm.SVC(kernel='rbf',gamma=0.4,C=1)
clf_SVC.fit(X_train,y_train)
print("SVMѵ��������:",clf_SVC.score(X_train,y_train))
print("SVM���Լ�����",clf_SVC.score(x_test,y_test))
predicted_y_SVM = clf_SVC.predict(x_test)
print('SVM��������:')
print(metrics.classification_report(y_test,predicted_y_SVM))
# ������ѵ��������: 1.0
# ���������Լ�����: 0.75
# ��������������:
#               precision    recall  f1-score   support
#            0       0.75      0.82      0.78        66
#            1       0.75      0.67      0.71        54
#     accuracy                           0.75       120
#    macro avg       0.75      0.74      0.74       120
# weighted avg       0.75      0.75      0.75       120
# SVMѵ��������: 1.0
# SVM���Լ����� 0.55
# SVM��������:
#               precision    recall  f1-score   support
#            0       0.55      1.00      0.71        66
#            1       0.00      0.00      0.00        54
#     accuracy                           0.55       120
#    macro avg       0.28      0.50      0.35       120
# weighted avg       0.30      0.55      0.39       120