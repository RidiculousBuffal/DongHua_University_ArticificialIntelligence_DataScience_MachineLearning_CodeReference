# 编写Python程序实现功能：从键盘输入若干姓名，保存在字符串列表中；输入任意姓名，检索列表 中是否存在。
# -*- coding: utf-8 -*-
import sys

names = []
i = 1
print('输入名字,按下0结束')

while True:
    name = input(f"input your {i} name!\n")
    if name == '0':
        break
    else:
        print("Success input!")
        i = i + 1
        names.append(name)

print(names)
while True:
    search_name = input("输入查询的名字,按下0结束\n")
    try:
        search_index =names.index(search_name)
        print(f"Success! 改名同学是列表中的第{search_index}名")
    except ValueError:
        if search_name == 0 :
            break
        else:
            print("姓名不在列表中!")
print('OVER!')