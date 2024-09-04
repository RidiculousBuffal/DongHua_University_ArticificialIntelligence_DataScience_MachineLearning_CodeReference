import numpy as np
from sklearn import datasets
from collections import Counter  # 为了做投票
from sklearn.model_selection import train_test_split



# 考虑K个最近的样本点,对样本点的y_i进行加权平均

# KNN训练集的目的:确定K,距离的计算方式,归一化方式

# 归一化
def normalized(arr, k):
    if k == 1:
        # 归一化
        print("对数据进行0-1归一化")
        for i in range(len(arr)):
            max_val = max(arr[i])
            min_val = min(arr[i])
            arr[i] = (arr[i] - min_val) / (max_val - min_val)
    elif k == 2:
        print("对数据进行Z-score标准化")
        for i in range(len(arr)):
            mean = np.mean(arr[i])
            std = np.std(arr)
            arr[i] = (arr[i] - mean) / std
    else:

        print("不对数据进行任何操作")
        return


# 计算距离
def euc_dis(instance1, instance2, p):
    if p == 1:
        # print("曼哈顿距离")
        return sum(abs(instance1 - instance2))
    elif p == 2:
        # print("欧氏距离")
        return np.sqrt(sum((instance1 - instance2) ** 2))
    else:
        # print("切比雪夫距离")
        return max(abs(a - b) for a, b in zip(instance1, instance2))


def calculate_rmse(actual, predicted):
    n = len(actual)
    mse = sum((actual[i] - predicted[i])**2 for i in range(n)) / n
    RMSE = mse**0.5
    return RMSE


def knn_classify(X, y, testInstance, k, p):
    # TODO  返回testInstance的预测标签 = {0,1,2}
    distances = [euc_dis(x, testInstance, p) for x in X]
    kneighbors = np.argsort(distances)[:k]
    count = Counter(y[kneighbors])
    return count.most_common()[0][0]

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state=2024)

for i in range(1, 4):
    for j in range(1, 4):
        normalized(X_train,i)
        normalized(X_test, i)
        if j ==1:
            print("曼哈顿距离")
        elif j==2:
            print("欧氏距离")
        else:
            print("切比雪夫距离")
        predictions = [knn_classify(X_train, y_train, data,3, j) for data in X_test]
        print("RMSE:"+str(calculate_rmse(y_test,predictions)))


