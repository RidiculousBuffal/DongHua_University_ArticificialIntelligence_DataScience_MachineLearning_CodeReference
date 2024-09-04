# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# 第一问的数据
raw_data = pd.read_excel('studentsInfo.xlsx', sheet_name='Group3')
data1 = raw_data[['序号', '性别', '年龄']]
data2 = raw_data[['序号', '身高', '体重', '成绩']]
data_new = pd.merge(data1, data2, how='inner')
# 按照‘月生活费‘对数据进行升序排列
# 先根据序号加入月生活费这一栏
# data_new['序号']：这是 data_new 数据框中的 "序号" 列，它作为映射的键。
# raw_data.set_index('序号')['月生活费']：这部分的目的是创建一个以 "序号"
# 列为索引的 Series，然后通过索引选择 "月生活费" 列的值。
# raw_data.set_index('序号')：这一部分将 raw_data 数据框的索引设置为 "序号"
# 列，以便能够根据该列的值进行映射。
# ['月生活费']：这一部分选择了设置了索引后的数据框中的 "月生活费" 列。
# data_new['序号'].map(raw_data.set_index('序号')['月生活费'])：这一部分将
# "序号" 列的值映射到相应的 "月生活费" 值，并将结果赋给 data_new['月生活费'] 列。
# data_new['序号'].map()：这是 map() 函数的调用，它将 "序号" 列的值作为输入，
# 并根据映射关系来获取对应的 "月生活费" 值。
# raw_data.set_index('序号')['月生活费']：这是映射关系，它将 "序号" 列的值
# 与 "月生活费" 列的值进行对应。

# data_new['月生活费']=np.NAN
# # 初始化
# i=0
# for index_ in data_new['序号'].tolist():
#     data_new['月生活费'].iloc[i]=raw_data.loc[raw_data['序号']==index_]['月生活费']
#     i=i+1
# print(data_new)


data_new['月生活费'] = data_new['序号'].map(raw_data.set_index('序号')['月生活费'])
data_new = data_new.sort_values(by='月生活费', ascending=True)
# 然后丢掉
data_new.drop('月生活费', axis=1, inplace=True)
print(data_new)
print('----------------------')
# 根据身高排序
data_new['排名'] = data_new['身高'].rank(axis=0,method='min', ascending=False).astype(int)
print(data_new)
print('----------------------')
