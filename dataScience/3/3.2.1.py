# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# 创建如下的Series 对象,其中a-f是索引标签
# a     b     c   d    e    f
# 30   25  27  41   25  34

my_series = pd.Series(
    data=[30, 25, 27, 41, 25, 34],
    index=[chr(ord('a') + i) for i in range(6)]  # ord 返回一个字符的uni编码
)

print(my_series)

# 增加新的数据,值为27,索引为g

new_series = pd.Series(
    data=[27],
    index=['g']
)

print('--------------------')
my_series = pd.concat([my_series, new_series], ignore_index=False)
print(my_series)
print('----------------')

# 修改索引d的对应的值为40
my_series['d'] = 40
print(my_series)
print('------------------')
# 查询值大于23的数据
search_list = my_series.loc[my_series.values > 27]
print(search_list)
print('------------------')
# 删除位置序号为1-3的数据
my_series.drop(my_series.index[1:4], inplace=True)
print(my_series)
print('------------------')
