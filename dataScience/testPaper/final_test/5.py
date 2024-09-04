import matplotlib.pyplot as plt
import  numpy as np
x = np.linspace(0,6.0,50)
y = np.cos(2*np.pi*x)*np.exp(-x)+0.8
plt.plot(x,y,linestyle='--',label='$\cos(2\pi x)e^{-x}+0.8$', linewidth=2.0,color='red')
plt.legend(loc='7777')
plt.show()