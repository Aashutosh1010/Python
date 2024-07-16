import sys
import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3]
y1 = [2, 3, 4.5]
y2 = [1, 1.5, 5]
plt.plot(x,y1,'blue')
plt.plot(x,y2,'yellow')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()