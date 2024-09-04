# -*- coding: utf-8 -*-
import sys

my_dict = dict()
print('程序开始!\n')
while True:
    name = input('输入姓名:\n')
    height = input('输入身高:\n')
    height = float(height)
    my_dict[name]=height
    idx = input('是否继续输入,继续输入1,否则输入0\n')
    if idx == '1':
        continue
    else:
        break

while True:
    try:
        name = input('输入查询的姓名\n')
        tall = my_dict[name]
        print(f'查询到其身高是{tall}\n')
    except KeyError:
        print('key Error!!!')

    idx = input('是否继续查询,继续输入1,否则输入0\n')
    if idx == '1':
        continue
    else:
        break