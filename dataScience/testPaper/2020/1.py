#     某商品的成本（cost）可以根据产量（output）进行计算： cost=0.14*output+42.7，编写程序模拟商品的生产数据，估计商品的成本（源程序fill_1.py）。
import numpy as np
# 1) 使用数组记录6次生产的商品产量（千件），分别为10、5、7、9、11、8；
output = np.array([10,5,7,9,11,8])
# 2) 根据公式计算每次生产商品的成本；
cost = 0.14*output+42.7
print('1:cost',cost)
# 3) 假设实际成本围绕计算的成本值上下波动，波动值服从均值为0、方差为2的正态分布，随机生成6个数据，模拟每次的波动；
varcost = np.random.normal(0,2,6)
print('2:variance',varcost)
# 4）加上波动值，计算6次生产商品的实际成本。
cost = cost+varcost
print('3:cost',cost)