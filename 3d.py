import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2*np.pi, 2*np.pi)
x, y = np.meshgrid(t, t)
z = np.sin(np.sqrt(x ** 2 + y ** 2))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")
ax.plot_surface(x, y, z)
plt.show()
