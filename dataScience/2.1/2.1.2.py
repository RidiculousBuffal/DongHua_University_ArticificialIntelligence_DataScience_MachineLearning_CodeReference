import numpy as np

names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
scores = np.array([[70, 85, 77, 90, 82, 84, 89],
                   [60, 64, 80, 75, 80, 92, 90],
                   [90, 93, 88, 87, 86, 90, 91],
                   [80, 82, 91, 88, 83, 86, 80],
                   [88, 72, 78, 90, 91, 73, 80]])

# 选择并显示scores数组的1行4行
print("选择并显示scores数组的1行4行")
print(scores[[1, 4]])

# 选择并显示scores数组中行序为2,4学生的Math和Python成绩
print("选择并显示scores数组中行序为2,4学生的Math和Python成绩")
print(scores[[2, 4]][0:(len(scores) + 1), (subjects == 'Math') | (subjects == 'Python')])
# 其中(0,len+1)代表先选中所有的列,然后再通过布尔数组确定具体的索引

# 选择并显示所有学生的Math和python成绩
print("选择并显示所有学生的Math和python成绩")
print(scores[0:len(names)][0:(len(scores)), (subjects == 'Math') | (subjects == 'Python')])

# 选择并显示scores数组中所有学生的Math和Art成绩
print("选择并显示scores数组中所有学生的Math和Art成绩")
print(scores[:, (subjects == 'Math') | (subjects == 'Art')])

# 选择并显示score数组中'王微'和'刘旭阳'的ENGLISH和ART成绩
print("选择并显示score数组中'王微'和'刘旭阳'的ENGLISH和ART成绩")
print(scores[(names == '王微') | (names == '刘旭阳')][:, (subjects == 'English') | (subjects == 'Art')])
