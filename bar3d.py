from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")

xpos = np.arange(10)
ypos = np.arange(10)
zpos = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = np.arange(1, 11)

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color="r")
plt.show()
