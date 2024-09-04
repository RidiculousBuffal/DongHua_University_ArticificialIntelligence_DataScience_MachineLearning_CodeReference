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
# 读取文件
data = pd.read_csv('bankpep.csv', index_col='id')
# 将YES和NO替换成1,0;sex的特征值替换成1,0
seq = ['married', 'car', 'save_act', 'current_act', 'mortgage', 'pep']
for feature in seq :  # 逐个特征进行替换
    data.loc[ data[feature] == 'YES', feature ] =1
    data.loc[ data[feature] == 'NO', feature ] =0

#将性别转换为整数1和0
data.loc[ data['sex'] == 'FEMALE', 'sex'] =1
data.loc[ data['sex'] == 'MALE', 'sex'] =0

#region ,children的取值超过两种,需要进行独热编码
dumm_reg = pd.get_dummies(data['region'],prefix='region')
dumm_child =pd.get_dummies(data['children'],prefix='children')
#删除原来两列
df1 = data.drop(['region','children'],axis=1)
#拼接
df2 = df1.join([dumm_reg,dumm_child],how='outer')
#换成0和1
#region ,children的取值超过两种,需要进行独热编码
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
#pep 是分类标签作为y,其余值是x
X = df2.drop(['pep'],axis=1)
y = df2['pep'].astype(int)
X_train,x_test,y_train,y_test = model_selection.train_test_split(X,y,test_size=0.3,random_state=1)
clf_tree = tree.DecisionTreeClassifier()
clf_tree.fit(X_train,y_train)#决策树训练
print("决策树训练集性能:",clf_tree.score(X_train,y_train))
print("决策树测试集性能:",clf_tree.score(x_test,y_test))
predicted_y = clf_tree.predict(x_test)
print('决策树的误差报告是:')
print(metrics.classification_report(y_test,predicted_y))
clf_SVC = svm.SVC(kernel='rbf',gamma=0.4,C=1)
clf_SVC.fit(X_train,y_train)
print("SVM训练集性能:",clf_SVC.score(X_train,y_train))
print("SVM测试集性能",clf_SVC.score(x_test,y_test))
predicted_y_SVM = clf_SVC.predict(x_test)
print('SVM的误差报告是:')
print(metrics.classification_report(y_test,predicted_y_SVM))
# 决策树训练集性能: 1.0
# 决策树测试集性能: 0.75
# 决策树的误差报告是:
#               precision    recall  f1-score   support
#            0       0.75      0.82      0.78        66
#            1       0.75      0.67      0.71        54
#     accuracy                           0.75       120
#    macro avg       0.75      0.74      0.74       120
# weighted avg       0.75      0.75      0.75       120
# SVM训练集性能: 1.0
# SVM测试集性能 0.55
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.55      1.00      0.71        66
#            1       0.00      0.00      0.00        54
#     accuracy                           0.55       120
#    macro avg       0.28      0.50      0.35       120
# weighted avg       0.30      0.55      0.39       120