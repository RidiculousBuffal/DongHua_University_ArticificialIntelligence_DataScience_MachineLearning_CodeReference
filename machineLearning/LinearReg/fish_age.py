import numpy as np
import pandas as pd

df = pd.read_csv("ex0.txt", delimiter="\t", header=None)
df.columns = ['X0','X1','Y']
X_train = df[['X0','X1']].to_numpy() #第一维特征全是1表示b
Y_train = df[['Y']].to_numpy()
X_train_T = X_train.T
OMEGA = np.linalg.inv(X_train_T@X_train)@X_train_T@Y_train
# print(OMEGA)
#将系数乘上特征值
Y_pred = X_train@OMEGA
print("预测值:")
print(Y_pred)
#计算损失函数
J_omega = (1/2)*np.sum((Y_train-Y_pred)**2)
print("代价函数值:",J_omega)