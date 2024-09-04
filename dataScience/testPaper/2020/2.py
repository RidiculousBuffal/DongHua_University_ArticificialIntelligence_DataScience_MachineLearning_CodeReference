import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

#     根据IDC的统计数据，各品牌手机在中国的年销量如表1所示（源程序fill_2.py）。
# 1) 根据表1的数据，绘制折线图分析各品牌销量发展趋势，如图1所示；

index = ['Huawei', 'Apple', 'OPPO', 'vivo', 'Mi'];
columns = ['Y2015', 'Y2016', 'Y2017', 'Y2018']
data = np.array([[62.9, 76.6, 90.9, 104.97], [58.4, 44.9, 41.1, 36.32],
                 [35.3, 78.4, 80.5, 78.94], [35.1, 69.2, 68.6, 75.97],
                 [64.9, 41.5, 55.1, 51.99]])
sales = DataFrame(data=data, index=index, columns=columns)
print(sales)
# 绘制折线图
psales = DataFrame(data.T, columns, index)
print(psales)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

psales.plot(title='2015~2018国内手机销量', linewidth=2, marker='o',
            linestyle='dashed', grid=True, alpha=0.9)
plt.show()

# #2)计算2018年各品牌手机的同比增幅，并在原数据中增加新列"2018同比增幅"；
sales['INC2018'] =sales['Y2018']-sales['Y2017']
print(sales)
