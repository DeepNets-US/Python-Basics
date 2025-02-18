import matplotlib.pyplot as plt

xs = list(range(2,21,2))
ys = [val**2 for val in xs]
ys2 = [val**4 for val in xs]

# First method
plt.plot(xs, ys, 'g-o', xs, ys2, 'b--^')
plt.show()

# Second Method
plt.plot(xs, ys, 'g-o')
plt.plot(xs, ys2, 'b--^')
plt.show()
