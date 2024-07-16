import sys
import matplotlib.pyplot as plt
import numpy as np
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y1 = [0, 3, 6, 9, 12, 15, 18, 21, 24]
y2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(x,y1,'blue')
plt.plot(x,y2,'yellow')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()