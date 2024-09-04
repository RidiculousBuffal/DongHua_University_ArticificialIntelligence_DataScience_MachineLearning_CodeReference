# -*- coding: gb2312 -*-
import matplotlib.pyplot as plt
import numpy as np
import warnings
# 忽略matplotlib所有警告
warnings.filterwarnings("ignore")
from mpl_toolkits import mplot3d
#matplotlib 字体调整
plt.rcParams["font.sans-serif"] = ["KaiTi"]
plt.rcParams["axes.unicode_minus"] = False

# 创建一个3*10的二维数组,记录每一步在三个轴向上移动的距离,在每个轴向上移动的距离服从标准正态分布(期望为0,方差为1)
# 行序为0,1,2分别对应x,y,z轴

rand_walk = np.random.normal(0, 1, size=(3, 1000))  # 随机生成
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
print('----------------ploting------------')
#--------------------------3D绘图----------------------------
fig = plt.figure  # 创建绘图区域
ax = plt.axes(projection='3d')
ax.plot3D(position[0], position[1], position[2], 'red', linestyle='--')
sc = ax.scatter3D(position[0], position[1], position[2], c=distance, cmap='viridis', linewidths=2)
ax.text3D(position[0][-1], position[1][-1], position[2][-1], 'stop')
cbar = plt.colorbar(sc)
cbar.set_label('距离原点的距离',fontsize=20)
ax.w_xaxis.set_pane_color('#deeaf6')
ax.w_zaxis.set_pane_color('#deeaf6')
ax.w_yaxis.set_pane_color('#deeaf6')
# 设置 XYZ坐标面的线型为虚线
ax.xaxis._axinfo['grid']['linestyle'] = '--'
ax.yaxis._axinfo['grid']['linestyle'] = '--'
ax.zaxis._axinfo['grid']['linestyle'] = '--'
ax.set_title('游走轨迹',fontsize=20)
plt.show()
