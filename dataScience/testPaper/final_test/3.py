#  以下是a，b，c，d四位同学在一月，二月和三月分别获得的零花钱数量。分别求一月，
# 二月，三月中每个月四人获得的零花钱总量；每个人三个月的平均零花钱；每个月零花
# 钱最多的人。（源程序文件fill_3.py）
from pandas import DataFrame
data = [[100,37,55],[46,66,53],[33,41,67],[86,89,76]]
#创建df1
df1=DataFrame(data,index=['a','b','c','d'],columns=['Jan','Feb','Mar'])
#输出三个月每月所有人零花钱的总和
print (df1.sum())
print()
#输出每人三个月的平均零花钱
print (df1.mean (axis=1))
print()
#输出每个月零花钱最多的人
print (df1.idxmax(axis=0))