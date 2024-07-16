import pandas as pd
import xlrd
import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(0,5*np.pi,0.1)
a = np.sin(x)
b = np.cos(x)
plt.plot(a,ls='--',color='blue')
plt.plot(b,color='red')
plt.show()