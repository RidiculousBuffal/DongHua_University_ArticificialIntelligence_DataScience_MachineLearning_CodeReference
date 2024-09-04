from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd

np.random.seed(1)
x = np.random.randint(0, 5, size=(6, 2))

y = np.array([0, 0, 0, 1, 1, 1])

data = pd.DataFrame(np.concatenate([x, y.reshape(-1, 1)], axis=1), columns=['x1', 'x2', 'y'])
print(data)
#    x1  x2  y
# 0   3   4  0
# 1   0   1  0
# 2   3   0  0
# 3   0   1  1
# 4   4   4  1
# 5   1   2  1
mnb = MultinomialNB()
mnb.fit(x, y)
print("样本数量:", mnb.class_count_)
print("特征数量:", mnb.feature_count_)
print("特征概率:", np.exp(mnb.feature_log_prob_))
# 样本数量: [3. 3.]
# 特征数量: [[6. 5.]
#  [5. 7.]]
# 特征概率: [[0.53846154 0.46153846]
#  [0.42857143 0.57142857]]