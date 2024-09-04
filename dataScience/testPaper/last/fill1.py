import pandas as pd
# 创建两个数据帧
df1 = pd.DataFrame({'X1': [1, 2, 3],
 'X2': ['X', 'Y', 'Z']},
 index=[0, 1, 2])
df2 = pd.DataFrame({'X2': ['A', 'B', 'C'],
 'X4': [4, 5, 6]},
 index=[1, 2, 3])
# 'outer' 方法拼接
df_outer = pd.concat([df1, df2], join='outer', axis=0)
print(df_outer)
# 'inner' 方法拼接
df_inner = pd.concat([df1, df2], join='inner', axis=0)
print(df_inner)