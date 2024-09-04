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

# �����ó�100���������ó�200������ѧϰ�õ��Ļع�ģ��,��������

data = pd.read_csv('advertising.csv', index_col=0)
x_100 = data.iloc[:100, 0:3]  # �Ա���
y_100 = data.iloc[:100, 3]  # �����
x_200 = data.iloc[:200, 0:3]
y_200 = data.iloc[:200, 3]
X = data.iloc[:, 0:3]
y = data.iloc[:, 3]
linreg_100 = LinearRegression()
linreg_200 = LinearRegression()
linreg_100.fit(x_100, y_100)
linreg_200.fit(x_200, y_200)
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.35, random_state=1)
# Ҫ��ͬһ���Լ��Ͻ��в���
y_test_pred_100 = linreg_100.predict(x_test)
y_test_pred_200 = linreg_200.predict(x_test)
test_err_100 = metrics.mean_squared_error(y_test, y_test_pred_100)
test_err_200 = metrics.mean_squared_error(y_test, y_test_pred_200)
print('100�����ķ����������', test_err_100)
print('200�����ķ����������', test_err_200)
predict_score_100 = linreg_100.score(x_test, y_test)
predict_score_200 = linreg_200.score(x_test, y_test)
print('100����������ϵ����:',predict_score_100)
print('200����������ϵ����:',predict_score_200)


# 100�����ķ���������� 2.2394422037366577
# 200�����ķ���������� 2.2307415325257622
# 100����������ϵ����: 0.9153969439224083
# 200����������ϵ����: 0.9157256433517305
# ��𲻴�,200Ҫ��һ��