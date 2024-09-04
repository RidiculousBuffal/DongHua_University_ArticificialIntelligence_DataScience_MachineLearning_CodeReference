import numpy as np
np.set_printoptions(precision=2,suppress=True)
arr = np.random.normal(0,1,size=(4,6))
print(arr)
print('----------------------')
print('1.\n',arr[0:2,:])
# 将arr 的axis1 index为2的数据全部替换成1
arr[:,2]=1
print('2.\n',arr)

