# -*- coding: gb2312 -*-
from typing import Any
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 2012-2020��ȫ���˾���֧������(��λ:��Ԫ)Ϊ[1.47,1.62,1.78,1.94,2.38,2.60,2.82,3.07,3.21]
# ģ������4-1������4-3,�����˾���֧����������ͼ,������С���α��,��ɫ����,����ע������ߵ�
# ,ͼ����ΪIncome,�������������,��󱣴�Ϊjpg�ļ�
data = pd.Series([1.47, 1.62, 1.78, 1.94, 2.38, 2.60, 2.82, 3.07, 3.21], index=range(2012, 2021),name='income')
plt.figure(figsize=(10,8))
# ���ǣ�. (period)
# ���ر�ǣ�, (pixel)
# Բ��ǣ�o (circle)
# ���α�ǣ�s (square)
# �����α�ǣ�^ (triangle up)
# ���������α�ǣ�v (triangle down)
# ���α�ǣ�D (diamond)
# �����α�ǣ�h (hexagon)
# �˱��α�ǣ�8 (octagon)
plt.plot(data, marker='s', color='black', linestyle='--')
# ��ߵ������:
max_index = data.idxmax()
max_value = data[max_index]
plt.annotate('Largest!', xy=(max_index, max_value), xytext=(2018.8, 2.6), arrowprops=dict(arrowstyle='->'), fontsize=16)
plt.legend([data.name],loc='upper left')
plt.xlabel('Year')
plt.ylabel('Income(RMB Ten Thousand)')
# plt.show()
plt.savefig('output1.png',dpi=600)
