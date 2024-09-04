import numpy as np
def generateData(w,b,dataNum=10):#根据w,b⽣成数据
    data = []
    for i in range(dataNum):
        noise = np.random.randn(1) * 0.01
        x0 = np.random.randn(1,w.shape[0])
        y0 = np.dot(x0, w) + b+noise
        x = [x0, y0]
        data.append(x)
    return data
