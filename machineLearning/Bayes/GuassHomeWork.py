import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import jieba
from sklearn import model_selection
from collections import Counter
from math import sqrt
from math import pi
from math import exp
from math import log10

def Guass_Predict(X_train: np.ndarray, X_test: np.ndarray, y_train_: np.ndarray) -> list:
    Y_ = np.array(y_train_)
    print("共", len(x_test), "轮测试")
    Y_1_mask = Y == 1
    Y_0_mask = Y == 0
    y_count = dict(Counter(Y_))
    print(y_count)
    y_1_prob = y_count[1] / len(Y_)
    y_0_prob = y_count[0] / len(Y_)
    ret_ = list()
    k = 0
    for test in X_test:
        # 计算y=1的概率
        print("第", k, "轮测试")
        k = k + 1
        mul_y_1_log_sum = 0
        mul_y_0_log_sum = 0
        for i in range(0, 35389):
            x_i_y_1_std = np.std(X_train[:, i][Y_1_mask])
            x_i_y_0_std = np.std(X_train[:, i][Y_0_mask])
            x_i_y_1_mean = np.mean(X_train[:, i][Y_1_mask])
            x_i_y_0_mean = np.mean(X_train[:, i][Y_0_mask])
            p_x_i_y_0 = (1 / sqrt(2 * pi * x_i_y_0_std * x_i_y_0_std)) * exp(
                -1 * (test[i] - x_i_y_0_mean) ** 2 / (2 * x_i_y_0_std * x_i_y_0_std))
            p_x_i_y_1 = (1 / sqrt(2 * pi * x_i_y_1_std * x_i_y_1_std)) * exp(
                -1 * (test[i] - x_i_y_1_mean) ** 2 / (2 * x_i_y_1_std * x_i_y_1_std))
            mul_y_1_log_sum = mul_y_1_log_sum + log10(p_x_i_y_1)
            mul_y_0_log_sum = mul_y_0_log_sum + log10(p_x_i_y_0)
        mul_y_1_log_sum = mul_y_1_log_sum + log10(y_1_prob)
        mul_y_0_log_sum = mul_y_0_log_sum + log10(y_0_prob)
        if mul_y_1_log_sum < mul_y_0_log_sum:
            ret_.append(0)
        else:
            ret_.append(1)
    return ret_


path1 = "email.txt"
train_file = open(path1, 'r', encoding="utf-8")
corpus = train_file.readlines()

split_corpus = []
for c in corpus:
    split_corpus.append(" ".join(jieba.lcut(c)))

cv = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
X = cv.fit_transform(split_corpus).toarray()

Y = [0] * 5000 + [1] * 5000

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.002)

# print(x_train[:,0][Y_==0])
predict = Guass_Predict(x_train, x_test, y_train)
print("预测值", predict)
print("真实值", y_test)
true = 0
for i in range(0, len(predict)):
    if predict[i] == y_test[i]:
        true = true + 1
print("准确率:",true/len(x_test))