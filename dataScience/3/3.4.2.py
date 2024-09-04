# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# 从studentsInfo.xlsx 读取Group1数据

studentsInfo = pd.read_excel('studentsInfo.xlsx', sheet_name='Group1')
print(studentsInfo)
print('-----------------')
# 使用平均值填充体重和成绩列的NaN数据

studentsInfo.fillna(
    {
        '体重': studentsInfo['体重'].mean(),
        '成绩': studentsInfo['成绩'].mean()
    },
    inplace=True
)
print(studentsInfo)
print('-----------------')
# 使用同一列前一行数据填充'年龄'列的NaN数据
studentsInfo['年龄'].fillna(method='ffill', inplace=True)
print(studentsInfo)
print('-----------------')
# 使用中位数填充月生活费列的NaN数据
studentsInfo.fillna(
    {
        '月生活费':studentsInfo['月生活费'].median()
    },
    inplace=True
)
print(studentsInfo)
print('-----------------')