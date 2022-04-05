import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 50)
x, y = np.meshgrid(t, t)
z = x * y

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")

ax.plot_surface(x, y, z, cmap="viridis")
plt.show()
