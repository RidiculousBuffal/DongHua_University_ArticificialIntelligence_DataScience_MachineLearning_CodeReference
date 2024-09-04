# 1) 根据表2和表3分别创建数据对象，然后将两个数据对象合并，如表4所示；
# 2) 统计每家出版社出版的图书数，如图3所示；
# 3) 显示一周各出版社销售额，如图4所示。
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

# 1)分别记录根据表2和表3中数据，然后合并
books1 = {"bookname": ['Python数据分析基础', '数据科学与大数据分析', '机器学习', '人工智能简史'],
          "press": ['人民邮电出版社', '高等教育出版社', '清华大学出版社', '人民邮电出版社'],
          "price": [38.9, 56.4, 45.2, 23.5], "sales": [25, 39, 44, 24]}
col_name = ['bookname', 'press', 'price', 'sales']
df1 = DataFrame(books1, index=['A01', 'A02', 'A03', 'A04'], columns=col_name)
print(df1)

books2 = {"bookname": ['Python程序设计', '数据科学导引', '深度学习', '机器学习实战', 'TensorFlow框架', ],
          "press": ['清华大学出版社', '高等教育出版社', '人民邮电出版社', '人民邮电出版社', '电子工业出版社'],
          "price": [42.1, 34.5, 67.1, 56.0, 78.2], "sales": [30, 18, 32, 20, 10]}
df2 = DataFrame(books2, index=['B01', 'B02', 'B03', 'B04', 'B05'], columns=col_name)
print(df2)

# 合并df1和df2
df3 = pd.concat([df1, df2])
print("数据集合并后:\n", df3)
# 2）统计每家出版社出版的图书数量
print("\n出版社出版的图书数:\n", df3['press'].value_counts(), "\n")
# 3)显示一周各出版社销售额
df3['total'] = df3['price'] * df3['sales']
group = df3.groupby(['press'])
print(group.aggregate({'total': np.sum}))
