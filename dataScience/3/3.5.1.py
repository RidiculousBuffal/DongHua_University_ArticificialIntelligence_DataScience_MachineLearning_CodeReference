# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# 读取数据
raw_data = pd.read_excel('studentsInfo.xlsx', sheet_name='Group3')
# 将'序号','性别','年龄'列保存到data1中
data1 = raw_data[['序号', '性别', '年龄']]
print(data1)
print('-------')
# 将'序号','身高','体重','成绩'保存到data2中
data2 = raw_data[['序号', '身高', '体重', '成绩']]
print(data2)
print('-------')
#data2合并到data1方式为内连接
data_new = pd.merge(data1,data2,how='inner')
print(data_new)
print('-------')