import numpy as np
from sklearn import datasets
from collections import Counter  # 为了做投票
from sklearn.model_selection import train_test_split


##标准化函数
def normalized(arr, k):
    if k == 1:
        # 归一化
        print("对数据进行0-1归一化")
        for i in range(len(arr)):
            max_val = max(arr[i])
            min_val = min(arr[i])
            arr[i] = (arr[i]-min_val)/(max_val-min_val)
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


def knn_classify(X, y, testInstance, k, p):
    # TODO  返回testInstance的预测标签 = {0,1,2}
    distances = [euc_dis(x, testInstance, p) for x in X]
    kneighbors = np.argsort(distances)[:k]
    count = Counter(y[kneighbors])
    return count.most_common()[0][0]


# 读入数据集
# 导入iris数据
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2003)

for i in range(1, 4):
    for j in range(1, 4):
        normalized(X_train,i)
        normalized(X_test,i)
        if j ==1:
            print("曼哈顿距离")
        elif j==2:
            print("欧氏距离")
        else:
            print("切比雪夫距离")
        predictions = [knn_classify(X_train, y_train, data,3, j) for data in X_test]
        correct = np.count_nonzero((predictions == y_test) == True)
        # accuracy_score(y_test, clf.predict(X_test))
        print("Accuracy is: %.8f" % (correct / len(X_test)))

