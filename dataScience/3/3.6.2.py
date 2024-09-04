import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.style.use('fivethirtyeight')
# 设置显示的最大行数
pd.set_option('display.max_rows', None)  # None 表示不限制行数
# 设置显示的最大列数
pd.set_option('display.max_columns', None)  # None 表示不限制列数
# 设置单元格的显示宽度
pd.set_option('display.max_colwidth', None)  # None 表示不限制宽度
Bankpep = pd.read_csv('bankpep.csv')
# 查看储户总数,以及居住在不同区域的储户总数
print(Bankpep['id'].count())
print('-------')
print(Bankpep.groupby('region')['id'].count())
# 计算不同性别储户的均值和方差
print(Bankpep.groupby('sex')['income'].mean())
print(Bankpep.groupby('sex')['income'].var())
# 统计每个性别中 pep 为 "YES" 的 id 总数
result = Bankpep[Bankpep['pep'] == 'YES'].groupby(['sex', 'region'])['id'].count()
print(result)
# 将存款账户,接受新业务的数据转化为整数值
Bankpep[Bankpep['save_act'] == 'NO'] = 0;
Bankpep[Bankpep['save_act'] == 'YES'] = 1;
Bankpep[Bankpep['pep'] == 'NO'] = 0;
Bankpep[Bankpep['pep'] == 'YES'] = 1;
Bankpep['save_act']=Bankpep['save_act'].astype(int)
Bankpep['pep']=Bankpep['pep'].astype(int)
Bankpep['income']=Bankpep['income'].astype(float)
# print(Bankpep['save_act'])
# print(Bankpep['pep'])
# 分析收入,存款账户和接受新业务之间的关系
result = Bankpep[['income', 'save_act', 'pep']].corr()
print(result)
# 绘制相关性热力图
plt.figure(figsize=(22, 18))
sns.heatmap(result, annot=False, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.xlabel('Variables')
plt.ylabel('Variables')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.savefig('result.png', dpi=600)