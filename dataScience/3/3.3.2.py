# -*- coding: utf-8 -*-
# 读入datingTestSet
import pandas as pd

#将列标签设置为  'flymiles', 'videogames', 'icecream', 'type'
datingTestSet = pd.read_csv('datingTestSet.csv', names=[
    'flymiles', 'videogames', 'icecream', 'type'
], skiprows=2)

# 读取前5条数据
print(datingTestSet[:5])
#显示所有type为largeDoses的数据
print(datingTestSet[datingTestSet['type']=='largeDoses'])

