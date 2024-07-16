import sys
import matplotlib.pyplot as plt
import numpy as np
slice= np.array([35, 25, 25, 15])
mylabels = ["Tomatoes", "Mangoes", "Oranges", "Apples"]
myexplode =[0.2, 0, 0, 0]
cols = ['red','blue','green','yellow']
plt.pie(slice, labels=mylabels, colors=cols, startangle=90, explode=myexplode, shadow=True, autopct='%.1f%%')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

