import pandas as pd
import numpy as np
from collections import Counter


def predict(X_test_: np.ndarray, conditional_p: dict, y_p: dict) -> list:
    print("开始预测:")
    ret_ = list()
    for i in range(len(X_test_)):
        max_ = -100
        winner = [()]
        for key, value in y_p.items():
            mul = 1
            for item in X_test_[i]:
                mul *= conditional_p[(key, item)]
            mul = mul * value
            print("在分类标签为", key, "时的概率为", mul)
            if mul > max_:
                max_ = mul
                winner = (key, mul)
        ret_.append(winner)
    return ret_


def fit(X: np.ndarray, y: np.ndarray, smooth: int) -> (dict, dict):
    if smooth == 1:
        print("当前使用拉普拉斯平滑")
    else:
        print("当前使用普通极大似然估计")
    _ret = dict()
    # print(y.T[0])
    # print(Counter(X.T[0][y.T[0] == -1]))
    # print(len(X.T))
    _y_counts = dict(Counter(y.T[0]))  # 记录y的不同值以及个数
    print(_y_counts)
    # 创建条件概率映射
    for key in _y_counts.keys():
        for i in range(len(X.T)):
            X_i_counts = dict(Counter(X.T[i][y.T[0] == key]))
            Len_Of_Current_X = len(np.unique(X.T[i].tolist()))
            for _key, _value in X_i_counts.items():
                print("在y=", key, "的条件下:", "X", i, "=", _key, "的个数为", _value)

                print("在y=", key, "的条件下:", "X", i, "=", _key, "的概率为",
                      (int(_value) + smooth) / (int(_y_counts[key]) + Len_Of_Current_X * smooth))
                _ret[(key, str(_key))] = (int(_value) + smooth) / (
                            int(_y_counts[key]) + Len_Of_Current_X * smooth)  # 统一变为字符串形式的key
    # 更新先验概率
    len_y = len(y.T[0])
    count_y = len(np.unique(y.T[0]))
    for key in _y_counts.keys():
        _y_counts[key] = (int(_y_counts[key]) + smooth) / (len_y + count_y * smooth)
    return _ret, _y_counts


data = pd.DataFrame(
    {
        'X1': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
        'X2': ['S', 'M', 'M', 'S', 'S', 'S', 'M', 'M', 'L', 'L', 'L', 'M', 'M', 'L', 'L'],
        'Y': [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]
    }, columns=[
        'X1', 'X2', 'Y'
    ]
)

X_train = data[['X1', 'X2']].to_numpy()
Y_train = data[['Y']].to_numpy().reshape(-1, 1)
ret, y_counts = fit(X_train, Y_train, 0)
X_test = np.array([[2, 'S']])
final = predict(X_test_=X_test, conditional_p=ret, y_p=y_counts)
print(final)  # (分类标签,概率)
