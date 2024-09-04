# -*- coding: gb2312 -*-
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")
# 创建一个3*10的二维数组,记录每一步在三个轴向上移动的距离,在每个轴向上移动的距离服从标准正态分布(期望为0,方差为1)
# 行序为0,1,2分别对应x,y,z轴

rand_walk = np.random.normal(0, 1, size=(3, 10))  # 随机生成
print("rand_walk")
print(rand_walk)
print("---------------")
position = rand_walk.cumsum(axis=1)  # 位置
print('positon')
print(position)
print('-----------------')
distance = np.sqrt(rand_walk[0] ** 2 + rand_walk[1] ** 2 + rand_walk[2] ** 2)  # 距离
np.set_printoptions(precision=2)
print('distance')
print(distance)
print('---------------')
# z轴最远:
print("the max distance of Z is:", end=' ')
print(np.abs(position[2]).max())
#最近距离值
print('the min distance of all is ', end=' ')
print(distance.min())
