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

# 保存到文件
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
data = pd.read_csv('bankdebt.csv', index_col=0, header=None)
data.loc[data[1] == 'Yes', 1] = 1
data.loc[data[1] == 'No', 1] = 0
data.loc[data[4] == 'Yes', 4] = 1
data.loc[data[4] == 'No', 4] = 0
data.loc[data[2] == 'Single', 2] = 1
data.loc[data[2] == 'Married', 2] = 2
data.loc[data[2] == 'Divorced', 2] = 3
X = data.loc[:, 1:3]
y = data.loc[:, 4].astype(int)  # 一定要加上整型转换
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)
joblib.dump(clf, 'bankdebt.pkl')
load_clf = joblib.load('bankdebt.pkl')
print(load_clf.score(X, y))
