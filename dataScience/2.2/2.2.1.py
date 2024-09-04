# -*- coding: gb2312 -*-
from typing import Any
import pandas as pd
import numpy as np
import inspect


def deb(arr):
    frame = inspect.currentframe().f_back
    code = frame.f_code
    arg_name = inspect.getframeinfo(frame).code_context[0].split('(')[1].split(')')[0].split('=')[0].strip()
    print(arg_name + ':')  # t调试,打印具体值
    print(arr)


# 大润发,沃尔玛,好德,农工商4个超市售卖苹果,梨,香蕉,橘子和芒果5种水果,使用numpy和ndarray实现以下功能
# 创建一维数组分别储存超市和水果的名称
shop = np.array(['大润发', '沃尔玛', '好德', '农工商'])
deb(shop)
fruit = np.array(['苹果', '梨', '香蕉', '橘子', '芒果'])
deb(fruit)
# 创建一个4*5的二维数组,分别储存价格,其中价格在4-10元之间
price = np.random.uniform(4, 10, size=(4, 5))
deb(price)
# 选择大润发的苹果和好德的香蕉,并将价格增加一元
##先选择大润发的苹果,给其加1
# var1 = price[shop == '大润发'][:, fruit == '苹果'] + 1
# var2 = price[shop == '好德'][:, fruit == '香蕉'] + 1
# var1 = var1[0][0]
# var2 = var2[0][0]
price[np.where(shop == '大润发')[0][0]][np.where(fruit == '苹果')[0][0]] += 1
price[np.where(shop == '好德')[0][0]][np.where(fruit == '香蕉')[0][0]] += 1
# np.where返回的是一个元祖(array([?], dtype=int64),) 由于是shop和fruit都是一维的,故只有一个元素
# 将np.where()[0]取出得到的是一个列表,列表中有一个元素是寻找的元素在对应array中的位置
# np.where()[0][0]是将列表中的第一个元素取出,也就是真正的下标
print('-----------new price------------')
print(price)
print('---------------')
# 农工商的水果大减价,将所有的水果价格减少2元
price[np.where(shop == '农工商')[0][0]] -= 2
print('-----------new price------------')
print(price)
print('---------------')
# 统计4个超市苹果和芒果的销售均价
means = price[:, (fruit == '苹果') | (fruit == '芒果')].mean(axis=0)
##行选中全部的行用  空格:空格 这样表示,其中空格可以省略所有就变成了: 这个样子
print(means)
# 找出橘子价格最贵的超市名称
name = shop[price[:, (fruit == '橘子')].argmax()]
print(name)
