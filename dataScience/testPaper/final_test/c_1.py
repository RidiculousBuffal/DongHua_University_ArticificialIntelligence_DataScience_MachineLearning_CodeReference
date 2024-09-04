from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#从文件中读取数据
df = pd.read_csv('bank-data.csv')

#1)按照age属性升序排列，并输出结果
df.sort_values(by ='age')

#2)计算并输出income列的均值和方差
inmean=  df['income'].mean() 
print(inmean)
print( df['income'].var())

#3)使用均值填充income列的缺失数据，然后删除仍然包括缺失数据的行；
df.fillna({'income':inmean})
df.dropna(inplace = True)
print(df)

#4)绘制age列的直方图和概率密度图；
df['income'].plot(kind='hist', bins=8, title='Residents Income Distribution' )
df['income'].plot(kind='kde',title='Residents Income Distribution',xlim=[0,80000], style = 'k--')
plt.show()

#5) 计算region属性中各个值出现的次数，并输出出现次数最多的区域
df['region'].value_counts().idxmax()

#6）按照列sex、regoin分组统计income的均值，并按sex绘制income的箱须图；
grouped =  df.groupby(['sex','region'])
print( grouped.aggregate({'income':np.mean}) )
df1 = df[['sex','income']]
df1.boxplot(by='sex',figsize=(6,6))
plt.show()

#7）绘制列age与income的散点图，并计算这两列数据的相关系数。
plt.scatter(  x=df['age'],y = df['income'],marker='*',label='(age,income)')
plt.show()
print( df['age'].corr( df['income'] ) )
