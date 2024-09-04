import matplotlib.figure
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots
import numpy as np
from matplotlib.patches import Rectangle
import seaborn as sns
plt.style.use('science')

fig: matplotlib.figure.Figure = plt.figure()
ax1: matplotlib.figure.Axes = fig.add_subplot(projection='3d')
# 移除网络线
ax1.grid(False)

for x in range(0, 256,10):
    for y in range(0, 256,10):
        for z in range(0, 256,10):
            ax1.scatter(x / 255, y / 255, z / 255, color=(x / 255, y / 255, z / 255,0.5))

# 设置坐标轴标签
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
plt.savefig('3d101.svg')