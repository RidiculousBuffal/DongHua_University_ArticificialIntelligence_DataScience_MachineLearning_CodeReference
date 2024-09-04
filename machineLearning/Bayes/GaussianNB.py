import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB

np.random.seed(0)
x = np.random.randint(0, 10, size=(2, 6))
y = np.array([0, 0, 0, 1, 1, 1])
data = pd.DataFrame({
    'x1': x[0],
    'x2': x[1],
    'y': y[0]
}, columns=['x1', 'x2', 'y'])
print(data)

gnb = GaussianNB()
gnb.fit(x.T, y)
# 每个类别的先验概率:
print("概率:", gnb.class_prior_)
# 每个类别的样本数量
print("样本数量:", gnb.class_count_)
# 每个类别的样本标签
print("标签",gnb.classes_)
#每个特征在每个类别下的均值
print("均值",gnb.theta_)
#每个特征在每个类别下的方差
print("方差",gnb.var_) #以前是sigma现在更新为var

#测试集
x_test = np.array([[6,3]])
print("预测结果:",gnb.predict(x_test))
print("预测结果概率",gnb.predict_proba(x_test))
#
#    x1  x2  y
# 0   5   3  0
# 1   0   5  0
# 2   3   2  0
# 3   3   4  0
# 4   7   7  0
# 5   9   6  0
# 概率: [0.5 0.5]
# 样本数量: [3. 3.]
# 标签 [0 1]
# 均值 [[2.66666667 3.33333333]
#  [6.33333333 5.66666667]]
# 方差 [[4.22222223 1.55555556]
#  [6.22222223 1.55555556]]
# 预测结果: [0]
# 预测结果概率 [[0.75713243 0.24286757]]