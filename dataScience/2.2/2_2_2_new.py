# -*- coding: gb2312 -*-
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")
# ����һ��3*10�Ķ�ά����,��¼ÿһ���������������ƶ��ľ���,��ÿ���������ƶ��ľ�����ӱ�׼��̬�ֲ�(����Ϊ0,����Ϊ1)
# ����Ϊ0,1,2�ֱ��Ӧx,y,z��

rand_walk = np.random.normal(0, 1, size=(3, 10))  # �������
print("rand_walk")
print(rand_walk)
print("---------------")
position = rand_walk.cumsum(axis=1)  # λ��
print('positon')
print(position)
print('-----------------')
distance = np.sqrt(rand_walk[0] ** 2 + rand_walk[1] ** 2 + rand_walk[2] ** 2)  # ����
np.set_printoptions(precision=2)
print('distance')
print(distance)
print('---------------')
# z����Զ:
print("the max distance of Z is:", end=' ')
print(np.abs(position[2]).max())
#�������ֵ
print('the min distance of all is ', end=' ')
print(distance.min())
