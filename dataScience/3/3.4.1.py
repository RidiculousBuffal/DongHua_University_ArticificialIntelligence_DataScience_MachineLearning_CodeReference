# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# 从studentsInfo.xlsx 读取数据

studentsInfo = pd.read_excel('studentsInfo.xlsx')
print(studentsInfo)
print('-------------')

# 将'案例教学'的值全部改为NaN

studentsInfo['案例教学'] = np.NaN
print(studentsInfo)
print('-------------')

# 滤除每一行数据中缺失值在3项以上的行
threhold = studentsInfo.shape[1] - 2
studentsInfo.dropna(thresh=threhold, inplace=True, axis=0)
print(studentsInfo)
print('-------------')

# 滤除值全部为NaN的列
studentsInfo.dropna(how='all', inplace=True, axis=1)
print(studentsInfo)
print('-------------')
