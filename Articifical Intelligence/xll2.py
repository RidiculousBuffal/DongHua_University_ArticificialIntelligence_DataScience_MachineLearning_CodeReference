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


# ����2���ƴ�
def generate_unique_binary_strings(num_strings, length):  # ���ɳ��ȹ̶���N��2���ƴ�(���ظ�)
    unique_strings = set()
    while len(unique_strings) < num_strings:
        binary_string = ''.join(random.choice('01') for _ in range(length))
        unique_strings.add(binary_string)
    return list(unique_strings)

#����
def decode(P_G: list, delta, L_x):
    P_G_decoded = []
    for s in P_G:
        P_G_decoded.append(L_x + delta * int(s, 2))
    return P_G_decoded


# f(x)=x^2
def f_x(x):
    return x * x

#������Ӧ��
def cal_fit_G(P_G_decoded: list):
    fit_G = []
    for value in P_G_decoded:
        fit_G.append(f_x(value))
    return fit_G

#������Ӧ�ȱ���
def cal_fxi_scale(fit_g: list):
    total = sum(fit_g)
    B = []
    for value in fit_g:
        B.append(value / total)
    return B

#������
def get_sum_scale_C(B: list):
    c = np.array(B)
    return c.cumsum(axis=0)

#�ֶķ�
def Roulette_Wheel_Choice(P_G: list, C: list, N):
    S_G = []
    for i in range(0, N):
        rand = np.random.rand()  # ����0-1֮����ȷֲ��������
        if (rand == 1):
            S_G.append(P_G[N - 1])
        else:
            index = np.searchsorted(np.array(C), rand, side='right')  # �ҵ���һ����rand��ĸ���
            S_G.append(P_G[index])
    return S_G

#�õ�����
def split_SG(SG: list):
    # ����ԭʼ�����˳��
    np.random.shuffle(S_G)

    # ��ԭ�����ΪN-2/2�������飬ÿ���������������ֵ
    n = len(S_G) // 2
    split_arrays = [S_G[i:i + 2] for i in range(0, len(S_G), 2)]
    # ����
    return split_arrays

#����
def crossOver(S_G_splited: list, pc):
    # �̶�Cpoint
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

#����
def Mutation(C_G: list, pm):
    M_G = []
    C_G_ = copy.copy(C_G)
    for j in range(0, len(C_G_)):
        # ����ÿ����������
        for i in range(0, len(C_G_[j])):
            rand = np.random.rand()
            if rand < pm:
                # �������
                # print("����!"+str(j))
                binary_list = list(C_G_[j])
                if binary_list[i] == '0':
                    binary_list[i] = '1'
                else:
                    binary_list[i] = '0'
                mutated_binary = ''.join(binary_list)
                C_G_[j] = mutated_binary  # ����ԭʼ�б�
        M_G.append(C_G_[j])
    return M_G


MAX_FIT = []
NUM = []
G = 0  # ��������
FES = 0  # ��Ӧ������
U_x = 31
L_x = 0
Search_Accuracy = 0.01  # ��������0.01
l = math.ceil(math.log2((U_x - L_x) / Search_Accuracy))  # �������ַ�������
N = 30  # ��ʼ��������Ϊ30��Ⱥ��
# ʵ����������:
delta = (U_x - L_x) / (np.exp2(l) - 1)
# N������ĳ�ʼȺ��
P_G = generate_unique_binary_strings(N, l)
# ����:
P_G_decoded = decode(P_G, delta, L_x)
# print(P_G)
# print(P_G_decoded)

# �����������Ӧ��
fit_g = cal_fit_G(P_G_decoded)

# FES = FES+N
FES = FES + N

# STEP 8
while G < 100:
    NUM.append(G)
    MAX_FIT.append(max(fit_g))

    # �ҵ�pG��ӵ�������Ӧ�ȵĸ���
    fit_max = max(fit_g)
    max_index = fit_g.index(fit_max)
    P_G_max = P_G[max_index]
    fit_min = min(fit_g)
    min_index = fit_g.index(fit_min)
    P_G_min = P_G[min_index]
    # ����һ������
    fit_g.remove(fit_max)
    fit_g.remove(fit_min)
    P_G.remove(P_G_min)
    P_G.remove(P_G_max)

    # ѡ�����
    # ����fit(x_i)/sum(fit(x_i))�ı���B
    B = cal_fxi_scale(fit_g)
    # ����������ۼ�ֵC
    C = get_sum_scale_C(B)
    # print(C)
    # �õ���һ����������:
    S_G = Roulette_Wheel_Choice(P_G=P_G, C=C, N=N - 2)
    # print(S_G)
    # �����ΪN-2/2��
    S_G_splited = split_SG(S_G)
    # print(S_G_splited)
    # �������
    pc = 0.8
    C_G = crossOver(S_G_splited, pc)
    # print(S_G_splited)
    # print(C_G)
    pm = 0.01
    M_G = Mutation(C_G, pm)
    # print(M_G)
    # ��MG�еĸ������
    M_G_decoded = decode(M_G, delta, L_x)
    FES = FES + N - 2
    fit_g = cal_fit_G(M_G_decoded)
    if max(fit_g) > fit_max:
        fit_g.append(max(fit_g))
        fit_g.append(max(fit_g))
        # ����2��
        max_index_ = fit_g.index(max(fit_g))
        M_G.append(M_G[max_index_])
        M_G.append(M_G[max_index_])
    else:
        fit_g.append(fit_max)
        fit_g.append(fit_max)
        M_G.append(P_G_max)
        M_G.append(P_G_max)
    P_G = M_G
    G = G + 1  # ִ��100��

figure: plt.Figure = plt.figure(figsize=(10, 10))
ax1: plt.Axes = figure.add_subplot(1, 1, 1)
ax1.plot(NUM, MAX_FIT, linestyle='-',marker='o')
plt.show()
ax1.set_xlabel("Calculus Of Evolutionary Steps")
ax1.set_ylabel("Max Fit in Group")

print(max(fit_g))
