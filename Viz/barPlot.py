import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10)
plt.bar(x, x*2)
plt.title('TV Sales per Month')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()
