import numpy as np

X = np.array([
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9],
    [1, 1, 1, 1, 1],
])

Y = np.array([1, 0, 1])

# 创建布尔数组指示Y等于1
mask = Y == 1

# 使用布尔数组对X的第一列进行索引，并计算平均值
mean_value = np.mean(X[:, 0][mask])

print("X的第一列中Y等于1的平均值:", mean_value)
print(X[:,0][mask])