import matplotlib.pyplot as plt
import numpy as np

vals = np.random.randn(1000)
plt.hist(vals, 20)
plt.show()
