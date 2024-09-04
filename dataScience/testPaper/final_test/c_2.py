import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import tree
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import joblib

# 设置显示的最大列数
pd.set_option('display.max_columns', None)  # None 表示不限制列数
# 设置单元格的显示宽度
pd.set_option('display.max_colwidth', None)  # None 表示不限制宽度
df = pd.read_excel('ENB2012_data.xlsx', skiprows=1, names=['Relative Compactness',
                                                           'Surface Area ',
                                                           'Wall Area ',
                                                           'Roof Area ',
                                                           'Overall Height',
                                                           'Orientation ',
                                                           'Glazing Area ',
                                                           'Glazing Area Distribution',
                                                           'Heating Load ',
                                                           'Cooling Load'])
# 统计各列数据的均值和方差，以及中位数。
print('平均值:\n', df.mean(), '\n 方差:\n', df.std(), '\n 中位数:\n', df.median())
# 在一张图中分别绘制Surface Area列与Heating Load以及Cooling Load两张散点子图。
# 数据处理
df.dropna(inplace=True, how='any')
fig: plt.Figure = plt.figure(figsize=(10, 8))
ax: plt.Axes = fig.add_subplot(1, 1, 1)
Surface_Area = df['Surface Area ']
Heating_Load = df['Heating Load ']
Cooling_Load = df['Cooling Load']
ax.scatter(x=Surface_Area, y=Heating_Load, color='red', alpha=0.2, marker='*')
ax.scatter(x=Surface_Area, y=Cooling_Load, color='blue', alpha=0.2)
ax.set_title("Surface Area and Heating Load,Cooling Load")
ax.legend(['heat', 'cool'])
plt.tight_layout()
plt.show()
# 将数据分割为训练集和测试集，在训练集上训练heating的回归模型，输出模型参数，分别计算模型在训练集和测试集上的均方误差和决定系数。
X = df.drop(['Heating Load ', 'Cooling Load'], axis=1)
y = df['Heating Load ']
X_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)
lingreg = LinearRegression()
lingreg.fit(X_train, y_train)
print('intercept_:', lingreg.intercept_, 'coef_:', lingreg.coef_)
y_test_pred = lingreg.predict(x_test)
y_train_pred = lingreg.predict(X_train)
print('在训练集上的均方误差:', metrics.mean_squared_error(y_train, y_train_pred))
print('在测试集上的均方误差:', metrics.mean_squared_error(y_test, y_test_pred))
print('在测试集上的决定系数:', lingreg.score(x_test, y_test_pred))
print('在训练集上的决定系数', lingreg.score(X_train, y_train_pred))
