import pandas as pd
import  numpy as np

data = pd.DataFrame(
    np.random.randint(10,100,size=(50,7)),
    columns=[chr(ord('a')+i) for i in range(0,7)]
)

print(data)

data.to_csv('out.csv')