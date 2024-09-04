# 用DataFrame存储如下表格数据，按照身高进行排序后输出年龄大于30岁的人信息（源
# 程序文件fill_2.py）
import pandas as pd
data = {'Age': [33,25,28,31], 'Height': ['178cm','165cm','180cm','162cm']}
df1 = pd.DataFrame(
    data=data,
    columns=['Age', 'Height'],
    index=['Tom', 'Jack', 'Lily', 'Rose']
)
print(df1)
# 按身高对数据进行排序
print(df1['Height'].sort_values())
#输出年龄大于30岁的人
print(df1[df1['Age']>30])