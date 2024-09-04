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
categories = np.unique(df['category'])
list_categories = categories.tolist()
colors = [plt.cm.coolwarm(i / float(len(categories) - 1)) for i in range(len(categories))]
k = 0
for i in range(0,len(categories)-1,2):
    slice_array = list_categories[i:i+2]
    print(slice_array)
    grid_obj = sns.lmplot(
        x="area",y="poptotal",col="category",data=df.loc[df.category.isin(slice_array),:],robust=False,aspect=1,
       scatter_kws=dict(s=60,linewidths=0.7,edgecolors='black',color=colors[i])
    )
    grid_obj.set_xlabels("Area")
    grid_obj.set_ylabels("Population")
    name = 'fig'+str(k)+'.svg'
    grid_obj.figure.savefig(name)
    k=k+1
