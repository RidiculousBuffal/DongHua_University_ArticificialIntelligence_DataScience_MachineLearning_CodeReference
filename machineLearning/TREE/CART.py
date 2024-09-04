from __future__ import annotations
import numpy as np
import math
from collections import Counter


#
# def create_tree(dataSet_: np.ndarray, attribute: list, doNotJudge: list) -> dict:
#     ret = dict()
#     tags__ = np.unique(dataSet_[:, -1])
#     index_ = cal_GainRito(dataSet_, attribute, doNotJudge)
#     current_best = index_[0]
#     best_tag = index_[1]
#     col_tags_ = np.unique(dataSet_[:, current_best])
#     temp = dict()
#     for tag__ in col_tags_:
#         # print(tag__ + ":")
#         mid__ = dataSet_[dataSet_[:, current_best] == tag__, :]
#         cnt = 0
#         none_zero_Y_tag = 0
#         for Y_tags_ in tags__:
#             len__ = len(mid__[mid__[:, -1] == Y_tags_, :])
#             # print(Y_tags_, ":", len__)
#             if len__ != 0:
#                 cnt += 1
#                 none_zero_Y_tag = Y_tags_
#         if cnt == 1:
#             # 只有一个子节点
#             temp[tag__] = none_zero_Y_tag
#         else:
#             doNotJudge.append(current_best)
#             temp[tag__] = create_tree(dataSet_[dataSet_[:, current_best] == tag__, :], attribute, doNotJudge)
#     ret[best_tag] = temp
#     return ret

def createTree(dataSet_: np.ndarray, attribute: list, doNotJudge: list) -> dict:
    ret = dict()
    Y_tag = np.unique(dataSet_[:, -1])
    Gini_result = cal_Gini(dataSet_, attribute,doNotJudge)
    Gini_attr_name = Gini_result[0]
    Gini_col_index = Gini_result[1]
    Gini_col_attr_name = Gini_result[2][0]
    cnt_attr = 0
    attr_ytag = 0
    others_ytag = 0
    others_attr = 0
    tmp = dict()
    for tag in Y_tag:
        mid = dataSet_[dataSet_[:, -1] == tag, :]
        attr = mid[mid[:, Gini_col_index] == Gini_col_attr_name, :]
        others = mid[mid[:, Gini_col_index] != Gini_col_attr_name, :]
        if len(attr) != 0:
            cnt_attr += 1
            attr_ytag = tag
        if len(others) != 0:
            others_attr += 1
            others_ytag = tag
    if cnt_attr == 1 and others_attr == 1:
        tmp = {'满足该条件': attr_ytag, '不满足该条件': others_ytag}
    if cnt_attr == 1 and others_attr != 1:
        tmp = {'满足该条件': attr_ytag,
               '不满足该条件': createTree(dataSet_[dataSet_[:, Gini_col_index] != Gini_col_attr_name, :], attribute, doNotJudge)}
    if cnt_attr != 1 and others_attr == 1:
        doNotJudge.append(Gini_col_index)
        tmp = {'满足该条件': createTree(dataSet_[dataSet_[:, Gini_col_index] == Gini_col_attr_name, :], attribute, doNotJudge),
               '不满足该条件': others_ytag}
    if cnt_attr != 1 and others_attr != 1:
        No_flag = createTree(dataSet_[dataSet_[:, Gini_col_index] != Gini_col_attr_name, :], attribute, doNotJudge)
        doNotJudge.append(Gini_col_index)
        Yes_flag = createTree(dataSet_[dataSet_[:, Gini_col_index] == Gini_col_attr_name, :], attribute, doNotJudge)
        tmp = {'满足该条件': Yes_flag, '不满足该条件': No_flag}
    ret[attribute[Gini_col_index]] = {Gini_col_attr_name: tmp}
    return ret


def cal_Gini(dataSet_: np.ndarray, attribute: list, doNotJudge: list) -> tuple:
    ret = ('1', '1', ('1', 1000000000))  # 名字,列号,列属性,gini
    col_ = dataSet_.shape[1]
    row_ = dataSet_.shape[0]
    Y_tags = np.unique(dataSet[:, -1])
    for i in range(0, col_ - 1):
        if doNotJudge is not None and i in doNotJudge:
            continue
        # 提取每一列的为特征
        print("当前特征是",i)
        col_attr = np.unique(dataSet_[:, i])
        counts = Counter(dataSet_[:, i])
        min_tag = ('1', 100000000000)  # 最小标签
        for tags in col_attr:
            has_attr = dataSet_[dataSet_[:, i] == tags, :]
            others = dataSet_[dataSet_[:, i] != tags, :]
            print("当前特征分组为","(",tags,",","其他)")
            len_has_attr = len(has_attr)
            len_others = len(others)
            sum_has_attr = 1
            sum_others = 1

            for Ytag in Y_tags:
                len_attr_Ytags = len(has_attr[has_attr[:, -1] == Ytag, :])
                len_other_Ytags = len(others[others[:, -1] == Ytag, :])
                sum_has_attr -= (len_attr_Ytags / len_has_attr) ** 2
                sum_others -= (len_other_Ytags / len_others) ** 2
            # 加权
            Gini_tag = (len_has_attr / row_) * sum_has_attr + (len_others / row_) * sum_others
            print("(",tags,",","其他)的基尼系数是:",Gini_tag)
            if Gini_tag < min_tag[1]:
                min_tag = (tags, Gini_tag)
                if Gini_tag < ret[2][1]:
                    ret = (attribute[i], i, min_tag)
    print("当前轮最好的是",ret[0])
    print("-------------------------------")
    return ret


# def cal_GainRito(dataSet_: np.ndarray, attribute: list, doNotJudge: list) -> tuple:
#     # 提取出分类特征
#     ret = ()
#     col_ = dataSet_.shape[1]
#     row_ = dataSet_.shape[0]
#     tags = np.unique(dataSet[:, -1])
#     H_Y = -1
#     sum_ = 0
#     for tag in tags:
#         counts_ = len(dataSet[dataSet[:, -1] == tag, :])
#         sum_ += counts_ / row_ * math.log(counts_ / row_, 2)
#     H_Y = H_Y * sum_
#     max_Gain_rito = -1000000000
#
#     for i in range(0, col_ - 1):
#         if i in doNotJudge:
#             continue
#         col_tags = np.unique(dataSet_[:, i])
#         col_tags_count = Counter(col_tags)
#         sum_col_H = 0
#         H_x = -1
#         sum_H_x = 0
#         for tag in col_tags:
#             sum_H_x += (col_tags_count[tag] / row_) * math.log(col_tags_count[tag] / row_, 2)
#         H_x = H_x * sum_H_x
#         for tag in col_tags:
#             # print(tag + ":")
#             H_ = -1
#             sum_ = 0
#             mid = dataSet_[dataSet_[:, i] == tag, :]
#             for Y_tags in tags:
#                 counted_Y_tags = len(mid[mid[:, -1] == Y_tags, :])
#                 # print(Y_tags, ":", counted_Y_tags)
#                 if counted_Y_tags != 0:
#                     sum_ += (counted_Y_tags / col_tags_count[tag]) * math.log2(counted_Y_tags / col_tags_count[tag])
#             H_ = H_ * sum_
#             sum_col_H += (col_tags_count[tag] / row_) * H_
#         Gain_ = H_Y - sum_col_H
#         Gain_rito = Gain_ / H_x
#         if Gain_rito > max_Gain_rito:
#             max_Gain_rito = Gain_rito
#             ret = (i, attribute[i])
#     return ret


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

returns = createTree(dataSet, attributes, [])
print(returns)
# print(returns)
# print(dataSet[dataSet[:, 0] != '1', :])

