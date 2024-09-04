# -*- coding: utf-8 -*-
import matplotlib.figure
import pandas
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 从high-speed rail.csv中读入文件
high_speed_rail = pd.read_csv("High-speed rail.csv", encoding='utf-8', index_col='Country')
# 各国运营里程对比柱状图,标注China为Longest
fig: matplotlib.figure.Figure = plt.figure(figsize=(20, 12))
ax1: matplotlib.figure.Axes = fig.add_subplot(2,2, 1)
ax1.set_title("Operating Mileage of High-speed Rail")
ax1.set_ylabel("Mileage(km)")
ax1.set_xlabel("Country")
ax1.bar(high_speed_rail.index, high_speed_rail['Operation'], color='blue')
# 使用annotate标注china为"Longest"
plt.annotate("Longest!", xy=('China', 20000), xytext=(1, 20000), arrowprops=dict(arrowstyle='->'), fontsize=16)

# 各国运营里程对比堆叠柱状图
ax2: matplotlib.figure.Axes = fig.add_subplot(2, 2, 2)
ax2.set_ylabel("Country")
ax2.set_xlabel("Mileage(km)")
ax2.set_title("Global trends of high-speed rail")
filter_data: pandas.DataFrame = high_speed_rail[['Operation', 'Under-construction', 'Planning']]
filter_data.plot(kind='barh', stacked=True, use_index=True, ax=ax2)
#各国运营里程占比饼图,其中China为扇形离开中心点
ax3:matplotlib.figure.Axes=fig.add_subplot(2,1,2)
miles:pandas.DataFrame = high_speed_rail[['Operation']]
miles.plot(kind='pie', y='Operation', ax=ax3, autopct='%1.1f%%',explode=[0.2,0,0,0,0,0],startangle=60,shadow=True,legend=False,ylabel="")
plt.savefig('4_2_2.png',dpi=600)