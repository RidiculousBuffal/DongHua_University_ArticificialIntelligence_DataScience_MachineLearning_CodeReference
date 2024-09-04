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
# �����ع�ģ�͵���������������ʹ��ȫ������ѧϰ�õ��Ļع�ģ��linreg�ڲ��Լ��ϵ����ܣ���ֻʹ��ѵ������ģ��linregTr���бȽϣ����Խ�����з�����
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
data = pd.read_csv('advertising.csv', index_col=0, encoding='gbk') #��һ���������в��ܷ���ȥ

# ģ��lingreg
x = data.iloc[:, 0:3].values.astype(float)
y = data.iloc[:, 3].values.astype(float)
linreg = LinearRegression()
linreg.fit(x, y)
print('linreg�Ľؾ���:', linreg.intercept_, "ϵ����:", linreg.coef_)

# ģ��linregTr
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.35, random_state=1)
linregTr = LinearRegression()
linregTr.fit(x_train, y_train)
print('linregTr�Ľؾ���:', linregTr.intercept_, "ϵ����:", linregTr.coef_)

# �������Լ���Զ��x_test,y_test Ҫ��ͬһ�����Լ���������
# ��linregTr����Ԥ��
y_test_pred_1 = linregTr.predict(x_test)
test_err1 = metrics.mean_squared_error(y_test, y_test_pred_1)
print('linregTr�ľ�������ǣ�', test_err1)
predict_score1 = linregTr.score(x_test, y_test)
print('����ϵ����:', predict_score1)

# ��linreg����Ԥ��
y_test_pred_2 = linreg.predict(x_test)
test_err2 = metrics.mean_squared_error(y_test, y_test_pred_2)
print('linreg�ľ�������ǣ�', test_err2)
predict_score2 = linreg.score(x_test, y_test)
print('����ϵ����:', predict_score2)

#
# linreg�Ľؾ���: 2.9388893694594085 ϵ����: [ 0.04576465  0.18853002 -0.00103749]
# linregTr�Ľؾ���: 2.9324713466040855 ϵ����: [0.04608839 0.18047646 0.00411699]
# linregTr�ľ�������ǣ� 2.3151369587841586
# ����ϵ����: 0.912537299857749
# linreg�ľ�������ǣ� 2.2307415325257622
# ����ϵ����: 0.9157256433517305

# ʹ��ȫ�����ݼ�ѵ���õ�������С,����ϵ������

