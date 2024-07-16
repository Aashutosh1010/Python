import pandas as pd
import xlrd
import matplotlib.pyplot as plt 
import numpy as np 
df = pd.read_csv("D:\data.csv")
x = df.month_number
y = df.total_profit
plt.plot(x,y,'blue')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Compony profit per month')
plt.show()
plt.plot(x, y,'-ok',ls = '--', linewidth = '3',color='red') 
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Compony profit per month')
plt.show()
y1 = df.facecream
y2 = df.facewash
y3 = df.toothpaste
y4 = df.bathingsoap
y5 = df.shampoo
y6 = df.moisturizer
plt.plot(y1,'-ok',color='red', linewidth = '3')
plt.plot(y2 ,'-ok',color='green', linewidth = '3')
plt.plot(y3, '-ok',color='blue', linewidth = '3')
plt.plot(y4, '-ok',color='purple', linewidth = '3')
plt.plot(y5, '-ok',color='brown', linewidth = '3')
plt.plot(y6, '-ok',color='yellow', linewidth = '3')
plt.title('Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.show()