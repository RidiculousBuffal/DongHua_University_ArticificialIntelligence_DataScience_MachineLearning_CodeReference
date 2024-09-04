# -*- coding: gb2312 -*-
from typing import Any

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
import scienceplots
plt.style.use('science')
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = ['Electronic accessories', 'Fashion accessories', 'Food and beverages', 'Health and beauty', 'Home and lifestyle', 'Sports and travel']
y = [2587.5015, 2585.995, 2673.564, 2342.559, 2564.853, 2624.8965]
# 将数据和标签进行升序排列
sorted_indices = np.argsort(y)
x_sorted = [x[i] for i in sorted_indices]
y_sorted = np.sort(y)

# 颜色映射
colors = plt.cm.viridis(np.linspace(0, 1, len(y_sorted)))

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图，并为每个柱子指定颜色
ax.bar(x_sorted, y_sorted, color=colors)

# 添加标题
ax.set_title('Sales by Category')

# 找到最高点并进行标记
max_index = np.argmax(y_sorted)
ax.annotate(f'{y_sorted[max_index]:.2f}', xy=(x_sorted[max_index], y_sorted[max_index]),
            xytext=(x_sorted[max_index], y_sorted[max_index] + 100),
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='->'))

# 旋转标签以避免重叠
plt.xticks(rotation=45)
plt.tight_layout()
# 显示图形
plt.show()