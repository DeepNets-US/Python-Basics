import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(2,11,2)
plt.plot(arr)
plt.show()

arr2d = np.random.random((3,5))
plt.plot(arr2d)
plt.show()


plt.plot(arr2d.T)
plt.show()
