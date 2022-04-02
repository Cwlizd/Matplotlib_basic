import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.arange(1, 101)
np.random.seed(1)
y = np.random.choice(range(1, 101), 100)
# size = np.random.choice(np.arange(1, 101), 100)
plt.scatter(x, y, marker="s", s=np.arange(
    1, 101), c=np.arange(1, 101), cmap="viridis")
plt.show()
