import sys
import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x,y,'blue')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

