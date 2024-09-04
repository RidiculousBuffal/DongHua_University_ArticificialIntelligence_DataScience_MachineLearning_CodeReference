# 数据清洗
import pandas as pd
# 1）从studentsInfo.xlsx 文件的 Group1表单中读取数据；
data_studentsInfo= pd.read_excel('studentsInfo.xlsx', sheet_name='Group1')
print(data_studentsInfo)
print(' ')
# 2）将“案例教学”列数据值全改为NaN
data_studentsInfo['案例教学'] =pd.NA
print(data_studentsInfo)
print(' ')
# 3）滤除每行数据中缺失3项以上（包括 3 项）的行；
data_studentsInfo = data_studentsInfo.dropna(thresh=data_studentsInfo.shape[1] - 3 + 1)
print(data_studentsInfo)
print(' ')
# 4）滤除值全部为 NaN 的列；
data_studentsInfo = data_studentsInfo.dropna(axis=1, how='all')