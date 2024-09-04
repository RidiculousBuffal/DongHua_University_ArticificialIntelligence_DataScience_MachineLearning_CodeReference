#     风记录数据集（）记录了2014年某区域发生的台风信息，包含台风名、台风等级、气压（百帕）、移动速度（公里/时)、纬度、经度、记录数、顺序、风速（米/秒）等9个属性，具体说明见"数据集说明"文件。（源程序fill_4.py）
# 1) 从文件中读出台风数据；
# 2）查看是否存在缺失数据，删除包含缺失数据的样本；
# 3）输出达到超强台风等级的台风名字
# 源程序文件（fill_4.py）
import pandas as pd
import numpy as np
winds = pd.read_csv('Typhoon.csv')
print(winds[0:5])
# 2）查看是否存在缺失数据，删除包含缺失数据的样本
print(winds.isna().any())
winds.dropna(how='any', inplace=True)
print(winds.isna().any())
# 3）输出达到超强台风等级的台风名
names = winds[winds['level'] == '超强台风']['windname'].unique()
print("\n达到超强台风等级：\n", names)
