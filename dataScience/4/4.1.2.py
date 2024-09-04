# -*- coding: gb2312 -*-
from typing import Any
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 2012-2020年全国人均可支配收入(单位:万元)为[1.47,1.62,1.78,1.94,2.38,2.60,2.82,3.07,3.21]
# 模仿例题4-1和例题4-3,绘制人均可支配收入折线图,数据用小矩形标记,黑色虚线,并用注解标出最高点
# ,图标题为Income,设置坐标轴标题,最后保存为jpg文件
data = pd.Series([1.47, 1.62, 1.78, 1.94, 2.38, 2.60, 2.82, 3.07, 3.21], index=range(2012, 2021),name='income')
plt.figure(figsize=(10,8))
# 点标记：. (period)
# 像素标记：, (pixel)
# 圆标记：o (circle)
# 方形标记：s (square)
# 三角形标记：^ (triangle up)
# 反向三角形标记：v (triangle down)
# 菱形标记：D (diamond)
# 六边形标记：h (hexagon)
# 八边形标记：8 (octagon)
plt.plot(data, marker='s', color='black', linestyle='--')
# 最高点的索引:
max_index = data.idxmax()
max_value = data[max_index]
plt.annotate('Largest!', xy=(max_index, max_value), xytext=(2018.8, 2.6), arrowprops=dict(arrowstyle='->'), fontsize=16)
plt.legend([data.name],loc='upper left')
plt.xlabel('Year')
plt.ylabel('Income(RMB Ten Thousand)')
# plt.show()
plt.savefig('output1.png',dpi=600)
