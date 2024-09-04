# 读取DataScience.xlsx 文件,保存到DataFrame 对象中
# 周次    	星期	    节次  	    课程  	            实验项目    	    课时数 	  类型  	   班级  	人数  	二级实验室   	地点
# 2            	1   	5~7	    数据结构	    顺序表的基本操作	    3	        验证型	数据科学181	24	基础实验室	11-505

import pandas as pd
import numpy as np

# 设置显示的最大行数
pd.set_option('display.max_rows', None)  # None 表示不限制行数
# 设置显示的最大列数
pd.set_option('display.max_columns', None)  # None 表示不限制列数
# 设置单元格的显示宽度
pd.set_option('display.max_colwidth', None)  # None 表示不限制宽度
DataScience = pd.read_excel('DataScience.xlsx', header=0)

# 查询实验教学计划的基本内容和总数
columns = DataScience.columns.tolist()
print('教学计划的基本内容:')
print(columns)
# 查询总数
print('一共有', DataScience.shape[0], '行')
print('一共有', DataScience.shape[1], '列')
# 查询实验计划中是否有null数据
print('Nan cols:')
print(DataScience.isnull().any())
# 星期        True
# 节次        True
# 课程        True
# 类型        True
# 二级实验室     True
# 地点        True

# 找到所有包含 NaN 值的行
nan_rows = DataScience[DataScience.isna().any(axis=1)]
# 导出到csv
# nan_rows.to_csv('pre.csv')
# nan_rows.to_excel('pre.xlsx')
# print(nan_rows)

# 填充缺失数据:
# 满足 班级为 数据科学(卓越)171 的 二级实验室都更换为人工智能实验室,地点都变成11-305
DataScience[DataScience['班级'] == '数据科学(卓越)171'] = DataScience[
    DataScience['班级'] == '数据科学(卓越)171'].fillna(
    {
        '二级实验室': '人工智能实验室',
        '地点': '11-305'
    }
)
# #测试
print(DataScience[DataScience.isna().any(axis=1)])
print('\n')
# 所有课程为数据结构的行节次变成5-7
DataScience[DataScience['课程'] == '数据结构'] = DataScience[DataScience['课程'] == '数据结构'].fillna(
    {
        '节次': '5~7'
    }
)
# #测试
print(DataScience[DataScience.isna().any(axis=1)])

# 所有节次为7-9的课设置为数据科学导论
DataScience[DataScience['节次'] == '7~9'] = DataScience[DataScience['节次'] == '7~9'].fillna(
    {
        '课程': '数据科学导论',
    }
)
# #测试
print('\n')
print(DataScience[DataScience.isna().any(axis=1)])

# 有一个7～9节次的数据科学导论的星期应该是4
DataScience[DataScience['节次'] == '7～9'] = DataScience[DataScience['节次'] == '7～9'].fillna(
    {
        '星期': 4
    }
)
# #测试
print('\n')
print(DataScience[DataScience.isna().any(axis=1)])
print('\n')
# 还剩最后一个,康康所有可视化分析的课的类型
print(DataScience[DataScience['实验项目'] == '可视化分析'])
# 发现是设计型
DataScience[DataScience['实验项目'] == '可视化分析'] = DataScience[DataScience['实验项目'] == '可视化分析'].fillna(
    {
        '类型': '设计型'
    }
)
# #测试
print('\n')
print(DataScience[DataScience.isna().any(axis=1)])
print('\n')
# 导出
DataScience.to_excel('New_dataScience.xlsx')
# 查询 课程,实验项目 类型 二级实验室 4列数据内容
print(DataScience[['课程', '实验项目', '类型', '二级实验室']])
print('\n')
# 统计每门课程的课时数
print(DataScience.groupby('课程')['课时数'].mean())
# 统计每周开设的各门课程的实验课时数
print(DataScience.groupby(['周次', '课程']).aggregate(
    {
        '课时数': np.sum
    }
))

# 统计每门课程的实验类型分布,value设置为类型的值
print(pd.crosstab(DataScience['课程'], DataScience['类型'], values=DataScience['类型'], aggfunc='count'))
print('-------------------------')

# 统计每个班的实验课表
# print(set(DataScience['周次'].tolist())) 发现是1-16周
Classes = set(DataScience['班级'].tolist())
DataScience['星期'] = DataScience['星期'].astype(int)
for Class in Classes:
    print(Class, '的课表如下:')
    print(DataScience[DataScience['班级'] == Class][['周次', '星期', '节次', '课程']].reset_index(drop=True))
    print('----------------')
# 分析各个二级实验室能够承担的课时数
print(DataScience.groupby('二级实验室')['课时数'].sum())
# 分析各个2级实验室支持的实验类型
labs = set(DataScience['二级实验室'].tolist())
for lab in labs:
    print(f"二级实验室{lab}支持的实验类型是{set(DataScience[DataScience['二级实验室']==lab]['类型'].tolist())}")
    print('-------------')