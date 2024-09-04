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
# �����ݺͱ�ǩ������������
sorted_indices = np.argsort(y)
x_sorted = [x[i] for i in sorted_indices]
y_sorted = np.sort(y)

# ��ɫӳ��
colors = plt.cm.viridis(np.linspace(0, 1, len(y_sorted)))

# ����ͼ�κ�������
fig, ax = plt.subplots(figsize=(10, 6))

# ������״ͼ����Ϊÿ������ָ����ɫ
ax.bar(x_sorted, y_sorted, color=colors)

# ��ӱ���
ax.set_title('Sales by Category')

# �ҵ���ߵ㲢���б��
max_index = np.argmax(y_sorted)
ax.annotate(f'{y_sorted[max_index]:.2f}', xy=(x_sorted[max_index], y_sorted[max_index]),
            xytext=(x_sorted[max_index], y_sorted[max_index] + 100),
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='->'))

# ��ת��ǩ�Ա����ص�
plt.xticks(rotation=45)
plt.tight_layout()
# ��ʾͼ��
plt.show()