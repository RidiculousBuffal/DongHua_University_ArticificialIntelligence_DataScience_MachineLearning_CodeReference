# -*- coding: gb2312 -*-
from typing import Any
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame

plt.rcParams["font.sans-serif"] = ["KaiTi"]
plt.rcParams["axes.unicode_minus"] = False
# 模仿例4.2,使用多个子图分别绘制人均可支配收入的折线图,箱型图,以及柱状图.
data = pd.Series([1.47, 1.62, 1.78, 1.94, 2.38, 2.60, 2.82, 3.07, 3.21], index=range(2012, 2021), name='income')
fig = plt.figure(figsize=(6, 6))
# 3个子图分别用(2,2,1),(2,2,2),(2,1,2)作为参数
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(data)
ax1.set_title('line chart')
ax1.set_xlabel('Year')
ax1.set_ylabel('income')
ax2 = fig.add_subplot(2, 2, 2)
data.plot(kind='box', ax=ax2, xticks=[])
ax2.set_xlabel('2012-2020')
ax2.set_ylabel('income')
ax2.set_title('box-whisker plot')
ax3 = fig.add_subplot(2, 1, 2)
data.plot(kind='bar', ax=ax3, width=0.8, color='steelblue', fontsize='small')
ax3.set_title('Bar chart')
ax3.legend([data.name], loc='upper left')
ax3.set_xlabel('Year')
ax3.set_ylabel('income')
plt.subplots_adjust()
plt.show()