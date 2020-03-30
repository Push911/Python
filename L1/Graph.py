import matplotlib.pyplot as plt
from math import *
import numpy as np

x = np.arange(-pi, pi, 0.1)
y = np.sin(x)

plt.plot(y)
plt.show()
