import numpy as np
import pandas as pd


def show_elements(array, start, end):
    print(array[start:end + 1])


# 创建一维数组
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
scores = np.array([[70, 85, 77, 90, 82, 84, 89],
                   [60, 64, 80, 75, 80, 92, 90],
                   [90, 93, 88, 87, 86, 90, 91],
                   [80, 82, 91, 88, 83, 86, 80],
                   [88, 72, 78, 90, 91, 73, 80]])

print(names)
# 在subject数组中选择并显示序号位1,2,4科目的名称
print("在subject数组中选择并显示序号位1,2,4科目的名称:")
print(subjects[[1, 2, 4]])
# 使用倒序选择
print("使用倒序选择:")
print(subjects[[-3, -5, -6]])
# 显示name数组的方绮雯
print("显示name数组的方绮雯:")
print(names[(names == '方绮雯')])
print(names[-3])

# 选择并显示names数组从2到最后的数组元素,选择并显示subject数组2-4的数组元素
print("选择并显示names数组从2到最后的数组元素,选择并显示subject数组2-4的数组元素")
show_elements(names, 2, len(names))
show_elements(subjects,2,4)

#布尔条件选择并显示subject数组English和Physics的科目名称
print("布尔条件选择并显示subject数组English和Physics的科目名称")
print(subjects[(subjects=='English')|(subjects=='Physics')])
