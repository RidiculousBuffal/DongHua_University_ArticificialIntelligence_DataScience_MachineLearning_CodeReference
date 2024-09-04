from sklearn.naive_bayes import BernoulliNB
from sklearn.preprocessing import Binarizer

import numpy as np
import pandas as pd

np.random.seed(1)
x = np.random.randint(-5, 5, size=(6, 2))
# 对x进行二值化
X_binary = Binarizer(threshold=0.0).transform(x)
print(X_binary)
y = np.array([0, 0, 0, 1, 1, 1])

data = pd.DataFrame(np.concatenate([X_binary, y.reshape(-1, 1)], axis=1), columns=['x1', 'x2', 'y'])
print(data)

#    x1  x2  y
# 0   0   1  0
# 1   1   0  0
# 2   0   0  0
# 3   0   1  1
# 4   1   1  1
# 5   0   0  1

bnb = BernoulliNB()
bnb.fit(X_binary, y)
print("出现1的次数:", bnb.feature_count_)
# 出现1的次数: [[1. 1.]
#  [1. 2.]]
# y=0的样本中x1有1个1,x2有1个1,所以输出的第一行为[1,1]
# y=1的样本中x1有1个1,x2有2个1,所以输出的第二行为[1,2]


# 类别占比p(y)
print("类别占比p(y):", np.exp(bnb.class_log_prior_))
# 特征概率,每个类别下,每个特征值为1的概率:
print("特征概率:", np.exp(bnb.feature_log_prob_))

x_test = np.array([[1, 0]])  # 测试数据
y_pred = bnb.predict(x_test) #进行预测
print(y)
