import numpy as np
a :np.ndarray= np.arange(1,7).reshape(3,2)
print(a)
print(a.sum(axis=0))