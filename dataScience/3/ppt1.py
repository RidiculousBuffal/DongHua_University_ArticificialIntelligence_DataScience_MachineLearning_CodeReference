# -*- coding: gb2312 -*-
import matplotlib.figure
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots
import numpy as np
from matplotlib.patches import Rectangle
import seaborn as sns


plt.style.use('science')
large = 22;
med = 16;
small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large,
          "font.sans-serif": "SimHei",
          "axes.unicode_minus": False}
plt.rcParams.update(params)
df: pd.DataFrame = pd.read_csv('midwest_filter.csv')
categories = np.unique(df['category'])  # 获得所有的类别(不重复)
colors = [plt.cm.coolwarm(i / float(len(categories) - 1)) for i in range(len(categories))]
data1 = df['poptotal'].tolist()
data2 = df['area'].tolist()
fig: matplotlib.figure.Figure = plt.figure(figsize=(10, 6))  # 所有的图都要在画布上画
ax1: matplotlib.figure.Axes = fig.add_subplot(1, 1, 1)  # 第一张子图
ax1.set_xlabel("Area")  # 设置x,y轴标签
ax1.set_ylabel("Population")
ax1.set_title("Population Vs Area")
for i , category in enumerate(categories):
    ax1.scatter('area','poptotal',data=df.loc[df.category==category,:],s=20,c=colors[i],label=str(category))
df_select: pd.DataFrame = df.loc[df.category, :]

ax1.legend()
start_x = 0.02
end_x = 0.04
plt.gca().axvspan(start_x, end_x, color='#dce4f2', alpha=0.4)
fig.set_facecolor('none')
plt.show()
