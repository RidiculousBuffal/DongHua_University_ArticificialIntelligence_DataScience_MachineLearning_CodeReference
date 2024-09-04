# -*- coding: gb2312 -*-
# -*- coding: gb2312 -*-
from typing import Any

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_excel('小区.xlsx')
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(2, 1, 1)
ax1.set_title('小区')
time = df['时间'].tolist()
PM25 = df['PM2.5'].tolist()
ax1.plot_date(time, PM25,linestyle='solid')
df2 = pd.read_excel('自建.xlsx')
time1 = df2['时间'].tolist()
PM25_2=df2['PM2.5'].tolist()
ax2 =fig.add_subplot(2,1,2)
ax2.plot_date(time1, PM25_2,linestyle='solid')
plt.show()
