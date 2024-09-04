import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('bank-data.csv')
data = data.sort_values(by='age')
print(data)

jz=data['income'].mean()
print(jz)
fc=data['income'].var()
print(fc)

data.dropna(subset='age',inplace=True)
data.fillna({'income':data['income'].mean()},inplace=True)
print(data)

plt.Figure(figsize=(10,6))
plt.hist(data['age'])

data['age'].plot(kind='kde')

print(data['region'].value_counts().idxmax())

q6=data.groupby(['sex']).aggregate({'income':np.mean})
print(q6)