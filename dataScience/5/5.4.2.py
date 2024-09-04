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
for feature in seq:  # 逐个特征进行替换
    data.loc[data[feature] == 'YES', feature] = 1
    data.loc[data[feature] == 'NO', feature] = 0

# 将性别转换为整数1和0
data.loc[data['sex'] == 'FEMALE', 'sex'] = 1
data.loc[data['sex'] == 'MALE', 'sex'] = 0

# region ,children的取值超过两种,需要进行独热编码
dumm_reg = pd.get_dummies(data['region'], prefix='region')
dumm_child = pd.get_dummies(data['children'], prefix='children')
# 删除原来两列
df1 = data.drop(['region', 'children'], axis=1)
# 拼接
df2 = df1.join([dumm_reg, dumm_child], how='outer')
# 换成0和1
# region ,children的取值超过两种,需要进行独热编码
lis = ['region_INNER_CITY',
       'region_RURAL',
       'region_SUBURBAN',
       'region_TOWN',
       'children_0',
       'children_1',
       'children_2',
       'children_3']
for ls in lis:
    df2[ls] = df2[ls].astype(int)
print(df2.head())
# pep 是分类标签作为y,其余值是x
X = df2.drop(['pep'], axis=1)
y = df2['pep'].astype(int)
sizes = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
for size in sizes:
    print('当gamma为',size,'时')
    X_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.35, random_state=1234)
    clf_SVC = svm.SVC(kernel='rbf', gamma=size, C=1000, probability=True)
    clf_SVC.fit(X_train, y_train)
    print("SVM训练集性能:", clf_SVC.score(X_train, y_train))
    print("SVM测试集性能", clf_SVC.score(x_test, y_test))
    predicted_y_SVM = clf_SVC.predict(x_test)
    print('SVM的误差报告是:')
    print(metrics.classification_report(y_test, predicted_y_SVM))
print('-------------------------------------------------')
X_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.35, random_state=1)

print('sigmoid')
clf_SVC = svm.SVC(kernel='sigmoid', gamma=0.6, C=1)
clf_SVC.fit(X_train, y_train)
print("SVM训练集性能:", clf_SVC.score(X_train, y_train))
print("SVM测试集性能", clf_SVC.score(x_test, y_test))
predicted_y_SVM = clf_SVC.predict(x_test)
print('SVM的误差报告是:')
print(metrics.classification_report(y_test, predicted_y_SVM))
print('linear')
clf_SVC = svm.SVC(kernel='linear', gamma=0.6, C=1)
clf_SVC.fit(X_train, y_train)
print("SVM训练集性能:", clf_SVC.score(X_train, y_train))
print("SVM测试集性能", clf_SVC.score(x_test, y_test))
predicted_y_SVM = clf_SVC.predict(x_test)
print('SVM的误差报告是:')
print(metrics.classification_report(y_test, predicted_y_SVM))
# 当gamma为 0.1 时
# SVM训练集性能: 1.0
# SVM测试集性能 0.5111111111111111
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.51      1.00      0.68        92
#            1       0.00      0.00      0.00        88
#     accuracy                           0.51       180
#    macro avg       0.26      0.50      0.34       180
# weighted avg       0.26      0.51      0.35       180
# 当gamma为 0.2 时
# SVM训练集性能: 1.0
# SVM测试集性能 0.5111111111111111
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.51      1.00      0.68        92
#            1       0.00      0.00      0.00        88
#     accuracy                           0.51       180
#    macro avg       0.26      0.50      0.34       180
# weighted avg       0.26      0.51      0.35       180
# 当gamma为 0.3 时
# SVM训练集性能: 1.0
# SVM测试集性能 0.5111111111111111
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.51      1.00      0.68        92
#            1       0.00      0.00      0.00        88
#     accuracy                           0.51       180
#    macro avg       0.26      0.50      0.34       180
# weighted avg       0.26      0.51      0.35       180
# 当gamma为 0.4 时
# SVM训练集性能: 1.0
# SVM测试集性能 0.5111111111111111
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.51      1.00      0.68        92
#            1       0.00      0.00      0.00        88
#     accuracy                           0.51       180
#    macro avg       0.26      0.50      0.34       180
# weighted avg       0.26      0.51      0.35       180
# 当gamma为 0.5 时
# SVM训练集性能: 1.0
# SVM测试集性能 0.5111111111111111
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.51      1.00      0.68        92
#            1       0.00      0.00      0.00        88
#     accuracy                           0.51       180
#    macro avg       0.26      0.50      0.34       180
# weighted avg       0.26      0.51      0.35       180
# 当gamma为 0.6 时
# SVM训练集性能: 1.0
# SVM测试集性能 0.5111111111111111
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.51      1.00      0.68        92
#            1       0.00      0.00      0.00        88
#     accuracy                           0.51       180
#    macro avg       0.26      0.50      0.34       180
# weighted avg       0.26      0.51      0.35       180
# 当gamma为 0.7 时
# SVM训练集性能: 1.0
# SVM测试集性能 0.5111111111111111
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.51      1.00      0.68        92
#            1       0.00      0.00      0.00        88
#     accuracy                           0.51       180
#    macro avg       0.26      0.50      0.34       180
# weighted avg       0.26      0.51      0.35       180
# 当gamma为 0.8 时
# SVM训练集性能: 1.0
# SVM测试集性能 0.5111111111111111
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.51      1.00      0.68        92
#            1       0.00      0.00      0.00        88
#     accuracy                           0.51       180
#    macro avg       0.26      0.50      0.34       180
# weighted avg       0.26      0.51      0.35       180
# -------------------------------------------------
# sigmoid
# SVM训练集性能: 0.5380952380952381
# SVM测试集性能 0.5555555555555556
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.56      1.00      0.71       100
#            1       0.00      0.00      0.00        80
#     accuracy                           0.56       180
#    macro avg       0.28      0.50      0.36       180
# weighted avg       0.31      0.56      0.40       180
# linear
# SVM训练集性能: 0.638095238095238
# SVM测试集性能 0.6611111111111111
# SVM的误差报告是:
#               precision    recall  f1-score   support
#            0       0.71      0.66      0.68       100
#            1       0.61      0.66      0.63        80
#     accuracy                           0.66       180
#    macro avg       0.66      0.66      0.66       180
# weighted avg       0.67      0.66      0.66       180
