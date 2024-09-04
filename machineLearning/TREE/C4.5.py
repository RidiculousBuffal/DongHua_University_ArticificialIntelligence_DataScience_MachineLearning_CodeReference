from __future__ import annotations
import numpy as np
import math
from collections import Counter


def create_tree(dataSet_: np.ndarray, attribute: list, doNotJudge: list) -> dict:
    ret = dict()
    tags__ = np.unique(dataSet_[:, -1])
    index_ = cal_GainRito(dataSet_, attribute, doNotJudge)
    current_best = index_[0]
    best_tag = index_[1]
    col_tags_ = np.unique(dataSet_[:, current_best])
    temp = dict()
    for tag__ in col_tags_:
        # print(tag__ + ":")
        mid__ = dataSet_[dataSet_[:, current_best] == tag__, :]
        cnt = 0
        none_zero_Y_tag = 0
        for Y_tags_ in tags__:
            len__ = len(mid__[mid__[:, -1] == Y_tags_, :])
            # print(Y_tags_, ":", len__)
            if len__ != 0:
                cnt += 1
                none_zero_Y_tag = Y_tags_
        if cnt == 1:
            # 只有一个子节点
            temp[tag__] = none_zero_Y_tag
        else:
            doNotJudge.append(current_best)
            temp[tag__] = create_tree(dataSet_[dataSet_[:, current_best] == tag__, :], attribute, doNotJudge)
    ret[best_tag] = temp
    return ret


def cal_GainRito(dataSet_: np.ndarray, attribute: list, doNotJudge: list) -> tuple:
    # 提取出分类特征
    ret = ()
    col_ = dataSet_.shape[1]
    row_ = dataSet_.shape[0]
    tags = np.unique(dataSet[:, -1])
    H_Y = -1
    sum_ = 0
    for tag in tags:
        counts_ = len(dataSet_[dataSet_[:, -1] == tag, :])
        sum_ += counts_ / row_ * math.log(counts_ / row_, 2)
    H_Y = H_Y * sum_
    max_Gain_rito = -1000000000

    for i in range(0, col_ - 1):
        if i in doNotJudge:
            continue
        col_tags = np.unique(dataSet_[:, i])
        col_tags_count = Counter(dataSet_[:, i])
        sum_col_H = 0
        H_x = -1
        sum_H_x = 0
        for tag in col_tags:
            sum_H_x += (col_tags_count[tag] / row_) * math.log(col_tags_count[tag] / row_, 2)
        H_x = H_x * sum_H_x
        print("当前特征", i, "的信息熵", "H(x)=", H_x)
        sum_out = 0
        for tag in col_tags:
            # print(tag + ":")
            H_ = -1
            sum_ = 0
            mid = dataSet_[dataSet_[:, i] == tag, :]
            for Y_tags in tags:
                counted_Y_tags = len(mid[mid[:, -1] == Y_tags, :])
                # print(Y_tags, ":", counted_Y_tags)
                if counted_Y_tags != 0:
                    sum_ += (counted_Y_tags / col_tags_count[tag]) * math.log2(counted_Y_tags / col_tags_count[tag])
            H_ = H_ * sum_
            sum_out += col_tags_count[tag] * H_ / row_
        Gain_ = H_Y - sum_out
        print("当前特征", i, "的信息增益", "Gain(Y,X)=", Gain_)
        Gain_rito = Gain_ / H_x
        print("当前特征", i, "的信息增益比", "Gain_R(Y,X)=", Gain_rito)
        if Gain_rito > max_Gain_rito:
            max_Gain_rito = Gain_rito
            ret = (i, attribute[i])
    print("这一轮中最好的特征是", ret[1])
    print("-----------------------------------------------------------")
    return ret


dataSet = np.array([[0, 0, 0, 0, 'no'],  # 数据集
                    [0, 0, 0, 1, 'no'],
                    [0, 1, 0, 1, 'yes'],
                    [0, 1, 1, 0, 'yes'],
                    [0, 0, 0, 0, 'no'],
                    [1, 0, 0, 0, 'no'],
                    [1, 0, 0, 1, 'no'],
                    [1, 1, 1, 1, 'yes'],
                    [1, 0, 1, 2, 'yes'],
                    [1, 0, 1, 2, 'yes'],
                    [2, 0, 1, 2, 'yes'],
                    [2, 0, 1, 1, 'yes'],
                    [2, 1, 0, 1, 'yes'],
                    [2, 1, 0, 2, 'yes'],
                    [2, 0, 0, 0, 'no']])

attributes = ['年龄', '有工作', '有自己的房子', '信贷情况']

returns = create_tree(dataSet, attributes, [])
print(returns)
