# -*- coding: gb2312 -*-
import math
import random
import copy
import numpy as np
from sko.GA import GA
import matplotlib.pyplot as plt
import scienceplots
plt.style.use("science")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


# 生成2进制串
def generate_unique_binary_strings(num_strings, length):  # 生成长度固定的N个2进制串(不重复)
    unique_strings = set()
    while len(unique_strings) < num_strings:
        binary_string = ''.join(random.choice('01') for _ in range(length))
        unique_strings.add(binary_string)
    return list(unique_strings)

#解码
def decode(P_G: list, delta, L_x):
    P_G_decoded = []
    for s in P_G:
        P_G_decoded.append(L_x + delta * int(s, 2))
    return P_G_decoded


# f(x)=x^2
def f_x(x):
    return x * x

#计算适应度
def cal_fit_G(P_G_decoded: list):
    fit_G = []
    for value in P_G_decoded:
        fit_G.append(f_x(value))
    return fit_G

#计算适应度比例
def cal_fxi_scale(fit_g: list):
    total = sum(fit_g)
    B = []
    for value in fit_g:
        B.append(value / total)
    return B

#比例和
def get_sum_scale_C(B: list):
    c = np.array(B)
    return c.cumsum(axis=0)

#轮赌法
def Roulette_Wheel_Choice(P_G: list, C: list, N):
    S_G = []
    for i in range(0, N):
        rand = np.random.rand()  # 生成0-1之间均匀分布的随机数
        if (rand == 1):
            S_G.append(P_G[N - 1])
        else:
            index = np.searchsorted(np.array(C), rand, side='right')  # 找到第一个比rand大的个体
            S_G.append(P_G[index])
    return S_G

#得到父代
def split_SG(SG: list):
    # 打乱原始数组的顺序
    np.random.shuffle(S_G)

    # 将原数组分为N-2/2个子数组，每个子数组包含两个值
    n = len(S_G) // 2
    split_arrays = [S_G[i:i + 2] for i in range(0, len(S_G), 2)]
    # 返回
    return split_arrays

#交叉
def crossOver(S_G_splited: list, pc):
    # 固定Cpoint
    Cpoint = 3
    C_G = []
    for value in S_G_splited:
        rand = np.random.rand()
        val1 = value[0]
        val2 = value[1]
        if rand < pc:
            left1 = val1[:Cpoint]
            right1 = val1[Cpoint:]
            left2 = val2[:Cpoint]
            right2 = val2[Cpoint:]
            result1 = left1 + right2
            result2 = left2 + right1
            C_G.append(result1)
            C_G.append(result2)
        else:
            C_G.append(val1)
            C_G.append(val2)
    return C_G

#变异
def Mutation(C_G: list, pm):
    M_G = []
    C_G_ = copy.copy(C_G)
    for j in range(0, len(C_G_)):
        # 遍历每个二进制数
        for i in range(0, len(C_G_[j])):
            rand = np.random.rand()
            if rand < pm:
                # 变异操作
                # print("变异!"+str(j))
                binary_list = list(C_G_[j])
                if binary_list[i] == '0':
                    binary_list[i] = '1'
                else:
                    binary_list[i] = '0'
                mutated_binary = ''.join(binary_list)
                C_G_[j] = mutated_binary  # 更新原始列表
        M_G.append(C_G_[j])
    return M_G


MAX_FIT = []
NUM = []
G = 0  # 迭代次数
FES = 0  # 适应度评价
U_x = 31
L_x = 0
Search_Accuracy = 0.01  # 搜索精度0.01
l = math.ceil(math.log2((U_x - L_x) / Search_Accuracy))  # 二进制字符串长度
N = 30  # 初始产生个数为30个群体
# 实际搜索精度:
delta = (U_x - L_x) / (np.exp2(l) - 1)
# N个个体的初始群体
P_G = generate_unique_binary_strings(N, l)
# 解码:
P_G_decoded = decode(P_G, delta, L_x)
# print(P_G)
# print(P_G_decoded)

# 计算解码后的适应度
fit_g = cal_fit_G(P_G_decoded)

# FES = FES+N
FES = FES + N

# STEP 8
while G < 100:
    NUM.append(G)
    MAX_FIT.append(max(fit_g))

    # 找到pG中拥有最高适应度的个体
    fit_max = max(fit_g)
    max_index = fit_g.index(fit_max)
    P_G_max = P_G[max_index]
    fit_min = min(fit_g)
    min_index = fit_g.index(fit_min)
    P_G_min = P_G[min_index]
    # 丢弃一个即可
    fit_g.remove(fit_max)
    fit_g.remove(fit_min)
    P_G.remove(P_G_min)
    P_G.remove(P_G_max)

    # 选择操作
    # 计算fit(x_i)/sum(fit(x_i))的比例B
    B = cal_fxi_scale(fit_g)
    # 计算比例的累加值C
    C = get_sum_scale_C(B)
    # print(C)
    # 得到第一个父代个体:
    S_G = Roulette_Wheel_Choice(P_G=P_G, C=C, N=N - 2)
    # print(S_G)
    # 随机分为N-2/2组
    S_G_splited = split_SG(S_G)
    # print(S_G_splited)
    # 交叉操作
    pc = 0.8
    C_G = crossOver(S_G_splited, pc)
    # print(S_G_splited)
    # print(C_G)
    pm = 0.01
    M_G = Mutation(C_G, pm)
    # print(M_G)
    # 对MG中的个体解码
    M_G_decoded = decode(M_G, delta, L_x)
    FES = FES + N - 2
    fit_g = cal_fit_G(M_G_decoded)
    if max(fit_g) > fit_max:
        fit_g.append(max(fit_g))
        fit_g.append(max(fit_g))
        # 复制2份
        max_index_ = fit_g.index(max(fit_g))
        M_G.append(M_G[max_index_])
        M_G.append(M_G[max_index_])
    else:
        fit_g.append(fit_max)
        fit_g.append(fit_max)
        M_G.append(P_G_max)
        M_G.append(P_G_max)
    P_G = M_G
    G = G + 1  # 执行100次

figure: plt.Figure = plt.figure(figsize=(10, 10))
ax1: plt.Axes = figure.add_subplot(1, 1, 1)
ax1.plot(NUM, MAX_FIT, linestyle='-',marker='o')
plt.show()
ax1.set_xlabel("Calculus Of Evolutionary Steps")
ax1.set_ylabel("Max Fit in Group")

print(max(fit_g))
