import pandas as pd
import numpy as np
#添加必要的头文件
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


#1.	读取文件E-commerce Customer Behavior - Sheet1.csv并将第0列设置为索引,输出前5行数据





# 2.	统计含有缺失数据的列的情况,如果含有,按照表格处理并覆盖原数据





# 3.	统计含有重复数据的行数,并删除，覆盖原数据。



# 4.	统计每个区域(City) 每一种会员类型(Membership Type)[Silver,Bronze,Gold]的客户数。





# 5.	给出平均星级排名(Average Rating)最高的区域(City)





# 6.	使用直方图绘制年龄分布图并将直条数(bins)设置为20,
# 在同一张图上绘制核密度分布图,在直方图上用箭头标记出最高点,图像命名为fig1.png,dpi=300保存在试题目录下的fig文件夹内。





# 7.	统计数值类型Age,Total Spend,Items Purchased,Average Rating,Days Since Last Purchase之间的相关性,打印出相关性矩阵
# 绘制5个变量之间的散点图矩阵,矩阵对角线上使用密度分布图像, 图像命名为fig2.png,dpi=300保存在试题目录下的fig文件夹内


# 将数据分割为训练集和测试集(测试集大小为50%),
# 在训练集上训练关于Satisfaction Level的分类模型(至少采用两种分类算法),
# 并比较之间的性能差异(相同or某一个更好),输出二者的性能评分和分类报告,并单独粘贴在注释行中。



#性能评分和分类报告:




#性能差异的比较