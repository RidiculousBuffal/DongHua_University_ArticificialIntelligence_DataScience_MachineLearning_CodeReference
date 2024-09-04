# -*- coding: utf-8 -*-
import pandas
import pandas as pd
import numpy as np
# 创建3*3的DataFrame 对象,数值为1-9 行索引为 a,b,c, 列索引为 one,two three
import warnings
warnings.filterwarnings("ignore")

my_DataFrame = pd.DataFrame(
    data=np.arange(1, 10, 1).reshape(3, 3),
    index=['a', 'b', 'c'],
    columns=['one', 'two', 'three']
)
print(my_DataFrame)
print('-----------------')

# 查询列索引为two 和 three 的两列数据

select_data = my_DataFrame.loc[:, ['two', 'three']]
print(select_data)
print('--------------------')

# 查询第0行,第2行,第0列,第2列的数据
select_data = my_DataFrame.iloc[[0, 2], [0, 2]]
print(select_data)
print('--------------------')

# 筛选出第1列中大于2的所有行数据,另存为data1对象
data1: pandas.DataFrame = my_DataFrame.loc[my_DataFrame.iloc[:, 1] > 2, :]
print(data1)
print('-----------')
# 为data1添加一列数据,列索引为four,值为10

data1['four'] = 10
print(data1)
print('-----------')
# 将data1中所有大于9的数据都改成8
masks = data1.iloc[:, :] > 9
data1[masks] = 8
print(data1)
print('-----------')
# 删除data1中第0行和第1行的数据
data1 = data1.drop(data1.index[[0, 1]])
print(data1)
print('-----------')
