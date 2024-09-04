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
from sklearn import metrics
# 延续回归模型的性能评估，计算使用全部数据学习得到的回归模型linreg在测试集上的性能，与只使用训练集的模型linregTr进行比较，并对结果进行分析。
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
data = pd.read_csv('advertising.csv', index_col=0, encoding='gbk') #第一列是索引列不能放上去

# 模型lingreg
x = data.iloc[:, 0:3].values.astype(float)
y = data.iloc[:, 3].values.astype(float)
linreg = LinearRegression()
linreg.fit(x, y)
print('linreg的截距是:', linreg.intercept_, "系数是:", linreg.coef_)

# 模型linregTr
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.35, random_state=1)
linregTr = LinearRegression()
linregTr.fit(x_train, y_train)
print('linregTr的截距是:', linregTr.intercept_, "系数是:", linregTr.coef_)

# 两个测试集永远是x_test,y_test 要对同一个测试集评估性能
# 对linregTr进行预测
y_test_pred_1 = linregTr.predict(x_test)
test_err1 = metrics.mean_squared_error(y_test, y_test_pred_1)
print('linregTr的均方误差是：', test_err1)
predict_score1 = linregTr.score(x_test, y_test)
print('置信系数是:', predict_score1)

# 对linreg进行预测
y_test_pred_2 = linreg.predict(x_test)
test_err2 = metrics.mean_squared_error(y_test, y_test_pred_2)
print('linreg的均方误差是：', test_err2)
predict_score2 = linreg.score(x_test, y_test)
print('置信系数是:', predict_score2)

#
# linreg的截距是: 2.9388893694594085 系数是: [ 0.04576465  0.18853002 -0.00103749]
# linregTr的截距是: 2.9324713466040855 系数是: [0.04608839 0.18047646 0.00411699]
# linregTr的均方误差是： 2.3151369587841586
# 置信系数是: 0.912537299857749
# linreg的均方误差是： 2.2307415325257622
# 置信系数是: 0.9157256433517305

# 使用全部数据集训练得到的误差更小,置信系数更高

