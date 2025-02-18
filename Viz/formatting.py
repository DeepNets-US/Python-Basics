import matplotlib.pyplot as plt

xs = list(range(2,21,2))
ys = [val**2 for val in xs]

plt.plot(xs, ys, 'g-o')
plt.show()
